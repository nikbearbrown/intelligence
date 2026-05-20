# Research notes — Chapter 17: AI as Data Point

**Book:** intelligence (*Intelligence? A Natural History of Mind Across the Animal Kingdom*)
**Chapter slug:** ai-as-data-point
**Date:** 2026-04-25
**Command:** `/chapter`
**Voice anchoring:** `voice-unanchored`. Both `style/` folders empty. Seventeenth drafted unit.

---

## Concept

The synthesis chapter. Slot artificial intelligence into the operational framework the previous sixteen chapters have built — the same per-axis comparative-cognition lens applied to bacterium, worm, octopus, crow, ape, dolphin, and human. The chapter argues that AI does not sit at a single height on a single axis but produces an *unfamiliar profile* — extreme highs on pattern recognition / prediction / retrieval, near-zero or sub-worm on embodied navigation, causal reasoning beyond training distribution, metacognitive monitoring, and participation in cumulative culture. The honest answer to "where does AI sit overall" depends entirely on which Chapter-1 definition of intelligence one started with — which was the structural point Chapter 1 established.

## Specification move

Three things unbundled before empirical work:

1. **Single-axis vs multi-axis question.** The framing "is AI as intelligent as a human" assumes intelligence is a single quantity. The book has spent sixteen chapters arguing it isn't. The single-axis question, applied to AI, has no good answer because it has no good answer applied to anything.
2. **Skill vs skill-acquisition efficiency (Chollet 2019).** The same external behavior can come from very different cognitive architectures. AI tends to "buy" skill with massive data; biology tends to "build" skill with priors + few-shot generalization. Chollet's ARC benchmark makes the difference visible.
3. **Function present vs stakes present.** The chapter's deepest specification. Most cognitive functions in this book exist in their carriers because the carrier has stakes — homeostatic costs, mortality, lineage. AI systems can have *functional analogs* of these capacities (interpretability has measured emotion-like internal states, ToM-like surface outputs) without having stakes that produced the capacities in biology. The chapter treats function as real where it can be observed and refuses to over-import the biological meaning.

## Empirical vs. non-empirical sub-claims

| Sub-claim | Status |
|---|---|
| Geirhos et al. 2018/2019 ImageNet CNNs biased toward texture not shape | **Empirical**, settled |
| Modern LLMs pass standard false-belief tests but fail Ullman perturbations | **Empirical**, settled |
| AI is superhuman at next-token prediction and benchmark pattern-recognition | **Empirical**, settled |
| Frontier models score below human ceiling on Chollet ARC | **Empirical**, settled (current as of 2026) |
| AI lacks stakes in the biological sense | **Architectural observation**, not empirically tested but uncontested |
| Function-vs-stakes distinction | **Synthetic claim**, useful framing |
| Shadow phylogeny / cognitive extremophile framing | **Interpretive claim**, derived from per-axis pattern |
| AI is participating in aggregation but not cumulative-culture layer of CI | **Inferred** (set up in Ch. 16) |
| The single-axis question is malformed | **Synthetic**, derived from Ch. 1 + 2-16 |

## Primary sources

1. **Geirhos, R., Rubisch, P., Michaelis, C., Bethge, M., Wichmann, F.A., Brendel, W. (2019).** "ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness." ICLR 2019 (Oral). https://arxiv.org/abs/1811.12231 — chapter's hook.
2. **Chollet, F. (2019).** "On the Measure of Intelligence." arXiv:1911.01547. https://arxiv.org/abs/1911.01547 — skill vs skill-acquisition framing + ARC benchmark.
3. **Ullman, T. (2023).** "Large language models fail on trivial alterations to theory-of-mind tasks." arXiv:2302.08399. https://arxiv.org/abs/2302.08399 — chapter reuses from Chs. 11/14 in the ToM section.
4. **Legg, S. & Hutter, M. (2007).** "Universal Intelligence: A Definition of Machine Intelligence." arXiv:0712.3329. https://arxiv.org/abs/0712.3329 — Chapter-1 callback.

Also referenced without primary URLs (already established in earlier chapters of this book):
- All sixteen prior chapters of this book — the chapter explicitly calls back to them by axis.
- Pearl's ladder of causation (Ch. 14).
- Polanyi tacit knowledge / record-vs-practice (Ch. 16).
- Tomasello cumulative culture / ratchet (Ch. 15-16).
- Sternberg, Wechsler, Boring definitions (Ch. 1).

