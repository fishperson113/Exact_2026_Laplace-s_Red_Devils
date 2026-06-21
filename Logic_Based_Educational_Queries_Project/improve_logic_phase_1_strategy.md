# Improve Logic — Phase 1 Strategy

> Tài liệu tổng hợp toàn bộ lỗi đã phân tích từ
> `outputs/Phase_1/exact_eval_round1_Laplaces-red-devils.json` và hướng dẫn cài đặt lại
> (prompt + code). Team: **Laplaces-red-devils**.

---

## 0. Cách chấm điểm (đã giải ngược, khớp 100% với file eval)

| Loại | Công thức 1 câu | Ghi chú |
|---|---|---|
| **Type 1** | `sample = 0.5·P1 + 0.5·P2` | P1 = đúng đáp án, P2 = `premises_used` (F1) |
| **Type 2** | `sample = P1` | Chỉ chấm đáp án (+ đơn vị) |

- `type1_points = Σ sample / 100`, `type2_points = Σ sample / 100` (mỗi câu tối đa 1.0 điểm).
- `base = type1_points + type2_points`. Bonus: **time 10%** + **data correctness 10%** cộng trên base.
- **P2 = F1** giữa tập `premises_used` của model và gold (precision = không thừa, recall = không thiếu). Thừa **và** thiếu đều bị phạt.

**Hiện trạng (round1):** type1 = **20.79**, type2 = **24.00**, base = **44.79**, time = **3.78**, **TỔNG = 48.57**.

---

## 1. Danh sách lỗi

### 1A. `wrong_answer` — P1 = 0 (mất nặng nhất)

| ID | Dạng | Đúng / Model | Nguyên nhân |
|---|---|---|---|
| T1_0025 | mcq | C / **B** | Giả định `operator_assigned` (không cho) → suy thừa 1 bước |
| T1_0024 | yes_no_uncertain | No / **Yes** | Giả định `manager_sign_off` (không cho) |
| T1_0028 | yes_no_uncertain | No / **Yes** | Giả định `completed_renal_screen` + bỏ qua rule chặn (premise 4) |
| T1_0032 | yes_no_uncertain | No / **Yes** | Bịa fact `redaction_complete` |
| T1_0048 | yes_no_uncertain | Uncertain / **Yes** | Mất premise meta + suy lạc đề (chứng minh blue_badge) |
| T2_0004 | physics | đúng số / **sai đơn vị** | Ghi `V/m`, cần `N/C` (`wrong_unit`) |

### 1B. `wrong_premises_used` — P1 = 100, chỉ mất P2

| ID | Dạng | Bản chất |
|---|---|---|
| T1_0021 | mcq | Explanation đúng, `premises_used` **thiếu** index 3 |
| T1_0007 | mcq | Explanation đúng, `premises_used` thiếu 5 |
| T1_0026 | yes_no_uncertain | Explanation đúng, `premises_used` thiếu 4, 9 |
| T1_0027 | mcq | Explanation đúng, `premises_used` thiếu 0, thừa 2 |
| T1_0031 | mcq | Liệt kê thiếu nhánh phủ định (3,4,9) |
| T1_0035 | mcq | Nhảy cóc, chỉ ghi [2,7,8] thay vì cả chuỗi |
| T1_0023 | mcq | **Thừa** premise 3 (rule không kích hoạt) — *lỗi model, không khiếu nại* |
| T1_0008 | yes_no_uncertain | **Gold sai**: gold thừa 5,6; model đúng [0,1,2,3,4] |

---

## 2. Nguyên nhân gốc (root cause)

### RC1 — Over-derivation: "không được nêu = mặc nhiên đúng" ⭐ (lỗi đắt nhất)
Model coi consequent là suy ra được **dù một vế antecedent chưa có fact**. Nó **tự điền fact còn thiếu**
(`manager_sign_off`, `completed_renal_screen`, `redaction_complete`, `operator_assigned`).

**Bằng chứng quyết định — model mâu thuẫn giữa MCQ và Yes/No/Uncertain (cùng kịch bản):**

| Kịch bản | MCQ | Yes/No/Uncertain |
|---|---|---|
| Atlas closure | T1_0023 → **ĐÚNG** ("chưa established") | T1_0024 → **SAI** (Yes) |
| Mira dose | T1_0027 → **ĐÚNG** ("cần review") | T1_0028 → **SAI** (Yes) |
| River Codex | T1_0031 → **ĐÚNG** ("chưa safe") | T1_0032 → **SAI** (Yes) |

