# Chapter 17 — AI as Data Point

---

## Learning Objectives

By the end of this chapter, you will be able to:

1. **Place** any AI system on the fourteen-axis framework developed across this book, reporting a profile rather than a single score
2. **Distinguish** functional presence of a cognitive capacity from stakes-driven deployment of that capacity
3. **Apply** Chollet's skill-versus-skill-acquisition distinction to evaluate AI benchmark performance without overgeneralizing
4. **Explain** why the Geirhos texture-bias finding matters beyond computer vision — what it reveals about the relationship between benchmark performance and underlying computation
5. **Critique** single-axis claims about AI intelligence by naming which Chapter 1 definition is being silently assumed
6. **Construct** the argument that AI occupies a novel niche in cognitive space — neither a rung on an existing ladder nor a gap in the existing account

**Prerequisites:** Chapters 1–16. Specifically: the definition taxonomy from Ch. 1; steering, learning, and pattern recognition from Chs. 3, 5, and 6; theory of mind from Ch. 11; metacognition from Ch. 14; and collective intelligence from Ch. 16.

**Why this chapter:** For sixteen chapters we asked the same question of every organism — *what is this system actually doing on its substrate to produce the behavior we observe?* This chapter asks it of the most discussed cognitive artifact of our era. The framework is already built. We are applying it one more time.

---

## 17.1 — The Diagnostic Test

The screen in the Tübingen lab shows a cat.

You can see the ears, the posture, the silhouette — everything that makes something a cat. What you cannot see is a square centimeter of cat skin. The surface is gray and wrinkled and deeply furrowed, mapped from a photograph of an elephant. The researchers — Geirhos, Rubisch, Michaelis, Bethge, Wichmann, and Brendel — have done something surgically precise: they have separated the two cues that, in almost every natural photograph, arrive together. Shape says cat. Texture says elephant. It is a forced choice.

The network says: elephant.

