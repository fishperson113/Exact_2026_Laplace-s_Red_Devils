# Hệ thống tri thức cho AI Agent: EXACT 2026 Challenge - Task Type 2 (Physics Problems)

## 1. Tổng quan Bài toán

EXACT 2026 là cuộc thi xây dựng hệ thống hỏi đáp (QA) ứng dụng Explainable AI (XAI). Trong đó, **Task Type 2** yêu cầu xây dựng một hệ thống giải các bài tập Vật lý bằng văn bản (tập trung vào mạch điện và tĩnh điện).
Hệ thống không chỉ cần đưa ra đáp án chính xác (kèm đơn vị) mà còn phải xuất ra được các bước suy luận Chain-of-Thought (CoT) chi tiết và minh bạch.

## 2. Bản đồ Dữ liệu & Không gian làm việc (File Paths)

Vui lòng tham chiếu các file sau trong quá trình tiền xử lý và huấn luyện. Lưu ý sử dụng phiên bản dataset mới nhất (15/05/2026) để tránh các lỗi dán nhãn từ ban tổ chức:

* **Dataset lỗi thời (Nhiều nhiễu/lỗi):** `EXACT Materials\Datasets\EXACT2026_dataset_2026-05-09\Physics_Problems_Text_Only\Physics_Problems_Text_Only.csv`
* **Dataset mới nhất (Đã fix bug - BẮT BUỘC DÙNG):** `EXACT Materials\Datasets\EXACT2026_dataset_2026-05-15\Physics_Problems_Text_Only\Physics_Problems_Text_Only.csv` *(Phiên bản drop-in replacement, đã xóa 403 dòng dữ liệu hỏng, hiện còn 1,352 bài tập hợp lệ).*
* **Changelog ghi nhận thay đổi:** `EXACT Materials\Datasets\EXACT2026_dataset_2026-05-15\CHANGELOG_TYPE2.md`
* **Notebook EDA (Tham khảo phân tích lỗi trên data cũ):** `app\notebooks\01_EDA_Dataset_Physics.ipynb`

## 3. Cấu trúc Dữ liệu & Ví dụ mẫu

Dữ liệu chuẩn bao gồm các trường: `id`, `question`, `cot`, `answer`, `unit`.

**Ví dụ:**

* **ID:** `TD401`
* **Question:** Calculate the energy stored in capacitor C when C = 100 μF and U = 30 V.
* **CoT:** Step 1: Identify the given values for capacitance (C) and voltage (U). Step 2: Recall the formula for the energy (E) stored in a capacitor, which is E = 0.5 × C × U^2. Step 3: Convert the capacitance to Farads: C = 100 μF = 100 × 10^-6 F = 1 × 10^-4 F. Step 4: Substitute the values into the formula: E = 0.5 × (1 × 10^-4 F) × (30 V)^2.
* **Answer:** `0.045`
* **Unit:** `J`

## 4. Cảnh báo Đỏ về Dữ liệu (Yêu cầu tiền xử lý mạnh tay)

Dù đã cập nhật bản 15/05, dữ liệu vẫn mang tính chất của máy dịch (từ Tiếng Việt) nên tiềm ẩn nhiều rủi ro. Agent cần thiết lập pipeline làm sạch dựa trên các báo cáo từ `01_EDA_Dataset_Physics.ipynb`:

* **Chất lượng dịch thuật & Logic:** CoT và Answer do hệ thống sinh ra có thể bị sai lệch kiến thức vật lý cơ bản hoặc tính toán sai. Cần cross-check tự động bằng script Python/SymPy.
* **Sự thiếu nhất quán về Format Toán học:** Các công thức và con số không theo chuẩn thống nhất (lẫn lộn giữa LaTeX, text thuần, ký hiệu scientific như 10^-5, v.v.). Cần chuẩn hóa format toàn bộ tập train.
* **Chiến lược bắt buộc:** Thực hiện EDA bổ sung trên bản cập nhật mới, thiết lập pipeline chuẩn hóa toán học và áp dụng **Tăng cường dữ liệu (Data Augmentation)** để đảm bảo mô hình học được logic toán lý chuẩn xác.

## 5. Ràng buộc Kỹ thuật & Quyền hạn (Strict Rules)

Agent đề xuất và xây dựng kiến trúc cần tuân thủ tuyệt đối các quy định của cuộc thi:

* **Giới hạn Model < 8B Tham số:** Chỉ được sử dụng Open-source LLM với tổng số tham số (Total Parameters) $\le$ 8B. (Các model MoE có tổng tham số > 8B nhưng active < 8B cũng **KHÔNG** được chấp nhận. Ví dụ: Qwen 30B-A3B bị cấm).
* **Kiến trúc Pipeline (Sequential vs Parallel):** Được phép dùng nhiều model $\le$ 8B khác nhau (ví dụ 1 model trích xuất, 1 model sinh code), miễn là chúng chạy nối tiếp (Sequential). Tuyệt đối cấm chạy song song (Parallel) 2 model $\le$ 8B cùng lúc trên RAM/VRAM.
* **Môi trường Hosting:** Bắt buộc tự host bằng **vLLM** (hoặc chuẩn tương đương) để ban tổ chức kiểm tra endpoint. **Cấm** sử dụng các dịch vụ API bên thứ ba (như Groq, Together AI, Fireworks, Replicate) dù chúng chạy model Open-source. Thời gian phản hồi tối đa của API là **60 giây/request**.
* **Tool Calling & Code Execution (Khuyến nghị dùng):** Được phép sinh và chạy code Python/SymPy, dùng máy tính hoặc Symbolic solvers. Lịch sử tool call phải được đưa vào phần CoT để tính điểm giải thích.
* **Dữ liệu ngoài & RAG:** Hoàn toàn được crawl web, dùng dữ liệu ngoài, hoặc tạo dữ liệu tổng hợp (synthetic data) từ GPT-4/Claude để train/fine-tune. Bắt buộc ghi nhận lại để khai báo trong *Data Disclosure Document*. (Cấm gọi API GPT-4/Claude lúc inference).

## 6. Tiêu chí Đánh giá và Tối ưu API Output

Hệ thống sẽ chấm điểm qua API JSON trả về. Agent cần thiết kế JSON Output đáp ứng 3 tiêu chí:

* **P1 - Correctness:** Đáp án số học và đơn vị chính xác (có dung sai). Trường bắt buộc: `"answer"`.
* **P2 - Explanation Quality:** Lời giải thích tự nhiên, dễ hiểu. Trường bắt buộc: `"explanation"`.
* **P3 - Reasoning Depth:** Độ sâu suy luận. Để tối ưu điểm này, API JSON nên bổ sung các trường tự chọn như `"cot"` (từng bước step-by-step rõ ràng), xuất log báo cáo tool call/code, và `"confidence"`.