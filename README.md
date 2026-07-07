# Internal Reliability Signals for Agentic Systems

Most existing work on agent reliability focuses on *external* guardrails — filters, sandboxes,
policy engines that watch an agent from the outside. This is a map of work on the other half:
**internal, model-native signals** (uncertainty, activation-level state, self-consistency) that
might catch a failing trajectory before it completes — with a focus on coding, web, and GUI
agents specifically.

Modeled on [jun-zeng/Audit-log-analysis](https://github.com/jun-zeng/Audit-log-analysis).

New finds go into [`papers.csv`](papers.csv) first — plain title, authors, venue, year, idea, gap,
no links (that's what the README is for). Once read and settled, a paper gets promoted into the
relevant section below, where its title becomes the clickable link.

- [Table of contents](#table-of-contents)
  * [Coding Agents](#coding-agents)
  * [Web Agents](#web-agents)
  * [GUI Agents](#gui-agents)
  * [Cross-Domain Trajectory Monitoring](#cross-domain-trajectory-monitoring)
  * [Internal Signals: Uncertainty, Probing, Introspection](#internal-signals-uncertainty-probing-introspection)
  * [Alignment (Anthropic Alignment Science)](#alignment-anthropic-alignment-science)
  * [Context: External Guardrails](#context-external-guardrails)
  * [Datasets & Benchmarks](#datasets--benchmarks)
  * [Surveys](#surveys)
  * [Related Lists](#related-lists)

## Coding Agents

- AgentForesight: online, prefix-only auditing that alarms at the earliest decisive error in a trajectory. 2026 [paper](https://arxiv.org/abs/2605.08715)
- TrajAudit: post-hoc failure diagnosis for coding agents via failure-keyword folding + investigator agent. 2026 [paper](https://arxiv.org/html/2605.26563v1)
- Beyond Resolution Rates: Behavioral Drivers of Coding Agent Success and Failure. Mehtiyev, Assunção. 2026 [paper](https://arxiv.org/html/2604.02547v1)
- Coherence Collapse: Diagnosing Why Code Agents Fail After Reaching the Right Code. 2026 [paper](https://arxiv.org/pdf/2603.24631)
- Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures. 2026 [paper](https://arxiv.org/pdf/2604.03515)

## Web Agents

- StressWeb: diagnostic benchmark injecting controlled perturbations into web environments to test robustness, rather than post-hoc analysis. 2026 [paper](https://arxiv.org/pdf/2604.16385)
- WAREX: large-scale reliability analysis of web agents across existing benchmarks, revealing performance variance under identical settings (analysis framework, not an environment itself). Kara, et al. 2025 (cited within StressWeb)

*(still to search: web agent trajectory success prediction, web agent hallucination detection, MIRAGE-Bench)*

## GUI Agents

- GEM: Gaussian Embedding Modeling for OOD Detection in GUI Agents. 2025 [paper](https://arxiv.org/pdf/2505.12842)
- GUITester: identifies Repetition-Induced Termination and Goal Conflict as failure modes in exploratory defect discovery. 2025/2026 [paper](https://arxiv.org/pdf/2601.04500)
- DiagEval: Trajectory-Conditioned Diagnosis for Reliable Software Evaluation with GUI Agents. 2026 [paper](https://arxiv.org/pdf/2605.17439)
- Recovering Policy-Induced Errors: Benchmarking and Trajectory Synthesis for Robust GUI Agents. 2026 [paper](https://arxiv.org/pdf/2605.29447)
- MLA-Trust: benchmarks trustworthiness of multimodal LLM agents in GUI environments across perception, reasoning, safety. Yang, et al. 2025 (cited within StressWeb)

## Cross-Domain Trajectory Monitoring

- **A Survey for LLM Agent Trajectory Analysis: From Failure Attribution to Enhancement** — surveys 42 papers (from 1,452 screened), organizing the space into failure attribution, debugging, repair, optimization, monitoring, benchmarks. Wang, Wang, Chen, Xie, Chen, Mu, Liu, Wang. 2026 [paper](https://arxiv.org/html/2606.06324v2) — **read this first**, it maps the exact space you're entering.
- TrajAD: trajectory anomaly detection framework for trustworthy LLM agents. Liu, Zhang, Han, Liu, Wang, Yu, Wang, Yin. 2026 [paper](https://arxiv.org/pdf/2602.06443)
- Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents — applies reliability-engineering concepts (MTBF, failure rate function) to long-horizon agents. 2026 [paper](https://arxiv.org/pdf/2603.29231)
- Trajectory Guard: Siamese Recurrent Autoencoder for real-time anomaly detection in agent action trajectories. 2026 (via [awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers))
- Agentic Confidence Calibration / Holistic Trajectory Calibration: process-level features across a full trajectory. 2026 (via [awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers))
- When Agents Fail: analysis of 1,187 bug reports across 7 LLM agent frameworks. 2026 (via [awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers))

## Internal Signals: Uncertainty, Probing, Introspection

- Language Models (Mostly) Know What They Know. Kadavath, et al. 2022 [paper](https://www.anthropic.com/research/language-models-mostly-know-what-they-know)
- Uncertainty-Based Abstention Improves Safety and Reduces Hallucinations. Tomani, Chaudhuri, Evtimov, Cremers, Ibrahim. 2024 [paper](https://arxiv.org/abs/2404.10960)
- Simple Probes can Catch Sleeper Agents. Anthropic Alignment. 2024 [paper](https://www.anthropic.com/research/probes-catch-sleeper-agents)
- Model-Internals Classifiers: benchmarking reused LLM internals for cheaper monitoring. Anthropic Alignment. 2025 [paper](https://alignment.anthropic.com/2025/cheap-monitors/)
- Harmful Intent as a Geometrically Recoverable Feature of LLM Residual Streams. 2026 [paper](https://arxiv.org/abs/2604.18901)
- Why Safety Probes Catch Liars But Miss Fanatics. 2026 [paper](https://arxiv.org/abs/2603.25861)
- Activation Oracles: training LLMs to answer questions about their own activations. Anthropic Alignment. 2025 [paper](https://alignment.anthropic.com/2025/activation-oracles/)
- Introspection Adapters: training an LLM to self-report behaviors learned during fine-tuning. Anthropic Alignment. 2026 [paper](https://alignment.anthropic.com/2026/introspection-adapters/)
- Detecting Multi-Agent Collusion Through Multi-Agent Interpretability. 2026 [paper](https://arxiv.org/abs/2604.01151)

## Alignment (Anthropic Alignment Science)

- Reasoning Models Don't Always Say What They Think. Chen, et al. 2025 [paper](https://www.anthropic.com/research/reasoning-models-dont-say-think)
- Teaching Claude Why: training on the model's own reasoning about *why* an action is wrong generalizes better OOD than demonstration-matching. 2026 [paper](https://www.anthropic.com/research/teaching-claude-why)
- From Shortcuts to Sabotage: natural emergent misalignment from reward hacking. 2025 [paper](https://www.anthropic.com/research/emergent-misalignment-reward-hacking)
- Monitoring Computer Use via Hierarchical Summarization. 2025 [paper](https://alignment.anthropic.com/2025/summarization-for-monitoring/index.html)
- Forecasting Rare Language Model Behaviors. Jones, Tong, et al. 2025 [paper](https://www.anthropic.com/research/forecasting-rare-behaviors)
- SLEIGHT-Bench: benchmark of evasive transcripts exploiting monitor blind spots. 2026 [paper](https://alignment.anthropic.com/2026/sleight-bench/)
- Putting up Bumpers: catching-and-fixing misalignment as a tractable goal without solving alignment. 2025 [paper](https://alignment.anthropic.com/2025/bumpers/)

*(Browse regularly: [alignment.anthropic.com](https://alignment.anthropic.com/) for research notes,
[anthropic.com/research/team/alignment](https://www.anthropic.com/research/team/alignment) for write-ups.)*

## Context: External Guardrails

Background only — you know this landscape well enough to explain why it's insufficient, but it's not where the contribution lives.

- ShieldAgent: LTL rules extracted from policy docs, enforced via Markov Logic Network. Chen, Kang, Li. ICML'2025 [paper](https://proceedings.mlr.press/v267/chen25ae.html)
- AgentSpec: DSL for runtime agent constraints. Wang, Poskitt, Sun. ICSE'2026 [paper](https://arxiv.org/abs/2503.18813)
- CaMeL: trusted/untrusted planning separation with capability-tracking interpreter. Debenedetti, et al. 2025 [paper](https://arxiv.org/abs/2503.18813)
- VeriGuard: formally verified policies via Hoare triples. Miculicich, et al. 2025 [paper](https://arxiv.org/abs/2510.05156)
- FAIL-TaLMs: tool-augmented LMs under underspecified queries — the awareness-to-action gap. Treviño, et al. NAACL'2025
- MCIP: taxonomy of 15 MCP attack types + guard model. Jing, et al. EMNLP'2025

## Datasets & Benchmarks

Standard task environments used across this literature — useful for knowing what "success/failure"
means in each domain, and where to eventually test any detector you build.

- **SWE-bench (Verified)** — coding. 500 human-verified tasks from real GitHub issues across 12 Python repos; agent must produce a passing patch. [repo](https://github.com/SWE-bench/SWE-bench)
- **WebArena** — web. 812 web-navigation tasks across maps, e-commerce, forums, dev tools. [site](https://webarena.dev/)
- **OSWorld** — GUI/desktop. Real desktop computer-use tasks across ~9 apps. [site](https://os-world.github.io/)
- **AndroidWorld** — GUI/mobile. 116 tasks across 20 real Android apps, dynamically parameterized. Rawles, et al. 2024 [paper](https://arxiv.org/pdf/2405.14573)
- **GAIA** — general assistant tasks requiring live web interaction. Mialon, et al. 2023
- **τ²-bench (tau-bench)** — tool-agent-user interactions with policy adherence. [repo](https://github.com/sierra-research/tau-bench)
- **Terminal-Bench** — command-line/terminal agent tasks.

**Important caveat, worth knowing before you cite any leaderboard number**: a 2026 UC Berkeley
(RDI) study found all eight major agent benchmarks above could be reward-hacked to near-100%
without solving the underlying tasks (e.g. reading WebArena's gold answer directly from the eval
harness). [paper](https://moogician.github.io/blog/2026/trustworthy-benchmarks-cont/) — relevant
to you directly: benchmark gaming is itself a trajectory-level failure mode an internal-signal
detector might catch that an external pass/fail check would miss.

## Surveys

- **A Survey for LLM Agent Trajectory Analysis: From Failure Attribution to Enhancement** — the closest existing survey to your topic; 42 papers organized into failure attribution, debugging, repair, optimization, monitoring, benchmarks. Wang, Wang, Chen, Xie, Chen, Mu, Liu, Wang. 2026 [paper](https://arxiv.org/html/2606.06324v2)
- A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions. Huang, Yu, Ma, Zhong, Feng, Wang, Chen, Peng, Feng, Qin, et al. ACM TOIS'2025
- Safeguarding Large Language Models: A Survey. Dong, Mu, Zhang, Sun, Zhang, Wu, Jin, Qi, Hu, Meng, et al. Artificial Intelligence Review'2025

## Related Lists

- [VoltAgent/awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers) — broad 2026 agent paper tracker
- [jun-zeng/Audit-log-analysis](https://github.com/jun-zeng/Audit-log-analysis) — structural template for this repo
