# EXACT 2026 - Official Q&A Document

**The 2nd International XAI Challenge for Transparent Educational Question-Answering IEEE IJCNN**

> **Last updated:** May 12, 2026
> This document compiles all questions received via email and during the Kick-off Workshop (May 9, 2026), along with the official answers from the Organizing Committee. These rulings are binding for the duration of the competition.

---

## 1. Models & Parameter Limits

### Q1. Interpretation of the "≤ 8B Parameters" Rule `[IMPORTANT]`

**Does the ≤ 8B rule mean (a) the nominal model label (e.g., "Qwen3-8B" passes even at 8.19B actual), (b) a strict 8.0B ceiling, or (c) a rounded threshold (≤ 9B)?**

**A1:** **Interpretation (a) - nominal 8B-class.** A model is accepted if its official label or release name falls in the 8B class, even if the exact parameter count is slightly above 8.0B due to embedding or tokenizer overhead. For example, DeepSeek-R1-0528-Qwen3-8B (8.19B) is eligible. Models nominally labeled 9B or larger are not eligible.

### Q2. Mixture-of-Experts (MoE) Models `[IMPORTANT]`

**For MoE architectures (e.g., Qwen3-30B-A3B with 3B active parameters), does the 8B limit apply to (a) total parameters or (b) active parameters per forward pass?**

**A2:** **(a) Total parameters.** The 8B cap applies to the total parameter count of the model, not the number of active parameters per forward pass.
**Reason:** Storage, deployment, and reproducibility costs scale with total parameters. Allowing MoE by active count would let teams ship 30B-100B systems disguised as 8B. Therefore, Qwen3-30B-A3B (30B total) is not eligible despite having only 3B active parameters.

### Q3. Using Multiple Models - Sequential vs. Parallel `[IMPORTANT]`

**Can we use two different models for each question type? Can we run multiple sub-8B models in parallel? Does the 8B limit apply to the whole pipeline or per model?**

**A3:** Yes, you may use different models for different tasks or pipeline stages. Here is the breakdown:

* **Sequential (different tasks):** You may use Model A (≤ 8B) for Type 1 and Model B (≤ 8B) for Type 2, or use one model for understanding and another for generation. As long as each individual model is within the 8B-class limit and they are invoked sequentially (one finishes before the next starts), this is allowed.
* **Parallel (simultaneous inference):** Running multiple LLMs simultaneously within a single inference call (e.g., two 8B models running in parallel and merging outputs) is **not allowed**. This would effectively give your system 16B of capacity at inference time, which violates the spirit of the 8B constraint.

> **Rule of thumb:** At any given moment during inference, only one LLM ≤ 8B should be actively loaded and running. You may switch between different models across pipeline stages, but you cannot have multiple LLMs loaded in memory simultaneously (e.g., two 8B models resident on GPU at the same time). The committee may inspect GPU memory usage during the Public Test Day to verify compliance.

### Q4. "Open-Source" License Definition

**Does "open-source" require a specific license (Apache-2.0, MIT, BSD), or do permissive research licenses (e.g., Llama Community License, Gemma License) also qualify?**

**A4:** We accept both strict OSI-approved licenses (Apache-2.0, MIT) and permissive community/research licenses that allow research and competition use, including:

* Llama Community License (Llama 3.x)
* Gemma Terms of Use
* Qwen License, DeepSeek License, Mistral Research License

**Minimum requirement:** Model weights must be publicly downloadable, and the license must permit use in this competition. If you are unsure about a specific model, tag `@[ADMIN]` in the `#topic-questions` channel on Discord for confirmation before using it.

### Q5. Using Third-Party API Providers / Cloud Inference Services `[IMPORTANT]`

**Can we use an API from an open-source AI provider (e.g., Together AI, Fireworks, Groq, Replicate) to host our model instead of self-hosting?**

**A5:** **No.** Third-party cloud inference services are not allowed, even if they serve open-source models within the 8B limit. The reason is that we cannot verify what model is actually running behind a third-party API. A provider could silently route requests to a larger model, apply proprietary optimizations, or change the model version without your knowledge.

You must self-host your model using your own infrastructure (local GPU, rented cloud GPU, Kaggle, Colab, etc.). To ensure transparency and enable verification, we require all teams to deploy their LLM component using vLLM (or a compatible OpenAI-style serving framework) so that:

* The model name and size are visible in the API metadata
* The committee can inspect the `/v1/models` endpoint to confirm which model is loaded
* Inference behavior is reproducible and auditable

