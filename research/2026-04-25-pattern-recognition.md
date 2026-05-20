# Research notes — Chapter 6: Pattern Recognition and Perception

**Book:** intelligence (*Intelligence? A Natural History of Mind Across the Animal Kingdom*)
**Chapter slug:** pattern-recognition
**Date:** 2026-04-25
**Command:** `/chapter`
**Voice anchoring:** `voice-unanchored`. Both `style/` folders empty. Sixth drafted unit.

---

## Concept

The vertebrate pallium as the architectural solution to pattern recognition. The chapter argues that a three-layered allocortex implementing dimensionality expansion + sparse coding + recurrent auto-association is the minimum machinery for the discrimination/generalization/invariance trio, that this architecture has been in place since the late Cambrian (preserved in lamprey), and that fish demonstrate the full recognition repertoire — face discrimination, viewpoint invariance, long-term pattern memory — that modern CNNs still fail to match without massive data augmentation.

## Specification move

Three things unbundled before empirical work:

1. **Discrimination vs. generalization.** Two computational goals that pull in opposite directions. The stability-plasticity dilemma is what happens when you try to maximize both at once. The vertebrate solution is to separate them anatomically and have them cooperate within the same auto-associative architecture.
2. **Pattern recognition vs. world model.** The chapter sticks to recognition (categorization, identification, discrimination). World-model claims (prediction, simulation, planning) are deferred to Chapter 9.
3. **Architecture vs. function.** The Suryanarayana 2017 finding is anatomical/molecular conservation in the lamprey lateral pallium. Whether the function is conserved is a separate inference. The chapter notes this in "What would change my mind."

## Empirical vs. non-empirical sub-claims

| Sub-claim | Status |
|---|---|
| Archerfish discriminate human faces from 44 alternatives at ~81% accuracy | **Empirical**, settled (Newport et al. 2016) |
| Goldfish recognize 2D color photographs of plastic objects rotated to novel viewpoints | **Empirical**, settled (DeLong et al. 2022) |
| Goldfish are faster on 180° rotations than ±90° | **Empirical**, settled (DeLong 2022) — interpretation contested |
| Hubel & Wiesel 1962 hierarchy of simple/complex/hypercomplex cells in cat V1 | **Empirical**, settled |
| Lamprey lateral pallium has the three-layered architecture conserved with mammalian cortex | **Empirical**, settled (Suryanarayana et al. 2017) |
| Cortex performs dimensionality expansion + sparse coding + auto-associative completion | **Empirical**, well-supported as a general scheme |
| Piriform cortex specifically implements this scheme via recurrent collaterals | **Empirical**, well-supported (Haberly, Wilson, others) — not directly cited via primary source in the chapter |
| CNNs are good at translation invariance but poor at rotation/scale invariance without augmentation | **Empirical**, settled |
| LeCun 1989 was the early CNN-for-real-world-task paper | **Empirical**, settled |
| The brain has stronger inductive biases than CNNs | **Synthetic claim**, well-supported but informal |
| Catastrophic forgetting solved differently in fish than in CNNs | **Empirical for fish memory stability**, theoretical for the comparison |
| Combinatorial olfactory coding yields trillions of discriminable patterns | **Mathematical/theoretical**, well-established |

## Primary sources

1. **Newport, C., Wallis, G., Reshitnyk, Y., Siebeck, U.E. (2016).** "Discrimination of human faces by archerfish (*Toxotes chatareus*)." *Scientific Reports* 6: 27523. https://www.nature.com/articles/srep27523 — the chapter's hook and the strongest behavioral evidence for fish face recognition.
2. **DeLong, C.M. et al. (2022).** "Visual Perception of Photographs of Rotated 3D Objects in Goldfish (*Carassius auratus*)." *Animals* 12(14): 1797. https://www.mdpi.com/2076-2615/12/14/1797 — viewpoint invariance evidence.
3. **Hubel, D.H. & Wiesel, T.N. (1962).** "Receptive fields, binocular interaction and functional architecture in the cat's visual cortex." *J Physiol* 160: 106–154. https://physoc.onlinelibrary.wiley.com/doi/10.1113/jphysiol.1962.sp006837 — foundational visual hierarchy paper.
4. **Suryanarayana, S.M., Robertson, B., Wallén, P., Grillner, S. (2017).** "The Lamprey Pallium Provides a Blueprint of the Mammalian Layered Cortex." *Current Biology* 27(21): 3264–3277. https://pubmed.ncbi.nlm.nih.gov/29056451/ — 500-million-year-old conservation of cortical architecture.
5. **LeCun, Y. et al. (1989).** "Backpropagation Applied to Handwritten Zip Code Recognition." *Neural Computation* 1(4): 541–551. https://direct.mit.edu/neco/article-pdf/1/4/541/811941/neco.1989.1.4.541.pdf — early CNN paper inspired by Hubel-Wiesel.
6. **Yamins, D.L.K., Hong, H., Cadieu, C.F., Solomon, E.A., Seibert, D., DiCarlo, J.J. (2014).** "Performance-optimized hierarchical models predict neural responses in higher visual cortex." *PNAS* 111(23): 8619–8624. https://www.pnas.org/doi/10.1073/pnas.1403112111 — the positive convergence finding: CNN trained on object categorization yields top-layer activations highly predictive of macaque IT neural firing on natural images, without being constrained to match neural data.
7. **Stabinger, S., Rodríguez-Sánchez, A., Piater, J. (2016).** "25 Years of CNNs: Can We Compare to Human Abstraction Capabilities?" *ICANN 2016*. https://link.springer.com/chapter/10.1007/978-3-319-44781-0_45 — sharper limit: feedforward CNNs (LeNet, GoogLeNet) cannot reliably learn the abstract same/different relation, even with thousands of training pairs.

