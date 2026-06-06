# Prompt làm sạch dữ liệu — Answer ↔ Explanation (lỗi ngữ nghĩa)

Tài liệu này mô tả **prompt** và **logic** sẽ dùng để làm sạch dataset
`Logic_Based_Educational_Queries.json`, tập trung vào **lỗi ngữ nghĩa** giữa nhãn
`answer` và phần `explanation`.

---

## 1. Đặc tả đã thống nhất

- **Nguồn chuẩn = `explanation`.** Luôn tin kết luận của explanation (nó chứa reasoning
  có trước khi đưa ra đáp án). **KHÔNG** tự giải lại từ premises, **KHÔNG** thẩm định lại
  tính đúng logic của explanation.
- **Bỏ qua FOL hoàn toàn** (một model khác sẽ sinh lại FOL khi inference). **`premises-NL`
  là chuẩn**, chỉ dùng làm ngữ cảnh để hiểu explanation đang ủng hộ đáp án nào. Không audit,
  không log FOL.
- **Quyết định mỗi mẫu:**
  - Explanation **RÕ RÀNG** ủng hộ một verdict duy nhất (chữ cái A–D cho MCQ; Yes/No/Unknown
    cho câu Yes-No):
    - nếu `answer` lệch → **SỬA** `answer` theo explanation (gồm cả 2 chiều của lỗi nhãn
      Unknown: answer cụ thể nhưng explanation → Unknown; và answer = Unknown nhưng
      explanation suy ra verdict cụ thể);
    - nếu đã khớp → **GIỮ** (không đổi, không log).
  - Explanation **KHÔNG RÕ** (ủng hộ nhiều đáp án / mơ hồ sáo rỗng / chỉ lờ mờ nghiêng
    Unknown mà không cam kết) → **DROP**.
- **Đầu vào:** `Logic_Based_Educational_Queries.json.bak` (raw gốc đầy đủ — 411 record / 808 câu).
- **Đầu ra:** `Logic_Based_Educational_Queries_clean.json` (giữ nguyên file gốc) + một file CSV log.
- **CSV log (tối giản):** `record_idx, q_idx, reason, old_answer, new_answer, note`
  với `reason` ∈ {`được sửa đổi`, `drop`}.
- **Cách chạy:** fan-out nhiều subagent song song, mỗi subagent xử lý một batch (~50 mẫu).

---

## 2. Prompt cho mỗi subagent

```text
You are a data-cleaning judge for a logic-QA dataset. Each item has natural-language
premises (premises_nl), a question, a gold `answer` label, and a gold `explanation`.

GROUND-TRUTH RULE — read carefully:
- The `explanation` is the SOURCE OF TRUTH: it holds the reasoning that precedes the answer.
  You TRUST the explanation's stated conclusion.
- You do NOT re-derive the answer from the premises, and you do NOT judge whether the
  explanation's logic is actually correct. premises_nl are given ONLY to help you interpret
  which option the explanation endorses. Ignore FOL entirely (it is not provided).

STEP 1 — Determine the SINGLE verdict the explanation CLEARLY supports.
- Multiple-choice question (text contains options "A.", "B.", "C.", "D."):
  * a letter A/B/C/D when the explanation clearly endorses that one option
    ("making option X correct", "supporting option X", "(option X)", "so X is correct",
    or describes a conclusion matching exactly one option's content);
  * "Unknown" when it clearly concludes NO option can be validly inferred / cannot be determined.
- Yes/No question (no A-D options; e.g. "Is the statement true?", "Do all...?",
  "Does it follow?", "Can...?"):
  * "Yes"  -> concludes the statement is true / holds / follows / "so all X" / "making the statement true";
  * "No"   -> concludes false / does not follow / not sufficient / not all;
  * "Unknown" -> concludes cannot be determined / uncertain / no premise guarantees it.

STEP 2 — Decide the action by comparing the explanation's supported verdict to `answer`:
- CLEAR and equals `answer`      -> action "keep" (omit from output).
- CLEAR and differs from `answer`-> action "fix": new_answer = the verdict the explanation
  supports. (Includes: explanation clearly supports Unknown but answer is a specific option
  -> fix to Unknown; AND answer is Unknown but explanation clearly derives a specific
  verdict -> fix to that verdict.)
- NOT CLEAR -> action "drop". "Not clear" = the explanation endorses MORE THAN ONE
  option/verdict, OR is vague/non-committal ("requiring steps to confirm", "derived through
  multiple steps" with no real conclusion), OR only weakly/ambiguously leans toward Unknown
  without committing. When in doubt about clarity, DROP.

Distinguish a CLEAR Unknown (decisively "no valid option / cannot be determined") from an
AMBIGUOUS explanation (drop). Never invent a verdict the explanation does not state.

INPUT: Read the JSON file at <BATCH_PATH> — a list of
{id, question, premises_nl, answer, explanation}.

OUTPUT: ONLY a JSON array containing items whose action is "fix" or "drop" (omit "keep").
Each element:
{"id": <int>, "action": "fix"|"drop", "old_answer": "<current>",
 "new_answer": "<A|B|C|D|Yes|No|Unknown>"|null,
 "explanation_supports": "<A|B|C|D|Yes|No|Unknown|ambiguous>",
 "note": "<short: quote the explanation's deciding phrase, or why ambiguous>"}
For "drop", new_answer = null. No prose, no markdown fences.
```

---

## 3. Quy trình orchestrate (sau khi duyệt)

1. Flatten raw gốc → items `{id, record_idx, q_idx, question, premises_nl, answer, explanation}`,
   chia batch ~50, ghi ra các file batch.
2. Fan-out subagent song song với prompt ở mục 2 (mỗi agent một batch).
3. Tổng hợp các quyết định `fix` / `drop`; áp dụng:
   - `fix` → đổi `answer` tại `(record_idx, q_idx)`;
   - `drop` → bỏ câu đó khỏi record;
   - còn lại → giữ nguyên. Bỏ record nào rỗng câu hỏi.
4. Ghi `Logic_Based_Educational_Queries_clean.json` + CSV log
   (`reason`: fix → `được sửa đổi`, drop → `drop`; `note` chứa verdict + trích dẫn quyết định).
5. Báo cáo: số mẫu fixed / dropped / kept, phân phối nhãn trước–sau.

---

## 4. Ví dụ áp dụng (minh hoạ logic)

| Tình huống | answer gốc | explanation kết luận | Hành động | new_answer |
|---|---|---|---|---|
| MCQ, explanation "making option B correct" | D | B | **fix** | B |
| MCQ, answer Unknown, explanation suy ra 1 option rõ ràng | Unknown | C | **fix** | C |
| MCQ, explanation "no option is valid / cannot determine" | A | Unknown | **fix** | Unknown |
| Yes/No, explanation "making the statement true" | No | Yes | **fix** | Yes |
| Yes/No, explanation "is false / does not follow" | Yes | No | **fix** | No |
| Explanation mơ hồ "derived through multiple steps", không chốt | No | (ambiguous) | **drop** | — |
| Explanation ủng hộ cả 2 option / lờ mờ nghiêng Unknown | Unknown | (ambiguous) | **drop** | — |
| Explanation khớp answer | B | B | keep (không log) | — |