**In summary:**

* **[Allowed]** Self-hosted on your own GPU (local, cloud VM, Kaggle, Colab, RunPod, etc.) using vLLM
* **[Allowed]** Tools, solvers, retrieval modules hosted anywhere (these are not LLMs)
* **[Not allowed]** Third-party inference APIs (Together AI, Fireworks, Groq, Replicate, Hugging Face Inference API, etc.)
* **[Not allowed]** Any endpoint where you do not control or cannot prove which model is running

### Q6. Knowledge Distillation from Larger Models

**Is it allowed to train on a larger model and then use its weights to fine-tune a smaller model?**

**A6:** Yes. You may use knowledge distillation, where a larger teacher model is used during training to produce a smaller student model, as long as:

* The final deployed model (the student) is within the 8B-class limit
* The teacher model is not called at inference time
* You fully disclose the distillation process and teacher model in your solution description

---

## 2. Tools, Data & Techniques

### Q7. Tool Use & Code Execution

**Is the LLM allowed to call external tools (e.g., write and execute code) to perform complex computations?**

**A7:** Yes, and this is encouraged. The following are all allowed:

* Code execution (Python, SymPy, etc.)
* Symbolic solvers (Z3, Prover9, custom engines)
* Calculators and math libraries
* Retrieval modules

**Constraints:**

* Tools themselves do not count toward the parameter limit, but they must not wrap or call closed-source LLMs
* Tool calls must be visible in the explanation/Chain-of-Thought output so that evaluators can verify the reasoning

### Q8. RAG Techniques

**Are Retrieval-Augmented Generation (RAG) techniques accepted?**

**A8:** Yes. You may build a knowledge base (e.g., physics formulas, regulation documents, solved examples) and retrieve from it during inference. This is a valid and encouraged approach.

### Q9. Internet Search / Online Retrieval

**Can we use tool calling to search or retrieve from sources available on the internet?**

**A9:** Yes, you may use internet search or retrieval during inference, as long as the retrieved content does not come from a closed-source LLM (e.g., you cannot query ChatGPT or Claude via API as a "retrieval" step). Retrieving from public databases, Wikipedia, textbooks, or similar open sources is fine.

### Q10. Using Synthetic Data from Closed-Source Models `[IMPORTANT]`

**Can we use synthetic data generated by closed-source models (ChatGPT, Claude) for training or testing purposes?**

**A10:** You may use synthetic data generated by closed-source models for **training and fine-tuning only**. This must be fully disclosed in your solution description.
However, closed-source models must **not** be called at inference time. The final deployed system must rely solely on open-source models within the parameter limit.

### Q11. External Data for Training `[IMPORTANT]`

**Is it allowed to use external data for training?**

**A11:** Yes. You may use any external dataset for training or fine-tuning, provided that you comply with the following disclosure requirement:

All teams must submit a **Data Disclosure Document** alongside their one-page solution description. This document should clearly describe:

* Every external dataset used (name, source URL, size, purpose)
* Any synthetic data generated by closed-source models (which model, how many samples, what for)
* Any crawled or scraped data (source URLs, volume, preprocessing steps)
* Any knowledge bases or retrieval corpora built for RAG

This applies to all external data regardless of how it was obtained or used (training, fine-tuning, retrieval, evaluation, etc.). The committee needs full visibility into your data pipeline to ensure fairness and reproducibility. Submissions without this document, or with undisclosed data sources discovered later, are grounds for disqualification.

### Q12. Web Crawling for Data

**Can I crawl data from the web? Would it be accepted?**

**A12:** Yes, crawled data may be used for training or building a retrieval knowledge base. As with all external data, it must be fully disclosed in your solution description.

---

## 3. Hosting & API

### Q13. Hosting the Live API Endpoint

**Are there restrictions on GPU type, cloud provider, geographic region, or response latency?**

**A13:**

* **GPU / Cloud provider:** No restriction on hardware or cloud provider. You may rent GPU VMs from Kaggle, Colab, RunPod, AWS, Modal Labs, or any provider and self-host your model there. This is different from using a third-party inference API (see Q5). As long as you control the deployment and serve the model yourself via vLLM, any infrastructure is acceptable.
* **Geographic region:** No restriction. We recommend a region with stable connectivity to Vietnam/EU to minimize network latency.
* **Latency:** The hard cap is 60 seconds per request. A timeout counts as a failed answer for that query. There is no separate latency target beyond this.
* **Uptime:** The endpoint must remain online during the entire evaluation window announced for each phase.