→ Dạng MCQ có sẵn đáp án "...not established" làm "mồi" cho model dừng đúng. Dạng Yes/No/Uncertain
không có mồi → model forward-chain tham lam tới "Yes". **4/5 câu `wrong_answer` rơi vào Yes/No/Uncertain.**

**Lưu ý:** model xử lý ĐÚNG khi điều kiện thiếu được nêu **tường minh là phủ định** ("lacks X", "no X" —
xem T1_0016, T1_0007, T1_0039). Lỗi chỉ xảy ra khi fact **vắng mặt thầm lặng**. Năng lực closed-world
đã có, chỉ cần kích hoạt đúng.

### RC2 — Mất premise meta + không neo vào predicate được hỏi (T1_0048)
- Premise 7 ("No premise states that Linh has pharmacy training") **có trong input**, nhưng bước
  formalize FOL quy nó về placeholder `(no FOL — ...)` → bị engine reasoning bỏ qua.
- Model lại đi chứng minh predicate **khác** (`blue_badge`) rồi trả "Yes", thay vì neo vào
  `pharmacy_training(Linh)` được hỏi.
- Đây là premise epistemic — **chính là cơ sở để trả Uncertain**. Vứt nó = mất cơ sở.

### RC3 — Bookkeeping `premises_used` (lỗi "chặng cuối", không phải lỗi tư duy)
- `premises_used` do **model tự sinh** trong JSON, prompt buộc nó khớp với các bước **`Rule:`/`Fact:`**
  (xem `prepare_data.py` dòng 37). Khi model **quên liệt kê một dòng `Rule:`** (dù bước `Derive:` và
  explanation vẫn dùng premise đó) → `premises_used` rớt index → P2 giảm.
- Code hiện **chỉ đọc lại** field model khai, **không** đối chiếu với explanation.

### RC4 — Nhiễu gold label (không cứu được bằng model)
- T1_0008: gold thừa premise 5,6 (vô can với câu hỏi). → khiếu nại.
- T1_0028: gold dùng premise 1 mà thiếu premise 0 (mâu thuẫn nội tại). → P2 có nhiễu nền.

### RC5 — Đơn vị Type 2 (T2_0004)
Trị số đúng, đơn vị tương đương vật lý nhưng sai quy ước (`V/m` vs `N/C`). Grader so khớp chuỗi.

---

## 3. Điểm model đang làm TỐT (giữ nguyên, không phá)
- Forward-chaining đa bước chắc chắn (T1_0030 4 bước, T1_0034 3 bước → P1=P2=100).
- Hình thức hóa FOL ổn định (∀, →, ¬; tách Rule/Fact/Derive/Conclusion).
- Xử lý đúng phủ định tường minh ("lacks/no") và "unknown" khi được flag thành premise (T1_0041, T1_0042).
- Tốc độ tốt (<13s/câu → ăn time bonus).

---

## 4. Cách sửa (theo thứ tự ưu tiên tác động điểm)

### FIX 1 — Closed-world reasoning cho Yes/No/Uncertain (tác động ~ +3.6 điểm Type 1) ⭐
**Vị trí:** `src/models/QA_model/prepare_data.py` → `SYSTEM_PROMPT_QA_COT`.

Thêm quy tắc quyết định 3 nhánh + cấm tự điền fact:

```
### Decision procedure (apply to EVERY question)
1. Identify the exact predicate X asked. Conclude ONLY about X.

2. GUARD (highest priority): a condition that is merely ABSENT (not mentioned, no fact)
   is UNKNOWN — neither true nor false. Never assume it true, and never assume it false
   (do NOT derive a negation from it). To apply a rule, every conjunct of its antecedent
   must have an explicit fact OR be previously derived. Never assume or invent a missing
   condition.

3. Classify the question framing:
   - PROVE-framing : "Do the premises prove / establish / show X?" or "Does X guarantee /
                      ensure / meet ALL requirements for Y?"
   - VALUE-framing : "Is it true that X? / Is X true? / Does ... have X? / Are all ... ?"

4. Evaluate IN THIS ORDER:
   a. Is ¬X derivable, or is X blocked/refuted? (an explicit false condition, a rule that
      forbids it, or a counterexample to a universal claim)            -> answer No
   b. Else, is X FULLY proven (every antecedent satisfied by facts/derivations)?
                                                                        -> answer Yes
   c. Else  (X is neither proven nor refuted — some required condition is only ABSENT):
        - PROVE-framing -> No        (the premises do not establish / guarantee X)
        - VALUE-framing -> Uncertain (last resort)

Never output Yes when any required condition is only absent. Use Uncertain ONLY at step 4c
and ONLY for VALUE-framing.
```

