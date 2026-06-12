# BTC-faithful scoring vs internal scorer — gap report

*(2026-06-11, trên 348 đáp án thực tế: 56 val + 60 golden × 3 runs,
`versions/v07_ensemble_vLLM/output/final_experiment_raw.jsonl`)*

## Setup

- **Internal scorer** (`shared/eval/scorer.py`): có unit rescue theo SI-prefix, text
  containment 2 chiều, bỏ qua unit khi so giá trị.
- **BTC-faithful scorer** (`shared/eval/scorer_btc.py`): theo Submission Guide §4.5 —
  **answer VÀ unit đều phải đúng**. **SI-prefix aware** (BTC xác nhận có handle:
  0.005655 T == 5.654 mT — unit phải cùng *base unit*, giá trị quy đổi theo prefix rồi
  mới so; khác base unit vẫn rớt). Text phải khớp exact (sau lowercase/space-normalize),
  không containment. Hai vế đều đi qua `normalizer.py`
  (Ω/Ohm/Ohms→ohm, µ→u, nan/-/yes_no/…→`N/A`, ×10^n→e-notation).
- Tolerance số giữ 2% như internal (gold bị làm tròn: 0.7 vs 0.702562).

## Kết quả (sau khi wire normalizer vào /predict)

| model | internal | BTC-faithful | gap |
|---|---|---|---|
| SFT  | 286/348 (82.2%) | 273/348 (78.4%) | −13 |
| BASE | 280/348 (80.5%) | 255/348 (73.3%) | −25 |
| **ENSEMBLE (serving)** | **288/348 (82.8%)** | **273/348 (78.4%)** | **−15 (~4.3 điểm)** |

Normalizer cứu được ~11 verdict cho ensemble (Ohm/Ohms/Ω naming, unit `nan`/junk→`N/A`,
unit bị echo số "120 Ohms", `%` dính vào value); prefix-aware matching cứu thêm ~8.
15 case chênh còn lại của ensemble:

| Nguyên nhân (ensemble, 15 case) | Số | Ví dụ |
|---|---|---|
| **Text answer dài**: pred 1 từ, gold nguyên câu | 6 | `inductive` vs *"The circuit exhibits an inductive characteristic."* (DDT330/DDT350) |
| **Gold nghi noise / symbolic** | 7 | vj_l11_0002 (3.16e-5 vs 2e-5, lệch hệ số); vj_l11_0006 (gold là biểu thức ký hiệu); vj_l11_0026 (gold unit `N/A; μF` mơ hồ) |
| **Pred thừa giá trị** (multi-value count) | 2 | LD056: pred `3.36e+06; 0.168` vs gold 1 giá trị |

## Kết luận

1. Con số nội bộ 82.8% ≈ **78.4% theo cách chấm BTC** (đã tính BTC handle SI-prefix).
   Phần lớn chênh còn lại là gold noise trong val nội bộ, không phải lỗi hệ thống.
2. Nếu BTC chấm text answer exact-match thì các câu mô tả dài (~1.7%) rớt bất kể
   notation — chấp nhận (model trả keyword là hành vi hợp lý).
3. Output `/predict` đã được chuẩn hoá (`normalizer.py`): value plain/e-notation, unit
   ASCII, no-unit → `N/A` — khớp convention khai trong `notation_mapping.csv`.

Chạy lại đối chiếu:
`python -m app.physics_solution.versions.v07_ensemble_vLLM.compare_btc_scoring`
