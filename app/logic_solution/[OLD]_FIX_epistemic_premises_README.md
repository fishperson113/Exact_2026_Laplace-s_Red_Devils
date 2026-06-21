# FIX: Xử lý mệnh đề "vắng mặt thông tin" (epistemic / meta premises)

> Handoff cho người sửa `logic_solution`. Đọc hết phần **Bối cảnh** trước khi code —
> phần **Cơ chế** và **Files cần sửa** ở dưới chỉ làm theo sau khi đã hiểu *vì sao*.

---

## 1. TL;DR

Pipeline (FOL model → QA model) đang **trả sai** với các mệnh đề kiểu
*"No premise states whether X"* / *"It is unknown whether X"*. Model FOL dịch nhầm
mệnh đề "không rõ thông tin" thành một **phủ định cứng** `¬X`, khiến QA model suy ra
đáp án sai (No) thay vì đúng (Uncertain).

**Cách sửa (KHÔNG train lại):** chèn 1 bước **code tất định** giữa Stage 1 và Stage 2 —
phát hiện mệnh đề epistemic trên NL gốc, rồi **ghi đè ô FOL tương ứng bằng một note
trung lập** (xoá phủ định giả, giữ nguyên số dòng để không lệch index). Tùy chọn thêm
1 câu nudge vào prompt QA. Không model nào bị đổi prompt/đổi input so với lúc train ở
phần chính → an toàn với cách đã huấn luyện.

---

## 2. Bối cảnh — mẫu đang lỗi (Asha)

### Input (gửi vào API, đúng schema BTC type1)

```json
{
  "query_id": "quick_type1_uncertain",
  "type": "type1",
  "query": "Does Asha have budget approval?",
  "premises": [
    "If a researcher completed ethics training and has lab access, then that researcher can handle participant data.",
    "If a researcher can handle participant data and has supervisor approval, then that researcher may join Study Alpha.",
    "Every researcher who may join Study Alpha is listed as an active contributor.",
    "Asha completed ethics training.",
    "Asha has lab access.",
    "Asha has supervisor approval.",
    "Study Alpha has 12 enrolled participants.",
    "No premise states whether Asha has budget approval."
  ],
  "options": ["Yes", "No", "Uncertain"]
}
```

### Gold (đúng)

```json
{ "answer": "Uncertain", "premises_used": [7] }
```

Câu hỏi "Asha có budget approval không?" — không premise nào quyết định → **Uncertain**.
Premise 7 chỉ nói *"không có dữ kiện nào đề cập"* (vắng mặt thông tin), KHÔNG nói Asha
thiếu budget approval.

### Model trả về (SAI)

```json
{
  "answer": "No",
  "premises_used": [0,1,2,3,4,5,6,7],
  "reasoning": {
    "type": "fol",
    "steps": [
      "Rule: ∀r ((completed_ethics_training(r) ∧ has_lab_access(r)) → can_handle_data(r))",
      "... (các bước modus ponens đúng nhưng KHÔNG liên quan câu hỏi) ...",
      "Fact: ¬has_budget_approval(Asha)",                        // ← FACT GIẢ
      "Conclusion: ¬has_budget_approval(Asha) is explicitly stated ⟹ No"
    ]
  }
}
```

Điểm chấm: `p1_score=0` (answer sai), `sample_score=11.11`.

---

## 3. Root cause — lỗi bắt nguồn từ Stage 1 (FOL), QA kế thừa

- Premise 7 là mệnh đề **meta/epistemic**: nói về *bản thân tập tri thức*
  ("không premise nào nói…"), không phải về thế giới. **FOL ở tầng object không biểu
  diễn được** loại câu này — cách đúng là dịch thành vô nghĩa object-level (bỏ / tautology),
  để `BudgetApproval(Asha)` ở trạng thái không xác định.