## The mechanism for the deep-dive

*The piriform cortex as auto-associative memory engine.* Three operations described in §6.3: (1) dimensionality expansion (input fibers project diffusely onto a much larger pyramidal-cell population, kernel-method-like), (2) sparse coding with lateral inhibition (only a few percent of pyramidal neurons fire for any odor; lateral inhibition decorrelates similar inputs into non-overlapping ensembles — solves discrimination), (3) recurrent collaterals shaped by Hebbian plasticity (pyramidal neurons that fire together strengthen connections; partial inputs get completed by the strengthened connectivity — solves generalization). One sentence: *the same circuit, in the same patch of cortex, simultaneously implements discrimination by sparse separation and generalization by recurrent completion.*

## Central analogy

*The cortex as a kernel method.* Used in §6.3. Dimensionality expansion in the cortex is the same mathematical trick used in machine learning's kernel methods to make non-linear classification problems linearly separable. The analogy lands cleanly because both depend on the geometric insight that high-dimensional spaces have more room to separate patterns than low-dimensional ones do. Where it breaks down: kernel methods do not have recurrent dynamics or Hebbian-shaped weights; they perform a static projection. The cortex is dynamical and learning. The break is a partial one — the analogy survives for the dimensionality-expansion step.

## Voice notes

- Natural-history register continued. Archerfish at the surface as the chapter's anchoring scene.
- First person used in §6.4 ("I find this comparison less embarrassing than instructive"), §6.5 ("I conclude"), and "Still puzzling."
- Single-sentence paragraphs at three pivots: end of §6.1 ("Each step up the ladder, the range of environments has widened, and the cortex is the thing that did the widening" — moved to §6.5 actually), end of §6.3 ("The fish was treating the rotated image as the same object"), end of §6.4 (single-sentence pivot is the "lesson is not that engineers were lazy" beat).
- Math kept off the page directly — combinatorial coding mentioned, but no equations. The Hebbian / recurrent / kernel stories carry the technical weight.
- Extension Note (fifth in book): instruments as perceptual extensions. Van Leeuwenhoek's animalcules, telescope, MRI, modern medical-imaging AI. The lens reveals data; the cortex does the recognition that matters.

## Risks flagged

- **The "olfactory receptors → 2^N combinatorial patterns" framing is qualitative.** The actual coding is more like activity-pattern-across-receptors, which produces a continuum of discriminable patterns rather than a clean binary count. The chapter renders this as "trillions of discriminable patterns through combinatorics" without overcommitting to a specific calculation. If review wants the math sharpened, this is where to do it.
- **The claim that piriform cortex specifically implements the auto-associative scheme** rests on decades of work by Lewis Haberly, Don Wilson, and others. I do not cite a specific primary paper for this; it is treated as well-established consensus. If review wants a single primary anchor, the Haberly 2001 *Chemical Senses* review or the Wilson & Sullivan 2011 *Neuron* paper are the standard citations.
- **The CNN-vs-cortex comparison is partly rhetorical.** I argue that engineers copied half the design (the Hubel-Wiesel feature hierarchy) and left out the other half (recurrent completion, sparse coding, thalamic gating). Some AI researchers would dispute the framing; modern transformer-based vision models do incorporate some of these mechanisms. The chapter's framing is defensible but not neutral.
- **The DeLong 2022 finding of "180° faster than ±90°" is interpreted as suggestive of viewpoint-dependent processing under viewpoint-independent recognition.** The "Still puzzling" line names this honestly.

## Process note

Sixth drafted unit. The natural-history register has now been carried across six units (preface + Ch. 1–6). The case for clearing the `voice-unanchored` flag by anchoring `books/intelligence/style/` is increasingly strong. Recommend after this batch is reviewed.