> Tận dụng năng lực có sẵn: diễn đạt "absent = giống lacks/unknown mà model vốn xử lý đúng (T1_0016)".

### FIX 1b — Ranh giới No vs Uncertain (quick rules + 1 cặp đối chứng)

Quét toàn bộ train (352 câu Yes/No/Uncertain → 303 Yes / **28 No** / **21 Uncertain**). Ranh giới:

- **No = mệnh đề bị BÁC BỎ (disproved):** có điều kiện bị nêu sai/chặn, có phản ví dụ phá mệnh đề
  "tất cả", phủ định suy ra được, hoặc framing "guarantee/meet-all" mà một điều kiện không được đảm bảo.
- **Uncertain = KHÔNG quyết được (undecidable):** hỏi "ALL/every" nhưng chỉ có "some/∃" và không có
  phản ví dụ; hoặc predicate được hỏi hoàn toàn không xuất hiện trong premises; hoặc một implication
  hợp lý nhưng không bị ép buộc cũng không bị mâu thuẫn.

> Một câu: **có bằng chứng phá → No; không phá được nhưng cũng không đủ khẳng định → Uncertain.**

**Quick rules (bản gọn ~60 token — ƯU TIÊN nhét vào prompt cho model nhỏ; rẻ token, ít loãng attention):**

```
### No vs Uncertain — quick rules
- A required condition is explicitly false / a counterexample defeats an "all" claim /
  the negation is derivable                                              -> No
- "guarantee / ensure / meet ALL ... for Y?" + some needed condition not assured  -> No
- "Are all/every ...?" but premises give only "some / ∃", with no counterexample  -> Uncertain
- The queried predicate never appears in ANY premise                     -> Uncertain
- Default reminder: a condition that is merely ABSENT (not mentioned in the reasoning chain)
  is UNKNOWN — neither true nor false. Never assume it true, and never assume it false
  (do NOT derive a negation from it).
```

> Trong prompt inference CHỈ dùng **quick rules + 1 cặp đối chứng** (rec 71 bên dưới) là đủ —
> **KHÔNG dán few-shot dài vào prompt** (kéo dài prompt → chậm prefill + loãng attention model nhỏ).
> Nếu muốn nhồi nhiều case ranh giới → soạn thẳng vào **SFT data** theo đúng format `prepare_data.py`
> (steps + JSON `premises_used/explanation/answer`), không để trong prompt.

**Cặp đối chứng vàng (cùng một bộ premises, record 71):**
`"Are all biometric systems secure?"` → **No** (có phản ví dụ ∃ not-secure) vs
`"Are all biometric systems portable?"` → **Uncertain** (không thông tin nào). Dùng cặp này làm
ví dụ "đinh" để model phân biệt rõ "có bằng chứng phá" vs "không có thông tin".

### FIX 2 — Chuẩn hóa đơn vị Type 2 (tác động +1.0 điểm Type 2)
**Vị trí:** prompt physics (Type 2) hoặc bước postprocess đơn vị.

```
Output the unit in the conventional SI form for the quantity:
electric field = N/C (NOT V/m), potential = V, energy = J, capacitance = F, ...
```
(Có thể thêm bảng ánh xạ đơn vị tương đương ở postprocess để ép `V/m -> N/C`.)

### FIX 3 — Giữ NL của premise epistemic + neo predicate (cứu T1_0048)
**3a. Pipeline (code):** với premise epistemic, **GIỮ NGUYÊN câu NL trong ô FOL** (gắn cờ `[UNCERTAIN]`),
thay vì sentinel trống. Đã sửa trong `neutralize_epistemic_fol` (`prepare_data.py`):

```python
_EPISTEMIC_FOL_TAG = "[UNCERTAIN]"
def neutralize_epistemic_fol(premises_nl, fol_list):
    out = list(fol_list)
    for i, nl in enumerate(premises_nl):
        if i < len(out) and is_epistemic_premise(nl):
            out[i] = f"{_EPISTEMIC_FOL_TAG} {str(nl).strip()}"   # giữ NL, còn predicate dưới dạng chữ
    return out
```
→ **Không** trích predicate bằng code (NL parsing khó). Giữ NL nguyên văn → Model 2 đọc trực tiếp câu
"...No premise states that Linh has pharmacy training" + câu hỏi để suy ra Uncertain.
→ Phải áp `neutralize_epistemic_fol` ở **cả đường Ensemble** (xem 9.A) — hiện đang thiếu.

