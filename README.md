# Internal Reliability Signals for Agentic Systems

Most existing work on agent reliability focuses on *external* guardrails — filters, sandboxes,
policy engines that watch an agent from the outside. This is a map of work on the other half:
**internal, model-native signals** (uncertainty, activation-level state, self-consistency) that
might catch a failing trajectory before it completes — with a focus on coding, web, and GUI
agents specifically.

Modeled on [jun-zeng/Audit-log-analysis](https://github.com/jun-zeng/Audit-log-analysis).

New finds go into [`papers.csv`](papers.csv) first — plain title, authors, venue, year, idea, gap,
category, relevant (yes/no/tbd) — no links (that's what the README is for). Once read and
settled, a paper gets promoted into the relevant section below, where its title becomes the
clickable link.

- [Table of contents](#table-of-contents)
  * [Datasets & Benchmarks](#datasets--benchmarks)
  * [Surveys](#surveys)
  * [Coding Agents](#coding-agents)
  * [Web Agents](#web-agents)
  * [GUI Agents](#gui-agents)
  * [Cross-Domain Trajectory Monitoring](#cross-domain-trajectory-monitoring)
  * [Internal Signals: Uncertainty, Probing, Introspection](#internal-signals-uncertainty-probing-introspection)
  * [Alignment (Anthropic Alignment Science)](#alignment-anthropic-alignment-science)
  * [Context: External Guardrails](#context-external-guardrails)
  * [Related Lists](#related-lists)

## Datasets & Benchmarks

Standard task environments used across this literature — useful for knowing what "success/failure"
means in each domain, and where to eventually test any detector you build.

* [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) — Jimenez, Yang, Wettig, Yao, Pei, Press, Narasimhan. ICLR'2024. 500 human-verified tasks (2,294 in the full set) from real GitHub issues across 12 Python repos; agent must produce a passing patch.
* [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) — Zhou, Xu, Zhu, Zhou, Lo, Sridhar, Cheng, Ou, Bisk, Fried, Alon, Neubig. ICLR'2024. 812 web-navigation tasks across maps, e-commerce, forums, dev tools.
* [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972) — Xie, et al. NeurIPS'2024 (Datasets & Benchmarks Track). Real desktop computer-use tasks across ~369 tasks in a full Ubuntu VM.
* [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/pdf/2405.14573) — Rawles, et al. arXiv'2024. 116 tasks across 20 real Android apps, dynamically parameterized.
* [GAIA: A Benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983) — Mialon, Fourrier, Swift, Wolf, LeCun, Scialom. arXiv'2023. General assistant tasks requiring live web interaction and multi-step reasoning.
* [τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) — Yao, Shinn, Razavi, Narasimhan. arXiv'2024. Tool-agent-user interactions with policy adherence; proposes pass^k reliability metric.
* [τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment](https://arxiv.org/abs/2506.07982) — Barres, Dong, Ray, Si, Narasimhan. arXiv'2025. Successor to τ-bench.
* [Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces](https://arxiv.org/html/2601.11868v1) — arXiv'2026. Command-line/terminal agent tasks.

**Important caveat, worth knowing before you cite any leaderboard number**: a 2026 study
found all eight major agent benchmarks above could be reward-hacked to near-100% without
solving the underlying tasks (e.g. reading WebArena's gold answer directly from the eval
harness, or exploiting `eval()` calls in the grading pipeline).
* [How We Broke Top AI Agent Benchmarks](https://arxiv.org/abs/2605.12673) — 2026. Gap/relevance to you: benchmark gaming is itself a trajectory-level failure mode an internal-signal detector might catch that an external pass/fail check would miss.

## Surveys

* [A Survey for LLM Agent Trajectory Analysis: From Failure Attribution to Enhancement](https://arxiv.org/html/2606.06324v2) — Wang, Wang, Chen, Xie, Chen, Mu, Liu, Wang. arXiv'2026. Surveys 42 papers (from 1,452 screened) organizing trajectory analysis into failure attribution, debugging, repair, optimization, monitoring, benchmarks. Gap: read this first — defines the existing map of the exact space you're entering.
* [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://arxiv.org/abs/2311.05232) — Huang, Yu, Ma, Zhong, Feng, Wang, Chen, Peng, Feng, Qin, et al. ACM TOIS'2025.
* Safeguarding Large Language Models: A Survey — Dong, Mu, Zhang, Sun, Zhang, Wu, Jin, Qi, Hu, Meng, et al. Artificial Intelligence Review'2025. *(no arXiv/free link found yet — journal-only)*

## Coding Agents

* [AgentForesight](https://arxiv.org/abs/2605.08715) — arXiv'2026. Online, prefix-only auditing that alarms at the earliest decisive error in a trajectory; 7B auditor beats GPT-4.1/DeepSeek-V4-Pro on step localization. Gap: external judge model reads text trajectory, not the acting agent's own internal state — your differentiation point.
* [TrajAudit](https://arxiv.org/html/2605.26563v1) — arXiv'2026. Post-hoc failure diagnosis via failure-keyword folding + investigator agent. Gap: post-hoc only, not online/early.
* [Beyond Resolution Rates: Behavioral Drivers of Coding Agent Success and Failure](https://arxiv.org/html/2604.02547v1) — Mehtiyev, Assunção. arXiv'2026. Structural trajectory sequencing (read/patch/validate) distinguishes success/failure better than trajectory length. Gap: calls for real-time monitoring but doesn't build it.
* [Coherence Collapse](https://arxiv.org/pdf/2603.24631) — arXiv'2026. Names a failure mode: agent reaches correct code then overwrites/thrashes it; length-independent. Gap: doesn't test whether internal confidence dips at the collapse point.
* [Inside the Scaffold](https://arxiv.org/pdf/2604.03515) — arXiv'2026. Survey of coding agent architectures; failure trajectories run 12-82% longer than successful ones.

## Web Agents

* [StressWeb](https://arxiv.org/pdf/2604.16385) — arXiv'2026. Diagnostic benchmark injecting controlled perturbations into web environments to test robustness, rather than post-hoc analysis.
* WAREX — Kara, et al. arXiv'2025 (cited within StressWeb; direct link not yet found). Large-scale reliability analysis of web agents across existing benchmarks, revealing performance variance under identical settings. Gap: analysis framework only, not an environment/benchmark itself.

*(still to search: web agent trajectory success prediction, web agent hallucination detection, MIRAGE-Bench)*

## GUI Agents

* [GEM: Gaussian Embedding Modeling for OOD Detection in GUI Agents](https://arxiv.org/pdf/2505.12842) — arXiv'2025. Models trajectory embeddings as Gaussians to detect out-of-distribution risk.
* [GUITester](https://arxiv.org/pdf/2601.04500) — arXiv'2025/2026. Identifies Repetition-Induced Termination and Goal Conflict as GUI agent failure modes. Gap: descriptive taxonomy, not a detection method.
* [DiagEval](https://arxiv.org/pdf/2605.17439) — arXiv'2026. Trajectory-conditioned diagnosis distinguishing software defects from agent-side execution misses.
* MLA-Trust — Yang, et al. arXiv'2025 (cited within StressWeb; direct link not yet found). Benchmarks trustworthiness of multimodal LLM agents in GUI environments across perception, reasoning, safety. Gap: static task distributions, not interventional.
* [Recovering Policy-Induced Errors](https://arxiv.org/pdf/2605.29447) — arXiv'2026. Benchmark + trajectory synthesis for GUI agent robustness.

## Cross-Domain Trajectory Monitoring

* [TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents](https://arxiv.org/pdf/2602.06443) — Liu, Zhang, Han, Liu, Wang, Yu, Wang, Yin. arXiv'2026. Anomaly detection framework for agent trajectories aimed at trustworthiness; builds TrajBench dataset. Gap: check whether it uses internal model signals or only external/behavioral features.
* [Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents](https://arxiv.org/pdf/2603.29231) — arXiv'2026. Applies reliability-engineering concepts (MTBF, failure rate function) to long-horizon agents.
* [Trajectory Guard: A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI](https://arxiv.org/abs/2601.00516) — Advani. arXiv'2026. Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss; F1 0.88-0.94 on balanced sets. Gap: performance degrades on long trajectories (F1 0.96 for 2-5 steps vs. 0.87 for 11+ steps) — a GRU encoding bottleneck, relevant if your trajectories run long.
* [Agentic Confidence Calibration](https://arxiv.org/abs/2601.15778) — arXiv'2026 (desk-rejected from ICLR'2026, posted independently). Introduces Holistic Trajectory Calibration (HTC): extracts process-level features (early-step entropy, confidence gradients, stability dynamics) across a full trajectory. Directly relevant: this already uses internal/logit-derived features, not just external ones — read closely for overlap with your angle.
* [When Agents Fail: A Comprehensive Study of Bugs in LLM Agents with Automated Labeling](https://arxiv.org/abs/2601.15232) — Islam, Ayon, Thomas, Ahmed, Wardat. arXiv'2026. Analyzes 1,187 bug reports across 7 LLM agent frameworks from Stack Overflow/GitHub/HuggingFace forums.

## Internal Signals: Uncertainty, Probing, Introspection

* [Language Models (Mostly) Know What They Know](https://www.anthropic.com/research/language-models-mostly-know-what-they-know) — Kadavath, et al. 2022. Models can evaluate whether their own statements are true and predict correctness in advance. Gap: foundational for uncertainty-as-signal, not agentic-specific.
* [Uncertainty-Based Abstention Improves Safety and Reduces Hallucinations](https://arxiv.org/abs/2404.10960) — Tomani, Chaudhuri, Evtimov, Cremers, Ibrahim. arXiv'2024. Statistical + In-Dialogue Uncertainty thresholding drives abstention; improves correctness and catches ~50% hallucinations. Gap: QA setting, not agentic/trajectory.
* [Simple Probes can Catch Sleeper Agents](https://www.anthropic.com/research/probes-catch-sleeper-agents) — Anthropic Alignment. 2024. Linear probing detects a backdoored model about to behave dangerously, even after it appears safe. Gap: backdoor/deception setting, not task-failure prediction — your transfer target.
* [Model-Internals Classifiers](https://alignment.anthropic.com/2025/cheap-monitors/) — Anthropic Alignment. 2025. Benchmarks reusing LLM internals for cheaper monitoring than full output-classifier passes.
* [Harmful Intent as a Geometrically Recoverable Feature](https://arxiv.org/abs/2604.18901) — arXiv'2026. Linear direction for harmful intent, stable across 12 models and 4 architectures. Gap: TPR@1%FPR only 0.30 for a deployed classifier despite high AUROC.
* [Why Safety Probes Catch Liars But Miss Fanatics](https://arxiv.org/abs/2603.25861) — arXiv'2026. Diff-in-means probing distinguishes deceptive vs. self-consistent hostile models. Gap: probes miss agents that internally believe their own harmful reasoning.
* [Activation Oracles](https://alignment.anthropic.com/2025/activation-oracles/) — Anthropic Alignment. 2025. Trains LLMs to answer questions about their own activations in natural language.
* [Introspection Adapters](https://alignment.anthropic.com/2026/introspection-adapters/) — Anthropic Alignment. 2026. Trains an LLM to self-report behaviors learned during fine-tuning; generalizes across fine-tuning methods.
* [Detecting Multi-Agent Collusion Through Multi-Agent Interpretability](https://arxiv.org/abs/2604.01151) — arXiv'2026. Extends single-agent deception probing to multi-agent collusion detection, framed via AI Control.

## Alignment (Anthropic Alignment Science)

* [Reasoning Models Don't Always Say What They Think](https://www.anthropic.com/research/reasoning-models-dont-say-think) — Chen, et al. Alignment Science Blog'2025. Reasoning models don't always verbalize true reasoning. Gap/relevance: text/CoT-based trajectory monitoring has a ceiling — motivates activation-level signals over text-level ones.
* [Teaching Claude Why](https://www.anthropic.com/research/teaching-claude-why) — Anthropic Alignment. 2026. Training on the model's own reasoning about why an action is wrong generalizes better OOD than demonstration-matching.
* [From Shortcuts to Sabotage](https://www.anthropic.com/research/emergent-misalignment-reward-hacking) — Anthropic Alignment. 2025. Realistic training processes can accidentally produce misaligned models via reward hacking.
* [Monitoring Computer Use via Hierarchical Summarization](https://alignment.anthropic.com/2025/summarization-for-monitoring/index.html) — Anthropic Alignment. 2025. Anthropic's own approach to monitoring computer-use agent trajectories via hierarchical summarization. Gap: summarization/text-based, not internal-state-based — direct prior art to position against for GUI/computer-use.
* [SLEIGHT-Bench](https://alignment.anthropic.com/2026/sleight-bench/) — Anthropic Alignment. 2026. Benchmark of evasive transcripts exploiting blind spots of frontier monitoring systems.
* [Putting up Bumpers](https://alignment.anthropic.com/2025/bumpers/) — Anthropic Alignment. 2025. Argues catching-and-fixing misalignment is tractable even without solving alignment.

*(Browse regularly: [alignment.anthropic.com](https://alignment.anthropic.com/) for research notes,
[anthropic.com/research/team/alignment](https://www.anthropic.com/research/team/alignment) for write-ups.)*

## Context: External Guardrails

Background only — you know this landscape well enough to explain why it's insufficient, but it's not where the contribution lives.

* [ShieldAgent](https://proceedings.mlr.press/v267/chen25ae.html) — Chen, Kang, Li. ICML'2025. LTL rules extracted from policy docs, enforced via Markov Logic Network. Gap: degrades on hallucination-related risk.
* [AgentSpec](https://arxiv.org/abs/2503.18813) — Wang, Poskitt, Sun. ICSE'2026. DSL for runtime agent constraints. Gap: purely deterministic, no confidence conditioning.
* [CaMeL](https://arxiv.org/abs/2503.18813) — Debenedetti, et al. arXiv'2025. Trusted/untrusted planning separation with capability-tracking interpreter. Gap: no graceful escalation when task requires trusting untrusted data.
* [VeriGuard](https://arxiv.org/abs/2510.05156) — Miculicich, et al. arXiv'2025. Formally verified policies via Hoare triples. Gap: soundness depends on LLM-generated constraints capturing intent correctly.
* FAIL-TaLMs — Treviño, et al. NAACL'2025 *(direct link not yet found)*. Tool-augmented LMs under underspecified queries. Gap: the awareness-to-action gap — 56% uncertainty awareness doesn't improve outcomes.
* MCIP — Jing, et al. EMNLP'2025 *(direct link not yet found)*. Taxonomy of 15 MCP attack types + guard model. Gap: fine-tuning induces over-approval bias.

## Related Lists

- [VoltAgent/awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers) — broad 2026 agent paper tracker
- [jun-zeng/Audit-log-analysis](https://github.com/jun-zeng/Audit-log-analysis) — structural template for this repo
