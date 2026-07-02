# Search Log

Track every search session here — database, exact query, date, and a one-line note on
yield. This is the single highest-leverage file for avoiding re-treading ground weeks
from now when you've forgotten what you already tried.

| Date | Source | Query | Yield / notes |
|---|---|---|---|
| 2026-07-01 | web (general) | "activation probing detect harmful intent agent before action 2026" | 6 relevant hits: geometric harmful-intent feature paper, multi-agent collusion detection, VoltAgent awesome-list, Zenity industry post. Strong seed batch for Track B. |

## Queued searches (not yet run)
- Semantic Scholar: citations of Tomani et al. 2024 (Uncertainty-Based Abstention) — filter for "agent" or "tool"
- Semantic Scholar: citations of Treviño et al. 2025 (FAIL-TaLMs) — this is your best anchor for the awareness-to-action gap, worth seeing who's built on it
- arXiv cs.CR: "self-consistency" + "prompt injection"
- arXiv cs.CL: "metacognition" + "LLM agent"
- Google Scholar: "epistemic action" + "language model agent"
- Connected Papers: seed graph from ShieldAgent AND from the Harmful Intent Geometric Feature paper — compare who cites both (that intersection is your niche)

## Search hygiene notes
- Re-run the core keyword clusters monthly — this subfield moves fast (note how many
  seed hits above are from 2026 itself).
- When a search yields an industry blog post making your exact argument (e.g. Zenity),
  that's a signal of good timing/relevance, not a reason to deprioritize the academic
  version — capture both, cite academic sources in the actual paper.

| 2026-07-01 | web (general) | "coding agent trajectory failure prediction early detection 2026" | Major hit: AgentForesight (closest existing analog to proposed direction — online auditing, prefix-only, earliest-alarm). Also TrajAudit, Coherence Collapse, Behavioral Drivers survey. |
| 2026-07-01 | web (general) | "web agent GUI agent trajectory anomaly detection failure early 2026" | GEM (OOD detection), GUITester (failure taxonomy), DiagEval, VoltAgent list hits (Trajectory Guard, Agentic Confidence Calibration, When Agents Fail). Web agent-specific results thin — needs a dedicated pass. |
| 2026-07-01 | web.fetch | anthropic.com/research/team/alignment | Team overview + publication list. Most relevant: "Teaching Claude why" (generalization via reasoning-based training), "From shortcuts to sabotage" (reward hacking root cause). |
| 2026-07-01 | web.fetch | anthropic.com/research/teaching-claude-why | Full read — core finding: training on reasoning-about-why generalizes OOD far better than demonstration/eval-matching. Structural parallel to internal-state-as-signal thesis. |

## Queued searches (updated)
- Web agents specifically: "web agent trajectory success prediction", "web agent hallucination detection", "MIRAGE-Bench web agent"
- "agentic confidence calibration holistic trajectory" (find full paper, check if internal-state based)
- Semantic Scholar: citations of AgentForesight — see who's extending it, and whether anyone's already tried the internal-state version
- Anthropic alignment: check "auditing hidden objectives" (referenced inside Teaching Claude Why) and "persona selection model" for internal-signal relevance

| 2026-07-01 | web.fetch | alignment.anthropic.com | Full research-notes blog index (2022-2026). Much more technical than main site. Core anchors found: Kadavath 2022 (uncertainty foundational), Simple Probes Catch Sleeper Agents (2024), Model-Internals Classifiers (2025). Domain-relevant: Monitoring Computer Use via Hierarchical Summarization (GUI-adjacent, Anthropic's own prior art). Important caveat found: Reasoning Models Don't Always Say What They Think (CoT unfaithfulness — argues for activation-level over text-level monitoring). |