**3b. Prompt:** khối "Handling premises that state information is absent/unknown" đã cập nhật theo cờ
`[UNCERTAIN]` (`prepare_data.py`). Củng cố thêm neo predicate ở bước 1 của Decision procedure (FIX 1).

### FIX 4 — Đồng bộ `premises_used` với explanation (tác động ~ +0.3 điểm)
**Vị trí:** `src/models/QA_model/inference.py` → `_parse_output` (dòng 158–222), và bản song song
`src/models/Ensemble_Model/inference.py` → `_parse_output` (dòng 295–357).

Sau khi parse, **ghi đè** `premises_used` bằng cách trích từ explanation + các bước `Derive:`:

```python
def _premises_from_text(explanation, reasoning_steps):
    txt = (explanation or "") + " " + " ".join(reasoning_steps or [])
    return sorted({int(n) for n in re.findall(r"premise\s+(\d+)", txt, re.I)})
# premises_used = union(model_emitted, _premises_from_text(...))  hoặc thay thế hẳn
```
Đã kiểm chứng: với T1_0021/0007/0026/0027, cách này tái tạo **đúng gold**.

> Bổ trợ (prompt): thêm vào output format — *"premises_used = đúng tập index (0-based) các premise đã
> trích trong explanation, không thừa không thiếu"*, và sửa few-shot example sang **0-based**.

---

## 5. Khiếu nại chấm lại (gửi RIÊNG cho ban tổ chức)
Phase 1 chỉ chấm answer + `premises_used` (không chấm explanation). Đề nghị:
- **Re-parse `premises_used` từ explanation** cho: **T1_0021, T1_0007, T1_0026, T1_0027**
  (explanation khớp gold, mảng bị lệch do serialize).
- **Review gold key T1_0008**: gold thừa 5,6; tập đúng là [0,1,2,3,4].
- **KHÔNG** khiếu nại T1_0023 (model thừa premise 3 — lỗi model, ngược lập luận, gây bất nhất).

Tác động khiếu nại nếu được chấp nhận: tổng ~48.57 → **~48.88**.

---

## 6. Bảng ưu tiên (impact ↓)

| Ưu tiên | Hạng mục | Cách | Điểm ước tính |
|---|---|---|---|
| 1 | Closed-world Yes/No/Uncertain (RC1) | FIX 1 (prompt) | **~ +3.6** (Type 1) |
| 2 | Đơn vị Type 2 (RC5) | FIX 2 | **+1.0** (Type 2) |
| 3 | Meta-premise + neo predicate (RC2) | FIX 3 | nằm trong +3.6 (T1_0048) |
| 4 | Đồng bộ premises_used (RC3) | FIX 4 (code) | ~ +0.3 |
| 5 | Khiếu nại gold/parse (RC3, RC4) | Section 5 | ~ +0.3 |

> **Trọng tâm:** FIX 1 + FIX 2. Hai cái này là lỗi thật của model và cho phần điểm lớn nhất.
> Các fix bookkeeping/khiếu nại chỉ vớt phần nhỏ — làm song song, không phải ưu tiên.

---

## 7. Checklist cài đặt lại
- [ ] Cập nhật `SYSTEM_PROMPT_QA_COT` (`prepare_data.py`): thêm Decision procedure 3 nhánh (FIX 1).
- [ ] Thêm chuẩn hóa đơn vị cho Type 2 (FIX 2).
- [ ] Đảm bảo premise meta giữ nguyên văn `[META]` trước khi vào QA model (FIX 3a).
- [ ] Ghi đè `premises_used` từ explanation trong `_parse_output` (FIX 4) — cả QA_model lẫn Ensemble_Model.
- [ ] (Tùy chọn) Thêm `premises_used` 0-based vào few-shot example của prompt.
- [ ] Chạy lại eval trên `dev`, so P1/P2 trước–sau, xác nhận không hồi quy các câu đang đúng.
- [ ] Gửi đơn khiếu nại (Section 5) riêng cho ban tổ chức.

---

## 8. Mẫu prompt QA hoàn chỉnh + Input/Output thực tế

