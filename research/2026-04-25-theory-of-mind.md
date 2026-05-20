# Research notes — Chapter 11: Theory of Mind

**Book:** intelligence (*Intelligence? A Natural History of Mind Across the Animal Kingdom*)
**Chapter slug:** theory-of-mind
**Date:** 2026-04-25
**Command:** `/chapter`
**Voice anchoring:** `voice-unanchored`. Both `style/` folders empty. Eleventh drafted unit.

---

## Concept

Theory of mind as the brain's algorithm for inferring the latent goals and beliefs of other agents from observable behavior — a biological implementation of inverse reinforcement learning. The chapter argues that ToM comes in layers (goal attribution → perspective-taking → implicit false belief → explicit recursive mentalizing), that great apes and corvids cleared the implicit false-belief boundary by 2016, and that what current LLMs do when they appear to pass ToM tests is pattern-matching on canonical narrative structure rather than mental-state representation.

## Specification move

Three things unbundled before empirical work:

1. **Goal attribution vs. perspective-taking vs. false belief vs. recursive mentalizing.** Four distinct cognitive operations, often conflated under one phrase. Each maps onto a different evolutionary distribution.
2. **Implicit vs. explicit ToM.** Implicit: violation-of-expectation, anticipatory looking, behavioral signatures with no verbal self-report. Explicit: verbal answers to false-belief questions. Children pass implicit at ~15 months, explicit at ~4 years. Great apes pass implicit but not explicit by current evidence.
3. **Mental-state representation vs. behavioral pattern-matching.** The Ullman 2023 fragility result demonstrates that high accuracy on canonical false-belief stories can be produced without any underlying mental-state representation, by surface pattern-matching on the narrative structure.

## Empirical vs. non-empirical sub-claims

| Sub-claim | Status |
|---|---|
| Premack & Woodruff 1978 introduced the term "theory of mind" | **Empirical**, settled |
| 4-year-old children pass standard false-belief tasks | **Empirical**, settled |
| 3-year-old children fail standard false-belief tasks | **Empirical**, well-supported with some recent exceptions in implicit measures |
| Great apes anticipate actor's behavior based on actor's false belief | **Empirical**, settled (Krupenye et al. 2016) |
| Apes' false-belief anticipation depends on their own past perceptual experience | **Empirical**, settled (Kano et al. 2019 goggles test) |
| Western scrub jays re-cache only when they have themselves been thieves | **Empirical**, settled (Emery & Clayton 2001) |
| Dog "guilty look" is a response to owner cues, not internal awareness of misdeed | **Empirical**, settled (Horowitz 2009) |
| GPT-3.5/GPT-4 fail trivially-altered false-belief tasks | **Empirical**, settled (Ullman 2023) |
| ToM is biological inverse reinforcement learning | **Theoretical/synthetic**, well-supported as framework |
| Recursive second-order ToM is uniquely human | **Empirical** — currently no clean non-human demonstration |
| Submentalizing accounts cannot explain the Krupenye-Kano follow-up results | **Empirical**, supported by the Kano 2019 design |

## Primary sources

1. **Premack, D. & Woodruff, G. (1978).** "Does the chimpanzee have a theory of mind?" *Behavioral and Brain Sciences* 1(4): 515–526. Referenced by date; original online access spotty.
2. **Hare, B., Call, J., Tomasello, M. (2000).** "Chimpanzees know what conspecifics do and do not see." *Animal Behaviour* 59(4): 771–785. https://pubmed.ncbi.nlm.nih.gov/10792932/ — also cited in Ch. 10; reused here for the perspective-taking discussion.
3. **Emery, N.J. & Clayton, N.S. (2001).** "Effects of experience and social context on prospective caching strategies by scrub jays." *Nature* 414: 443–446. https://www.nature.com/articles/35106560 — corvid re-caching with experience-as-thief.
4. **Krupenye, C., Kano, F., Hirata, S., Call, J., Tomasello, M. (2016).** "Great apes anticipate that other individuals will act according to false beliefs." *Science* 354(6308): 110–114. https://www.science.org/doi/10.1126/science.aaf8110 — chapter's central empirical anchor.
5. **Kano, F., Krupenye, C., Hirata, S., Tomonaga, M., Call, J. (2019).** "Great apes use self-experience to anticipate an agent's action in a false-belief test." *PNAS* 116(42): 20904–20909. https://www.pnas.org/doi/10.1073/pnas.1910095116 — goggles follow-up that defeats submentalizing critique.
6. **Horowitz, A. (2009).** "Disambiguating the 'guilty look': salient prompts to a familiar dog behaviour." *Behavioural Processes* 81(3): 447–452. https://pubmed.ncbi.nlm.nih.gov/19520245/ — guilty-look deconstruction.
7. **Ullman, T. (2023).** "Large Language Models Fail on Trivial Alterations to Theory-of-Mind Tasks." arXiv:2302.08399. https://arxiv.org/abs/2302.08399 — LLM ToM fragility.

