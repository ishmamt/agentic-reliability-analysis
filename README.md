# Awesome Internal Reliability for Agentic Systems

> A curated map of research on making LLM agents more reliable — with emphasis on
> **internal, model-native signals** (uncertainty, self-consistency, activation-level
> state) as opposed to purely external guardrails (filters, sandboxes, policy engines).
>
> **Current scope (as of July 2026):** narrowed to trajectory-level failure signals in
> a specific agent domain — coding agents, web agents, or GUI agents — with the
> question: *can we detect, from the trajectory itself (ideally from internal model
> state, not just external judges), that an agent is heading toward failure before
> it completes?*
>
> Modeled loosely on [jun-zeng/Audit-log-analysis](https://github.com/jun-zeng/Audit-log-analysis).
> Started: July 2026. Maintainer: Ishmam.

## How this repo is organized

Four tracks. A and B are the general background from the original scoping pass.
C and D are where the current focused direction lives — read those first.

- **Track A — External Guardrails** (context / related work): runtime enforcement,
  formal verification, isolation architectures, benchmarking & threat modeling.
- **Track B — Internal / Epistemic Signals** (general): uncertainty & calibration,
  activation probing / representation monitoring, self-consistency as a signal,
  intent & deception detection, metacognition.
- **Track C — Domain-Specific Trajectory Failure Detection** (current focus): coding
  agents, web agents, GUI agents — behavioral and internal signals that predict
  failure early, before task completion.
- **Track D — Alignment-Adjacent (Anthropic Alignment Team)**: work on why agentic
  misalignment happens and what generalizes — structurally the training-side mirror
  of your inference-side question.

Each paper entry follows this format:

```
- **[Title](link)** — Authors, Venue Year.
  *One-line mechanism.* Gap/limitation. `tags: #tag1 #tag2`
```

See [`papers.csv`](papers.csv) for the structured/filterable version of the same data
(better for sorting by year, tag, or "read status" once this grows past ~40 entries).
See [`SEARCH_LOG.md`](SEARCH_LOG.md) for queries already run, so you don't duplicate search effort.

---

## Track A: External Guardrails (context)

### Runtime Enforcement
- **[ShieldAgent](https://proceedings.mlr.press/v267/chen25ae.html)** — Chen, Kang, Li, ICML 2025.
  *Extracts LTL safety rules from policy docs, enforces via Markov Logic Network at inference time.*
  Gap: degrades on hallucination-related risk — exactly where internal confidence matters. `tags: #ltl #policy #runtime`
- **[AgentSpec](https://arxiv.org/abs/2503.18813)** — Wang, Poskitt, Sun, ICSE 2026.
  *DSL for runtime constraints (trigger → predicate → enforcement action).*
  Gap: purely deterministic, no confidence-conditioned enforcement. `tags: #dsl #runtime #deterministic`
- **[CaMeL](https://arxiv.org/abs/2503.18813)** — Debenedetti et al., 2025.
  *Separates trusted planning (P-LLM) from untrusted extraction (Q-LLM); capability-tracking interpreter.*
  Gap: no graceful escalation when task requires trusting untrusted data. `tags: #capability-tracking #prompt-injection`
- **[IsolateGPT](https://arxiv.org/abs/2403.04960)** — Wu et al., 2024.
  *Process isolation for third-party LLM apps via permission-controlled hub.*
  Gap: intra-app compromise unaddressed; paper admits internal safety assessment is weak. `tags: #isolation #sandboxing`

### Formal & Probabilistic Verification
- **[VeriGuard](https://arxiv.org/abs/2510.05156)** — Miculicich et al., 2025.
  *Synthesizes formally verified Python policies (Hoare triples via Nagini).*
  Gap: soundness depends on LLM-generated constraints capturing intent correctly — no internal check on that translation step. `tags: #formal-verification #hoare-logic`
- **[AgentGuard](https://ieeexplore.ieee.org/) (search title)** — Koohestani, ASEW 2025.
  *Online MDP + probabilistic model checking (PCTL/Storm) for behavioral assurance.*
  Gap: tracks behavioral frequency, not epistemic state — a high-probability path can still contain uncertain intermediate steps. `tags: #probabilistic-verification #mdp`

### Benchmarking & Threat Modeling
- **[ASB (Agent Security Bench)](https://arxiv.org/abs/) (search title)** — Zhang et al., ICLR 2025.
  *4 attack types × 10 scenarios × 13 LLMs; 84.3% avg attack success, no defense < 44.5%.*
  Gap: more capable models = more vulnerable (instruction-following amplifies susceptibility). `tags: #benchmark #attack-taxonomy`
- **[RealSafe](https://aclanthology.org/) (search title)** — Ma, COLING 2025.
  *12 LLMs × 14 scenarios, paired Risk/Helpfulness metric.*
  Gap: models proceed confidently through ambiguous instructions — epistemic overconfidence, not adversarial failure. `tags: #benchmark #risk-utility-tradeoff`
- **[FAIL-TaLMs](https://aclanthology.org/) (search title)** — Treviño et al., NAACL 2025.
  *Tool-augmented LMs under under-specified queries / unavailable tools. Claude: 56% uncertainty-awareness (28–54pt above peers), doesn't translate to better outcomes.*
  Gap: **awareness-to-action gap** — this is your strongest existing evidence pointer. `tags: #benchmark #uncertainty-awareness #tool-use`
- **[MCIP](https://arxiv.org/abs/) (search title)** — Jing et al., EMNLP 2025.
  *CI-grounded taxonomy of 15 MCP attack types + fine-tuned guard model.*
  Gap: fine-tuning induces "over-approval" bias — executes valid-looking calls without questioning them. `tags: #mcp #taxonomy #guard-model`
- **[Safe-MCP](https://github.com/SAF-MCP/safmcp)** — 2025.
  *MITRE ATT&CK adapted to MCP; 85 techniques / 14 tactics.*
  Gap: purely descriptive, all mitigations protocol-layer. `tags: #mcp #taxonomy`

---

## Track B: Internal / Epistemic Signals (core focus)

### Uncertainty, Calibration & Abstention
- **[Uncertainty-Based Abstention Improves Safety and Reduces Hallucinations](https://arxiv.org/abs/2404.10960)** — Tomani, Chaudhuri, Evtimov, Cremers, Ibrahim (Meta/TUM), 2024.
  *Statistical uncertainty + In-Dialogue Uncertainty (verbalized); abstention improves correctness 2-8%, catches ~50% hallucinations on unanswerable Qs, 70-99% safety improvement.*
  Anchor paper for your proposal — not agentic-specific though (QA setting). `tags: #abstention #calibration #core-anchor`

### Activation Probing / Representation-Level Monitoring
- **[Harmful Intent as a Geometrically Recoverable Feature of LLM Residual Streams](https://arxiv.org/abs/2604.18901)** — 2026.
  *Linear direction for harmful intent, stable across 12 models / 4 architectures / abliterated variants; 100 labeled examples suffice. AUROC near-ceiling but TPR@1%FPR only 0.30 for a deployed classifier — important methodological caveat.*
  `tags: #activation-probing #linear-probe #harmful-intent`
- **[Why Safety Probes Catch Liars But Miss Fanatics](https://arxiv.org/abs/2603.25861)** — 2026.
  *Difference-in-means probing (Marks & Tegmark methodology) distinguishes deceptive vs. "fanatical"/self-consistent hostile models; intent crystallizes in middle layers (16-21).*
  Directly relevant: shows probes work for deception but not for agents that "believe their own" harmful reasoning. `tags: #activation-probing #deception #layer-analysis`
- **[Building Production-Ready Probes For Gemini](https://arxiv.org/abs/2601.11516)** — 2026.
  *Survey/practitioner report on deploying activation probes as safety monitors in production; cites probes as cheaper than output-classifiers.*
  Good source for practical deployment considerations + further citation chasing. `tags: #activation-probing #production #survey`
- **[NeuroFilter: Privacy Guardrails for Conversational LLM Agents](https://github.com/VoltAgent/awesome-ai-agent-papers)** — 2026 (via VoltAgent awesome-list).
  *Activation-space linear separation for privacy-violating intent + multi-turn drift detection.*
  `tags: #activation-probing #privacy #drift-detection`
- **[Learning to Stay Safe: Adaptive Regularization Against Safety Degradation during Fine-Tuning](https://arxiv.org/abs/2602.17546)** — 2026.
  *Harmful intent linearly predictable pre-decoding (AUROC > 0.9); uses activation-based risk predictor to modulate SFT loss dynamically.*
  Interesting because it uses the internal signal at *training* time, not just inference — adjacent but different application. `tags: #activation-probing #training-time #adaptive-regularization`

### Multi-Agent / Systemic Internal Monitoring
- **[Detecting Multi-Agent Collusion Through Multi-Agent Interpretability](https://arxiv.org/abs/2604.01151)** — 2026.
  *Extends single-agent deception probing to multi-agent collusion detection; white-box activation access threat model, explicitly framed via AI Control literature (Greenblatt et al. 2024).*
  Very close to your "internal state as first-class safety primitive" framing, but for multi-agent systems — worth reading closely for methodology to borrow/differentiate from. `tags: #multi-agent #activation-probing #ai-control #core-related`

### Intent-Aware Detection (industry / applied)
- **[Beyond Authorization: Intent-Aware Detection for AI Agents](https://zenity.io/blog/security/intent-aware-detection)** — Zenity, 2026 (industry blog, not peer-reviewed).
  *Passes input through a small LLM, reads internal activations to classify malicious intent rather than analyzing text I/O.*
  Not academic, but useful as evidence the industry is converging on the same idea independently — cite as motivation, not as a rigorous source. `tags: #industry #intent-detection #motivation-evidence`

### To Triage (found but not yet read/categorized)
- Self-consistency as a security signal — search "self-consistency prompt injection detection", "reasoning path divergence adversarial"
- Metacognition / "knowing what you don't know" in LLM agents — search "LLM introspection agentic", "metacognitive agents tool use"
- Epistemic action vocabulary (express-uncertainty, escalate-with-reason as first-class actions) — likely needs to be searched via RL/agent-training literature, not safety literature directly

---

---

## Track C: Domain-Specific Trajectory Failure Detection (current focus)

### Coding Agents
- **[AgentForesight](https://arxiv.org/abs/2605.08715)** — 2026.
  *Reframes failure detection as **online auditing**: at each step, an auditor sees only the prefix and must alarm at the earliest decisive error, not post-hoc. Trained via coarse-to-fine RL on AFTraj-2K corpus (Coding, Math, Agentic domains). Compact 7B auditor beats GPT-4.1/DeepSeek-V4-Pro on step localization.*
  **This is your closest existing analog.** Its auditor is a separate judge model reading text trajectories — it does not use the acting agent's own internal state. That's your open differentiation: does the *acting model's own* uncertainty/activations predict the same decisive-error point earlier or more cheaply than an external judge? `tags: #coding #online-auditing #early-failure #core-related #differentiate-here`
- **[TrajAudit](https://arxiv.org/abs/2605.26563)** — 2026.
  *Post-hoc failure diagnosis for coding agents; folds trajectory via a failure-keyword dictionary, uses an investigator agent to localize the failing step.*
  Post-hoc, not online — good contrast case for why online/early detection is harder and more valuable. `tags: #coding #post-hoc #failure-localization`
- **[Beyond Resolution Rates: Behavioral Drivers of Coding Agent Success and Failure](https://arxiv.org/html/2604.02547v1)** — Mehtiyev & Assunção, 2026.
  *Structural trajectory properties (how agents sequence reading/patching/validation) distinguish success from failure more reliably than trajectory length; explicitly calls for real-time monitoring using behavioral signatures.* `tags: #coding #behavioral-signatures #benchmark-analysis`
- **[Coherence Collapse: Diagnosing Why Code Agents Fail After Reaching the Right Code](https://arxiv.org/pdf/2603.24631)** — 2026.
  *Identifies "Coherence Collapse": agent reaches correct code, then overwrites/thrashes it. Length-independent, dissociates from context-window degradation. Proposes edit-commit checkpointing as an intervention.*
  Interesting failure mode because it's *not* a capability failure — the right answer existed mid-trajectory and was lost. Good test case for whether internal confidence dips at the collapse point. `tags: #coding #failure-taxonomy #checkpointing`
- **[Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures](https://arxiv.org/pdf/2604.03515)** — 2026.
  *Surveys trajectory/behavior studies across agents; failure trajectories run 12-82% longer than successful ones; repo navigation dominates over patch writing.* `tags: #coding #survey #behavioral-signatures`

### Web Agents
- *(to triage — search "web agent trajectory success prediction", "web agent hallucination detection", cross-reference MIRAGE-Bench: "LLM agent is hallucinating and where to find them")*

### GUI Agents
- **[GEM: Gaussian Embedding Modeling for OOD Detection in GUI Agents](https://arxiv.org/pdf/2505.12842)** — 2025.
  *GUI agents are vulnerable to out-of-distribution risk (non-existent functions/apps, exceeding capability). Models trajectory embeddings as Gaussians for OOD detection.*
  Directly relevant framing: OOD-ness as an early-warning signal, close cousin to uncertainty-based abstention. `tags: #gui #ood-detection #embedding`
- **[GUITester: Enabling GUI Agents for Exploratory Defect Discovery](https://arxiv.org/pdf/2601.04500)** — 2025/2026.
  *Analyzes why GUI agents fail to detect defects near defect locations: "Repetition-Induced Termination" (retry loop until hard timeout) and "Goal Conflict" (planning/execution/reflection modules misinterpret defects as failures).*
  Concrete failure-mode taxonomy for GUI agents — useful for defining what "early signal" should predict. `tags: #gui #failure-taxonomy #anomaly-detection`
- **[DiagEval: Trajectory-Conditioned Diagnosis for Reliable Software Evaluation with GUI Agents](https://arxiv.org/pdf/2605.17439)** — 2026.
  *Formulates evaluator failure (not just agent failure) as trajectory-level diagnosis; distinguishes software defects from agent-side execution misses using cross-trajectory evidence.* `tags: #gui #evaluator-reliability #diagnosis`
- **[Recovering Policy-Induced Errors: Benchmarking and Trajectory Synthesis for Robust GUI Agents](https://arxiv.org/pdf/2605.29447)** — 2026.
  *Benchmark + trajectory synthesis for GUI agent robustness; useful bibliography for the broader GUI-agent trajectory literature (AgentTrek, AGUVis, GUI-Robust, etc.).* `tags: #gui #benchmark #robustness`

### Cross-Domain / General Trajectory Anomaly Detection
- **Trajectory Guard** (via VoltAgent awesome-list, 2026).
  *Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss for real-time anomaly detection in agent action trajectories.*
  Not internal-state-based (operates on action sequences), but directly relevant as an architecture baseline for "real-time" claims. `tags: #cross-domain #anomaly-detection #autoencoder;to-read`
- **Agentic Confidence Calibration / Holistic Trajectory Calibration** (via VoltAgent awesome-list, 2026).
  *Extracts process-level features across an agent's entire trajectory to diagnose failures — calibration framing applied at trajectory level rather than single-step.*
  Closely adjacent to your framing; check if it uses internal (activation/logit) features or only external process features. `tags: #cross-domain #calibration #trajectory-level;to-read`
- **When Agents Fail: A Comprehensive Study of Bugs in LLM Agents** (via VoltAgent awesome-list, 2026).
  *Analyzes 1,187 bug reports from LLM agent software across seven frameworks — useful empirical failure taxonomy to ground what "failure" should mean across domains.* `tags: #cross-domain #failure-taxonomy #empirical;to-read`

---

## Track D: Alignment-Adjacent (Anthropic Alignment)

Two sources here, and they're not equivalent: **alignment.anthropic.com** (the
Alignment Science Blog) is where the technical research notes live — several entries
below are core anchors, not just adjacent context. **anthropic.com/research** is the
polished, PR-facing version of a subset of that work.

### Alignment Science Blog (alignment.anthropic.com) — primary source, check this often

**Core anchors — read these regardless of final domain choice:**
- **["Language Models (Mostly) Know What They Know"](https://www.anthropic.com/research/language-models-mostly-know-what-they-know)** — Kadavath et al., 2022.
  *Models can evaluate whether their own statements are true and predict in advance whether they'll answer correctly.* Likely the foundational paper underlying every uncertainty-as-signal approach since. `tags: #uncertainty #foundational #core-anchor`
- **["Simple Probes can Catch Sleeper Agents"](https://www.anthropic.com/research/probes-catch-sleeper-agents)** — 2024.
  *Linear probing detects when a backdoored model is about to behave dangerously, even after it has learned to behave safely during training/eval.* Structurally identical to your thesis (internal signal precedes the bad action) just applied to backdoors rather than task failure. `tags: #activation-probing #early-detection #core-anchor`
- **["Model-Internals Classifiers"](https://alignment.anthropic.com/2025/cheap-monitors/)** — 2025.
  *Benchmarks approaches that reuse LLM internals to make monitoring cheaper than full output-classifier passes.* Directly relevant methodology/cost-comparison for anything you build. `tags: #activation-probing #monitoring #cost #core-anchor`

**Domain-relevant:**
- **["Monitoring Computer Use via Hierarchical Summarization"](https://alignment.anthropic.com/2025/summarization-for-monitoring/index.html)** — Feb 2025.
  *Anthropic's own approach to monitoring computer-use (GUI-adjacent) agents via hierarchical summarization of trajectories.* If your domain lands on GUI/computer-use agents, this is Anthropic's own prior art to position against — note it's summarization-based (external/text), not internal-state-based. `tags: #gui #computer-use #monitoring #differentiate-here`
- **["Forecasting Rare Language Model Behaviors"](https://www.anthropic.com/research/forecasting-rare-behaviors)** — Jones, Tong et al., 2025.
  *Forecasts whether risks will occur post-deployment using limited test data.* Relevant framing for "predicting rare failure before it happens" even outside the safety context. `tags: #forecasting #rare-events #methodology`

**Important caveat/risk for your method:**
- **["Reasoning Models Don't Always Say What They Think"](https://www.anthropic.com/research/reasoning-models-dont-say-think)** — Chen et al., 2025.
  *Reasoning models don't always verbalize their true reasoning — casts doubt on whether monitoring chain-of-thought text alone reliably catches issues.* Important for you: if your "trajectory signal" is text/CoT-based rather than activation-based, this is evidence of a ceiling on that approach — a reason to prefer internal/activation signals over text-monitoring where feasible. `tags: #cot-faithfulness #caveat #core-related`

**Monitor robustness (stress-testing whatever you build):**
- **["SLEIGHT-Bench"](https://alignment.anthropic.com/2026/sleight-bench/)** — May 2026.
  *Benchmark of evasive transcripts exploiting blind spots of frontier monitoring systems.* Use this as a template for adversarially evaluating your own early-detection signal, not just testing it on natural failures. `tags: #monitor-robustness #benchmark #adversarial`
- **["Activation Oracles"](https://alignment.anthropic.com/2025/activation-oracles/)** — Dec 2025.
  *Trains LLMs to answer questions about their own activations in natural language, generalizing to uncovering misalignment from fine-tuning.* A different mechanism (verbalized self-report of internals) worth comparing against direct probing. `tags: #activation-probing #introspection #self-report`
- **["Introspection Adapters"](https://alignment.anthropic.com/2026/introspection-adapters/)** — Apr 2026.
  *Trains an LLM to self-report behaviors it learned during fine-tuning; generalizes across very different fine-tuning methods.* `tags: #introspection #self-report;to-read`

**Broader framing (read if time permits):**
- **["Putting up Bumpers"](https://alignment.anthropic.com/2025/bumpers/)** — Apr 2025.
  *Argues that even without solving alignment, catching-and-fixing misalignment (i.e., detection + correction pipelines) is a tractable goal.* Good framing device for your thesis statement: you're not claiming to fix agent reliability, you're building the "catch it early" bumper. `tags: #framing #methodology`

### anthropic.com/research (main site) — secondary/announcement layer
- **["Teaching Claude why"](https://www.anthropic.com/research/teaching-claude-why)** — May 2026. *(already logged above; polished version of the alignment.anthropic.com post)*
- **["From shortcuts to sabotage: reward hacking"](https://www.anthropic.com/research/emergent-misalignment-reward-hacking)** — Nov 2025.
- **["Next-generation Constitutional Classifiers"](https://www.anthropic.com/research/next-generation-constitutional-classifiers)** — Jan 2026.
- **["Automated Alignment Researchers"](https://www.anthropic.com/research/automated-alignment-researchers)** — Apr 2026.
- **["Disempowerment patterns in real-world AI usage"](https://www.anthropic.com/research/disempowerment-patterns)** — Jan 2026.

*(Browse both regularly: [alignment.anthropic.com](https://alignment.anthropic.com/) for research notes, [anthropic.com/research/team/alignment](https://www.anthropic.com/research/team/alignment) for polished write-ups.)*

---

## Related existing curated lists (don't duplicate, cross-reference instead)
- [VoltAgent/awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers) — broad 2026 agent paper tracker, not internal-signal-focused but good raw feed.

## Contributing
When you add a paper: fill in `papers.csv` first (structured), then promote well-understood
entries into this README with the gap/limitation written in your own words — that act of writing
the gap is where your literature review argument actually gets built.