> Đã tích hợp các rule vào `src/models/QA_model/prepare_data.py` → `SYSTEM_PROMPT_QA_COT`
> (đây là prompt ACTIVE — cả `QA_model/inference.py` lẫn `Ensemble_Model/inference.py` đều import).
> Bản trong `FOL_Z3/prompts.py` là **bản trùng cũ, không dùng cho inference** — bỏ qua.

### 8.1. SYSTEM prompt (đã tích hợp — bản đang dùng)

```
### Role
You are a logic-based educational QA system. You are given natural-language premises (indexed from 0), their First-Order Logic (FOL) translations, the answer options, and a question.

### How to read options (follow this convention ABSOLUTELY)
- If options is non-empty: answer MUST be EXACTLY one of the provided option entries, verbatim — no adding/removing/paraphrasing, no invented text. If options are letters (A/B/C/D) -> answer the letter; if full statements -> answer the statement; yes/no -> exactly "Yes"/"No"/"Uncertain".
- If options is empty ([]): free-form answer (a number or short text).
For a yes/no question the options are ["Yes", "No", "Uncertain"]; choose "Uncertain" only when the premises are genuinely insufficient.

### Output
First, reason in ordered steps over the FOL premises. Each step starts with exactly one prefix:
- Rule: / Fact: / Derive: / Conclusion: (Conclusion is the last step, exactly one).
Write Rule:/Fact:/Derive: in FOL notation; every Rule:/Fact: must come from a given FOL premise — never invent one.
Then output ONE JSON object on the final line, "answer" LAST:
{"premises_used": [<0-based indices>], "explanation": "<concise justification>", "answer": "<answer>"}

### premises_used and explanation (STRICT — both are graded)
- premises_used = EXACTLY the 0-based indices cited in your Rule:/Fact: steps — no more, no less.
- In explanation, cite every premise you rely on as "premise N" (0-based) explicitly.
- The "premise N" set in explanation MUST equal premises_used.
- Do NOT count a premise whose rule does not fire / that you only mention to reject.

### Closed-world decision procedure (apply to EVERY question)
1. Identify the exact predicate X asked. Conclude ONLY about X.
2. An ABSENT condition is UNKNOWN — neither true nor false. Never assume true, never derive its negation. Every antecedent conjunct needs an explicit fact or prior derivation.
3. Framing: PROVE ("prove/establish/guarantee/meet ALL") vs VALUE ("is X / has X / are all").
4. In order: (a) ¬X derivable or X blocked/counterexampled -> No; (b) X fully proven -> Yes;
   (c) only-absent condition -> PROVE:No / VALUE:Uncertain.

### No vs Uncertain — quick rules
- explicit-false condition / counterexample to "all" / negation derivable -> No
- "guarantee/meet ALL ...?" + needed condition not assured -> No
- "all/every ...?" but only "some/∃", no counterexample -> Uncertain
- queried predicate never appears in any premise -> Uncertain

### Handling premises that state information is absent/unknown
A FOL line prefixed "[UNCERTAIN]" (the premise's original sentence) means that fact is UNKNOWN:
treat it as UNKNOWN (do NOT negate it); if your conclusion relies on it, add a Fact: step
"Fact: premise i states <X> is unknown", cite "premise i", include i in premises_used.
Answer "Uncertain" unless OTHER premises decide.
```
*(Bản đầy đủ nằm trong code; ở đây rút gọn cho dễ đọc.)*

### 8.2. Mẫu 1 — VALUE-framing → **Uncertain** (cơ chế premise epistemic)

Premise 7 là NL "vắng mặt thông tin" → `neutralize_epistemic_fol` GIỮ NGUYÊN câu NL trong ô FOL, gắn cờ `[UNCERTAIN]` (predicate vẫn còn dưới dạng chữ).

**USER (đưa vào QA model):**
```
Premises (NL):
0. If a clinic volunteer has first-aid certification and completed patient privacy training, then the volunteer may assist at the triage desk.
1. If a volunteer may assist at the triage desk and has morning availability, then the volunteer is assigned to the morning triage shift.
2. Every volunteer assigned to the morning triage shift receives a blue access badge.
3. Linh has first-aid certification.
4. Linh completed patient privacy training.
5. Linh has morning availability.
6. The morning triage shift needs 3 volunteers.
7. No premise states that Linh has pharmacy training.

Premises (FOL):
0. ∀v ((first_aid(v) ∧ privacy_training(v)) → triage_eligible(v))
1. ∀v ((triage_eligible(v) ∧ morning_available(v)) → morning_triage(v))
2. ∀v (morning_triage(v) → blue_badge(v))
3. first_aid(Linh)
4. privacy_training(Linh)
5. morning_available(Linh)
6. morning_shift_needs(3)
7. [UNCERTAIN] No premise states that Linh has pharmacy training.

Options:
A. Yes
B. No
C. Uncertain

Question:
Does Linh have pharmacy training?
```