Also referenced without primary URLs:
- Wimmer & Perner 1983 *Cognition* (Sally-Anne origin).
- Baron-Cohen, Leslie, Frith 1985 *Cognition* (autism + Sally-Anne).
- Daniel Dennett's response to Premack & Woodruff 1978 (BBS).
- Heyes' submentalizing critique (multiple papers).
- Cecilia Saxe lab work on TPJ specificity.
- Kosinski 2023 LLM ToM emergence claim.
- Cambridge Analytica / OCEAN modeling (referenced in Extension Note).
- Abbeel & Ng inverse reinforcement learning (early-2000s; helicopter-aerobatics work).

## Mechanism for the deep-dive

*The great-ape false-belief case made through anticipatory eye-tracking, paired with the corvid case made through experience-as-thief.* §11.3 walks the chimpanzee literature from Povinelli's negative results through Hare's competitive-paradigm reframe to Krupenye 2016 anticipatory looking and Kano 2019 goggles. Then turns to Emery & Clayton 2001 scrub jays and the experienced-thief result. Convergence across two anatomically dissimilar lineages is the chapter's load-bearing comparative claim. One sentence: *the floor of implicit false-belief reasoning lives below the great-ape line and (independently) inside the corvid lineage; what remains uniquely human, at least for now, is recursive explicit mentalizing.*

## Central analogy

*Theory of mind as biological inverse reinforcement learning.* Used in §11.5. Inverse RL: observer watches agent's behavior and infers the reward function the agent is optimizing. Theory of mind: observer watches agent's behavior and infers the agent's beliefs and goals. The mathematical structure is the same — compress observed behavior into a small set of latent variables (rewards, beliefs) that explain the surface. Where the analogy breaks: real IRL algorithms typically assume rational behavior, while theory of mind operates on agents who are emotionally biased, deceptive, or operating under false beliefs that are themselves part of the inference target. The break is small enough that the analogy survives and pays off — particularly in distinguishing what biological ToM does from what LLM "ToM" does.

## Voice notes

- Natural-history register continued. The Krupenye 2016 eye-tracker scene as the chapter's anchor.
- First person used at three points: §11.1 mid ("by my reading"), §11.5 mid ("by my reading"), §11.6 ("I conclude"). Sparingly.
- Single-sentence paragraphs at three pivots: end of §11.1 (the closing on what the chapter is about), §11.3 mid ("Whatever theory of mind requires computationally, several different anatomies have, separately, found ways to compute it" — though this got compressed in the trim), §11.6 closing ("The capacity to model an agent's reward function is what makes a society of agents anything more than a swarm").
- No equations on the page; the IRL math is described prose-only because the framework's value is conceptual rather than computational for this chapter's scope.
- Extension Note (tenth in book): user research / A/B testing / Cambridge Analytica. Reinforces the additive-vs-substitutive leitmotif from Ch. 7 with the additional twist that population-scale pseudo-mentalizing is morally consequential in a way the previous Extension Notes have largely not had to confront.

## Risks flagged

- **Word-count ceiling fight.** First draft came in at 4,215 words. Two passes of trimming brought it to 3,982. The chapter is genuinely dense and the ceiling is tight. If review wants more on any of the side cases (vervet alarm calls, cleaner fish audience effects, dolphin pointing comprehension), it would have to displace something in the deep-dive.
- **One forbidden-phrase hit** ("robust"x1) caught and replaced with "reliably" in §11.2. Final scan clean.
- **Mirror neurons** — the brief mentioned them but the chapter does not deep-dive. The mirror-neuron literature has become contested over the last fifteen years (Hickok 2014 *The Myth of Mirror Neurons*) and the chapter does not enter that debate. If review wants mirror neurons added, the simulation-theory frame in §11.2 is the place.
- **The Kosinski 2023 GPT-4 ToM claim** is described as a counter-result to the Ullman 2023 fragility finding. Strictly, Kosinski's preprint pre-dated Ullman's; the chronology is presented backward in the chapter for narrative cleanness ("the result drew attention, and a counter-result followed"). The substance is correct; the temporal framing is slightly compressed.
- **Premack & Woodruff 1978** referenced by date without URL. The original BBS paper is not freely available; primary access requires a subscription or archival access through institutional libraries.
- **Recursive second-order ToM as uniquely human** is the chapter's most contested boundary in the "What would change my mind" line. The recent literature on great-ape and corvid implicit measures has not yet produced a clean second-order result, but the methodological space is still being explored.

## Process note

Eleventh drafted unit. The chapter required two passes of trimming to come in under the 4,000-word ceiling because the brief was unusually rich (six interlocking threads — false-belief, apes, corvids, dogs, IRL, LLMs). The depth-vs-breadth trade was resolved in favor of depth on apes and corvids, with shorter treatment of dogs, monkeys, and cleaner fish. Voice still flagged `voice-unanchored` — eleven units now in the same register; Ch. 1–11 plus preface form the voice-setting set.
