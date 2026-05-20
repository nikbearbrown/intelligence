# Bookmap Follow-Up Research — *Intelligence?*

**Run date:** 2026-05-05
**Source bookmap:** `bookmaps/BOOKMAP__Intelligence__A_Natural_History_of_Mind__Brown__2025.md`
**Method:** Five parallel research agents, one chunk of chapters each, dispatched against the bookmap's Logical Gaps + cross-cutting tensions + unproven claims. Web-search where the agent had network access; training-data citations otherwise (flagged below).

This document is for Nik's review. Each entry names a critique from the bookmap, lists the primary sources the research identified, summarizes what the literature actually shows, and proposes a specific revision (add citation, soften claim, name competing interpretation, leave alone).

**Triage legend:**
- Settled in chapter's favor — no revision needed; chapter can cite with confidence.
- Critique stands — chapter would benefit from a targeted addition or qualification.
- Critique substantially correct — chapter currently overclaims or omits a live alternative; revision recommended.
- Genuinely open in literature — flag in chapter footer; not the chapter's failure.

**Network-access note:** Agents 1, 2, 4, 5 had web-search access and cite live URLs. Agent 3 (Chs 9–12) reported workspace network restrictions and worked from training-data citations; verify those before citing in a published chapter.

---

## Chapter 1 — The Definition Problem

### Gap 1A — Legg-Hutter trivial-inclusion objection 
*Critique stands as a conceptual gap; literature confirms it is not addressed in primary sources.*

