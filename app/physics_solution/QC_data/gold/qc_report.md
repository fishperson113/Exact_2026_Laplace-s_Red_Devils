# QC report (execution-grounded)

- input problems: **1671**
- CLEAN **1546** | FIX **38** | DROP **66** | error/pending 21
- kept (CLEAN+FIX) -> `problems_qc.jsonl`: **1605**
- fixed (review) -> `qc_fixed.jsonl`: **38**
- dropped (review) -> `qc_dropped.jsonl`: **66**

## FIX by error_type
- missing_unit: 6
- sign_corruption: 2
- number corruption: 2
- missing unit: 2
- number_corruption: 2
- corrupted exponent in Coulomb's constant: 1
- corrupted_digit: 1
- OCR/typo – exponent digit misread: 1
- corrupted exponent (6 <-> 9): 1
- missing unit specification: 1
- dropped_symbol: 1
- missing percent sign: 1
- missing_percent_requirement: 1
- corrupted number/math symbol: 1
- ocr_typo: 1
- missing π: 1
- dropped_math_symbol: 1
- single_digit_typo: 1
- missing_radical: 1
- extra_π_symbol_in_number: 1
- missing radical (1/√3 written as 1/3): 1
- unit_corruption: 1
- corrupted number: 1
- unit_ocr_corruption: 1
- extraneous digit: 1
- decimal_point_loss: 1
- typo: 1
- swapped_resistivity_values: 1
- corrupted number (likely OCR misread '0.1' as '0.5'): 1

## DROP by error_type
- fix_unconfirmed: 11
- none: 11
- missing_data: 3
- wrong_given_answer: 2
- missing_diagram: 2
- answer_mismatch: 2
- incorrect_answer_key: 2
- answer_key_wrong: 2
- missing_info: 1
- answer_key_error: 1
- ambiguous_corruption_or_wrong_answer: 1
- missing_geometry: 1
- missing_figure: 1
- missing_information: 1
- missing_qualifier: 1
- missing_question: 1
- given_answer_wrong: 1
- inconsistent_statement: 1
- invalid_correct_answer: 1
- incorrect_gold_answer: 1
- missing_percentage: 1
- given_answer_wrong_or_text_incomplete: 1
- missing_units_specification: 1
- truncated: 1
- likely physics-meaning word change: 1
- corrupted_statement: 1
- ambiguous_corruption: 1
- wrong_physics_word_not_repairable: 1
- correct_answer_mismatch: 1
- unrepairable: 1
- incorrect_answer: 1
- given_answer_incorrect: 1
- missing_options_or_ambiguous: 1
- statement_error: 1
- corrupt_answer: 1
- incorrect_given_answer: 1
- truncated_statement: 1
- answer_error: 1
- missing_definition: 1

## DROP by source
- btc_golden: 33
- vietjack: 33

## DROP by domain
- CH: 23
- LDDT: 16
- TD: 13
- NL: 5
- DDT: 5
- THCB: 4