**ASSISTANT (output mong đợi):**
```
Fact: premise 7 states whether pharmacy_training(Linh) is unknown
Derive: no Rule has pharmacy_training(_) as consequent, and no Fact asserts pharmacy_training(Linh)
Derive: pharmacy_training(Linh) is neither provable nor refutable; premise 7 marks it UNKNOWN
Conclusion: pharmacy_training(Linh) is undetermined ⟹ Uncertain
{"premises_used": [7], "explanation": "The question asks about pharmacy_training(Linh). No rule concludes it and no fact asserts it; premise 7 states this information is unknown. It is neither proven nor refuted, so the answer is Uncertain.", "answer": "Uncertain"}
```

### 8.3. Mẫu 2 — PROVE/guarantee-framing → **No** (điều kiện bị chặn, premise tối thiểu đúng)

**USER:**
```
Premises (NL):
0. If a satellite has calibrated thermal sensors, then it can monitor surface temperature.
1. If a satellite can monitor surface temperature and has cloud-penetrating radar, then it can support disaster mapping.
2. If a satellite supports disaster mapping, then it can provide emergency response data.
3. Satellite Vega has calibrated thermal sensors.
4. Satellite Vega does not have cloud-penetrating radar.
5. Satellite Vega has a high-resolution optical camera.
6. All satellites with high-resolution optical cameras can capture daytime images.

Premises (FOL):
0. ∀x (calibrated_thermal(x) → monitor_temp(x))
1. ∀x ((monitor_temp(x) ∧ cloud_radar(x)) → disaster_mapping(x))
2. ∀x (disaster_mapping(x) → emergency_data(x))
3. calibrated_thermal(Vega)
4. ¬cloud_radar(Vega)
5. optical_camera(Vega)
6. ∀x (optical_camera(x) → daytime_images(x))

Options:
A. Yes
B. No
C. Uncertain

Question:
Does having thermal sensors and an optical camera guarantee emergency response data in this case?
```

**ASSISTANT (output mong đợi):**
```
Rule: ∀x (calibrated_thermal(x) → monitor_temp(x))
Rule: ∀x ((monitor_temp(x) ∧ cloud_radar(x)) → disaster_mapping(x))
Rule: ∀x (disaster_mapping(x) → emergency_data(x))
Fact: calibrated_thermal(Vega)
Fact: ¬cloud_radar(Vega)
Derive: calibrated_thermal(Vega) ⟹ monitor_temp(Vega) [modus ponens, premise 0]
Derive: ¬cloud_radar(Vega) makes the antecedent of premise 1 false ⟹ disaster_mapping(Vega) not derivable
Derive: without disaster_mapping(Vega), premise 2 cannot yield emergency_data(Vega)
Conclusion: emergency_data(Vega) is NOT guaranteed ⟹ No
{"premises_used": [0, 1, 2, 3, 4], "explanation": "From premise 3 and premise 0, Vega can monitor surface temperature. But premise 4 says Vega lacks cloud-penetrating radar, so the antecedent of premise 1 fails and disaster mapping is not derivable; therefore premise 2 cannot guarantee emergency response data.", "answer": "No"}
```
> Lưu ý: premise 5, 6 (optical camera / daytime images) **không được cite, không vào premises_used** —
> đúng tập tối thiểu (chính là điểm gold-key của T1_0008 đang sai).

### 8.4. Cơ chế parsing `premises_used` từ explanation (lưới an toàn — FIX 4)

Vì prompt đã BUỘC explanation cite "premise N" và bằng đúng premises_used, ta thêm bước ghi đè
deterministic trong `_parse_output` (cả `QA_model/inference.py` và `Ensemble_Model/inference.py`):

```python
import re
def premises_from_explanation(explanation: str) -> list[int]:
    return sorted({int(n) for n in re.findall(r"premise\s+(\d+)", explanation or "", re.I)})

# trong _parse_output, sau khi lấy parsed["explanation"] và premises_used model tự khai:
expl_idx = premises_from_explanation(parsed.get("explanation", ""))
if expl_idx:                       # explanation có cite → tin explanation
    premises_used = expl_idx       # ghi đè (hoặc: sorted(set(model_pu) | set(expl_idx)))
```

