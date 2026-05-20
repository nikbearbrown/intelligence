# Research notes — Chapter 4: Learning and Memory

**Book:** intelligence (*Intelligence? A Natural History of Mind Across the Animal Kingdom*)
**Chapter slug:** learning-and-memory
**Date:** 2026-04-25
**Command:** `/chapter`
**Voice anchoring:** `voice-unanchored`. Both `style/` folders empty. Fourth drafted unit (preface, Ch. 1, Ch. 2, Ch. 3 are the prior set).

---

## Concept

The molecular and circuit machinery by which a nervous system protects what it has previously learned while admitting what is new. The chapter argues that *associative learning* — Pavlov's dogs, Kandel's sea slug, Bliss & Lømo's rabbit — is the bilaterian solution to *prediction*: a synapse-level mechanism that lets one moment shape the strength of a connection for hours, days, or weeks, and that solves the continual-learning problem (catastrophic forgetting) that artificial neural networks still struggle with.

## Specification move

Three things get unbundled:

1. **Habituation vs. sensitization vs. associative learning.** Non-associative forms (habituation, sensitization) precede the bilaterian floor. Associative learning — *if A then expect B* — was previously thought to require a centralized brain but is now also documented in the cnidarian *Nematostella* (Botzer 2023), pushing the floor below bilaterians.
2. **Short-term vs. long-term memory.** Short-term is modulation of existing proteins (the cAMP-PKA cascade in *Aplysia*). Long-term requires new gene transcription (CREB-1 activation; CREB-2 brake release). The two operate on different timescales and are gated separately.
3. **Local synaptic learning vs. backpropagation.** Biological learning uses local rules (eligibility traces, neuromodulator broadcast, Hebbian co-firing). Backpropagation is mathematically optimal but biologically implausible. The chapter argues the *local* rules are what give biology its solution to catastrophic forgetting, which AI is still trying to recover algorithmically (EWC, replay).

## Empirical vs. non-empirical sub-claims

| Sub-claim | Status |
|---|---|
| Pavlov was a physiologist, not a Watsonian behaviorist | **Empirical**, settled (Pavlov 1927 lectures themselves are the evidence) |
| *Nematostella* shows classical conditioning to light/shock | **Empirical**, recent (Botzer et al. 2023 PNAS) |
| Sensitization in *Aplysia* operates via 5-HT → cAMP → PKA → K⁺ channels → enhanced glutamate release | **Empirical**, settled (Kandel and colleagues, summarized in 2000 Nobel lecture) |
| Long-term facilitation in *Aplysia* requires CREB-1 activation and CREB-2 derepression | **Empirical**, settled (Bartsch et al. 1995 Cell) |
| Hebbian "fire together wire together" was articulated in 1949 | **Empirical**, settled (Hebb 1949 *The Organization of Behavior*) |
| LTP in mammalian hippocampus discovered 1973 | **Empirical**, settled (Bliss & Lømo 1973 J Physiol) |
| NMDA receptor as coincidence detector | **Empirical**, settled |
| Kamin blocking (1968) is real | **Empirical**, settled |
| Rescorla-Wagner formal model captures the surprise-driven update rule | **Mathematical/empirical**, settled in mammals, more variable in invertebrates |
| Catastrophic forgetting in feed-forward neural networks | **Empirical**, settled |
| EWC (Kirkpatrick 2017) is "analogous to synaptic consolidation" | **Settled** as a claim in the paper; the analogy is the authors' own framing |
| Planarian memory persists through head regeneration | **Empirical**, settled (Shomrat & Levin 2013) |
| Memory in planarians stored at least partly outside the brain | **Inference** from Shomrat-Levin; substrate not yet identified |
| Levin's "TAS framework" / bioelectric memory hypothesis | **Speculative**; not invoked by name in the chapter |

## Primary sources