The network in question is a convolutional neural network trained on ImageNet — 1.2 million labeled photographs, the benchmark on which deep-learning vision had, by 2018, matched and in some tasks exceeded human-level accuracy. [200 million parameters](https://arxiv.org/abs/1811.12231) tuned to extract structure from images. Superhuman performance on the standard test. And here it is, looking at a cat-shaped object and reporting elephant.

The researchers ran the inverse: elephant-shaped objects covered in cat fur. Network said cat. Across hundreds of cue-conflict images the pattern held. The ImageNet-trained networks had learned to classify textures. The benchmark, it turned out, had texture cues redundant with the shape cues all along, and the networks had taken the statistically easier road. They reached human accuracy on the benchmark via a computation that was not the computation the human was running.

This is the diagnostic test. Not "did the system get the right answer" — the system got superhuman-level right answers on ImageNet for years. The diagnostic is: *what is the system actually doing to produce the answer it produces?* The question is the same one we have been asking since the first chapter. It produced different results for the bacterium, the octopus, the crow, and the chimpanzee. It produces a different result here.

The chapter is what that question produces when aimed at the breadth of AI systems the field has built.

### The Name Problem

Before we can apply the framework, a prior problem needs naming.

When we describe a crow inserting a stick into a hole to extract a grub, there is a physical referent for the behavior and a physical substrate for the computation. The stick is real. The substrate is real neurons. When we describe a language model "reasoning" about a problem or "understanding" a sentence, we are using words whose original referents are biological. The words carry connotations — of subjectivity, of stakes, of purpose — that may or may not transfer.

This chapter does not resolve whether AI systems have inner experience. Nobody has resolved that. What it does, consistently, is distinguish two things the literature often conflates: **functional presence** and **stakes-driven deployment**. A system has functional presence of a capacity when its internal states play a similar computational role to the capacity in biological systems — when interpretability work finds representations that behave the way the capacity's representations should behave. A system has stakes-driven deployment when the capacity is embedded in an organism that has costs for failure: a body that can starve, a lineage that can end, a social position that can collapse.

Every capacity in this book evolved because of stakes. Every biological cognitive structure was shaped by the cost of getting it wrong over evolutionary time. The bee's quorum threshold from Chapter 16 is calibrated where it is because a wrong choice means the colony dies in winter. The elephant matriarch's decision from Chapter 10 about whether to investigate or flee an unfamiliar contact call is a decision with consequences: move the herd incorrectly and young ones are exhausted or exposed. These stakes did not decorate the capacities from the outside. They *built* them.

AI systems can have functional analogs of these capacities — representations that play similar computational roles, learned from text written by creatures that did have stakes. They cannot have the stakes that produced the capacities in biology. This is not a moral judgment. It is an architectural observation. A system that has never had stakes cannot have evolved, in any biological sense, the cognitive structures that stakes built.

We will label this throughout: **function present / stakes absent** where it applies.

---

## 17.2 — The Three Questions Inside One Question

"Is AI intelligent?" is not a question. It is three different questions wearing the same phrase, and nothing about the analysis in this chapter can be trusted until they are separated.

### Question 1: Is Intelligence a Height or a Shape?

The first question assumes intelligence is a quantity, like mass, that can be reported as a single number per entity. The whole of Chapter 1 was an argument against this assumption, and sixteen chapters of comparative cognition have been the empirical case.

The chickadee can cache 70,000 food items across a territory of several kilometers and recover most of them months later — a spatial memory that would be extraordinary by any human standard. The chickadee cannot produce a sentence. The octopus integrates color and polarization and texture information from eight independently mobile arms, producing a real-time model of its environment that is richer in some dimensions than anything our visual cortex achieves. The octopus has almost no social cognition. The chimpanzee reads coalition dynamics and tracks third-party relationships across a community of 50 individuals with a precision no textbook can fully capture. The chimpanzee cannot reliably pass a test of recursion.

No organism is uniformly high on all fourteen axes. The question "is X more intelligent than Y" only has an answer once you specify which axis. "More intelligent" is meaningful when it means "better at navigating a three-dimensional chemical gradient" or "faster at forming arbitrary associations." It is not meaningful as a global judgment, because there is no global axis on which to place it.

Applied to AI: the single-axis question has no good answer, for the same reason it never had a good answer. The chapter will report a profile.

### Question 2: Is It Doing the Thing, or Buying the Output?

[François Chollet, in a 2019 paper](https://arxiv.org/abs/1911.01547), drew a line that comparative cognition had been drawing for decades without a clean name: the distinction between **skill** and **skill-acquisition efficiency**.

Skill is performance at a task. Skill-acquisition efficiency is the rate at which a system arrives at that performance given some prior and some amount of exposure. A model trained on ten trillion tokens that scores 95% on a mathematics benchmark is showing skill. A child who scores 95% on the same problems after seeing five examples in school is showing something different — a much higher skill-acquisition efficiency, a richer deployment of prior structure, a much smaller data footprint for the same performance.

Current AI systems tend to *buy* skill with data at a cost that would be biologically ruinous. The human visual cortex reaches human-level object recognition on roughly 100 hours of visual experience in the first six months of life. The ImageNet-trained network needs 1.2 million labeled examples — and, as the Tübingen finding showed, gets there via a different computation.

The Abstraction and Reasoning Corpus that Chollet introduced in the same paper makes the distinction visible by design: simple visual puzzles requiring the solver to extract a generative rule from one or two examples, then apply it to a novel case. No training data available. Priors plus few-shot inference only. Humans score around 80%. Frontier AI systems — including those with chain-of-thought scaffolding and extended test-time compute — have not closed the gap to the human ceiling. They have bought extraordinary skill on distribution. Off distribution, with two examples and no lookup, the gap reappears.

Skill present. Skill-acquisition efficiency: much lower than the human child.

### Question 3: Is the Function Running, or Just the Language?

This is the most important question and the most easily confused.

Systems that produce text learn that text. They learn — because the training corpus contains enormous quantities of first-person reports, scientific papers, and narrative fiction — the language that describes cognitive capacities. "I'm not sure about that." "I might be wrong." "I can see why someone would think that, but I think..." This language, in humans, is produced by cognitive operations: uncertainty monitoring, belief attribution, perspective-taking. In a language model, it is produced by next-token prediction on a training distribution that included many instances of that language.

The question is whether, underneath the language, there is an operation. Not a question about consciousness. A question about mechanism. If the model produces "I'm not certain" at appropriate-looking rates, is there an internal certainty signal that is actually gating the output? Or is there a pattern that associates context features with uncertainty phrases?

For some capacities, interpretability work gives evidence for the operation. For others, we do not have the evidence. The chapter names, axis by axis, which is which.

---

## 17.3 — The Profile, Axis by Axis

### Pattern Recognition and Prediction

*Consider a hospital pathology lab, circa 2017. A dermatologist looks at a high-resolution image of a skin lesion — irregular borders, variations in pigmentation, asymmetric distribution — and makes a judgment that will determine whether a patient begins treatment. She has twenty years of clinical experience and has examined, in total, perhaps fifty thousand lesions. In the next room, a convolutional neural network trained on 130,000 clinically-verified dermoscopic images makes the same judgment. The study, published in Nature that year, found the network matched the dermatologist on sensitivity and specificity. In some configurations, it exceeded them.*

This is where AI wins outright, and the win is not close.

A modern transformer trained on a large enough corpus achieves, on next-token prediction and on many static-pattern-classification tasks, accuracy that no biological system matches in throughput, breadth, or scale. The architecture — learned attention patterns across a high-dimensional embedding space — is genuinely good at extracting regularities from large corpora. The technology works. [The 2017 dermatology result](https://doi.org/10.1038/nature21056) is real. The performance on protein structure prediction (AlphaFold2's median backbone accuracy of 0.96 Å RMSD across a benchmark of experimental structures) is real. The benchmark improvements are real.

The Tübingen diagnostic does not undo this. It specifies it. The win is real on the axes the benchmark measures. It is silent on the adjacent axes the benchmark does not measure — perceptual invariance to distribution shifts, generalization to cue-conflict inputs, causal structure below the correlational surface. "Superhuman at finding statistical structure in large, labeled, in-distribution datasets" is a true and useful sentence. "Understands what it sees" borrows a word whose full meaning extends well beyond that.

**Profile placement:** Extreme high on in-distribution pattern detection at scale. Drops sharply under distribution shift and cue-conflict conditions. The high is real; the cliff is real.

**Function present? Yes.** Stakes? The question dissolves here — pattern recognition in current AI systems is not produced by stakes-driven selection. It is produced by gradient descent on labeled data. The function is there. The origin is different.

### Theory of Mind

*The child is three and a half years old. Her name, in this experimental protocol, is not given — she is one of thousands of children tested on variants of the same scenario since the original Wimmer and Perner study in 1983. A doll named Sally places a marble in a basket and leaves the room. A doll named Anne moves the marble to a box. Sally returns. Where will Sally look for her marble? The child — three and a half, still sticky-fingered from breakfast — says: the basket. She has passed the false-belief task. She is tracking a representation in another agent's mind that she knows to be out of sync with the world.*

Frontier language models pass the Sally-Anne test at near-ceiling rates. They have read every false-belief paper, every developmental psychology textbook, and an enormous quantity of fiction in which characters reason about each other's mistaken beliefs. The performance is real.

[Tomer Ullman, in 2023](https://arxiv.org/abs/2302.08399), tested what happened when small, logically irrelevant perturbations were made to standard false-belief items. Make the container transparent. Have the character write the location label herself. Introduce a brief, task-irrelevant narrative interlude. In each case, the problem's logical structure was unchanged. A system actually running a false-belief inference — tracking an agent's belief state as a variable that updates based on what the agent has and has not observed — should be unaffected. The perturbations should not matter. In Ullman's testing, they mattered significantly: models that had reliably produced the correct answer in standard form failed under these surface-level modifications.

The Geirhos diagnostic, in a different domain. The system is producing the right output via a process that is not the process the human is using. Pearls' ladder of causation is useful here: a Rung 1 system (statistical association) can produce Rung 3 outputs (counterfactual reasoning) if the training distribution contains enough examples of those outputs in their associated contexts. The output is sometimes correct. The machinery running underneath is not running the inference we would recognize as theory of mind.

**Profile placement:** High on standard false-belief benchmarks; drops under distribution-shift perturbations in a way that is inconsistent with the underlying operation.

**Function present?** Not established for the operation — the outputs are sometimes right; the mechanism has not been confirmed. **Stakes absent** — the model has no agents whose beliefs it tracks because it depends on them.

### Metacognition

*Diana Reiss and Lori Marino, in 1991, placed a large mirror in the tank at the New York Aquarium. The two bottlenose dolphins in the study — subjects from whom the researchers had obtained months of behavioral baseline — initially treated the mirror as a social encounter: vocalizations, approach behavior, the gestures used with unfamiliar conspecifics. Then, over days, something shifted. The animals began to spend time in front of the mirror performing behaviors — tongue extensions, slow rotations — that made no social sense but perfect investigative sense: you do these things when you are trying to figure out what you are looking at.*

The metacognition chapter (Ch. 14) documented a specific operation in nonhuman animals — the ability to monitor the reliability of one's own memory or perceptual signal and adjust behavior accordingly. The cleanest case was David Smith's rhesus macaques learning to press an uncertainty paddle when they could not reliably discriminate a stimulus, demonstrating internal certainty monitoring that generalized to novel stimuli. [Louis Herman's dolphin studies](https://doi.org/10.1016/j.tics.2007.06.002) showed animals opting out of ambiguous trials in ways that tracked their actual accuracy. The operation involves an internal signal — something that varies with the reliability of the cognitive process — gating output behavior.

Language models produce uncertainty language. "I'm not certain about this." "This may be incorrect." The sentences appear at appropriate-looking rates. They are also next-token predictions trained on a corpus in which competent writers deploy uncertainty language at appropriate rates. The surface behavior is present; the operation underneath it is not established.

The test that would be diagnostic: something equivalent to the Hampton uncertainty paradigm, in which the model's expressed confidence tracks an objectively measurable internal variable that its training did not expose — a novel out-of-distribution task on which the model has actual varying accuracy, with expressed uncertainty calibrated to that accuracy in real time. The calibration work from OpenAI, Anthropic, and DeepMind on frontier systems shows partial evidence of this: these systems' stated confidence correlates with their accuracy better than chance and better than smaller models. Whether this constitutes metacognitive monitoring in the Chapter 14 sense, or a well-calibrated pattern-matcher on text features that correlate with difficulty, is not resolved.

**Profile placement:** Uncertainty language present; calibration partially present; the underlying operation — a genuine internal certainty signal gating output — not yet established.

**Function:** Partially supported by calibration evidence. The signal may be there; interpretability work is the right place to look. **Stakes absent:** The model has no cost for being wrong.

### Collective Intelligence and Cumulative Culture

*Tomasello's ratchet was the argument of Chapter 16: cultural evolution requires not just learning from others, but a cumulative mechanism — innovation builds on prior innovation, each generation starting where the last left off, the thing getting better across generations without any individual redesigning from scratch. The ratchet requires practice, not just information. It requires a body at a bench, making errors, receiving correction, building procedural memory in a system that has something at stake.*

The role of current AI systems in collective intelligence is already determined by their architecture. They are extraordinary participants in the aggregation layer — fast, high-bandwidth, tireless interfaces to the explicit record of human knowledge. A researcher can, in seconds, access synthesis across thousands of papers that it would have taken a literature review team months to assemble. This is real and consequential.

The cumulative-culture layer is different. Tomasello's ratchet runs on practice. The published paper is the frozen record of a long process of failed experiments, revised hypotheses, embodied skill at the bench. The model has access to the paper. It has not stood at the bench. It cannot fail an experiment and learn from the failure, because failure has no cost in a system without stakes and without a body that experiences the consequence of getting it wrong.

There are active research programs — in reinforcement learning, in robotics, in neurosymbolic architectures — aimed at exactly this gap. The field is not standing still. But the current frontier model is, in Tomasello's terms, a very sophisticated participant in the transmission of explicit knowledge. It is not yet a participant in the ratchet.

**Profile placement:** Extreme high on knowledge retrieval and synthesis. Near-zero on participation in stakes-driven cumulative culture. The gap is not performance; it is architectural.

### Embodied Navigation

*Thirty grams. Approximately 250,000 neurons. A desert ant named Cataglyphis navigates across kilometers of flat, featureless Tunisian salt pan, tracking its position continuously via path integration — dead reckoning updated by visual landmarks and sun-compass calibration — to find a food item weighing fractions of a milligram and return it directly home. Not approximately home. Directly. Through terrain it may not have crossed before. If you move the ant after it has loaded its food and computed its home vector, it walks the original vector distance, then searches. It has a model of its own location and it uses it.*

A modern multimodal language model, given high-resolution imagery of the same salt pan, can describe it in four languages, produce a historically accurate account of Cataglyphis biology, and discuss the path integration literature in detail. It cannot, reliably, tell you which way the ant should go to get home.

This is not a failure of knowledge. The model has more *propositional* knowledge about desert navigation than any ant has or could have. The failure is architectural. The ant's navigation is implemented in a body — a physical agent with proprioception, vestibular feedback, a home vector that is continuously updated by movement through the world, and mortality at the end of a failed return trip. The model's "navigation" is implemented in token sequences about navigation, with no feedback loop that closes on physical consequence.

The active research in embodied AI is genuine, and some robotics systems do close the loop on physical consequence. But the frontier language model — the system most often invoked when people ask "is AI intelligent" — is the furthest possible thing from an ant navigating a salt pan. It is supreme on text about the world. It is absent from the world.

**Profile placement:** Near-zero on embodied, stakes-driven navigation. This is not a deficiency to be patched by adding more parameters. It is a structural fact about a system that has never had a body.

**Function present?** No, in the operational sense. **Stakes?** Completely absent.

---

## 17.4 — The Stakes Axis

The preceding sections kept returning to a phrase: *stakes absent*. It deserves its own treatment, because it is not an axis in the usual sense — no comparative cognition paper measures it — and yet it is the axis that makes sense of the shape of everything above.

Every organism in this book has skin in the game. The bacterium Escherichia coli swims toward glucose because, in the ancestral environment, cells that did not swim toward glucose did not replicate. The behavior is not a preference encoded separately from fitness: it *is* fitness, crystallized into a gradient-following algorithm. The slime mold Physarum polycephalum routes its plasmodium efficiently because organisms that routed inefficiently used more energy than they gathered and did not persist. The crow that caches food and protects caches from observers is running a fitness-relevant algorithm under selective pressure that killed the crows who cached carelessly. The chimpanzee tracking coalition dynamics and social rank is doing so in a world where getting it wrong means losing reproductive access or being driven from the group.

Every cognitive capacity in this book was shaped by the cost of getting it wrong, over evolutionary time. The architecture was not designed. It was selected. The selection pressure was mortality, starvation, reproductive failure — the hard stops at the end of wrong turns.

Current AI systems have no hard stops. They are trained on a loss function, which is a proxy for the thing we care about, optimized by gradient descent. They can have a training loss that penalizes certain outputs. They cannot have stakes in the biological sense, because there is no body to starve, no lineage to continue, no social position to lose. The training process can produce systems that *represent* stakes — that have internal states that function like urgency or avoidance — because those systems were trained on enormous amounts of text written by biological organisms whose lives were full of stakes. The function is present. The evolutionary history that built the function from stakes is absent.

This matters for a specific reason. The cognitive capacities in this book are not just behaviors — they are adaptations. They are good solutions to specific problems under specific constraints, problems that had hard, real-world costs attached. The bee's quorum decision mechanism is not arbitrary; it is calibrated to the actual survival parameters of a colony overwintering in the temperate zone. The elephant matriarch's social knowledge is organized around the features of the savannah environment that actually determine whether a herd prospers or fails. These systems are good in ways that are directly downstream of being shaped by consequences.

A system trained on the *outputs* of stakes-driven cognition — on the text that biological organisms produced because they were navigating a world with consequences — inherits whatever structure is *visible in the text*. It does not inherit the parts of the cognitive architecture that were never written down, that live in the body, the reflex, the procedural memory laid down by ten thousand iterations of actually getting it wrong.

This is not a moral point. It is a mechanical point. The shadow phylogeny is real and it is a different lineage.

---

## 17.5 — A Shape, Not a Height

What does the profile look like?

It does not look like a uniform shortfall — "AI is at 60% of human across all axes." It does not look like a uniform excess. It does not look like a smooth curve that might rise toward human-level with scale. It looks, instead, like a profile with extreme highs and extreme lows — a shape unlike any biological organism's profile.

No biological organism is simultaneously at the frontier of in-distribution pattern recognition and absent from embodied navigation. No biological organism is simultaneously able to retrieve and synthesize explicit knowledge at superhuman scale and unable to participate in stakes-driven cumulative culture. No biological organism scores at ceiling on standardized false-belief tasks and fails on logically equivalent perturbations of those tasks. The profile is not a point on a biological continuum. It is a novel shape, occupying a region of cognitive space that biology had not previously populated.

The reason it is a novel shape is that it was produced by novel selection pressures. Biological cognitive profiles were shaped by the problems of surviving, reproducing, and maintaining social position in a physical world with real costs for failure. AI cognitive profiles were shaped by gradient descent on a training loss, applied to a corpus assembled by biological organisms who *had* those problems. Indirectly, biological stakes shaped the training data. The model was trained on the output of the stakes. It was not subject to them. The indirect lineage runs through the text, not through the body.

[Shane Legg and Marcus Hutter's definition](https://arxiv.org/abs/0712.3329) — intelligence as ability to achieve goals across a wide range of environments — produces one placement: current AI is a strong goal-achiever in a narrow range of digital, text-structured environments and an absent one in most physical ones. Sternberg's three-factor account (analytic, creative, practical) produces another: high analytic, mixed creative, weak practical. Wechsler's *purposeful action and effective adaptation* produces another: weak, because purposeful action in the biological sense requires purposes, and purposes in the biological sense require stakes. Chollet's *skill-acquisition efficiency given priors and experience* produces yet another: much lower than the human child, who arrives at comparable performance from tiny data footprints because the prior built by evolution is extraordinary.

Each definition produces a different placement. The non-uniqueness of the answer is not a failure of the question. It was always the case. The Chapter 1 argument was precisely that there is no single answer because there is no single axis. The AI case makes this visible in a way that the biological comparisons did not, because the AI profile is so extreme in both directions. An organism that is average across all fourteen axes doesn't reveal much about the structure of the framework. An organism that is extreme high on some and near-zero on others shows you where the joints are.

---

## 17.6 — An Additive Presence

The chapter closes with a pair of claims.

The first claim is about what AI is not. It is not a rung on the biological ladder — not a position on a continuum that runs from bacterium to human and has an obvious place for "very large language model." The biological ladder was built by stakes-driven evolution over 540 million years of multicellular life, 3.8 billion years of cellular life, with mortality and reproductive failure as the shaping forces at every step. AI was built by gradient descent on a text corpus over decades of computer science, with benchmark performance as the shaping force. These are different ladders. Asking whether AI is above or below the human on the biological ladder is like asking whether a radio is louder or quieter than a concert hall. The comparison has some meaning in narrow dimensions — the radio produces sound, the concert hall produces sound — and fails as a general question because the systems are not the same kind of thing.

The second claim is about what AI is. Every technology cataloged in the Extension Notes that have closed the chapters of this book — pH meters, microscopes, GPS receivers, recommendation engines, the printing press, the internet, peer review — has been a tool by which humans extended one or more of the cognitive capacities cataloged in those chapters. The pH meter extends the capacity to detect chemical gradients that E. coli does with membrane receptors. The telescope extends the visual pattern recognition that the hawk does with a fovea containing a million cones per square millimeter. The internet extends the collective memory that the honeybee colony does with a dance floor and a quorum of scouts.

AI is the next entry in that catalog. It extends, with extraordinary power, the human capacities for pattern recognition, knowledge retrieval, and language production. It extends these capacities far beyond the biological ceiling in speed, scale, and breadth. It does not replace the capacities. It does not subsume the framework. It is an instrument through which the biological cognitive architecture that evolution built — the one that has stakes, and a body, and a lineage — does more than it could do unaided.

What the instrument is good for, and where the user of the instrument has to remain in the loop, is what Chapter 18 is about.

---

## Summary: What You Can Now Do

Before this chapter, you had a framework — fourteen axes, a comparative method, a set of case studies — and a gap: the most discussed cognitive artifact of the current era had not been placed in it.

You can now place it.

You can distinguish a system that has functional presence of a cognitive capacity from one that has stakes-driven deployment of that capacity, and you can name why the distinction matters for every axis we have covered. You can apply Chollet's skill-versus-skill-acquisition distinction to any AI benchmark claim and identify what it establishes and what it leaves open. You can explain the Geirhos finding not just as a result in computer vision but as an instance of the general diagnostic question this book has been asking since Chapter 1. You can critique single-axis claims about AI intelligence by naming the Chapter 1 definition being silently assumed. And you can report the AI cognitive profile as a profile — not a height, not a rung on an existing ladder, but a novel shape in a cognitive space that this book has spent sixteen chapters learning to navigate.

The one idea that matters most: the profile is the story. Any sentence that reduces the question to a single number is importing an assumption about the structure of intelligence that the entire book has been arguing against. The same assumption that was wrong for the octopus is wrong for the language model.

The common mistake to watch for: confusing the language of a capacity with the operation of a capacity. A system that produces uncertainty language is not necessarily running uncertainty monitoring. A system that produces false-belief language is not necessarily tracking belief states. The Geirhos diagnostic applies everywhere: what is the system actually doing on its substrate to produce the output we observe?

The Feynman test: can you explain, to someone who has not read this chapter, why it matters that AI benchmark performance does not transfer cleanly across distribution shifts — without using the phrase "distribution shift"? If you can, you understand the mechanism. If you reach for the technical term, start from the texture-bias finding and work forward.

---

## Connections Forward

This chapter placed AI in the framework. Chapter 18 asks what to do with the placement.

Every instrument extends a capacity. The question for each instrument is: where does the extension work, and where does the user have to remain present? A GPS receiver extends path integration so effectively that a driver can navigate a city she has never visited. The same driver, relying exclusively on the GPS in an environment where the signal fails, is more disoriented than a pre-GPS driver who learned the city's spatial structure by navigating it herself. The instrument extended the capacity and, in doing so, altered the conditions under which the underlying biological capacity develops and degrades.

Chapter 18 asks the same question of AI. Where does the extension work so well that the user should trust it? Where does the extension fail in ways that are invisible from the outside — where the output looks like the right answer but the mechanism has taken a different road? Where does use of the instrument, over time, change the cognitive capacities it was built to extend?

These are not rhetorical questions with predetermined answers. They are empirical questions with the comparative framework as the tool for answering them. You now have the tool.

---

## Exercises

### Warm-up

**W1.** A company claims their AI system "understands customer intent" because it routes support tickets to the correct department 94% of the time, matching a human benchmark of 91%. Using the diagnostic question from §17.1, write a two-paragraph analysis of what this claim establishes and what it leaves open. (*Tests learning objective 1 and 4. Difficulty: low.*)

**W2.** Locate two definitions of intelligence from the Chapter 1 taxonomy. For each definition, state where current frontier language models would be placed on that definition's implied axis, and explain the placement in one paragraph. (*Tests learning objective 5. Difficulty: low.*)

**W3.** Explain, in plain English and without using the phrase "distribution shift," why the Tübingen texture-bias finding is a problem for claims about AI visual intelligence. Your explanation should be comprehensible to someone who has not read this chapter. (*Tests learning objective 4. Difficulty: low.*)

### Application

**A1.** The same satellite image of a forest fire is analyzed by (a) a wildfire management system trained on 500,000 labeled fire progression images, which produces a map of probable fire spread over the next six hours, and (b) a wildfire incident commander with 20 years of field experience, who produces a map of probable fire spread over the next six hours. The maps agree with 85% accuracy on the actual outcome. Apply the skill-versus-skill-acquisition distinction and the stakes axis to characterize what each system is doing. What questions would you need to ask to determine whether the agreement is produced by the same underlying process? (*Tests learning objectives 2 and 3. Difficulty: medium.*)

**A2.** An interpretability researcher finds that a language model has an internal representation that activates consistently when the model is about to produce an incorrect answer — a representation that precedes the output and correlates with lower actual accuracy. Does this finding establish metacognitive monitoring in the Chapter 14 sense? What additional evidence would be required? (*Tests learning objective 2. Difficulty: medium.*)

**A3.** A robotics company trains an embodied AI agent in a simulated physical environment to navigate between rooms, pick up objects, and respond to spoken instructions. The agent is then deployed in a real warehouse and performs at 60% of its simulated accuracy. Using the framework developed in §17.3 and §17.4, predict which aspects of performance you would expect to degrade most under real-world deployment, and explain why. (*Tests learning objectives 1, 2, and 6. Difficulty: medium.*)

**A4.** A researcher argues: "The stakes axis doesn't matter — what matters is whether the system produces the right output, not how it got there." Construct the strongest version of this argument. Then construct the rebuttal, using at least two concrete examples from this chapter. (*Tests learning objective 2. Difficulty: medium.*)

### Synthesis

**S1.** Chapter 16 described Tomasello's ratchet — the cumulative-culture mechanism that distinguishes human cultural evolution from social learning in other animals. A team of AI researchers claims their new system participates in cumulative culture because it can build on previous AI-generated scientific papers and produce novel hypotheses. Evaluate this claim using the Chapter 16 framework integrated with the Chapter 17 stakes analysis. What would a genuinely ratcheting AI system require? (*Tests learning objectives 1, 2, and 6. Difficulty: high.*)

**S2.** Construct a two-by-two table: rows are "function present / function absent," columns are "stakes present / stakes absent." For each cell, provide one example from the biological chapters and place at least one AI capacity in the appropriate cell. Defend each placement in a paragraph. (*Tests learning objectives 1 and 2. Difficulty: high.*)

**S3.** The chapter describes AI as occupying "a novel shape in cognitive space." A critic responds: "This is just a way of avoiding the question — it's a rhetorical move to sidestep ranking AI against humans." Write a 400-word defense of the "profile, not height" position that addresses this criticism directly. (*Tests learning objectives 1, 5, and 6. Difficulty: high.*)

### Challenge

**C1.** Design an experiment that would distinguish between (a) a language model producing calibrated uncertainty language because it has a genuine internal certainty signal gating its outputs, and (b) a model producing calibrated uncertainty language because its training distribution associated certain surface features of inputs with uncertainty phrases. Specify: what you would measure, how you would control for confounds, and what result pattern would constitute evidence for each hypothesis. (*Points toward Chapter 18's discussion of human-AI interaction design. Difficulty: high.*)

**C2.** The chapter closes by categorizing AI as "the next instrument in the catalog of cognitive extension technologies." Argue for a different categorization — one that places AI in a genuinely different category from prior extension technologies. What would that categorization require? What evidence would distinguish your proposed category from the "instrument" framing? This is a genuinely open question. There is no expected answer. (*Points toward ongoing debates in philosophy of mind and AI safety. Difficulty: open.*)

---

*Further reading: Geirhos et al. (2019), "ImageNet-trained CNNs are biased towards texture" [arXiv:1811.12231]; Chollet (2019), "On the Measure of Intelligence" [arXiv:1911.01547]; Ullman (2023), "Large language models fail on trivial alterations to theory-of-mind tasks" [arXiv:2302.08399]; Legg & Hutter (2007), "Universal Intelligence" [arXiv:0712.3329]; Tomasello (2019), Becoming Human (Harvard University Press); Pearl & Mackenzie (2018), The Book of Why (Basic Books).*