**Kiểm chứng trên 2 mẫu trên:**
- Mẫu 1: explanation chứa "premise 7" → `premises_from_explanation` = **[7]** ✓ (khớp).
- Mẫu 2: explanation chứa "premise 3, 0, 4, 1, 2" → **[0,1,2,3,4]** ✓ (khớp, loại đúng 5,6).

→ Dù model tự khai `premises_used` lệch (bỏ sót / thừa), lưới này tái tạo lại từ explanation đúng.

### 8.5. ⚠ Lưu ý train/inference consistency
`SYSTEM_PROMPT_QA_COT` dùng CHUNG cho cả sinh SFT data (`build_messages_for_sample`) và inference.
Sửa prompt này nghĩa là:
- **Nếu regenerate SFT data + train lại** → train khớp inference, rule có hiệu lực đầy đủ. (khuyến nghị)
- **Nếu chỉ chạy inference trên model CŨ** (đã train bằng prompt cũ) → có **mismatch**; rule mới chỉ là
  "nhắc nhẹ", hiệu quả một phần. Muốn chắc các case Yes/No/Uncertain → **train lại**.

---

## 9. Modules cần chỉnh — code theo Stage

Pipeline: **NL premises → [FOL Stage: Model 1] → FOL → [QA Stage: Model 2] → answer + premises_used**.
Bảng module và trạng thái:

| Stage | Module | Hàm/Thành phần | Trạng thái |
|---|---|---|---|
| FOL | `QA_model/prepare_data.py` | `is_epistemic_premise`, `neutralize_epistemic_fol`, `_EPISTEMIC_FOL_TAG` | ✅ đã sửa (giữ NL + cờ `[UNCERTAIN]`) |
| FOL | `Ensemble_Model/inference.py` | `QAModel.generate` + `generate_batch` | ✅ đã vá (gọi neutralize) |
| QA | `QA_model/prepare_data.py` | `SYSTEM_PROMPT_QA_COT` | ✅ đã sửa (rule + options) |
| QA | `QA_model/inference.py` | `_parse_output` | ✅ đã thêm override (`_from_expl`) |
| QA | `Ensemble_Model/inference.py` | `_parse_output` | ✅ đã thêm override (mirror) |

### 9.A — FOL Stage: chuẩn hóa premise epistemic (FIX 3)

**Hàm (`QA_model/prepare_data.py`, dòng ~183–199) — đã đổi sang giữ NL + cờ `[UNCERTAIN]`:**
```python
_EPISTEMIC_FOL_TAG = "[UNCERTAIN]"
def is_epistemic_premise(nl: str) -> bool: ...
def neutralize_epistemic_fol(premises_nl, fol_list) -> list[str]:
    # ô FOL của mệnh đề "vắng mặt thông tin" → GIỮ NGUYÊN câu NL: "[UNCERTAIN] <nl gốc>"
    # (predicate còn dưới dạng chữ; KHÔNG cần train lại Model 1 vì output của nó bị ghi đè)
```

**GAP cần vá:** đường production `Ensemble_Model/inference.py` đẩy FOL thô từ Model 1 sang QA mà
**KHÔNG** neutralize → nếu Model 1 sinh phủ định giả `¬X` thay vì giữ NL, QA bị dẫn sai (gốc lỗi T1_0048).
Đường standalone `QA_model/inference.py:93` đã có lưới này; cần mirror sang Ensemble:

```python
# Ensemble_Model/inference.py — thêm import
from models.QA_model.prepare_data import (
    ...,
    neutralize_epistemic_fol,            # << THÊM
)

# trong class QAModel.generate(...) — TRƯỚC khi format prompt:
def generate(self, premises_nl, premises_fol, question, options=None, max_new_tokens=...):
    premises_fol = neutralize_epistemic_fol(premises_nl, premises_fol)   # << THÊM (lưới an toàn)
    user_content = USER_TEMPLATE_QA_COT.format(
        premises_nl_block=format_premises_nl(premises_nl),
        premises_fol_block=format_premises_fol(premises_fol),
        ...
    )
# Áp y hệt trong generate_batch(...) (cùng file) để cả batch path được phủ.
```
> Hiệu quả: premise epistemic LUÔN được giữ dạng `[UNCERTAIN] <nl>` trước khi vào QA, bất kể Model 1 sinh gì
> → QA không bao giờ suy `¬X` từ "vắng mặt thông tin", và vẫn thấy predicate dưới dạng chữ. Khớp đúng
> prompt QA (khối "Handling premises ... absent/unknown").