### Q14. Verification of Models Behind API Endpoints `[IMPORTANT]`

**Since an API is essentially a black box, how will the committee verify the actual model being used? What prevents an endpoint labeled "7B" from routing to a 32B or 70B model?**

**A14:** The committee employs multiple verification mechanisms:

* **vLLM deployment requirement:** All teams must serve their LLM via vLLM (or compatible OpenAI-style framework). The committee may query your `/v1/models` endpoint at any time to confirm the loaded model name and size. See Q5 for details.
* **Solution description review:** Teams must declare all models, tools, and infrastructure in the one-page description. False declarations are grounds for disqualification.
* **Public Test Day (Top 10):** Finalists run their systems live before the Challenge Chairs, who may inspect the deployment environment, GPU memory usage, and model loading.
* **Post-competition audit:** The committee reserves the right to request code repositories, model checkpoints, or deployment logs from any team at any stage.
* **Community reporting:** Participants may report suspected violations in the `#topic-questions` channel on Discord or by tagging `@[ADMIN]`.

Teams found to have misrepresented their models will be disqualified and their results removed from the leaderboard.

### Q15. Resource Constraints for Hosting During Evaluation

**Do I need to keep the API running all day during evaluation? How do I manage the hosting resources?**

**A15:** Your API must be online for the **full duration** of the evaluation window for each phase (typically 1-2 days). You will be notified of the exact windows in advance.

For resource management, consider:

* Free-tier GPU platforms (Kaggle, Colab) for smaller models
* On-demand cloud GPUs (Modal Labs, RunPod, AWS Spot) for cost efficiency
* On-premise GPUs if available

The 8B-class model requirement was designed in part to keep hosting costs reasonable.

---

## 4. Dataset & Evaluation

### Q16. Dataset Release & Access

**Has the dataset been released? Where can I access it?**

**A16:** Yes, the datasets were released on May 9, 2026, and have been sent to all registered teams via email. Two text-only archives are available:

* **Type 1:** Logic-Based Educational Queries (411 records, 808 questions)
* **Type 2:** Physics Problems (1,755 text-only problems)