## Mechanism for the deep-dive

*A walk through five of the book's axes (pattern recognition, theory of mind, metacognition, collective intelligence, navigation/embodiment) plus the cross-cutting "stakes" axis, with each axis's AI placement reported honestly.* §17.3 walks the axes; §17.4 names the resulting profile (the shadow phylogeny, the cognitive extremophile niche). The chapter's load-bearing claim: the profile is unlike any biological organism's, and trying to summarize it as a single "level" is the framing error Chapter 1 was written to prevent.

## Central analogy

*AI as a shadow phylogeny — a non-biological lineage of cognitive systems with its own profile and its own selection pressures (gradient descent, RLHF, training-corpus composition) rather than the biological selection pressures (mortality, lineage, homeostasis) that shaped every other system in the book.* The analogy does productive work because it lets the reader see AI as having its own niche rather than as an inferior copy of biological cognition. Where it breaks: phylogeny in biology means descent with modification through generations of replicators with stakes; AI lacks generational replication in the biological sense. The chapter names the breakdown ("a different ladder, one that nature did not build") rather than smuggle it in.

## Voice notes

- Natural-history register continued. The Geirhos cat-with-elephant-skin scene as the chapter's anchor (a clean diagnostic that opens the door to the architectural reading).
- First person used at four points: §17.3 metacognition section ("I am not aware of a passing case"), §17.4 ("I conclude"), "What would change my mind," "Still puzzling." Sparingly.
- Single-sentence paragraphs at three pivots: §17.3 closing of the stakes section ("The function is present. The stakes are not."), §17.4 mid ("It is a different ladder, one that nature did not build"), §17.5 closing ("It is, on the present evidence, an additive presence in our world").
- Math kept off the page — the chapter is qualitative-architectural.
- **No Extension Note** — this is the synthesis chapter. The Extension Note device has been the leitmotif builder; Chapter 18 will name the leitmotif explicitly. Including an Extension Note here would dilute the structural close of the device.

## Risks flagged

- **Overclaiming AI absences.** The chapter is careful to label what is observed (functional emotion-like internal states are real, pattern recognition is real, retrieval is real) versus what is unestablished (metacognitive machinery, theory-of-mind process, participation in cumulative-culture layer). The pattern is mixed; the chapter reflects the mixedness.
- **Underclaiming AI capabilities.** The chapter explicitly names AI as superhuman on certain axes. It does not adopt the dismissive "stochastic parrots" framing. The functional capacities are real where they can be measured.
- **The "no stakes" claim is architectural, not empirical.** AI systems do not die, do not have lineages in the biological sense, do not face homeostatic costs. This is a structural fact about current systems, not a measured deficit. The chapter labels this as architectural observation.
- **Frontier model performance moves fast.** ARC scores, ToM benchmark scores, etc. shift on a months-to-quarters timescale. The chapter avoids citing specific 2025-2026 numbers that will be stale; instead it cites the structural pattern (failure on perturbation, scaling with compute rather than priors) which has held even as raw scores climb.
- **Many candidate axes from the brief were compressed.** The brief touched on emotion-vector probes (Anthropic interpretability work), JEPA/world models, navigation successor representation, MirrorBench, Mirror-Window Game, Artificial Dopamine Q-learning, mechanized convergence, narrow-slice-of-humanity training data. The chapter does not cite the more recent and unverified items. The Anthropic functional-emotion interpretability work is referenced obliquely ("functional internal states have been measured in interpretability studies") without citing a specific paper that I could not verify in this session.
- **The "Mirror-Window Game" / "Claude Opus 4.6 marking itself"** item from the brief was DROPPED. Could not be verified, looked speculative, no load-bearing role.
- **The "Artificial Dopamine 2024 Q-learning algorithm" claim** from the brief was DROPPED. Could not be verified.
- **Specific numbers** like "200 million parameters" for ResNet — left as approximations or qualitative descriptions where exactness was not load-bearing.

## Process note

Seventeenth drafted unit. Word count 2967 — within the 2,000–4,000 envelope, on the lower-middle end. The argument is dense and the chapter's structural function (synthesis pass setting up Ch. 18) does not benefit from padding. Voice still flagged `voice-unanchored` — seventeen units now in the same register; the case for clearing the flag is overwhelming.