- Nhưng FOL model được train theo khuôn cứng *"n NL premises → exactly n FOL formulas,
  same order"* nên khi gặp câu không hiểu, nó **bám từ khoá bề mặt**: thấy
  `No ... budget approval` → sinh `¬has_budget_approval(Asha)` (vứt mất "no premise
  states whether").
- QA model nhận FOL đó, thấy `Fact: ¬has_budget_approval(Asha)`, **tin theo** (QA được
  train để "reason trên FOL"), rồi chốt No. Lỗi **dây chuyền 2 tầng**: FOL dịch sai → QA
  không nghi ngờ.

> **Lưu ý quan trọng:** ta CHƯA xác nhận 100% bằng mắt vì response API không in field
> `fol`. Trước khi sửa, nên **bật log `fol_generated`** chạy lại mẫu Asha, soi dòng FOL
> thứ 8. Nếu là `¬has_budget_approval(Asha)` → đúng chẩn đoán này.

---

## 4. Vì sao KHÔNG chọn 2 cách "hiển nhiên" khác

| Ý tưởng | Vì sao loại |
|---|---|
| Sửa prompt FOL: "đừng dịch mệnh đề chứa whether / no premise states" | (1) Phá alignment **n-to-n** → output còn 7 dòng → lệch toàn bộ index `premises_used` (đúng bug đã gặp ở mẫu FOL 35 dòng / NL 36 dòng). (2) Model đã SFT mạnh "luôn dịch" → chỉ thị mới ở prompt **bị phớt lờ** (cùng bài học CoT: target lúc train thắng lời dặn ở prompt). |
| Train lại FOL/QA với mẫu epistemic | Đúng về lâu dài nhưng **không có thời gian train lại** (yêu cầu của đề bài này). Để dành cho vòng data sau. |

→ Chọn **can thiệp bằng code tất định ngoài model**.

---

## 5. Cơ chế giải pháp — luồng dữ liệu

### Hiện tại (lỗi)

```
premises_nl (8) ─► [Stage 1 FOL] ─► fol_list (8)
                                       fol_list[7] = "¬has_budget_approval(Asha)"  ← SAI
                                       │
premises_nl + fol_list + options + question ─► [Stage 2 QA] ─► "No"
```

### Sau khi sửa

```
premises_nl (8) ─► [Stage 1 FOL]  ─► fol_list (8)     ← Stage 1 CHẠY Y HỆT (prompt+input không đổi)
       │             (không đổi)          │
       │                                  ▼
       └─► [BƯỚC MỚI: regex quét premises_nl gốc] ─► phát hiện index 7 là epistemic
                                          │
                                          ▼
              GHI ĐÈ TẠI CHỖ: fol_list[7] = "(no FOL — premise only states that information is absent/unknown)"
                                          │  (vẫn 8 phần tử → index 0..7 KHÔNG lệch)
                                          ▼
premises_nl + fol_list(đã sửa) + options + question ─► [Stage 2 QA] ─► "Uncertain"
       ▲                                                                    ▲
  NL câu 7 GIỮ NGUYÊN (sự thật)                              + (tùy chọn) nudge prompt
```

### Stage 2 nhìn thấy gì — before vs after

**Trước (lỗi):**
```
Premises (NL):
  7. No premise states whether Asha has budget approval.
Premises (FOL):
  7. ¬has_budget_approval(Asha)        ← phủ định GIẢ → QA bám vào → No
```

**Sau:**
```
Premises (NL):
  7. No premise states whether Asha has budget approval.        ← giữ nguyên
Premises (FOL):
  7. (no FOL — premise only states that information is absent)   ← không còn fact giả
```
QA mất chỗ bám sai → buộc dựa vào NL câu 7 (vẫn còn) → hiểu đúng "không xác định" → **Uncertain**.

### Vì sao an toàn với cách đã train

- **FOL model: zero distribution shift.** Prompt y nguyên, vẫn nhận đủ 8 NL, vẫn sinh 8
  công thức. Ta chỉ **vứt bỏ/thay 1 output SAU KHI nó chạy xong**.
- **Giữ alignment n-to-n.** Ghi đè *tại chỗ, không xoá* → `fol_list` vẫn 8 phần tử →
  `premises_used` của QA vẫn map đúng index.
- **Quét trên NL gốc, không quét FOL.** NL là input chuẩn BTC (đáng tin); FOL output có
  thể méo.
- **QA model: shift rất nhỏ và lành.** Note trung lập *không sinh suy diễn nào*; trong khi
  `¬X` giả thì *chủ động kéo* suy diễn sai. Đổi "fact giả độc hại" lấy "note vô hại" là
  nâng cấp ròng.

---

## 6. Files cần sửa

### 6.1. `app/logic_solution/parsing.py` — THÊM helper (file này torch-free, dùng chung)

> Đặt ở `parsing.py` để **cả** `ensemble.py` (in-process) **lẫn** `app/core/pipeline_logic.py`
> (vLLM gateway, import từ `app.logic_solution.parsing`) đều dùng được mà không kéo theo torch.

Thêm:

```python
import re

# Mẫu mệnh đề "vắng mặt / không chắc chắn thông tin" — REGEX HẸP, chỉ bắt meta thật,
# KHÔNG bắt mọi "whether" (có premise hợp lệ chứa "whether").
_EPISTEMIC_PATTERNS = [
    r"\bno premise\b.{0,40}\bwhether\b",
    r"\bno premise (?:states|specifies|mentions|indicates)\b",
    r"\bit is (?:un)?known whether\b",
    r"\b(?:not|isn't|is not) (?:specified|stated|known|mentioned) whether\b",
    r"\b(?:does not|doesn't|do not|don't) (?:state|specify|say) whether\b",
    r"\bno (?:information|statement|fact)\b.{0,40}\bwhether\b",
    r"\bunspecified whether\b",
]
_EPISTEMIC_RE = re.compile("|".join(_EPISTEMIC_PATTERNS), re.IGNORECASE)

# Note trung lập đặt vào ô FOL của mệnh đề epistemic (thay cho phủ định giả).
_EPISTEMIC_FOL_SENTINEL = "(no FOL — premise only states that information is absent/unknown)"


def is_epistemic_premise(nl: str) -> bool:
    """True nếu mệnh đề NL chỉ nêu sự VẮNG MẶT/không chắc chắn thông tin."""
    return bool(_EPISTEMIC_RE.search(str(nl)))


def neutralize_epistemic_fol(premises_nl: list[str], fol_list: list[str]) -> list[str]:
    """Ghi đè TẠI CHỖ ô FOL của mệnh đề epistemic bằng note trung lập.

    - Quét premises_nl GỐC (không quét fol_list — NL đáng tin hơn).
    - GIỮ NGUYÊN số phần tử của fol_list (chỉ replace, không xoá) → index không lệch.
    - Trả về list mới (không mutate input).
    """
    out = list(fol_list)
    for i, nl in enumerate(premises_nl):
        if i < len(out) and is_epistemic_premise(nl):
            out[i] = _EPISTEMIC_FOL_SENTINEL
    return out
```

### 6.2. `app/logic_solution/pipeline/ensemble.py` — chèn bước neutralize vào `run()`

Trong method `EnsemblePipeline.run()`, NGAY SAU dòng sinh FOL (hiện ~dòng 85) và TRƯỚC
khi gọi QA:

```python
from parsing import neutralize_epistemic_fol   # thêm import ở đầu file

# ... trong run(), sau:
fol_list, fol_raw = self.fol_model.generate(premises_nl, self.fol_max_tokens)
fol_latency = time.perf_counter() - t0

# ── BƯỚC MỚI: gỡ phủ định-giả ở mệnh đề epistemic trước khi đưa vào QA ──
fol_list = neutralize_epistemic_fol(premises_nl, fol_list)

# ... rồi mới gọi self.qa_model.generate(premises_nl, fol_list, ...)
```

> `fol_raw` (raw debug) giữ nguyên; chỉ `fol_list` đưa vào QA là bản đã neutralize.

### 6.3. `app/core/pipeline_logic.py` — đồng bộ cho luồng vLLM

Đây là gateway phục vụ qua HTTP (BTC chấm qua đây). Phải sửa **giống hệt** để hành vi
khớp bản in-process. Sau `fol_list = parse_fol(fol_raw)` và TRƯỚC khi build `qa_user`:

```python
from app.logic_solution.parsing import parse_fol, parse_qa_output, neutralize_epistemic_fol

# ... sau:
fol_list = parse_fol(fol_raw)

# ── gỡ phủ định-giả ở mệnh đề epistemic trước khi đưa vào QA ──
fol_list = neutralize_epistemic_fol(premises_nl, fol_list)
```

> ⚠️ Field `"fol"` trả về cho client nên là `fol_list` SAU neutralize để debug nhất quán.
> Nên log cả `fol_raw` (trước) lẫn `fol_list` (sau) để đối chiếu khi cần.

### 6.4. Nudge prompt QA — cho phép TRÍCH mệnh đề đã neutralize vào `premises_used`

**VÌ SAO BẮT BUỘC (không còn là tùy chọn cho mục tiêu này):** prompt QA hiện tại quy định
*"viết mọi Rule:/Fact: bằng FOL notation"* và *"premises_used = index các premise cite trong
Rule:/Fact: steps"*. Dòng FOL đã neutralize `(no FOL — ...)` KHÔNG phải FOL notation → model
không tạo được Rule:/Fact: từ nó → **index của nó bị loại khỏi `premises_used`**. Nhưng gold
lại cần index đó (vd Asha gold = `[7]`). Để model coi mệnh đề đã neutralize như một premise
HỢP LỆ có thể trích, phải nới prompt rõ ràng.

> Phân tầng mục tiêu:
> - Chỉ cần **answer đúng** (Uncertain) → deterministic code (6.1–6.3) là ĐỦ, không cần sửa prompt.
> - Cần model **trích được index** mệnh đề epistemic vào `premises_used` → **BẮT BUỘC** thêm clause này.

`app/logic_solution/prompts/prompt.py` — `SYSTEM_PROMPT_QA`, thêm khối sau (đặt ngay dưới
khối `### Output`, để nó nằm cạnh quy tắc premises_used mà nó đang nới):

```
### Handling premises that state information is absent/unknown
Some FOL lines are NOT formulas but a marker such as
"(no FOL — premise only states that information is absent/unknown)".
Such a line is still a REAL premise and you MUST treat it as citable:
- Treat the corresponding fact as UNDETERMINED — do NOT derive a negation from it.
- If your conclusion relies on this absence of information, write a Fact: step that
  references it in words, e.g. "Fact: premise i states whether <X> is unknown",
  and INCLUDE that premise's 0-based index in "premises_used" (this is the one
  allowed exception to the "FOL-notation only" rule above).
- The answer is "Uncertain" unless OTHER premises decide the question.
```

Vì sao clause này nới đúng chỗ:
- Cho phép **một ngoại lệ có kiểm soát** với quy tắc "FOL-notation only" — chỉ áp dụng cho
  dòng marker, nên trên mẫu thường (không có marker) clause này **vô hiệu**, model hành xử như cũ.
- Giữ prefix `Fact:` → **parser không cần đổi** (`extract_reasoning_steps` đã gom dòng `Fact:`).
- `premises_used` do model emit trong JSON → parser đã lấy sẵn; chỉ cần model chịu bỏ index vào.

> ⚠️ **CẢNH BÁO consistency:** đây vẫn là prompt đổi so với lúc train (distribution shift).
> Dù clause có điều kiện (chỉ kích hoạt khi gặp marker) nên rủi ro thấp, vẫn BẮT BUỘC:
> (a) test trên TOÀN dev before/after — chắc mẫu thường KHÔNG đổi đáp án/`premises_used`;
> (b) dùng prompt y HỆT ở MỌI nơi (`logic_solution/prompts/prompt.py` + bất kỳ chỗ nào
> `pipeline_logic.py`/route vLLM nạp `SYSTEM_PROMPT_QA`). Hai luồng phải cùng một prompt.

---

## 7. Guardrails BẮT BUỘC trước khi chốt

1. **Regex phải HẸP.** Đã viết để chỉ bắt cụm meta đặc trưng, KHÔNG bắt mọi "whether"
   (vd "If a student passes whether or not they study..." là premise hợp lệ, KHÔNG được
   neutralize). Nếu thêm pattern, test kỹ false positive.
2. **Đo trên TOÀN dev trước/sau thay đổi** (`data/processed/dev.csv`). Xác nhận:
   - (a) lật đúng các mẫu epistemic sang Uncertain;
   - (b) accuracy các mẫu KHÁC **không tụt** (false positive của regex là rủi ro lớn nhất).
   Đây là sửa ở inference không qua train → bằng chứng số là thứ duy nhất đáng tin.
3. **Xác nhận root cause trước:** bật log `fol_generated` chạy lại Asha, kiểm dòng FOL số 8
   đúng là `¬has_budget_approval(Asha)`.

---

## 8. Test nhanh sau khi sửa

Chạy mẫu Asha (mục 2) qua pipeline. Kỳ vọng:

```json
{
  "query_id": "quick_type1_uncertain",
  "answer": "Uncertain",          // ← từ "No" thành "Uncertain"
  "unit": "",
  "explanation": "...",
  "premises_used": [7],           // ← phải CÓ index 7 (nhờ clause 6.4); KHÔNG còn [0..7] sai
  "reasoning": {
    "type": "fol",
    "steps": [
      "Fact: premise 7 states whether Asha has budget approval is unknown",   // ← cite được dòng đã neutralize
      "Conclusion: budget approval is undetermined ⟹ Uncertain"
    ],
    "fol": [                        // ← TRƯỜNG MỚI (xem mục 10): FOL CUỐI (sau neutralize)
      "...",
      "(no FOL — premise only states that information is absent/unknown)"   // index 7 đã neutralize
    ]
  }
}
```

> Nếu thiếu clause 6.4: `answer` vẫn ra "Uncertain" (nhờ deterministic code) nhưng
> `premises_used` sẽ **KHÔNG có 7** (model không cite được dòng marker) → mất điểm p2.
> Có clause 6.4 → model trích được index 7 như gold.

Và FOL stage giờ phải cho (dòng index 7):
```
[7] (no FOL — premise only states that information is absent/unknown)
```
thay vì `¬has_budget_approval(Asha)`.

---

## 9. Tóm tắt thay đổi

| File | Thay đổi | Bắt buộc? |
|---|---|---|
| `app/logic_solution/parsing.py` | Thêm `is_epistemic_premise`, `neutralize_epistemic_fol`, regex + sentinel | ✅ |
| `app/logic_solution/pipeline/ensemble.py` | Gọi `neutralize_epistemic_fol` trong `run()` giữa Stage 1 và Stage 2 | ✅ |
| `app/core/pipeline_logic.py` | Gọi `neutralize_epistemic_fol` giữa `parse_fol` và build `qa_user` | ✅ (cho luồng vLLM) |
| `app/logic_solution/prompts/prompt.py` | Clause "Handling premises that state info absent/unknown" vào `SYSTEM_PROMPT_QA` (6.4) | ✅ nếu cần `premises_used` trích index epistemic; ⚠️ test dev before/after |
| `app/logic_solution/utils/postprocess.py` | Thêm param `fol_list` vào `format_submission`, đặt `fol` vào trong `reasoning` (mục 10) | ✅ (yêu cầu mới) |
| `app/logic_solution/run.py` | Truyền `fol_list=out.fol_list` khi gọi `format_submission` (mục 10) | ✅ (yêu cầu mới) |

**Không** đụng vào: `fol_model.py`, `qa_model.py` (logic generate), hay bất kỳ prompt nào
của FOL stage. Trọng tâm là 1 hàm tất định + 2 chỗ gọi nó, cộng việc surface `fol` ra output.

---

## 10. BỔ SUNG (yêu cầu mới): thêm trường `fol` vào `reasoning`

**Mục tiêu:** đưa danh sách FOL do model 1 sinh ra vào response, **cùng cấp với `type` và
`steps`** trong object `reasoning`, để dễ debug Stage 1 ngay trên output.

```json
"reasoning": {
  "type": "fol",
  "steps": ["Rule: ...", "Fact: ...", "Conclusion: ..."],
  "fol": [                                  // ← TRƯỜNG MỚI
    "∀x (CompletedResearch(x) → SubmittedThesis(x))",
    "...",
    "(no FOL — premise only states that information is absent/unknown)"
  ]
}
```

> **`fol` LUÔN là bản FOL CUỐI — sau khi đã chạy qua regex neutralize (mục 5).**
> Tức ĐÚNG cái FOL mà QA đã đọc để suy luận — KHÔNG in bản thô trước neutralize.
> Lý do: nhìn `fol` + `steps` phải khớp nhau (steps reason trên đúng FOL này), và người đọc
> thấy luôn ô nào đã bị thay sentinel → hiển thị nhất quán, không gây hiểu nhầm.
> Đây chính là `PipelineOutput.fol_list` (đã là bản neutralize nếu làm mục 6.2).
> Bản thô `fol_raw` chỉ dùng debug nội bộ, **KHÔNG** đưa vào `reasoning.fol`.

### 10.1. `app/logic_solution/utils/postprocess.py` — `format_submission`

Thêm param `fol_list` và đặt vào `reasoning`:

```python
def format_submission(
    query_id: str,
    answer: str,
    explanation: str,
    premises_used: list[int] | None = None,
    reasoning_steps: list[str] | None = None,
    options: list[str] | None = None,
    unit: str = "",
    fol_list: list[str] | None = None,        # ← THÊM
) -> dict:
    return {
        "query_id":      str(query_id),
        "answer":        snap_answer_to_options(answer, options or []),
        "unit":          str(unit or ""),
        "explanation":   clean_explanation(explanation),
        "premises_used": list(premises_used or []),
        "reasoning": {
            "type":  "fol",
            "steps": list(reasoning_steps or []),
            "fol":   list(fol_list or []),    # ← THÊM (cùng cấp type/steps)
        },
    }
```

### 10.2. `app/logic_solution/run.py` — truyền `fol_list` khi gọi

Trong vòng lặp, chỗ gọi `format_submission(...)`, thêm:

```python
submission = format_submission(
    query_id        = query_id,
    answer          = out.answer,
    explanation     = out.explanation,
    premises_used   = out.premises_used,
    reasoning_steps = out.reasoning.get("steps", []),
    options         = options,
    unit            = out.unit,
    fol_list        = out.fol_list,           # ← THÊM (đã là bản neutralize từ ensemble.run)
)
```

> `PipelineOutput.fol_list` đã có sẵn (ensemble.py dòng ~107). Không cần đổi `PipelineOutput`.

### 10.3. `app/core/pipeline_logic.py` (luồng vLLM) — surface `fol` trong reasoning

`run_logic_pipeline` hiện trả flat dict (`fol` dạng string join + `reasoning_steps` rời).
Có 2 lựa chọn, chọn 1:

- **(khuyến nghị)** Đổi field `fol` từ string sang **list** cho khớp output schema:
  ```python
  return {
      "answer": answer,
      "explanation": explanation,
      "fol": fol_list,                 # ← list thay vì "\n".join(fol_list), khớp reasoning.fol
      "premises_used": premises_used,
      "reasoning_steps": reasoning_steps,
      ...
  }
  ```
  rồi tại **chỗ lắp ráp response BTC cuối cùng** (route gọi `run_logic_pipeline` — thường ở
  `app/api/routes/logic.py`), khi dựng object `reasoning`, đặt thêm `"fol": result["fol"]`
  vào cùng cấp `type` và `steps`.

- Hoặc nếu muốn tối thiểu thay đổi: giữ `fol` string như cũ cho client cũ, đồng thời thêm
  `"fol_list": fol_list` để route dùng dựng `reasoning.fol`.

> ⚠️ **TÌM chỗ lắp ráp `reasoning` cho luồng vLLM**: `pipeline_logic.py` KHÔNG tự dựng
> object `{reasoning:{type,steps}}` — việc đó nằm ở route/handler gọi nó. Người sửa cần
> mở route đó và thêm `fol` vào cùng chỗ đang set `type`/`steps`. Hai luồng (in-process
> `run.py` và vLLM route) phải cho ra **cùng** cấu trúc `reasoning`.

### 10.4. Schema BTC — ĐÃ XÁC NHẬN OK

Unified Output Schema của BTC định nghĩa `reasoning = {type, steps}`; `fol` là field dư.
**Đã xác nhận BTC chấp nhận field dư (bỏ qua key lạ)** → để `fol` luôn bật, không cần toggle.
`reasoning.fol` an toàn để giữ thường trực trong output (vừa nộp được, vừa tiện debug Stage 1).
