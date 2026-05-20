# Research notes — Chapter 2: Before Brains

**Book:** intelligence (*Intelligence? A Natural History of Mind Across the Animal Kingdom*)
**Chapter slug:** before-brains
**Date:** 2026-04-25
**Command:** `/chapter`
**Voice anchoring:** `voice-unanchored`. Both `style/` folders empty. Preface and Ch. 1 set most of the voice; Ch. 2 continues to set it.

---

## Concept

Aneural cognition. The chapter argues that the functional ingredients of a decision — sensing, memory, integration, variable response — appear in cells, cell networks, and plants without any neuron. The cognitive primitive being computed is *valence*: the categorization of stimuli as approach-or-avoid. Valence precedes neural hardware, and the neural hardware that came later refines but does not invent it.

## Specification move

Three things need to be pulled apart before the chapter can do empirical work:

1. **Decision vs. reflex.** A decision varies with internal state, prior experience, or competing inputs. A reflex is fixed. The four-ingredient minimum (sensing + memory + integration + variable response) operationalizes the distinction.
2. **Taxis vs. tropism.** Tropism is fixed growth response. Taxis is active sensing with temporal comparison. Bacterial chemotaxis is taxis; phototropism in a sunflower is tropism. The chapter is about taxis-class behavior.
3. **Functional behavior vs. inflated claim.** "Bee shows pessimism-like cognitive bias" is a careful, empirical claim. "Bee feels sadness" is an inflated claim. Aneural cognition often produces clean evidence for the careful version and zero evidence for the inflated version. The chapter treats this distinction explicitly in §2.5.

## Why E. coli chemotaxis is the deep-dive

The brief covers bacteria, slime molds, and plants. The SKILL says one mechanism gets the deep-dive. *E. coli* chemotaxis is the cleanest choice because:
- The molecular cascade (MCP → CheA → CheY → flagellar motor; CheR/CheB → methylation → memory) is fully worked out.
- The temporal-integration math (Segall-Block-Berg 1986: past second positive weight, prior 3 sec negative weight, 4-second window total) is precise enough to put on the page.
- It demonstrates all four ingredients of a decision in a 2-micrometer cell — the cleanest possible existence proof for the chapter's thesis.
- It connects directly to Ch. 3 (steering nematodes), where the same decision logic appears with neurons added.

The slime mold (Tero rail network, Boisseau habituation), Venus flytrap (Böhm calcium counting), and sagebrush (Karban volatile chemotypes) get treated in §2.4 as illustrations of the same architecture in different substrates — not as their own deep-dives.

## Empirical vs. non-empirical sub-claims

| Sub-claim | Status |
|---|---|
| *E. coli* runs and tumbles via flagellar rotation switching | **Empirical**, settled (Berg & Brown 1972) |
| *E. coli* biases its random walk in chemical gradients | **Empirical**, settled |
| Methylation of MCPs by CheR/CheB is the memory mechanism | **Empirical**, settled |
| 4-second temporal comparison window with positive-then-negative weighting | **Empirical**, settled (Segall-Block-Berg 1986) |
| *Physarum* solves shortest-path mazes | **Empirical**, settled (Nakagaki 2000) |
| *Physarum* network mimics Tokyo rail efficiency | **Empirical**, settled (Tero 2010) |
| *Physarum* habituates to bitter compounds with substance specificity and spontaneous recovery | **Empirical**, settled (Boisseau 2016) |
| Venus flytrap closes only after two trigger-hair touches within ~30 seconds | **Empirical**, settled |
| Calcium decay is the biochemical timer for the two-touch rule | **Empirical**, settled (Böhm 2016) |
| Sagebrush volatile communication primes neighboring plant defenses | **Empirical**, settled (Karban et al. 2006 and successors) |
| *Mimosa pudica* habituates to harmless drop stimuli for up to a month | **Contested** (Gagliano 2014 vs. Biegler critique) |
| Pea plants associate fan direction with light direction | **Likely false** (Markel 2020 failed replication) |
| The "Wood Wide Web" cooperative-trees framing | **Contested** in current ecological literature |
| Valence (approach/avoid) is the cognitive primitive on which all later cognition is built | **Synthetic claim** — supported by continuity arguments, not by a single experiment |

## Primary sources