Access them at the official competition page: [https://ura.hcmut.edu.vn/exact](https://ura.hcmut.edu.vn/exact)
A `README` inside each archive describes the schema and field semantics.

**Dataset updates and changelog:** As teams report annotation issues (see Q22), we will periodically release updates and maintain a changelog on the official website and in the `#announcements` channel on Discord. Please check regularly to ensure you are working with the latest version.

Using the official dataset for training is not mandatory. You are free to use our dataset for training, modify it, augment it with your own data, or build an entirely different training set. The only requirement is that you clearly describe all data used in your Data Disclosure Document (see Q11). The official dataset primarily defines the format and types of questions your system will be evaluated on.

### Q17. Test Format: One Type or Both? `[IMPORTANT]`

**Will the test set contain only one dataset type, or both?**

**A17:** The test set will contain **both** Type 1 (Logic-Based) and Type 2 (Physics) queries, combined into a unified query stream. Your system must be able to handle both types.

We strongly encourage all teams to develop strategies for both dataset types. The format of the test queries will follow the same structure as the training datasets that have been provided, so use those as your reference for building and testing your pipeline. Teams that only handle one type will miss a significant portion of the test set and score accordingly. Plan your approach to cover both types from the start.

### Q18. Single API for Both Types `[IMPORTANT]`

**When we implement the API for live testing, should it be a single API that handles both types of answers?**

**A18:** Yes. You must provide a **single API endpoint** that accepts queries of both types and returns the appropriate answer format. The query payload will include a field indicating the query type so your system can route accordingly.

### Q19. Dataset Quality Issues - QA Samples in Type 2 `[IMPORTANT]`

**The admin confirmed that samples with `id_prefix = QA` (401 samples) in Physics_Problems_Text_Only.csv were annotation errors. Will the committee release a cleaned version, or should teams filter them out?**

**A19:** Teams should **filter out** the QA-prefixed samples themselves. These 401 samples were from the annotation pipeline and should be excluded. We will not release a separate cleaned file, as the filtering is straightforward (exclude records where the ID starts with "QA"). The effective Type 2 dataset after filtering contains 1,354 valid problems.

### Q20. Mathematical Notation in Outputs

**Is there any constraint on mathematical notation? For example, are √2 and \sqrt{2} considered the same?**

**A20:** For evaluation purposes, we will normalize common mathematical notations. Both Unicode symbols (`√2`) and LaTeX notation (`\sqrt{2}`) are accepted and treated as equivalent. The same applies to fractions, exponents, and other common expressions. We recommend using a consistent notation throughout your outputs for clarity, but you will not be penalized for notation style as long as the mathematical content is correct.

### Q21. Detailed Scoring Criteria

**What are the detailed scoring criteria used by the Challenge Chairs?**

**A21:** The final score is a weighted combination of three criteria (weights will be published alongside the evaluation):

* **P1 - Correctness:** Automated exact-match against ground truth. For Type 2, a numerical tolerance is applied along with unit matching.
* **P2 - Explanation Quality:** The committee reviews clarity, coherence, and faithfulness of the natural-language explanations.
* **P3 - Reasoning Depth:** Extra credit for verifiable reasoning evidence such as FOL derivations, Chain-of-Thought steps, or cited premises. This criterion is evaluated live on the Public Test Day for the Top 10 teams.

### Q22. Bonus for Reporting Dataset Annotation Issues

**Will EXACT 2026 keep the incentive for reporting dataset issues?**

**A22:** Yes, this incentive is retained. Teams that report verified dataset issues (incorrect labels, ambiguous questions, formatting bugs) during Phase 1 or Phase 2 receive a bonus on the final score.

**How to report:** Post in the `#dataset-issue-report` channel on Discord and tag `@[ADMIN]`. Each report must include the record ID, the issue type, and a short justification. The committee will verify each report and publish accepted issues in a public erratum.

---

## 5. Submission & Timeline

### Q23. Submission Format & Channel

**What is the preferred submission format and channel?**

**A23:** Your submission package consists of:

* Public URL of your live API endpoint (must return responses in the specified JSON schema)
* One-page solution description (PDF) listing all models used, tools, and approach overview
* Data Disclosure Document (PDF) describing all external data sources used throughout your pipeline (see Q11 for details)

**Channel:** Submit through the official web form at [https://ura.hcmut.edu.vn/exact](https://ura.hcmut.edu.vn/exact). Email submissions to `ura.hcmut@gmail.com` are accepted as a backup. GitHub issues are not an accepted submission channel.

### Q24. Phase 1 & Phase 2 Evaluation Timeline

**What are the deadlines for the Phase 1 and Phase 2 feedback?**

**A24:** Teams must keep the API endpoint online for the full evaluation window of each phase based on the timeline below:

| Phase | Dates | Feedback by |
| --- | --- | --- |
| **Phase 1 evaluation** | Jun 1-2, 2026 | End of Jun 2, 2026 |
| **Model refinement** | Jun 3-4, 2026 | - |
| **Phase 2 evaluation** | Jun 5-7, 2026 | End of Jun 7, 2026 |
| **Top 10 announcement** | Jun 10, 2026 | - |
| **Public Test Day** | Jun 15, 2026 | - |

---

## 6. General

### Q25. Local GPU vs. Cloud GPU

**Is it possible to use a local/personal/lab GPU instead of cloud GPUs?**

**A25:** Yes. There is no restriction on where you host your model. Local GPU, cloud GPU, or any combination is fine, as long as the API endpoint is publicly accessible from the evaluation server via the internet. If using a local machine, ensure your endpoint is reachable (e.g., via ngrok, a reverse proxy, or port forwarding) and remains online during the evaluation windows.

---

## 7. Team Registration & Management

### Q26. Team Registration, Modifications, and Member Changes `[IMPORTANT]`

**How do I register a new team, add/remove members, or make changes to my team?**

**A26:** All team-related matters (new registration, adding or removing members, changing team name, merging with other individuals) will be handled and confirmed through our official Discord server.

Please make sure your team is fully set up and stable on Discord. The organizing committee will use Discord as the primary channel to verify and confirm team rosters. If you have any team-related issues, please post in the `#team-issue-report` channel and tag `@[ADMIN]`. We will not process team changes via email after the registration deadline.

### Q27. Individual Registrants Seeking a Team

**I registered as an individual and still don't have a team. What should I do?**

**A27:** Please join the official Discord server and tag `@[ADMIN]` in the `#team-issue-report` channel. We will assist you in finding a team as quickly as possible. When forming teams, we aim to pair participants from different institutions, countries, and backgrounds to create a diverse and enriching collaboration environment.