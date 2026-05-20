# Research notes — Chapter 9: Simulation and Planning

**Book:** intelligence (*Intelligence? A Natural History of Mind Across the Animal Kingdom*)
**Chapter slug:** simulation-and-planning
**Date:** 2026-04-25
**Command:** `/chapter`
**Voice anchoring:** `voice-unanchored`. Both `style/` folders empty. Ninth drafted unit.

---

## Concept

Mental simulation as the mammalian (and corvid) cognitive innovation. The chapter argues that hippocampal forward and reverse replay is the neural substrate of running the world forward in the head, that this capacity climbs Pearl's ladder of causation from intervention to counterfactual reasoning, and that the rat-regret findings of Steiner & Redish 2014 demonstrate counterfactual processing in non-humans.

## Specification move

Three things unbundled before empirical work:

1. **Disappointment vs. regret.** Disappointment is the generic *worse-than-expected* signal (the dopamine dip from Ch. 8). Regret is the specific *I had a better option that I did not take* signal that requires representing the unchosen action. Only the second qualifies as counterfactual reasoning.
2. **Model-free vs. model-based reinforcement learning** (callback to Ch. 8). Model-free caches values; model-based simulates outcomes. The chapter is about model-based.
3. **Substrate vs. function** (callback to Ch. 6's lamprey-pallium argument). The mammalian neocortex is one anatomical solution to simulation. The corvid brain is another. The function evolved twice; the architecture is not the constraint.

## Empirical vs. non-empirical sub-claims

| Sub-claim | Status |
|---|---|
| Rats at Restaurant Row turn their heads back after skipping a good offer and encountering a bad one | **Empirical**, settled (Steiner & Redish 2014) |
| OFC neurons during the look-back encode the missed action, not the missed reward | **Empirical**, settled (Steiner & Redish 2014) |
| Pre-movement hippocampal replay sweeps depict future paths to remembered goals | **Empirical**, settled (Pfeiffer & Foster 2013) |
| Post-reward hippocampal replay runs in reverse order from the reward | **Empirical**, settled (Foster & Wilson 2006) |
| Tolman's VTE is the behavioral signature of mental simulation | **Empirical/inferential**, supported by modern neurophysiology |
| Western scrub jays remember what-where-when of caching episodes | **Empirical**, settled (Clayton & Dickinson 1998) |
| Corvids plan for future motivational states they do not currently have | **Empirical**, well-supported (Clayton lab follow-up work) |
| Bischof-Köhler hypothesis (animals stuck in time) | **Empirical**, falsified for corvids and some primates |
| Sur ferret-rewiring experiments show neocortex pluripotency | **Empirical**, settled |
| Rao-Ballard predictive-coding framework explains neocortical computation | **Theoretical/well-supported**, not airtight; alternative frameworks exist |

## Primary sources

1. **Steiner, A.P. & Redish, A.D. (2014).** "Behavioral and neurophysiological correlates of regret in rat decision-making on a neuroeconomic task." *Nature Neuroscience* 17: 995–1002. https://www.nature.com/articles/nn.3740 — chapter's hook and load-bearing counterfactual evidence.
2. **Pfeiffer, B.E. & Foster, D.J. (2013).** "Hippocampal place-cell sequences depict future paths to remembered goals." *Nature* 497: 74–79. https://www.nature.com/articles/nature12112 — forward replay.
3. **Foster, D.J. & Wilson, M.A. (2006).** "Reverse replay of behavioural sequences in hippocampal place cells during the awake state." *Nature* 440: 680–683. https://www.nature.com/articles/nature04587 — reverse replay.
4. **Clayton, N.S. & Dickinson, A. (1998).** "Episodic-like memory during cache recovery by scrub jays." *Nature* 395: 272–274. https://www.nature.com/articles/26216 — what-where-when memory.
5. **Tolman, E.C. (1948).** "Cognitive Maps in Rats and Men." *Psychological Review* 55: 189–208. https://psychclassics.yorku.ca/Tolman/Maps/maps.htm — VTE and the cognitive-map argument.

Other references in the chapter without primary URLs:
- Sur, Garraghty, Roe ferret-rewiring work (referenced by name).
- Adams & Dickinson 1981 devaluation (already cited in Ch. 8).
- Pearl's *The Book of Why* / ladder of causation (referenced by name).
- Apollo simulators / digital twins (treated in the Extension Note).

## The mechanism for the deep-dive

*Hippocampal replay as the substrate of simulation.* §9.3 walks the architecture: place cells fire at specific locations during normal movement; during sharp-wave ripples (~100 ms high-frequency oscillations in CA1/CA3) the same place cells fire in fast sequences that depict trajectories rather than current location. Forward replay (Pfeiffer-Foster 2013) before movement to a remembered goal; reverse replay (Foster-Wilson 2006) after reward arrival. The two replay directions map onto two computational jobs — prospective planning and credit assignment. One sentence: *the hippocampus is a trajectory simulator running the same place-cell map that previously mapped the rat's current location, sweeping that map forward to plan future paths and backward to assign reward credit through past ones.*

## Central analogy

*Replay as digital-twin run.* The hippocampal replay sweep is a fast, compressed rehearsal of a trajectory the animal might or did take, on substrate that normally encodes actual movement. The Extension Note develops this directly: a NASA digital twin runs a fast computational rehearsal of a candidate intervention before the operator commits to it; the rat's hippocampus runs a fast neural rehearsal of a candidate trajectory before the rat commits to it. Where the analogy breaks: digital twins are typically built deliberately on engineering models; hippocampal replay emerges from cellular dynamics that the brain did not "design" for the purpose. The shared structure is the *fast compressed rehearsal of an unconfirmed trajectory*, not the engineering pedigree.

## Voice notes

- Natural-history register continued. The Restaurant Row scene as the chapter's anchor.
- First person used in §9.3 ("I find this an extraordinary result"), §9.5 ("I find this the most important comparative result"), §9.6 ("I conclude"). Sparingly.
- Single-sentence paragraphs at three pivots: end of §9.1 ("The chapter is the architecture under that look-back"), end of §9.4 ("The rats showed the second" — actually the closing of §9.4 is the *passed-it* line about the policy change), §9.6 closing ("The brain that regrets is the brain that imagines. The brain that imagines is the brain that, in the end, builds digital twins.").
- Math kept off the page. The chapter is mechanism-rich but not equation-rich; the deep-dive describes neural sequences and timescales without formalizing them.
- Extension Note (eighth in book): digital twins, Apollo simulators, scenario planning. Reinforces the leitmotif from Ch. 7 (additive vs substitutive extension) but tilts toward additive — the simulator extends the cortex's reach without obviously substituting for it.

## Risks flagged

- **The chapter is rich on hippocampal replay** but compresses the neocortex-as-generative-model story. The Rao-Ballard predictive-coding claim is referenced but not deep-dived. If review wants more on predictive coding, it would need a section that displaces some of the replay material.
- **Corvids treated compactly.** Clayton-Dickinson 1998 is the load-bearing citation; the broader Clayton-lab follow-ups are referenced in summary. If review wants more on the social-theft / re-caching results, that is where to expand.
- **Pearl's ladder of causation** is named without a primary citation. Pearl & Mackenzie's *The Book of Why* (2018) is the popular treatment; the more technical version is in Pearl 2009 *Causality*. Neither is in the citation list. If review wants Pearl directly anchored, that is the place.
- **The Sur ferret-rewiring claim** is well-known but cited by name only. The original is Sur, Garraghty, Roe 1988 *Science* and the Sharma, Angelucci, Sur 2000 *Nature* paper. Could be added if review wants tighter sourcing.

## Process note

Ninth drafted unit. The replay-as-simulator story is one of the cleaner mechanistic stories in modern neuroscience and the chapter leans into it. The corvid case is included specifically to establish the substrate-vs-function distinction, since the chapter is otherwise mammal-heavy. Voice still flagged `voice-unanchored` — nine units now in the same register; the case for clearing the flag is overwhelming at this point.