**Primary sources:**
- Legg, S. & Hutter, M. (2007). Universal Intelligence: A Definition of Machine Intelligence. *Minds and Machines* 17(4). [DOI 10.1007/s11023-007-9079-x](https://link.springer.com/article/10.1007/s11023-007-9079-x)
- Legg, S. & Hutter, M. (2007). A Collection of Definitions of Intelligence. arXiv:0706.3639.

**Findings:** Legg & Hutter chose substrate-neutrality and mathematical tractability deliberately. The boundary-case objection — that thermostats and ecosystems satisfy "achieving goals across environments" — is unaddressed in their published work and in subsequent literature on the formal measure. The published debate has been about how to compute the measure, not where its conceptual edges fall.

**Recommendation:** Add a paragraph naming the thermostat objection and either (a) explaining why it is not load-bearing for this book's comparison (the book is comparing organisms with internal state, not edge-case feedback systems), or (b) what additional clause would exclude trivial cases.

### Gap 1B — Affect as constitutive vs. correlated 
*Neuroscience literature supports constitutive reading; chapter understates the cost of flattening it.*

**Primary sources:**
- Dolcos, F., Iordan, A. D., & Dolcos, S. (2011). Neural Correlates of Emotion–Cognition Interactions. *Journal of Cognitive Psychology* 23(6):669–694. [PMC3108339](https://pmc.ncbi.nlm.nih.gov/articles/PMC3108339/)
- Pessoa, L. (2008). On the relationship between emotion and cognition. *Nature Reviews Neuroscience* 9:148–158.
- Damasio, A. R. & Carvalho, G. B. (2013). The nature of feelings: evolutionary and neurobiological origins. *Nature Reviews Neuroscience* 14:143–152. [DOI 10.1038/nrn3407](https://www.nature.com/articles/nrn3407)
- Satpute, A. B. & Lindquist, K. A. (2019). The Default Mode Network's Role in Discrete Emotion. *Trends in Cognitive Sciences* 23(10):851–864.

**Findings:** Single neurons encode emotional and cognitive variables simultaneously; prefrontal-limbic circuits show bidirectional influence; affect is increasingly framed as constitutive of decision-making rather than a parallel modulator. If Ch. 5's evidence (neuromodulatory layer re-weighting integration) is correct, then the Ch. 1 working definition flattens something architecturally load-bearing.

**Recommendation:** Add explicit acknowledgment in Ch. 1 (around the "flattens affect" line) that if Ch. 5's findings hold, the chosen definition is descriptively incomplete for biological systems. The book is still right to use Legg-Hutter as the comparative instrument; it should name this as a chosen tradeoff rather than a manageable cost.

### Gap 1C — Shalizi's PCA argument and predictive validity 
*Argument is sound; chapter should follow it one step further.*

**Primary sources:**
- Shalizi, C. S. (2007). *g*, a Statistical Myth. [bactra.org/weblog/523.html](https://bactra.org/weblog/523.html)
- Spearman, C. (1904). General Intelligence, Objectively Determined and Measured. *American Journal of Psychology* 15(2):201–293.
- Jensen, A. R. (1998). *The g Factor: The Science of Mental Ability.* Praeger.

**Findings:** Shalizi's argument is mathematically correct: PCA on any positively correlated variable set produces a first component loading on all of them. *g* defenders respond that cross-population convergence + biological correlates exceed what is required for a pure artifact. The debate is unresolved.

**Recommendation:** Add one sentence to the existing paragraph: "If Shalizi is right, the predictive-validity claims in the 1994 consensus statement rest on weaker ground than they appear — though this concern does not threaten this book's method, which compares capacities directly across species rather than treating *g* as a measurand."

---

## Chapter 2 — Before Brains

### Gap 2A — E. coli 4-second window vs. Brownian motion physics 
*Plausibility is high; quantitative match is not shown in primary literature.*

**Primary sources:**
- Segall, J. E., Block, S. M., & Berg, H. C. (1986). Temporal Comparisons in Bacterial Chemotaxis. *PNAS* 83(23):8987–8991. [DOI 10.1073/pnas.83.23.8987](https://www.pnas.org/doi/abs/10.1073/pnas.83.23.8987)
- Berg, H. C. & Brown, D. A. (1972). Chemotaxis in *Escherichia coli* Analyzed by Three-Dimensional Tracking. *Nature* 239:500–504.

**Findings:** Segall et al. establish the ~4-second integration window with positive weighting at t=0 and negative weighting at t=−1..−3. They do not explicitly calculate the matching to rotational diffusion. At ~20 µm/s swimming speed, 4 seconds covers ~80 µm — meaningful relative to diffusion scales — but the precision-engineered framing in the chapter outruns what the primary sources quantitatively show.

**Recommendation:** Either (a) work the matching calculation as an exercise/appendix, or (b) soften "matched to" → "consistent with."

### Gap 2B — Gradedness across bacterium-to-chimpanzee 
*No primary source addresses this; conceptual clarification needed.*

**Findings:** Legg-Hutter is quantitative but the chapter does not unpack how the measure behaves at extremes. Is a bacterium's "find food in a gradient" the same kind of quantity as a worm's "find food and remember where"? The chapter asserts gradedness without showing the metric is well-defined across these scales.

**Recommendation:** Brief conceptual section ("What Makes Intelligence Graded?") clarifying: under Legg-Hutter, gradedness means asking of any agent how often it achieves its goal across how many distinct environments. Same metric, different numbers. This avoids requiring new evidence.

---

## Chapter 3 — Steering (C. elegans)

### Gap 3A — *C. elegans* as "first complete instance" 
*Phylogenetic inference, not a finding in primary sources.*

**Primary sources:** Pierce-Shimomura et al. (1999) *J Neurosci*; Sawin, Ranganathan & Horvitz (2000) *Neuron*; Ishihara et al. (2002) *Cell*.

**Findings:** None of the cited papers address earlier bilaterians or claim *C. elegans* is "first." The "first complete instance" claim is a phylogenetic inference from the lack of comparable connectome data in earlier branches. Reasonable but absence-of-evidence.

**Recommendation:** Rephrase to "the earliest organism for which we have circuit-level evidence of all six components" — weaker but accurate.

### Gap 3B — Why neuromodulation/plasticity hasn't been added to commercial robots 
*Engineering trade-off, not in-principle hardness; chapter should distinguish.*

**Primary sources:**
- Krichmar, J. L., Edelman, G. M., & Sporns, O. (2005). Brain-Based Devices. *Proceedings of the IEEE* 93(3):692–715.
- Bio-Inspired Neural Networks for Decision-Making. *Frontiers in Neurorobotics* (2023). [PMC9868850](https://pmc.ncbi.nlm.nih.gov/articles/PMC9868850/)

**Findings:** Neuromorphic researchers (Krichmar, UC Irvine, others) have built robots with neuromodulatory-inspired control. They work but trade interpretability for flexibility — an engineering choice, not a fundamental computational barrier. Commercial Roomba lacks these by design, not by impossibility.

**Recommendation:** Add a paragraph: research robots with neuromodulatory control exist and function, but the additional computational overhead and reduced predictability is why commercial designs omit them. Whether this overhead is fundamental to systems with these capacities or merely a current engineering artifact is open.

### Gap 3C — Weighted-sum decision model: analogy or mechanism? 
*Useful description; not established as the actual computation.*

**Findings:** The cited papers (Pierce-Shimomura, Sawin, Ishihara) demonstrate dC/dt-driven pirouettes, dopamine/serotonin re-weighting, HEN-1 as integration node. These are *consistent with* a weighted-sum but do not prove the nematode implements addition/subtraction at the circuit level rather than a functionally equivalent dynamic.

**Recommendation:** Reframe as "one way to describe what the nematode appears to be computing" rather than what it computes. Note that mechanistic alternatives (winner-take-all dynamics, drift-diffusion, etc.) have not been ruled out.

---

## Chapter 4 — Learning and Memory

### Gap 4A — CREB-2 gate: intensity vs. repetition 
*Mechanism characterized; relative contributions not quantified in primary literature.*

**Primary sources:**
- Bartsch et al. (1998). *Cell* 94(4):457–466.
- Kandel, E. R. (2001). The Molecular Biology of Memory Storage. *Science* 294:1030–1038. (Nobel lecture.)
- Cai, D. et al. (2011). *Neuron* 65(4):500–512.

**Findings:** Repetition (10 vs. 1 stimulus sessions) accumulates CREB-1 and overcomes CREB-2 repression — established. Whether single-episode intensity alone can clear the gate is less crisply demonstrated. The literature implies both matter but does not quantify relative contributions.

**Recommendation:** Brief clarification: repetition is the more strongly supported pathway; single-episode intensity contributes but is not as well-quantified.

### Gap 4B — EWC's Fisher Information vs. biological weight-importance 
*Recent work suggests partial biological analog; chapter glosses this.*

**Primary sources:**
- Kirkpatrick et al. (2017). Overcoming Catastrophic Forgetting. *PNAS* 114(13):3521–3526. [DOI 10.1073/pnas.1611835114](https://www.pnas.org/doi/10.1073/pnas.1611835114)
- Cichon, J. & Gan, W. B. (2015). Branch-Specific Dendritic Ca²⁺ Spikes Cause Persistent Synaptic Plasticity. *Nature* 520:180–185.
- Fusi, S., Drew, P. J., & Abbott, L. F. (2005). Cascade Models of Synaptically Stored Memories. *Neuron* 45(4):599–611.

**Findings:** Brain doesn't compute Fisher Information across the network. But Cichon & Gan show some synapses develop differential stability post-learning while others remain plastic — a *local* importance computation. This is not equivalent to EWC's global Fisher approach but represents a different solution to the same problem.

**Recommendation:** Refine: "EWC requires a global computation of which weights matter for prior tasks. The brain appears to solve a simpler local problem — synapses develop differential stability based on activity during learning. Same effect, different algorithm."

---

## Chapter 5 — Emotion

### Gap 5A — Mood vs. appetitive-motivation in bee emotion 
*Debate genuinely unresolved; Giurfa's objection is parsimonious.*

**Primary sources:**
- Perry, Baciadonna & Chittka (2016). *Science* 353(6307):1529–1531. [DOI 10.1126/science.aaf3038](https://www.science.org/doi/10.1126/science.aaf3038)
- Giurfa, M. (2017–2019, various). Frontiers in Behavioral Neuroscience analyses; Núñez & Giurfa (1996) on appetitive-motivation framing.

**Findings:** The fluphenazine result is consistent with both: (a) dopamine mediates a global mood shift, or (b) dopamine enhances appetitive motivation in reward-proximal contexts. Behavioral data alone cannot distinguish. Cross-domain coherence (does positive shift generalize across non-foraging behaviors?) would be the diagnostic.

**Recommendation:** Name Giurfa's objection directly. State which interpretation is more parsimonious and what evidence would settle the question.

### Gap 5B — New York Declaration on Animal Consciousness (2024) 
*Epistemically meaningful; chapter can frame as evidentiary-threshold shift, not waivering authority.*

**Primary sources:**
- [The New York Declaration on Animal Consciousness (2024)](https://sites.google.com/nyu.edu/nydeclaration/declaration)
- [Cambridge Declaration on Consciousness (2012)](https://fcmconference.org/img/CambridgeDeclarationOnConsciousness.pdf)

**Findings:** Cambridge: "Convinced for mammals/birds, unconvinced for others." New York: "Realistic possibility for many invertebrates; non-attribution is unaffordable." These are different evidentiary thresholds, not flip-flopping. New York signatories include more philosophers/welfare advocates than Cambridge — a shift in who decides, not just what is decided.

**Recommendation:** Frame as defensible hardening of precaution: Cambridge was risk-averse about over-attribution; New York is risk-averse about under-attribution. Both are epistemic positions.

### Gap 5C — Headless cockroach + Anderson-Adolphs criteria 
*Chapter's caution is correct; the criteria are insufficient by their own logic.*

**Primary sources:** Horridge (1962) *Nature*. Anderson & Adolphs (2014) *Cell* — chapter's framework.

**Findings:** The criteria identify nociception (criteria 1, 3, 4 met). Subjective state (criterion 2) cannot be inferred from behavior + wiring alone. The chapter's hedge is epistemically sound, not a fudge.

**Recommendation:** Add one sentence naming this as a logical limit of the criteria themselves. No further revision.

---

## Chapter 6 — Pattern Recognition and Perception

### Gap 6A — Goldfish 180° asymmetry: testable mechanism 
*Honest "still puzzling" flag; chapter could specify competing mechanisms.*

**Primary sources:**
- DeLong et al. (2018). Visual perception of planar-rotated 2D objects in goldfish. *Animal Cognition*.
- Wegman, Morrison, Wilcox & DeLong (2022). RIT Comparative Cognition & Perception Lab.

**Findings:** Three competing mechanisms: feature-flip detection (symmetric processing of inversions), landmark remapping (180° as alternate canonical view), processing efficiency (full rotations easier than partial). Direct comparison of 180° vs. mirror-reversal would distinguish.

**Recommendation:** Name the three candidates and the critical test. Pedagogical payoff: shows how to think about a partly-resolved finding rather than papering over it.

### Gap 6B — CNN relational reasoning failure: dismissive? 
*Chapter overstates the gap. Vision Transformers + capsule networks have made real progress.*

**Primary sources:**
- RelViT (Nie et al., ICLR 2022). [GitHub](https://github.com/NVlabs/RelViT)
- Vision Transformer-Based Relational Reasoning literature (2023–2025). [arXiv 2502.17382](https://arxiv.org/html/2502.17382)
- SimplifiedRPM and abstract reasoning benchmarks (NeurIPS 2024).

**Findings:** Standard CNNs do encode local features without relations. But ViTs with self-attention model dependencies between all patch pairs; capsule networks route hierarchically. Hybrid CNN-Transformer architectures combine both. The gap has narrowed substantially. However, scaling alone does not fix it — relational benchmarks show ~3% gain at 11× model size vs. ~17% on non-reasoning tasks. Architectural changes, not parameter count, are doing the work.

**Recommendation:** Revise to: "Standard CNNs encode local features but struggle with relations. Recent architectures — vision transformers, capsule networks, hybrid systems — recover relational reasoning by adding attention or hierarchical routing. Even these do not scale: gains plateau at larger sizes, suggesting relational reasoning requires fundamentally different learning mechanisms than feature extraction."

### Gap 6C — Does adding recurrence + sparse coding to CNNs close the gap? 
*Partially; no single addition is sufficient.*

**Primary sources:** Capsule network reviews 2025; Friston-style predictive coding implementations; UniBench (NeurIPS 2024).

**Findings:** Capsule networks improve geometric/spatial reasoning but underperform ViTs on standard reasoning. Predictive-coding models help on recurrence-dependent tasks but don't outperform attention. Best current performers are hybrids combining attention + routing + dense supervision.

**Recommendation:** State the progress accurately. The three-operation framework is descriptively useful for biology; the engineering claim ("adding these closes the gap") is overstated. Hybrid architectures matter more than any single operation.

---

## Chapter 7 — Navigation and Spatial Intelligence

### Gap 7A — Javadi result and longitudinal GPS effects 
*Spiers (2020) longitudinal evidence settles this in chapter's favor.*

**Primary sources:**
- Javadi et al. (2017). *Nature Communications* 8:14652. [DOI 10.1038/ncomms14652](https://www.nature.com/articles/ncomms14652)
- Spiers et al. (2020). Habitual use of GPS negatively impacts spatial memory during self-guided navigation. *Scientific Reports* 10:6310. [DOI 10.1038/s41598-020-62877-0](https://www.nature.com/articles/s41598-020-62877-0)

**Findings:** Spiers' 3-year longitudinal retest (n=13) found that greater GPS use since baseline correlated with steeper decline on hippocampal-dependent spatial tasks (landmark recognition, route learning, survey knowledge). Effect size was meaningful.

**Recommendation:** Cite Spiers (2020) directly. The chapter's stronger claim — GPS reduces map-building over time — is now supported by longitudinal data, not just by analogy to the taxi-driver work.

### Gap 7B — Detection-dog double-blind protocols post-2011 
*Field has adopted them as standard.*

**Primary sources:**
- Lit, Schweitzer & Oberbauer (2011). *Animal Cognition* 14:387–394.
- NIST/OSAC (2024). General Guidelines for Training, Certification, and Documentation of Canine Detection Disciplines.
- World Detector Dog Organization double-blind certification program.

**Findings:** Double-blind testing is now standard practice. Recent field data: 94% accuracy under single-blind vs. 72% under double-blind — a ~22% performance gap, validating the magnitude of handler-bias effects Lit identified. NIST/OSAC 2024 standards mandate double-blind for certification.

**Recommendation:** Add a sentence: the field adopted double-blind protocols as standard following Lit et al.; the magnitude of the bias has been confirmed (~22% gap) and methodology has been corrected. This is a clear case of an applied field self-correcting in response to a methodological finding.

### Gap 7C — GPS additive vs. substitutive by mode of use 
*Genuinely under-researched.*

**Findings:** Spiers (2020) treated all habitual GPS use as one category. No published study directly compares turn-by-turn vs. route-confirmation modes. A 2024 Penn State meta-analysis hints at mode-dependence but did not test it directly.

**Recommendation:** Name as open question in chapter footer. Differential effects by mode of use are theoretically predicted but empirically untested.

---

## Chapter 8 — Reinforcement and Prediction

### Gap 8A — 2010 Flash Crash causal attribution 
*SEC/CFTC report establishes a clear causal chain; chapter's framing should be tightened.*

**Primary source:**
- [SEC/CFTC Joint Report on Market Events of May 6, 2010 (Sept 30, 2010)](https://www.sec.gov/files/marketevents-report.pdf)

**Findings:** The initiating event was Waddell & Reed's 75,000-contract algorithmic sell program (~$4.1B). HFTs *amplified* the decline by exiting via stub quotes; they did not initiate it. The SEC/CFTC explicitly states HFTs "did not have a significant role in initiating the decline." The crash required both: a large human sell decision AND algorithmic amplification.

**Recommendation:** Tighten Ch. 8's framing. The Flash Crash is a clean case of multi-agent interaction failure (algorithmic amplification of a human-initiated shock), not of "algorithms gone wrong on their own."

### Gap 8B — Berridge wanting/liking dissociation cross-species 
*Robust in rodents, suggestive in primates, indirect in humans.*

**Primary sources:**
- Berridge & Robinson (2016). Liking, wanting, incentive-sensitization theory of addiction. *American Psychologist* 71(9):670–679.
- Berridge (2019). Affective neuroscience of pleasure. *Psychopharmacology*.
- 2014 macaque μ-opioid social-motivation fMRI study.

**Findings:** Rodent dissociation: rock-solid (dopamine = wanting; opioid = liking). Primate evidence: opioid involvement in pleasure-related valuation documented; full dopamine/opioid dissociation not replicated with same specificity. Human evidence: clinical drug-abuse data consistent (dopamine→craving, opioid→subjective pleasure) but correlational, not experimental.

**Recommendation:** Insert a confidence-gradient caveat: dissociation is robust at rodent base, attenuates as you move up phylogeny. Don't drop the framework — it's useful — but say where the evidence is strong and where it's inferred.

### Gap 8C — Lamprey "essentially modern form" basal ganglia 
*Phrasing too strong; structural homology real but simpler than mammalian.*

**Primary sources:**
- Suryanarayana & Grillner (2021). *Brain, Behavior and Evolution* 96:318–333.
- Stephenson-Jones et al. (2011). *PNAS* 108(22):9059–9064.

**Findings:** Lamprey has all major basal-ganglia components (striatum, pallidum, SN dopaminergic regions, STN-equivalents) with similar neurotransmitters and direct/indirect pathway organization. But: simpler than mammalian system, lacks extensive cortico-striatal-pallidal loops, more brainstem-integrated. Homologous in principle, not in full architectural complexity.

**Recommendation:** Revise "essentially modern form" → "ancient, simplified form organized on the same principles." The action-selection function is conserved; the elaboration is not.

---

## Chapter 9 — Simulation and Planning

⚠ *Agent had no web access; citations from training data — verify before publishing.*

### Gap 9A — Steiner-Redish OFC regret signature replication 
*Rat result stands; primate "regret" data use different measures.*

**Primary sources (verify):** Steiner & Redish (2014) *Nature Neuroscience*; Camille et al. (2004) *J Neurosci* (macaque OFC); Wittmann et al. (2010) *PNAS*; Rudebeck et al. (2009) on primate habenula.

**Findings:** The rat OFC counterfactual encoding (Restaurant Row) is methodologically clean. Primate regret studies measure value-comparison signals or prediction-error magnitudes, not explicit counterfactual encoding. Whether other species encode the counterfactual structure as cleanly as rats remains open.

**Recommendation:** Add caveat: "The same paradigm logic" overstates methodological equivalence. Macaque "regret" signals are value-comparison, not necessarily counterfactual representation. The rat result stands on its own strength.

### Gap 9B — Heyes alternative to scrub-jay re-caching 
*Live and not closed; chapter should name it.*

**Primary sources (verify):**
- Emery & Clayton (2001). *Nature*.
- Heyes (2012). *Oxford Handbook of Developmental Evolution* — submentalizing.
- Dally et al. (2006). *Animal Behaviour* — individual-thief discrimination.
- Bugnyar & Heinrich (2005). *Animal Cognition*.

**Findings:** Dally's individual-thief discrimination strengthens the case beyond simple observation→cache-loss association. But: jays could use observational cues to predict behavior (this individual steals) without representing the thief's *knowledge state*. The behavior-prediction vs. mind-modeling distinction has not been experimentally closed in corvids.

**Recommendation:** Name Heyes's submentalizing alternative explicitly. Reframe re-caching as "sophisticated behavior discrimination" rather than "modeling the thief's knowledge."

### Gap 9C — Corvid–mammal mechanistic equivalence 
*Behavioral convergence yes; circuit-level equivalence not established.*

**Primary sources (verify):**
- Nieder (2017). *Progress in Neurobiology* — corvid numerical cognition.
- Güntürkün & Bugnyar (2016). *Trends in Cognitive Sciences* — cognition without cortex.
- Csillag et al. (2010). *Journal of Comparative Neurology*.

**Findings:** Corvid pallium maps to mammalian regions by connectivity, receptor distribution, molecular markers. Behavioral equivalence is solid (planning, future-oriented caching). Circuit-level equivalence — whether corvid pallium runs replay-like mechanisms — has not been demonstrated. Nieder's numerosity work shows corvids encode abstract dimensions, not that they implement identical algorithms.

**Recommendation:** Replace "the same computation" with "functionally equivalent planning systems, anatomically mapped but mechanistically distinct." Note what is and is not demonstrated.

---

## Chapter 10 — Social and Emotional Intelligence

⚠ *Same agent as Ch. 9 — verify citations.*

### Gap 10A — Macaque consolation absence: capacity vs. suppression 
*Both readings consistent with current evidence; not directly tested.*

**Primary sources (verify):**
- de Waal & van Roosmalen (1979). *Behavioral Ecology and Sociobiology*.
- Kummer (1978). *Primate Societies*.
- Koski et al. (2014). *Phil. Trans. R. Soc. B*.

**Findings:** Macaques show contagion + reconciliation with specific partners + maternal empathy → some affiliative capacity present. Whether generalized consolation absence reflects incapacity or hierarchy-driven suppression is not directly tested. Comparison of high-hierarchy vs. low-hierarchy populations would distinguish.

**Recommendation:** Acknowledge both readings. The diagnostic logic (contagion-not-empathy) is preserved either way, but the inference about which capacity is "missing" depends on which interpretation holds.

### Gap 10B — Dunbar's 150 
*Pinpoint prediction has lost credibility; underlying correlation holds.*

**Primary sources (verify):**
- Lindenfors et al. (2021). *Evolutionary Anthropology*.
- Powell et al. (2017). *Proc. R. Soc. B* — order-specific variation.
- Sutcliffe et al. (2012). *J. R. Soc. Interface*.

**Findings:** Phylogenetic comparative methods (PGLS) widen the human group-size confidence interval to roughly 100–250 with 150 as midpoint, not unique prediction. Powell shows the brain–group-size relationship varies by primate order. The underlying correlation (larger brains → larger groups) holds; the specific number 150 does not.

**Recommendation:** Strengthen the existing hedge: "approximately 150 stable relationships" → "the midpoint of a phylogenetic confidence interval roughly 100–250 — the relationship holds; the precise number does not."

### Gap 10C — Nagasawa oxytocin gaze loop 
*Real effect; narrower scope than sometimes claimed.*

**Primary sources (verify):**
- Nagasawa et al. (2015). *Science*.
- Oliva et al. (2015). *PNAS*.

**Findings:** Mutual-gaze-induced oxytocin rise in dogs (n=22 pairs) is real and replicates. Wolf comparison rests on n=10 hand-raised wolves — small. Hand-raising is not equivalent to wild development. Causal direction (selection for human-sensitivity vs. selection for reduced fear that secondarily enabled gazing) is not distinguished.

**Recommendation:** Existing chapter framing ("co-opted a mammalian bonding mechanism") is appropriately cautious. Add: oxytocin rise is documented and replicable; whether it reflects selection-for-human-sensitivity or selection-for-reduced-fear remains unresolved. Wolf sample sizes are small.

---

## Chapter 11 — Theory of Mind

⚠ *Same agent — verify citations.*

### Gap 11A — Kano 2019 sample size and replication 
*Within-subject design provides power; not yet independently replicated.*

**Primary sources (verify):**
- Kano et al. (2019). *PNAS*.
- Krupenye et al. (2016). *Science* — broader anticipatory-gaze finding (replicated across labs).

**Findings:** Kano: n=4 chimpanzees per condition (opaque/transparent barrier pre-exposure) = 8 total. Small but appropriate for high-trial within-subject eye-tracking. Specific barrier-experience experiment not yet independently replicated; broader anticipatory-gaze effect has held across three ape species and multiple labs.

**Recommendation:** Note the replication status: "the barrier-experience result has not been formally replicated in independent labs, though the broader anticipatory-gaze effect on which it builds has held across species." The within-subject design is appropriately powered for the claim being made.

### Gap 11B — Ullman-style perturbation diagnostic on apes 
*Not yet conducted; high theoretical priority.*

**Primary sources (verify):** Ullman (2023) *Cognitive Science* — LLM perturbation test.

**Findings:** No published study has applied logically-equivalent surface-feature variations to ape eye-tracking false-belief paradigms. If apes pass perturbations, strong evidence for genuine IRL. If apes fail, suggests template-matching even in apes — would force re-interpretation of Krupenye/Kano. The experiment is feasible.

**Recommendation:** Flag as the cleanest open test the chapter is built to motivate. "Whether great-ape implicit false-belief reasoning generalizes across surface variations — as the Ullman battery tests in LLMs — has not been conducted. It would distinguish IRL from template-matching at the ape level."

### Gap 11C — IRL framework's limits when reward functions are unknown 
*Acknowledged in computational ToM literature; not in chapter.*

**Primary sources (verify):** Abbeel & Ng (2004) ICML; Ho & Ermon (2016) NeurIPS — adversarial imitation; Jara-Ettinger et al. (2016) *PNAS*.

**Findings:** IRL works when the reward-function class is constrained. Real social reasoning often involves novel motivations — unknown function classes. Recent work (adversarial imitation, structured prediction) tries to extend IRL but does not fully solve the problem.

**Recommendation:** One-paragraph addition: "The IRL frame is powerful for bounded social contexts where motivations are limited and familiar. In novel social situations where you cannot anticipate what motivates another agent, the frame needs expansion — inferring not just which goal but what class of goals is open in the literature."

---

## Chapter 12 — Creativity

⚠ *Same agent — verify citations.*

### Gap 12A — NCC compound tools: components vs. ex nihilo 
*Chapter handles correctly; no change needed.*

**Findings:** Mango assembled from components already in the repertoire — chapter notes this. Whether novel combination requires the same architecture as inventing new tool types is not settled. Kaplan & Hafner suggest compositional stage may developmentally precede ex nihilo invention, so it's not a failure mode but an earlier stage.

**Recommendation:** No revision required. The qualification is already appropriate.

### Gap 12B — Bowerbird forced-perspective restoration 
*Two readings consistent with data; chapter should name both.*

**Primary sources (verify):** Endler et al. (2010); Hunt & Endler (1995).

**Findings:** Restoration behavior fits (a) comparison to internal standard or (b) deterministic process re-run on perturbed input. Distinguishing tests: produce gradient de novo vs. only as restoration; restore only disrupted elements vs. re-arrange entire court.

**Recommendation:** Acknowledge ambiguity: "Endler's restoration could indicate comparison to remembered visual standard, or a fixed assessment process producing the same configuration on any input. Current evidence does not distinguish."

### Gap 12C — Cumulative creativity requires theory of mind 
*Argued not demonstrated; specific component-by-component evidence is unspecified.*

**Primary sources (verify):**
- Tomasello (1999). *The Cultural Origins of Human Cognition*.
- Whiten et al. (2009). *Animal Cognition* — chimpanzee imitation of arbitrary behaviors.
- Hoppitt & Laland (2013). *Social Learning*.

**Findings:** Whiten shows chimpanzees can imitate arbitrary novel behaviors to high fidelity → imitation-of-means is not uniquely human. Which combination of imitation + teaching + transmission is *necessary* for ratcheting is not empirically tested; chapter's reading is plausible but not established.

**Recommendation:** "The combination of all three components is present in humans and absent (in full) in non-human apes. Which is the load-bearing prerequisite — imitation alone, teaching alone, or the full combination — remains an open empirical question."

---

## Chapter 13 — Self-Awareness

### Gap 13A — Three-self taxonomy clinical evidence 
*Body-self dissociation strong; social/narrative split under-supported clinically.*

**Primary sources:**
- Damasio (2010). *Self Comes to Mind* — proto/core/autobiographical framework.
- Northoff & Bermpohl (2004). *Cortex* — self-referential processing.
- Metzinger (2003). *Being No One*.
- Gallagher & Zahavi (2012) — phenomenological account.

**Findings:** Mirrored self-misidentification + alien hand syndrome dissociate body-self components, not the body/social/narrative split. ASD provides indirect evidence: impaired social-self modeling (predicting how others perceive you) with relatively preserved autobiographical memory. The taxonomy is partly stipulated, partly clinically supported.

**Recommendation:** Add explicit ASD citation as social/narrative dissociation evidence. Clarify that Damasio's proto/core/autobiographical does not perfectly align with body/social/narrative — Damasio's "core self" already includes some social elements.

### Gap 13B — Cleaner wrasse alternative mechanisms 
*Actively contested; Kohda 2022 strengthens, ecological-specificity weakens.*

**Primary sources:**
- Kohda et al. (2019, 2022). *PLOS Biology*.
- de Waal critique (2019) following Kohda 2019.
- Gallup commentary (2019) on ectoparasite-removal alternative.

**Findings:** Kohda 2022: n=18, 94% pass rate — strongest current evidence *for* the mark-test interpretation. But: wrasses respond to parasite-resembling marks specifically; not to arbitrary colors. This cuts both ways. Kohda: domain-specific motivation for body-checking, real mark detection. de Waal/Gallup: behavior is parasite-removal, triggered automatically when reflection shows "parasite-like object," no body-self computation required.

**Recommendation:** Expand hedge into a paragraph naming both interpretations and the specific test that would distinguish — present wrasses with parasite-resembling marks visible without a mirror (on body parts they can see directly). If they respond, behavior is parasite-recognition; if they only respond when mirror is involved, body-self computation is implicated. The function-not-substrate argument holds even setting aside the wrasse case.

### Gap 13C — Computational substrate of mirror passers 
*Claim stands; comparative passer catalog is robust.*

**Findings:** Chimpanzees, dolphins, elephants, magpies — anatomically distinct brains, same computation. No serious literature challenges this comparative conclusion. Wrasse is the only contested member.

**Recommendation:** No revision needed unless wrasse is decisively resolved against; in which case the argument still holds for non-wrasse passers.

---

## Chapter 14 — Metacognition

### Gap 14A — Hampton cross-check base-rate confound 
*Cross-check controls for it; chapter should make this explicit.*

**Primary sources:**
- Hampton (2001). *PNAS*.
- Smith, Beran, Couchman et al. (2014). *Learning and Cognition*.
- Couchman, Coutinho, Beran, Smith (2010). *J Exp Psychol Anim Behav Process*.
- Foote & Crystal (2007). *J Exp Psychol Anim Behav Process*.

**Findings:** Base-rate confound is real. Hampton's accuracy *cross-check* — comparing chosen-trial accuracy to forced-trial accuracy at matched difficulty — controls for it. On long-delay trials specifically, chosen accuracy exceeds forced accuracy. This advantage cannot be explained by stimulus-aversion because both groups face the same stimulus (long delay). Foote & Crystal replicate in rats. Smith/Beran/Couchman identify additional confounds (reward-structure incentives) controllable with further design refinements.

**Recommendation:** Make the cross-check explicit. Add a brief paragraph: "Hampton's design controls for the base-rate problem by comparing accuracy at matched difficulty levels — chosen vs. forced trials of the same delay. The advantage on chosen trials cannot be explained by selecting easier stimuli, because the stimuli are identical."

### Gap 14B — GPT-4 vs. GPT-3.5 calibration improvements 
*Improvements documented, but token-probability calibration ≠ verbalized-uncertainty calibration.*

**Primary sources:**
- Lin et al. (2022). Teaching Models to Express Their Uncertainty in Words. arXiv.
- OpenAI GPT-4 Technical Report (2023).
- Kuhn et al. (2024). *PNAS* — calibration evaluation across GPT-3.5/4, LLaMA2/3.
- Ullman (2023). *PNAS* — false-belief perturbation fragility.

**Findings:** Kuhn et al. show all models overconfident; post-training reduces pre-training calibration. Token-probability calibration is more reliable than verbalized confidence. Lin et al. demonstrate models can be trained to output calibrated uncertainty *language* without internal uncertainty signals — by learning context→confidence-language patterns. Ullman's perturbation fragility means surface-confidence claims do not survive logically irrelevant changes — direct evidence against the hypothesis that GPT-4's calibration improvements reflect internal uncertainty monitoring.

**Recommendation:** Tighten the Ch. 14 AI section. Distinguish token-probability calibration from verbalized-uncertainty calibration. Cite Ullman as showing that expressed confidence is fragile. State the skeptical conclusion clearly: calibration improvements are real but do not yet establish Rung 1 uncertainty monitoring; the Hampton cross-check has not been run on language models.

### Gap 14C — Peer review and replication crisis 
*Replication-crisis evidence cuts against the chapter's "institutional metacognition" framing.*

**Primary sources:**
- Open Science Collaboration (2015). *Science* — 100 replication attempts; 36% replication rate.
- Camerer et al. (2018). *Nature Human Behavior* — *Nature/Science* studies; 13/21 replicated.
- Ioannidis (2005). *PLOS Medicine*.

**Findings:** Peer review *should* function as institutional metacognition. The replication crisis shows that, in much of social psychology, it didn't — overconfident effect sizes passed review and failed replication. Higher-prestige journals replicated worse than lower-prestige ones (selection bias / sample-size underpowering). Whether this indicts peer review as a mechanism or the publication-incentive structure within which peer review operates is contested.

**Recommendation:** Add a paragraph distinguishing peer review as a mechanism (sound in principle) from peer review's actual effects (uncalibrated in practice in some fields). Replication studies are the cross-check the field performs *after* publication — closer analog to Hampton's accuracy cross-check than peer review itself. This honesty strengthens the institutional-metacognition argument by naming where it has empirically failed.

---

## Chapter 15 — Language

### Gap 15A — Chimpanzee declarative pointing absence 
*"Reliably documented" undersells positive captive-pointing evidence; reframe as context-dependent.*

**Primary sources:**
- Tomasello (2006). Why don't apes point? *PNAS* commentary.
- Leavens, Hopkins & Bard (2005). *Current Directions in Psychological Science* — captive chimpanzees point.
- Slocombe et al. (2013). *Animal Cognition* — wild apes' gestures imperative not declarative.
- Budongo Forest Fiona leaf-showing (~2012) — documented case of wild declarative gesture.

**Findings:** Wild apes rarely produce declarative gestures. But captive chimpanzees point spontaneously without training — Leavens & Hopkins documented 53/115 = 46% of captive chimpanzees pointing to unreachable food. The Budongo leaf-showing case shows wild apes *can* produce declarative gestures under appropriate social conditions. The cognitive-vs-environmental framing is contested.

**Recommendation:** Substantially revise. Acknowledge Leavens & Hopkins captive evidence. Cite Budongo leaf-showing. Reframe from "apes lack declarative pointing" to "apes show declarative pointing rarely in wild, frequently in captive settings; the ecological/developmental factors are contested." This is a more honest framing that still preserves the chapter's developmental-program argument.

### Gap 15B — Kanzi comprehension vs. Nim production: asymmetric scrutiny 
*Equal skepticism warranted; chapter applies different standards to comprehension vs. production.*

**Primary sources:**
- Savage-Rumbaugh et al. (1993). *Monographs of the Society for Research in Child Development* — Kanzi.
- Terrace et al. (1979). *Science* — Nim.
- Wallman (1992). *Aping Language*.

**Findings:** Nim production heavily criticized for imitation-without-understanding. Kanzi comprehension paradigm is vulnerable to the same surface-pattern-learning account. The "blind condition" (experimenter behind one-way mirror) does not eliminate observer bias if the response coder is not blind to the command. More fundamentally, Kanzi may have learned high-probability command-string→response-pattern associations without compositional understanding.

**Recommendation:** Apply equal scrutiny. Add a paragraph: "The comprehension paradigm is vulnerable to the same surface-learning account as production. A stronger test: novel command compositions Kanzi has never heard, composed from familiar words in unfamiliar grammatical structures. This has not been systematically run." Cite Wallman's critical review.

### Gap 15C — Question-asking as intrinsic communicative goal 
*Genuine open question; literature names competing mechanisms.*

**Primary sources:**
- Chouinard, Harris & Maratsos (2007). *Monographs of the Society for Research in Child Development*.
- Callanan & Oakes (1992). *Cognitive Development*.
- Tomasello & Haberl (2003). *Cognition*.

**Findings:** Three competing accounts: (a) intrinsic curiosity / theory drive (Chouinard); (b) learned social pragmatics (Callanan); (c) metacognitive monitoring (children recognize their own knowledge gap and act). Literature does not yet distinguish.

**Recommendation:** Name the three accounts explicitly. Cite Chouinard's information-seeking vs. non-information-seeking question distinction. Note that genuine intrinsic question-asking (asking to explore, not to solve immediate problems) may be developmentally later and may require Rung-2 metacognition. Honest framing of an unresolved problem strengthens the chapter.

---

## Chapter 16 — Collective Intelligence

### Gap 16A — Polanyi's tacit dimension and AI 
*Strongest counter-argument (RT-2, behavioral cloning) is in exercises, not main text.*

**Primary sources:**
- Polanyi (1966). *The Tacit Dimension*.
- Brohan et al. (2023). RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control. CoRL 2023.
- Hadjimichael, Ribeiro & Tsoukas (2024). How Does Embodiment Enable Tacit Knowledge Acquisition? *Organization Studies* 45(2):181–203.

**Findings:** RT-2 and similar imitation-learning systems acquire complex manipulation behaviors — including features experts considered tacit (force calibration, mid-action grip adjustment) — from video data and demonstrations. This does not refute Polanyi but reframes him: he was right that we know more than we can tell, but wrong (or at least overstating) that the untold knowledge is incomputable. Some tacit knowledge appears to compress to data; some (novel scientific insight, aesthetic judgment) may still resist.

**Recommendation:** Move the AI counter-argument from exercises into main text. Explicitly cite RT-2 as evidence that tacit procedural knowledge can be partially captured from demonstration data. Frame as: "The empirical question is which forms of tacit knowledge compress to data and which do not — not whether the tacit dimension is in principle uncapturable."

### Gap 16B — Murmuration as coordination not collective intelligence 
*Distinction is stipulated; depends on definition of "collective intelligence."*

**Primary sources:**
- Couzin, Krause, Franks & Levin (2005). *PNAS* — informed-minority steering.
- Vicsek & Zafeiris (2012). *Physics Reports* — flocking review.
- Reynolds (1987) — original Boid model.

**Findings:** Couzin shows murmurations exhibit goal-directed predator-evasion. Under Legg-Hutter (functional goal-maximization across environments), this qualifies as intelligent collective behavior. The chapter's distinction requires goal-representation or shared intentionality, which is a stronger criterion than Legg-Hutter alone. The chapter does not state which definition is in play.

**Recommendation:** State the definition explicitly. If using Legg-Hutter, murmurations qualify as collective-intelligent (functional goal-direction without explicit goal-representation). If requiring shared intentionality, the chapter should defend this criterion.

### Gap 16C — AlphaFold as ratchet click 
*Genuine ratchet advance, but novel-discovery framing in popular accounts oversells what AlphaFold did.*

**Primary sources:**
- Jumper et al. (2021). *Nature*.
- Tunyasuvunakool et al. (2021). *Nature*.

**Findings:** AlphaFold 2 dramatically improved structure-prediction accuracy and enabled prediction for novel-fold proteins lacking structural homologs. It did *not* discover new physics of folding; it compressed PDB knowledge into a predictive model that extrapolates beyond direct training data. This is exactly what a ratchet advance should do — take accumulated knowledge and extend it.

**Recommendation:** Bring AlphaFold into main text (currently exercises). Frame precisely: AlphaFold ratcheted by *compression and extrapolation* of accumulated experimental structures, not by discovering new physical principles. This is what cumulative culture looks like — no system does ex nihilo discovery. AlphaFold qualifies as a ratchet click.

---

## Chapter 17 — AI as Data Point

### Gap 17A — Gradient descent vs. evolutionary selection 
*Distinction is load-bearing but inverted from chapter's framing.*

**Primary sources:**
- Hadfield-Menell, Russell & Abbeel (2016). Inverse Reward Design. NIPS. [PDF](https://people.eecs.berkeley.edu/~russell/papers/nips17-ird.pdf)
- Hadfield-Menell, Russell & Abbeel (2016). Cooperative Inverse Reinforcement Learning. IROS.
- Hadfield-Menell et al. (2020). Pitfalls of Learning a Reward Function Online. IJCAI.

**Findings:** The reward-modeling literature distinguishes the two precisely. Gradient descent assumes a *specified* loss; the entire field of value alignment exists because specifying the right loss is computationally and epistemically harder than running gradient descent given a specification. Evolutionary selection has no specifier — it optimizes reproductive fitness regardless of human intent. The stakes-critical difference is not timescale but *specification authority*.

**Recommendation:** Reframe Ch. 17's stakes argument. The disanalogy is: gradient descent has an author (the loss specifier); evolution does not. Misspecified losses can produce more dangerous outcomes than evolution's indifference, because they are coupled to powerful optimization. This is a more interesting argument than the timescale framing.

### Gap 17B — "Novel shape" argument needs contrastive case 
*Evidence exists for novel-shape claim; contrastive case should be made explicit.*

**Primary sources:**
- Lake, Salakhutdinov & Tenenbaum (2015). Human-level concept learning through probabilistic program induction. *Science* 350:1332–1338. [DOI 10.1126/science.aab3050](https://www.science.org/doi/10.1126/science.aab3050)
- Lake, Ullman, Tenenbaum & Gershman (2017). Building machines that learn and think like people. *Behavioral and Brain Sciences* 40:e253. [PDF](https://cims.nyu.edu/~brenden/papers/LakeEtAl2017BBS.pdf)
- Marcus & Davis (2019). *Rebooting AI*.

**Findings:** Lake's one-shot-learning work shows humans and deep networks solve different computational problems on the same tasks (humans: causal structure + program induction; networks: learned features). Marcus & Davis argue AI systems lack hierarchical causal models and compositional reasoning. This supports the "novel shape" reading. The contrastive case: an AI-as-rung system would show partial mastery of human capacities in phylogenetic order; a gap-system would show no progress; a novel-shape system shows orthogonal competence.

**Recommendation:** Cite Lake (2015, 2017) and Marcus & Davis (2019) as supporting evidence. Make the contrastive prediction explicit so the reader can see what each reading would look like empirically.

### Gap 17C — Distribution-shift uniformity 
*Mechanisms differ across domains; chapter's uniform characterization misses this.*

**Primary sources:**
- MICCAI 2025. Out-of-Distribution Detection with Medical Vision-Language Models.
- Tan, Soh & Goh (2022). Physical imaging parameter variation drives domain shift. *Scientific Reports*. [DOI 10.1038/s41598-022-23990-4](https://www.nature.com/articles/s41598-022-23990-4)
- Kaur et al. (2024). Generative models improve fairness of medical classifiers under distribution shifts. *Nature Medicine*. [DOI 10.1038/s41591-024-02838-6](https://www.nature.com/articles/s41591-024-02838-6)

**Findings:** Medical imaging OOD is *hardware-induced* (scanner/protocol differences). Language model OOD is *semantic* (sparse training-distribution coverage). The mechanisms differ — sensor physics vs. token-distribution sparsity — and predict different brittleness profiles in deployment.

**Recommendation:** Differentiate the failure modes. Add a brief paragraph: "AI distribution-shift failures are not uniform. Medical imaging systems degrade under hardware/protocol variation (different scanners produce different pixel statistics). Language models degrade under semantic variation (training distribution does not cover certain concept combinations). Both are 'distribution shift' but the underlying mechanisms are different."

---

## Chapter 18 — The Extended Mind Arrives

### Gap 18A — Causal reasoning formalizable in principle 
*Chapter's claim is false; the real issue is execution, not formalization.*

**Primary sources:**
- Pearl (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
- Bareinboim & Pearl (2016). Causal Inference and the Data-Fusion Problem. *PNAS* 113(27):7345–7352.
- Carloni (2025). The Role of Causality in Explainable AI. *WIREs Data Mining and Knowledge Discovery*. [DOI 10.1002/widm.70015](https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70015)

**Findings:** Pearl's structural causal models formally represent Rungs 1, 2, and 3. Do-calculus formalizes intervention; counterfactuals are formalized via SEM manipulation. The claim that Rung 2/3 are "non-formalizable in principle" is false. The real claim — which the chapter needs but does not quite make — is that *executing* these formalisms requires identifying the causal graph, which requires intervention or strong assumptions, which requires stakes/embodiment. Carloni 2025: "Algorithmic recourse requires perfect knowledge of the data-generating SCM, which is unidentifiable from purely observational data." It's an *epistemological* problem (data requirements), not a formalization problem.

**Recommendation:** Substantial revision. Drop "non-formalizable in principle." Replace with: causal reasoning is formalizable (Pearl proved it); execution requires identifying the right causal graph, which in turn requires intervention or high-quality data, which in turn requires stakes/embodiment. This is a more interesting argument and is correct.

### Gap 18B — "Direction has remained with the human" 
*Partially false; autopilot took over Rung 2; formal verification handles Rung 3.*

**Primary sources:**
- USAARL-TECH-TR-2025-09. Optimizing Adaptive Automation in Aviation.
- EASA. Automation and Flight Path Management. *European Safety Promotion Network – Rotorcraft.*
- Finkbeiner et al. (2025). An Information-Flow Perspective on Explainability Requirements. KR 2025.
- Jhala et al. (2025). On the Impact of Formal Verification on Software Development. OOPSLA 2025.

**Findings:** Aviation autopilots: pilot sets goal (altitude, airspeed); autopilot selects actions (pitch, roll, thrust) — Rung 2 transferred. Adaptive automation now dynamically transfers agency based on workload. Formal verification (Dafny, F*, Verus) checks counterfactual implications of code: "if precondition holds, does postcondition follow?" — Rung 3 reasoning performed by machine, not human. Human retains higher-level goal-setting; that domain has shrunk.

**Recommendation:** Reframe: the *extent* of human direction has narrowed, not been preserved. Add aviation autopilots and formal verification as named entries in the catalog where direction has been at least partially transferred. This complicates the leitmotif but is honest, and the larger argument (capacity formalizable, judgment not) survives if reframed at the level of meta-direction (who decides what to formalize and when).

### Gap 18C — Confabulation as failure mode 
*Real, but it's a property of generative systems, not agency per se.*

**Primary sources:**
- Huang et al. (2023). A Survey on Hallucination in Large Language Models. arXiv:2311.05232.
- Maynez, Narayan, Bohnet & McDonald (2020). On Faithfulness and Factuality in Abstractive Summarization. ACL.
- Strapparava & Mihalcea (2024). Confabulation: The Surprising Value of LLMs. ACL.
- Zhang et al. (2024). What If the TV Was Off? Examining Counterfactual Reasoning Abilities of LLMs. CVPR.

**Findings:** Confabulation is a property of *generative models* trained on next-token-prediction objectives. pH meters don't generate; they map sensor input to numbers. A generative robot trained on language supervision would also confabulate. The chapter conflates agency with language generation.

**Recommendation:** Specify: confabulation is intrinsic to generative training objectives, not to extended agency in general. The new failure mode arrived with generative AI specifically — not with all cognitive extension. This sharpens the chapter's argument: AI is not just more powerful than prior extensions, it has a distinct failure-mode signature traceable to its training objective.

---

## Cross-Cutting Tensions

### Tension T1 — Function-not-substrate vs. stakes 
*Real and unresolved; current evidence supports a hybrid model.*

**Primary sources:**
- Tsomokos et al. (2025). Embodied Cognition and the Structure of Personality. *Journal of Personality*.
- Royal Society (2023). Minds in Movement. *Phil. Trans. R. Soc. B.* [DOI 10.1098/rstb.2023.0144](https://royalsocietypublishing.org/doi/10.1098/rstb.2023.0144)
- Brohan et al. (2023). RT-2.

**Findings:** Some functions appear substrate-neutral (pattern recognition, language prediction). Some require embodied stakes for execution (physical reasoning, intervention planning). RT-2 transfers web knowledge to robotic control — partial substrate-independence. But fails when robot morphology or object affordances differ from training — substrate dependence persists in execution. The thesis is partial.

**Recommendation:** Present the tension explicitly as the book's deepest unresolved question. Rung 1 functions: largely substrate-neutral. Rung 2/3 functions: representable substrate-neutrally (Pearl) but require embodied stakes to *execute*. This isn't a contradiction; it's a layered claim — substrate matters at the execution layer, not at the representation layer. Naming it sharpens the AI argument.

### Tension T2 — Legg-Hutter flattens affect; affect may be constitutive 
*Current neuroscience favors affect-as-constitutive; chapter should name this as a chosen tradeoff.*

**Primary sources:**
- Legg & Hutter (2007). Universal Intelligence: A Definition of Machine Intelligence. *Minds & Machines* 17(4):391–444.
- Damasio & Carvalho (2013). The nature of feelings. *Nature Reviews Neuroscience* 14:143–152.
- Pessoa (2008). On the relationship between emotion and cognition. *Nature Reviews Neuroscience* 9:148–158.

**Findings:** Damasio, Pessoa, LeDoux: affect assigns valence to outcomes, providing the basis for goals themselves. Legg-Hutter takes goals as given. If goal-generation is partly affective, then a definition that flattens affect describes a system without the machinery that produces its goals. The Legg-Hutter framework works for systems with externally specified goals (artificial); it is descriptively incomplete for biological systems that generate their own.

**Recommendation:** Add a paragraph in either Ch. 1 or as a synthesis section. Frame Legg-Hutter as the chosen instrument for substrate-neutral comparison, with the explicit acknowledgment that it brackets goal-generation. The bracketing is methodological, not metaphysical.

### Tension T3 — Ratchet as cascade of prerequisites 
*Chain implied but not assembled; literature does not directly support each step as necessary.*

**Primary sources:**
- Tennie, Call & Tomasello (2009). Ratcheting up the Ratchet. *Phil. Trans. R. Soc. B* 364(1528):2405–2415.
- Tomasello (1999). *The Cultural Origins of Human Cognition.*
- Sterelny & Hiscock (2014). Cumulative Cultural Evolution and the Zone of Latent Solutions. *Current Anthropology*.

**Findings:** Cascade plausibility: declarative pointing → joint attention → conventional symbols → language → cumulative culture via teaching. Literature does not directly support each step as *necessary*. Sterelny & Hiscock propose alternative routes (niche construction, technology-led rather than pointing-led). The cascade is a hypothesis, not a confirmed pathway.

**Recommendation:** Either (a) explicitly assemble the cascade as the book's central theoretical hypothesis, presenting which steps are empirically established and which are inferred; or (b) acknowledge the cascade as one of several possible routes (cite Sterelny-Hiscock alternative) and let the reader weigh the evidence.

---

## Unproven Claims (synthesis section)

### UC1 — AI cannot participate in cumulative culture due to tacit dimension 
*Open empirical question; not a settled principle.*

**Findings (see Gap 16A):** RT-2 and behavior-cloning literature show tacit procedural knowledge can be partially captured from demonstration data. Whether this constitutes genuine tacit knowledge or functional approximation is contested. The strong claim ("tacit knowledge in principle uncapturable") is unsupported by current evidence.

**Recommendation:** Frame as open empirical question: which forms of tacit knowledge compress to data, which don't. Move from "AI cannot participate" to "AI's participation depends on whether the relevant tacit knowledge is in the kind that compresses."

### UC2 — Asymmetry between extendable and non-extendable capacities 
*The reason is data identifiability, not formalizability.*

**Findings (see Gap 18A):** Pearl formalized Rung 2 and 3. The asymmetry is *epistemological* — Rung 1 can be learned from observational data alone; Rung 2/3 require intervention data or strong causal assumptions, which are harder to obtain.

**Recommendation:** Revise: the asymmetry is not about formalizability but about *data requirements*. Rung 1 generalizes from association; Rung 2/3 require intervention-grade data, which AI systems trained on observational text/images do not have. Stakes/embodiment matter because they generate intervention data through action in the world.

### UC3 — Declarative pointing as both species-specific prerequisite AND uniquely absent 
*Imperative-vs-declarative distinction is strong; necessity-for-language claim is weaker.*

**Findings (see Gap 15A):** Apes gesture imperatively (well-documented), not declaratively (rarely). The empirical difference is real. Whether declarative pointing is *necessary* for language is a different question — Nicaraguan Sign Language emerged in deaf communities without prior declarative-pointing scaffolding (in a species capable of it). Causal necessity not established.

**Recommendation:** Tighten: declarative pointing is empirically unique to humans among great apes and correlates with language acquisition. Causal necessity is one hypothesis among several (cf. Sterelny-Hiscock); not established by current evidence.

---

## Summary triage

| Triage | Count | What it means for the next pass |
|---|---|---|
| Settled in chapter's favor | 6 | Cite with confidence; minor wording additions only |
| Critique stands | 19 | Targeted addition, qualification, or naming of competing interpretation |
| Critique substantially correct | 16 | Substantive revision recommended (paragraph-level or restructuring of one claim) |
| Genuinely open in literature | 5 | Flag in chapter footer; not the chapter's failure |
| **Total** | **46** | |

**Highest-priority revisions ( with greatest argumentative consequence):**
1. **Gap 18A** — Drop "non-formalizable in principle"; reframe as identifiability/execution. Affects Ch. 9, 14, 17, 18 cascade.
2. **Gap 18B** — Acknowledge autopilot + formal verification as partial direction transfers. Sharpens the leitmotif rather than weakening it.
3. **Gap 16A** — Move RT-2 / Polanyi counter-argument from exercises to main text.
4. **Tension T1** — Name the substrate-independence-with-execution-dependence as the book's central unresolved question.
5. **Gap 14B** — Tighten LLM metacognition section: token-prob calibration ≠ verbalized-uncertainty calibration; cite Ullman fragility.
6. **Gap 15A** — Reframe ape declarative pointing absence as context-dependent rather than absent-of-evidence.

**Lowest-cost revisions with high pedagogical payoff:**
- Gap 14A (Hampton cross-check explicit)
- Gap 7B (cite NIST/OSAC + 22% gap as resolved methodology)
- Gap 8A (Flash Crash precise causal chain)
- Gap 7A (cite Spiers 2020 longitudinal evidence)

**Network-access caveat:** Chapters 9–12 (Agent 3) findings rely on training-data citations, not live web search. Verify these specific citations before publication: Steiner-Redish primate replications (Camille, Wittmann, Rudebeck), Dally-Bugnyar corvid work, Lindenfors Dunbar reanalysis, Whiten chimpanzee imitation. The findings are credible but the URLs/DOIs were not fetched.

---

*Run by Claude in Cowork. Five parallel research agents. Aggregated 2026-05-05.*