### 9.B — QA Stage: prompt (đã xong)

`QA_model/prepare_data.py` → `SYSTEM_PROMPT_QA_COT` đã tích hợp:
- Decision procedure (GUARD absent=UNKNOWN, framing PROVE/VALUE, thứ tự No→Yes→Uncertain).
- Quick rules No vs Uncertain.
- `premises_used`/`explanation` STRICT (buộc cite "premise N", bằng đúng `premises_used`).
- "How to read options" đã sửa (khớp letter/statement/Yes-No, không bịa text).

> ⚠ Prompt này DÙNG CHUNG train + inference (xem 8.5). Sửa xong nên **regenerate SFT data + train lại**.

### 9.C — QA Stage: override `premises_used` từ explanation (FIX 4)

Thêm helper + ghi đè trong `_parse_output` của **CẢ HAI** file
(`QA_model/inference.py` dòng ~158–222 và `Ensemble_Model/inference.py` dòng ~295–357):

```python
# top-of-file (cạnh các import re có sẵn)
def premises_from_explanation(explanation: str) -> list[int]:
    import re
    return sorted({int(n) for n in re.findall(r"premise\s+(\d+)", explanation or "", re.I)})

# --- Nhánh JSON hợp lệ (sau khi có parsed["explanation"]) ---
expl = str(parsed.get("explanation", "")).strip()
pu_expl = premises_from_explanation(expl)
return {
    "answer": str(parsed["answer"]).strip(),
    "explanation": expl,
    "premises_used": pu_expl if pu_expl else _premises(parsed),   # << tin explanation, fallback model
    "reasoning_steps": reasoning_steps,
}

# --- Nhánh regex-fallback (JSON cụt) — áp cùng logic với biến `explanation` của nhánh đó ---
pu_expl = premises_from_explanation(explanation)
premises_used = pu_expl if pu_expl else premises_used
```
> Vì prompt đã buộc explanation cite "premise N" bằng đúng `premises_used`, override này tái tạo đúng
> tập gold (đã kiểm chứng [7] và [0,1,2,3,4] ở mục 8.4) — vớt P2 ngay cả khi chưa train lại.
> Chọn `pu_expl if pu_expl else model` (ưu tiên explanation); nếu lo explanation sót, đổi thành
> `sorted(set(pu_expl) | set(model_pu))`.

### 9.D — Ngoài phạm vi 2 stage (ghi chú)
FIX 2 (chuẩn hóa đơn vị Type 2: `V/m → N/C`) thuộc **module physics/Type-2**, không nằm ở QA/FOL stage
trên — xử lý riêng ở prompt physics hoặc bước postprocess đơn vị.

### 9.E — ⚠ Dữ liệu train THIẾU case uncertain/epistemic (gốc rễ tầng dữ liệu)

Quét `train/dev/test.csv` (620/78/78 dòng): **0 premise nào** thuộc dạng epistemic
("No premise states whether X" / "It is unknown whether X"). Nghĩa là **model chưa từng thấy**
pattern này lúc train → đây là gốc rễ ở TẦNG DỮ LIỆU khiến T1_0048 sai (eval có, train không).
(21 case Uncertain trong train đều là kiểu ∀-vs-∃, KHÔNG phải epistemic-premise.)

- **Pipeline build SFT đã SẴN SÀNG:** `build_messages_for_sample` → `neutralize_epistemic_fol` đã được
  kiểm chứng: nếu có premise epistemic, FOL tự thành `[UNCERTAIN] <nl>`, assistant target ra
  `premises_used=[i]`, `answer=Uncertain`. (Test synthetic kiểu T1_0048 PASS.)
- **Việc cần làm:** **augment dữ liệu train** bằng các case epistemic (synthetic) — NL premise
  "No premise states whether X", FOL = `[UNCERTAIN] ...`, answer = Uncertain (hoặc No nếu premise khác
  quyết được), `premises_used` = index premise đó. Rồi **train lại QA model**.
- Không augment thì dù prompt + neutralize + `[UNCERTAIN]` đã đúng, model vẫn yếu ở case epistemic vì
  thiếu ví dụ học.

**Regenerate SFT data:** sau khi thêm rows epistemic vào nguồn (CSV/reasoning), chạy lại bước build
dataset (qua `build_messages_for_sample`) — `[UNCERTAIN]` được áp tự động, train khớp inference 1:1.