1. **Pavlov, I.P. (1927).** *Conditioned Reflexes: An Investigation of the Physiological Activity of the Cerebral Cortex.* Translated by G.V. Anrep. Oxford University Press. https://psychclassics.yorku.ca/Pavlov/ — for the physiological framing of conditioning.
2. **Botzer, G. et al. (2023).** "Associative learning in the cnidarian *Nematostella vectensis*." *PNAS* 120(13): e2220685120. https://www.pnas.org/doi/10.1073/pnas.2220685120 — pushes associative-learning floor below bilaterians.
3. **Kandel, E.R. (2000 Nobel Lecture).** *The Molecular Biology of Memory Storage: A Dialogue Between Genes and Synapses.* — for synthesis of *Aplysia* work; not directly cited (the chapter cites Bartsch 1995 instead, which is a primary paper from the same lab).
4. **Bartsch, D., Ghirardi, M., Skehel, P.A. et al. (1995).** "*Aplysia* CREB2 represses long-term facilitation: relief of repression converts transient facilitation into long-term functional and structural change." *Cell* 83: 979–992. https://pubmed.ncbi.nlm.nih.gov/8521521/ — the CREB-2 brake-release finding; shows that long-term memory is gated, not automatic.
5. **Hebb, D.O. (1949).** *The Organization of Behavior.* Wiley. — referenced for the 1949 Hebbian principle without direct URL (the book is the primary source).
6. **Bliss, T.V.P. & Lømo, T. (1973).** "Long-lasting potentiation of synaptic transmission in the dentate area of the anaesthetized rabbit following stimulation of the perforant path." *J Physiol* 232: 331–356. https://physoc.onlinelibrary.wiley.com/doi/10.1113/jphysiol.1973.sp010273 — first LTP paper.
7. **Kamin, L.J. (1968).** "Attention-like processes in classical conditioning." In *Miami Symposium on the Prediction of Behavior*. — referenced without URL (book chapter, not online).
8. **Rescorla, R.A. & Wagner, A.R. (1972).** "A theory of Pavlovian conditioning: Variations in the effectiveness of reinforcement and nonreinforcement." In Black & Prokasy (eds.), *Classical Conditioning II*. — chapter cites via the Scholarpedia summary at https://www.scholarpedia.org/article/Rescorla-Wagner_model since the original chapter is not freely available online.
9. **Kirkpatrick, J., Pascanu, R., Rabinowitz, N. et al. (2017).** "Overcoming catastrophic forgetting in neural networks." *PNAS* 114(13): 3521–3526. https://www.pnas.org/doi/10.1073/pnas.1611835114 — Elastic Weight Consolidation.
10. **Shomrat, T. & Levin, M. (2013).** "An automated training paradigm reveals long-term memory in planarians and its persistence through head regeneration." *J Exp Biol* 216(20): 3799–3810. https://journals.biologists.com/jeb/article/216/20/3799/11714/An-automated-training-paradigm-reveals-long-term

## The mechanism for the deep-dive

*The Aplysia molecular cascade for sensitization and its conversion to long-term memory.* The deep-dive walks the cascade step by step (5-HT receptor → adenylyl cyclase → cAMP → PKA → K⁺-channel phosphorylation → broadened action potential → more Ca²⁺ → more glutamate per spike) and then names the conversion to long-term memory through nuclear translocation of PKA, CREB-1 activation, gene transcription, and structural growth — with the Bartsch 1995 CREB-2 brake as the chapter's prettiest result. The same cascade is then connected to Hebbian learning and NMDA-receptor coincidence detection in the mammalian hippocampus (Bliss-Lømo 1973). One sentence: *the synapse remembers because its proteins were designed to be tuned by precise patterns of activity, gated against runaway change by a molecular brake that converts transient experience into structure only when experience repeats.*

## Central analogy

*The brake on long-term memory.* CREB-2 is the brake; CREB-1 is the gas. Both are needed for long-term memory: foot off the brake, foot on the gas. The analogy lands cleanly because every reader has the intuition that a system with a gas-and-brake setup is doing something more sophisticated than a system with only a gas pedal. Where it breaks down: a real brake is mechanical and continuous; CREB-2 is a transcriptional repressor whose displacement is biochemical and discrete. The break-down is small enough that the analogy survives.

## Voice notes

- Natural-history register continued. Pavlov as physiologist. Kandel as a researcher making a career-defining choice in 1962.
- Math is present — the molecular cascade is laid out as a single arrow chain (5-HT → cAMP → PKA → K⁺ → Ca²⁺ → glutamate) — to honor the mechanism-on-the-page rule. No equations.
- First person used at three points (§4.4 closing, §4.5 opening, "Still puzzling").
- Single-sentence paragraphs at three pivots: end of §4.1 ("The argument was right"), middle of §4.4 ("And it does not catastrophically forget"), and the close of the planarian section ("I find that result hard to fit into the chapter's tidy story. I include it because the story is not, in fact, tidy.").
- Extension Note on writing — the third in the book (Ch. 2 had pH meters, Ch. 3 had the Roomba). The chapter explicitly notes that "the leitmotif of this book is starting to have a shape," planting the seed for the eventual naming in Ch. 18.

## Risks flagged

- **The planarian post-decapitation memory result is genuinely strange.** I include Shomrat-Levin 2013 and explicitly say I cannot fit it into the molecular cascade. The "Still puzzling" section names this directly. Reviewers may want to either expand or compress this passage.
- **The CREB-2 brake-release finding is presented from the 1995 Bartsch paper.** Subsequent work has elaborated the picture (CPEB, ApAF, etc.). The chapter does not engage that complexity; it sticks to the headline finding.
- **The "catastrophic forgetting solved by sea slugs" framing is rhetorically strong.** Strictly, *Aplysia* is not solving the same task that an LLM faces. The lesson generalizes — sparse local updates protect prior learning — but the framing oversimplifies. I would defend the framing because it lands the conceptual point even if it understates the disanalogy.
- **Rescorla-Wagner is cited via Scholarpedia** because the original 1972 book chapter is not freely available. If review wants a primary URL, this is the one to flag.
- **Hebb 1949 is referenced without a direct link.** It is a book; no online primary source. Mentioned by date and full reference name.

## Process note

Fourth drafted unit. With four units in the natural-history register (preface + Ch. 1 + Ch. 2 + Ch. 3 + Ch. 4 = five total), the workshop now has substantial material to anchor `style/` if Bear approves the voice. Recommendation: drop copies of Ch. 2, Ch. 3, and Ch. 4 into `books/intelligence/style/` after review to clear the `voice-unanchored` flag for future chapters.