1. **Berg, H.C. & Brown, D.A. (1972).** "Chemotaxis in *Escherichia coli* analysed by Three-dimensional Tracking." *Nature* 239: 500–504. https://www.nature.com/articles/239500a0
2. **Segall, J.E., Block, S.M., & Berg, H.C. (1986).** "Temporal comparisons in bacterial chemotaxis." *PNAS* 83(23): 8987–8991. https://www.pnas.org/doi/abs/10.1073/pnas.83.23.8987 — the 4-second leaky-integrator window and CheR/CheB knockout result.
3. **Segall, J.E., Block, S.M., & Berg, H.C. (1986).** PubMed entry: https://pubmed.ncbi.nlm.nih.gov/3024160/
4. **Nakagaki, T., Yamada, H., & Tóth, Á. (2000).** "Maze-solving by an amoeboid organism." *Nature* 407: 470. https://www.nature.com/articles/35035159
5. **Tero, A. et al. (2010).** "Rules for Biologically Inspired Adaptive Network Design." *Science* 327(5964): 439–442. https://www.science.org/doi/10.1126/science.1177894
6. **Boisseau, R.P., Vogel, D., & Dussutour, A. (2016).** "Habituation in non-neural organisms: evidence from slime moulds." *Proceedings of the Royal Society B* 283(1829): 20160446. https://royalsocietypublishing.org/doi/10.1098/rspb.2016.0446
7. **Böhm, J., Scherzer, S., Krol, E. et al. (2016).** "The Venus Flytrap *Dionaea muscipula* Counts Prey-Induced Action Potentials to Induce Sodium Uptake." *Current Biology* 26(3): 286–295. https://pubmed.ncbi.nlm.nih.gov/26804557/
8. **Karban, R., Shiojiri, K., Huntzinger, M., & McCall, A.C. (2006).** "Damage-induced resistance in sagebrush: volatiles are key to intra- and interplant communication." *Ecology* 87(4): 922–930. https://pubmed.ncbi.nlm.nih.gov/16676536/
9. **Gagliano, M. et al. (2014).** "Experience teaches plants to learn faster and forget slower in environments where it matters." *Oecologia* 175: 63–72. https://link.springer.com/article/10.1007/s00442-013-2873-7
10. **Biegler, R. (2018).** "Insufficient evidence for habituation in *Mimosa pudica*. Response to Gagliano et al. (2014)." *Oecologia*. https://link.springer.com/article/10.1007/s00442-017-4012-3
11. **Markel, K. (2020).** "Lack of evidence for associative learning in pea plants." *eLife* 9: e57614. https://elifesciences.org/articles/57614

## The mechanism for the deep-dive (one sentence)

*E. coli* implements all four ingredients of a decision — sensing (MCPs), memory (CheR/CheB methylation), integration (CheA-CheY kinase cascade), and variable response (run-or-tumble flagellar bias) — in a 2-micrometer cell, computing a 4-second leaky-integrator temporal derivative of attractant concentration with positive weighting on the past second and negative weighting on the prior three.

## Central analogy

*The drunkard's walk biased by gradient.* Used in §2.3. The bacterium's run-and-tumble is a random walk with a switching rule: tumbles get *suppressed* when conditions improve, *fired* when conditions worsen. The walk is not steered; it is biased. Where the analogy breaks down: a real drunkard does not have an enzymatic memory of the last four seconds, and a real drunkard's walk has no preferred direction by design. The bacterium has the memory; the bias is the whole point. The analogy survives this break-down because the drunkard's walk is the *null* model and the bacterium's deviation from it is exactly what we want the reader to see.

## Voice notes

- Natural-history register, per `book.md`. Attenborough × Feynman.
- Math on the page in §2.3 (the leaky-integrator equation in plain prose form, with explanation).
- First person used at three points (§2.1 "you should be allowed to find that strange. I find it strange"; §2.5 "the most careful position is..."; "What would change my mind"). Sparingly.
- Single-sentence paragraphs at three pivots: "The decision is real" (closing §2.3); "There is no neuron in any of them" (closing §2.4); "Decisions, then, did not begin with brains" (opening §2.6).
- **Extension Note** included at the end. Per the book brief, the device starts in Ch. 2 and runs through Ch. 18 where the leitmotif is named.
- No textbook scaffolding (no Learning Objectives, no Prerequisites).

## Risks flagged

- **The plant-cognition section is the chapter's most fragile.** Mimosa is contested, peas-and-fans is likely false, the Wood Wide Web is overstated. §2.5 names this directly. If review wants a stronger or weaker stance, this is where to adjust.
- **The slime-mold treatment is brief.** Tero rail network and Boisseau habituation get a paragraph each; the mechanism behind cytoplasmic-streaming-as-computation gets one sentence. A longer treatment would push past the 4,000-word ceiling and require cutting elsewhere — likely the bacterial deep-dive, which I think is wrong to cut.
- **Quorum sensing was dropped.** The brief mentioned Bonnie Bassler's work on *Vibrio harveyi*. I held it back because the chapter is about *individual* aneural cognition, and collective intelligence is Ch. 16. Quorum sensing belongs there.
- **Suzanne Simard / Wood Wide Web.** Mentioned briefly in §2.5 with the contested framing. The full treatment belongs in Ch. 16 (collective intelligence) or possibly Ch. 4 (learning), and not here.

## Process note

This is the first chapter of *Intelligence?* drafted with the full natural-history register established. The preface and Ch. 1 worked through definitional groundwork; this is the first chapter that does the empirical work the book promises. Voice is still flagged `voice-unanchored` — the first three drafted units (preface + Ch. 1 + Ch. 2) are the voice-setting set.
