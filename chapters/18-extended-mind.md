# Chapter 18: The Extended Mind Arrives
## When the Catalog Closes on Itself

---

### Learning Objectives

By the end of this chapter, you should be able to:

1. **Explain** the Clark-Chalmers extended mind thesis and distinguish the constitutive from the instrumentalist reading, without requiring either to support the chapter's central claim
2. **Apply** the capacity/direction distinction to analyze any cognitive technology — biological, mechanical, or algorithmic — and identify what the human user must supply that the tool cannot
3. **Trace** the catalog of extension technologies across the book's seventeen chapters and identify the structural pattern common to every entry
4. **Evaluate** where AI sits in this catalog relative to prior tools, including where it extends further and where the directing requirement is correspondingly more demanding
5. **Articulate** the relationship between Pearl's ladder of causation (Rungs 1, 2, 3) and the formalizable/non-formalizable boundary in human cognition

**Prerequisites:** Chapter 17's placement of AI on the cognitive ladder; Chapters 2–16's Extension Notes, which this chapter synthesizes; Chapter 1's account of why intelligence resists singular definition.

**Where this fits:** This is the book's penultimate chapter. It is where the leitmotif carried quietly through every Extension Note becomes the explicit argument. Chapter 19 names the implication.

---

### Chapter Opening: The Notebook and the Nose

On a winter morning in 1994, Andy Clark and David Chalmers were thinking about a man named Otto.

Otto has Alzheimer's disease in its early stages. His biological memory is unreliable. But Otto is a functioning person with a social life and a job and places to be. He manages this by carrying a notebook. When he learns something worth keeping, he writes it in. When he needs it back, he opens the notebook and reads. The notebook has been his companion for years. He trusts it. He panics when he misplaces it. He would be far less Otto without it.

Clark and Chalmers asked: in what meaningful sense is that notebook *not* part of Otto's mind?

It is doing exactly what Inga's hippocampus does for Inga — encoding information, retaining it, making it available on demand. The only difference is that Otto's storage medium is paper rather than synaptic protein. If we call Inga's memory *her memory*, they argued, we should call Otto's notebook *his memory*. The mind is not the skull. The mind is the functional system, wherever it runs.

That paper was cited forty thousand times. The argument is still running.

I want to hold that argument beside a very different image, because the book needs both.

Somewhere on the outskirts of a military checkpoint, a dog named Rex is working. Rex has roughly three hundred million olfactory receptors in his nose — compared to about six million in his handler's. Rex can detect parts-per-trillion of explosive precursors that are simply not available to any human sensory system, by any act of will or training. When Rex sits, his handler stops.

The dog-handler unit is a cognitive system in something close to the Clark-Chalmers sense: Rex supplies a sensory capacity the handler does not have, the handler supplies the goal-structure that deploys Rex's capacity. Rex does not have the goal of *finding bombs*. Rex has the goal of finding the smell that produces the reward. The *finding bombs* goal lives in the handler's mind, and nowhere else in the system.

These two images — Otto's notebook and Rex's nose — together give us the chapter's problem. The extended mind thesis is correct about something important: the functional boundary of cognition has never been the skull. But correct about something else, equally important, is that every extension in that catalog — every notebook, every dog, every instrument, every algorithm — has required a directing layer that the extension itself could not provide.

This chapter is where we name that directing layer, trace it through everything the book has built, and ask what it means that the newest entry in the catalog is the most powerful tool we have ever made.

---

## 18.1 Three Specifications Before Walking

Three distinctions are needed before the catalog can be walked honestly.

**The constitutive versus instrumentalist dispute.** Clark and Chalmers argued that Otto's notebook *constitutes* part of his cognitive system. Critics — Fred Adams, Ken Aizawa, Rob Rupert — argued that coupling a process to cognition is not the same as the process being cognitive. Otto is coupled to his notebook the way a calculator is coupled to an accountant's hand, but we do not say the calculator is thinking. The chapter does not need to settle this. The structural claim here is weaker and more durable: *whichever reading is right*, every extension technology in human history has required a directing substrate that the technology itself does not provide. If you are a constitutivst, the directing substrate is part of an extended mind. If you are an instrumentalist, the directing substrate is the mind, full stop, and the technology is a very good instrument. Either way, the agency lives somewhere specific, and it is not in the notebook.

**The additive versus substitutive question.** An additive technology increases the functional reach of a capacity without removing the underlying capacity. Writing extended the memory range of the individual brain without replacing the brain's ability to remember. The printing press extended writing's reach without eliminating handwriting. The internet extended print's reach without eliminating books. The biological substrate and the technological extension coexist; the organism is more capable, not replaced. A substitutive technology removes the biological capacity it extends. GPS following has been shown to reduce hippocampal engagement in navigation tasks. Whether it also reduces hippocampal capacity over time — whether navigation skill atrophies when GPS is always available — is the question the research is still working out. The chapter's position: the historical pattern at the system level has been overwhelmingly additive. Substitution happens at margins. It does not define the catalog.

**Capacity versus direction.** This is the deepest distinction, and it is the chapter's central move. Every cognitive technology extends a specific *capacity* — perception, memory, calculation, communication, prediction, generation. Every cognitive technology requires a specific *directing* effort from the user — what to point the capacity at, how to interpret what comes back, when to trust the result, when not to, and who is responsible when the result is wrong. The capacities that get offloaded are the ones that can be specified precisely enough to delegate. The directing capacities are the ones that cannot — not yet, and perhaps not ever in the same way. The line between them moves. But the line persists.

Judea Pearl's three-rung ladder of causation, introduced in Chapter 1 and traced across the biological tree in Chapter 17, maps cleanly onto this distinction. Capacity extension has lived almost entirely at Rung 1 — the association rung, the rung of statistical regularity, of prediction from correlations in the training distribution. Direction has lived at Rungs 2 and 3 — the intervention rung (changing the world and observing what happens) and the counterfactual rung (imagining what would have happened differently). Each formalization the field has accomplished has been a Rung 1 task, now handled by a tool. The Rung 2 and Rung 3 work — problem formulation, causal reasoning beyond the training distribution, the audit of one's own uncertainty — has stayed with the human. Because we do not yet know how to formalize it.

---

## 18.2 The Catalog, Walked

This book has closed every chapter with an Extension Note: a brief account of a tool that extends the cognitive capacity the chapter examined. Collected and laid side by side, those notes form a single argument. Let me walk it.

**Chapter 2 — Valence detection.** The bacterium reads chemical gradients with surface receptors refined over three billion years of selection. The chemist reads them with a pH meter. Capacity extended: *gradient sensing*. Directing capacity required: deciding what gradient to measure, in what medium, at what time, for what purpose. The pH meter does not know to be deployed. It does not know whether the measurement means what the researcher thinks it means.

**Chapter 3 — Steering.** The nematode runs goal-directed navigation with labeled-line sensors and a small set of behavioral switches. The Roomba runs goal-directed navigation with bump sensors and a finite-state controller. The subsumption architecture that Brooks described — the world as its own best model, reactive control layered into behavioral modes — is the worm's architecture in silicone. Capacity extended: *steering toward valued states and away from disvalued ones*. Directing capacity required: *defining what counts as a valued state*. The homeowner defines the floor as the relevant region. The Roomba does not.

**Chapter 4 — Memory.** Writing is how humanity solved the catastrophic-forgetting problem that plagues gradient-descent learning systems. We build an external storage medium that does not interfere with the biological memory it supplements. Capacity extended: *long-term storage and retrieval of information across time*. Directing capacity required: deciding what to record, what to retrieve, and what the retrieved entry means in the context doing the retrieving. A library of ten million volumes does not know which paper answers the question you brought to it this morning.

**Chapter 5 — Affect.** Sentiment analysis classifiers, facial expression recognition systems, biometric affect detectors — all attempt to read the emotional valence of text, face, or physiological signal. Capacity extended: *categorizing emotional content at scale*. Directing capacity required: deciding when sentiment matters, what to do when it is detected, whether the categorization scheme is appropriate to the specific context. A classifier does not know whether it is reading a sincere apology or sarcasm. Lisa Feldman Barrett's critique of basic emotion theory applies directly: there is no one-to-one mapping between the signal and the state, and a system that assumes there is will fail in precisely the cases that matter most.

**Chapter 6 — Pattern recognition.** The microscope, the telescope, the medical-imaging AI, the spectroscope — all extend perceptual resolution beyond the limit of the unaided eye or the unaided time budget. Capacity extended: *detection of patterns at scales, speeds, or wavelengths unavailable to unaugmented biology*. Directing capacity required: the structured knowledge that distinguishes signal from artifact, anomaly from noise, finding from confound. A novice at the microscope sees a smear. An expert sees a meiotic spindle in the same visual field. The artifact is in the same position on the slide. The tool provides the resolution. It does not provide the knowledge that makes the resolution mean something.

**Chapter 7 — Navigation and spatial intelligence.** GPS tells you where you are on the earth's surface within a few meters. Rex tells his handler where explosive precursors are in the air within a few meters. Capacity extended: *spatial and olfactory localization beyond unaided biology*. Directing capacity required: goal-setting and threat assessment. GPS tells you where you are; it does not tell you whether you should go where you are going. Rex signals that the smell is present; he does not assess whether the smell indicates a threat, a false alarm, or a training artifact. Both tools have produced the same class of failure: the GPS-led truck driving into a lake; the dog trained to signal on the handler's own cue rather than on explosives. The directing layer was absent or compromised, and the capacity ran without direction.

**Chapter 8 — Prediction and reinforcement.** Recommendation engines, trading algorithms, reinforcement learning systems — all extend the capacity to predict reward-contingent outcomes at scales no individual human could process. Capacity extended: *reward-prediction at scale across large state spaces*. Directing capacity required: *specifying the reward correctly*. Goodhart's Law, named after the British economist who formalized it: when a measure becomes a target, it ceases to be a good measure. A recommendation engine optimizing for engagement produces an outrage feed. The engagement metric was specified. The outrage was the consequence. No human chose for the engine to produce outrage. The engine did precisely what it was told to do, and what it was told to do was insufficient.

**Chapter 9 — Simulation.** Apollo 13's digital twin, trained on the mission's exact systems, allowed engineers in Houston to run scenarios they could not run on the spacecraft itself. Modern simulation software allows engineers to test designs against physics before building anything. Capacity extended: *running the world forward under specified conditions without physically instantiating those conditions*. Directing capacity required: *choosing which conditions to simulate, and trusting that the simulation captures the relevant features of reality*. A simulator that does not include the failure mode you are approaching cannot warn you about it. The simulation's usefulness is bounded by the imagination of the people who specified it.

**Chapter 10 — Social intelligence.** Social network platforms, organizational charts, CRM systems — all extend the capacity to track and manage relationships at a scale beyond Dunbar's number, beyond what any unaided primate brain can hold. Capacity extended: *relationship tracking at population scale*. Directing capacity required: *deciding which relationships matter, and what to do with what you know*. The graph of the organization does not tell you who to trust. The platform that mapped two billion people's social graphs did not tell anyone what to do with the map.

**Chapter 11 — Theory of mind.** A/B testing, user research, behavioral economics instruments — all attempt to do theory of mind at population scale: model what users want, what they will click, what they will do in response to which interventions. Capacity extended: *modeling the mental states of others at scales beyond individual observation*. Directing capacity required: *deciding what to optimize for, and bearing responsibility for the consequences when the population behaves the way you incentivized it to behave*. Cambridge Analytica had the tool. Cambridge Analytica lacked — or declined to apply — the directing layer.

**Chapter 12 — Creativity.** CAD software, generative image systems, large language models in their capacity as text generators — all extend the capacity to produce artifacts that meet specified constraints. Capacity extended: *generating novel artifacts within a specification*. Directing capacity required: *deciding which constraints, evaluating whether the generated artifact actually meets them, and judging whether the artifact is useful for purposes the specification did not anticipate*. A generative system that produces fluent text does not know whether the text is true, relevant, appropriate, or harmful. The human specifying the prompt is providing a directing layer. The quality of the output is bounded by the quality of the direction.

**Chapter 13 — Self-awareness.** Mirrors, cameras, biofeedback systems — all extend self-perception by providing a third-person view of the self that the first-person view cannot supply. Capacity extended: *self-observation from a perspective other than one's own*. Directing capacity required: *deciding what to make of what you see*. The mirror presents. It does not interpret. It does not tell you whether the thing you see is something to change.

**Chapter 14 — Metacognition.** Confidence intervals, error bars, prediction markets, replication protocols — all extend the capacity for calibrated uncertainty monitoring beyond the individual researcher's unaided introspection. Capacity extended: *making one researcher's uncertainty legible to others and to herself*. Directing capacity required: *deciding which questions are worth being uncertain about, and acting on the calibration with intellectual honesty*. A confidence interval does not absolve the researcher of the obligation to be honest about her doubts. A 95% confidence interval does not prevent its construction around a cherry-picked result.

**Chapter 15 — Language.** Writing, the printing press, the internet — the same capacity (linguistic transmission across time and space) at three step changes of fidelity and reach. With each step change, the directing capacity required remained unchanged in form even as it became more demanding in practice: *deciding what to say, knowing whether the receiver understood, taking responsibility for the consequences of being heard*. The printing press made it possible to spread heresy across a continent. It made it possible to spread the Reformation. The capacity is the same in both cases. The direction is what differed.

**Chapter 16 — Collective intelligence.** Institutions, protocols, peer review, open-source version control — all raise the fidelity of knowledge transmission across communities and generations, clicking the cumulative-culture ratchet that Tomasello and Henrich identified as the distinctive human capacity. Capacity extended: *preserving and building on knowledge across individuals and time*. Directing capacity required: *the practice that the record alone cannot transmit*. The paper captures the result. The apprenticeship transmits the tacit knowledge of how to produce results worth capturing. No institution has yet automated the tacit layer.

Now the pattern.

Walk that catalog. The technologies in it span three billion years of biology and three thousand years of human artifact-making. They include organisms (bacteria, dogs, bees), hand-held instruments (pH meters, microscopes, mirrors), paper-based notation systems (writing, printing), electromechanical devices (GPS, MRI scanners), and vast informational systems (the internet, recommendation engines, simulation software).

What is conserved is not the technology. What is conserved is the *shape* of each entry: a specific capacity offloaded to a substrate that does it better than unaided biology; a specific directing effort retained by the human deploying the substrate; and the consistent observation that when the directing effort is insufficient, the extended capacity produces unintended consequences. The capacity runs. But without direction, it runs in the wrong direction, or into a lake, or toward outrage, or into the service of a regime's political ends.

[FIGURE: The catalog as a two-column table. Left column: the extension technology and the capacity it extends. Right column: the directing capacity required that the technology does not supply. Each row is one chapter's Extension Note entry. Students should notice: (1) that the right column items do not get smaller as the tools get more powerful — if anything they get larger; (2) that every right-column item involves some combination of goal-setting, plausibility-auditing, causal reasoning, and accountability; (3) that the right-column items map onto Pearl's Rungs 2 and 3 while the left-column items map onto Rung 1.]

---

## 18.3 The Newest Entry

Where does AI go in this catalog?

It goes on the shelf with the others. It is the most powerful single entry — extending pattern recognition, prediction, and generation at a scale and across a breadth of domains that no prior tool has approached. A large language model trained on the collective written output of human civilization has compressed, into a set of parameters, a Rung 1 representation of a staggering fraction of what humanity has said, classified, described, and reasoned about. The capacity this represents is real. It is not adequately described by dismissing it as "stochastic parrots" or "autocomplete." Something genuinely novel is happening when a system produces, in response to a well-specified prompt, an output that is useful to an expert asking a question the expert already knows the answer to. That kind of output requires more than memorization; it requires the Rung 1 analog of reasoning, which is pattern interpolation in a rich semantic space.

What it does not require, and what current AI systems do not have, is what the right-hand column of the catalog has always required.

Problem formulation is a Rung 2 act. You have to intervene on your own knowledge state — to ask, *what is it that I actually need to know here, as distinct from what I initially thought I needed to know?* — and that question cannot be answered by interpolation in the training distribution. The training distribution reflects questions that have already been formulated. The question worth asking next is not in it.

Plausibility auditing is a Rung 3 act. You have to construct a counterfactual: *if this output were wrong, what would I expect to see, and do I see it?* A language model cannot do this for its own outputs in any systematic way, because the counterfactual requires an accurate model of the model's own failure modes — a metacognitive structure that current systems do not have and that cannot be built from the training data alone.

Causal reasoning beyond the training distribution is the open Rung 3 problem that Chapter 17 traced through the comparative cognition literature — the capacity that appears in fragments in great apes and corvids and cetaceans, the capacity that the book has been building toward since Chapter 14. Current AI systems are in the same position as a system trained on extensive observational data about billiard balls: they can predict where the balls will go under conditions similar to the training set. They cannot reason about what would happen if you introduced a new ball, changed the table's incline, or asked why the balls move at all.

Accountability is the structure that exists *because* an agent has stakes. Stakes are what make direction non-optional: if you are wrong and you bear the consequences, you have an incentive to be right that purely predictive systems do not share. Current AI systems do not have stakes. They do not have careers that end, relationships that suffer, or physical bodies that bear consequences. The accountability relationship — the structure in which the human asking the question is the one who lives with the answer — has not been transferred to the tool. It is an open philosophical and legal question whether it could be, or whether accountability is constitutively the kind of thing that requires a subject of experience to bear it.

These are not technical limitations waiting for the next generation of models to solve. They may be technical limitations waiting for a very different architecture to solve. Or they may be limitations that are *structural* — that arise from the fact that the directing layer is what it is, and that any system that could provide it would not be providing it in the way that a tool provides a capacity, but in the way that an agent exercises judgment. The distinction between tool and agent is the distinction Chapter 17 built the entire comparative analysis toward. We do not yet have an artificial agent in that sense. We have extraordinary tools.

---

## 18.4 The Asymmetry Beneath the Pattern

There is something deeper in the catalog's right-hand column that I want to name explicitly, because it connects the book's first chapter to its last.

Every entry in the right-hand column involves something that the biological literature associates with high rungs of Pearl's ladder. Problem formulation requires knowing what you do not know — a metacognitive act. Plausibility auditing requires imagining counterfactuals — a Rung 3 act. Causal reasoning requires modeling interventions — a Rung 2 act. Accountability requires having stakes — a condition that requires embodiment, history, and continuity of self across time.

These are precisely the capacities the book has been tracing as they appear, unevenly and incompletely, across the animal kingdom. Theory of mind shows up in Chapter 11 in fragments, in apes and corvids, and becomes richer in primates. Metacognition appears in Chapter 14 in dolphins and great apes. Causal reasoning appears in Chapter 9 in mammals running virtual simulations of the near future. Language — the capacity that made cumulative culture possible — is Chapter 15, and Chapter 15 is careful to say that the full human language system involves not just the production of symbol strings but the ability to ask genuine questions, to build on what others have imagined, and to accumulate knowledge across generations.

The asymmetry is this: the capacities that have been extended by every tool in the catalog are the capacities that appear early in the phylogenetic tree — at low rungs of cognitive complexity, available in relatively simple nervous systems. Gradient sensing in bacteria. Steering in nematodes. Pattern recognition in fish. Even the capacities extended by the most powerful AI tools — prediction, generation, retrieval — are extensions of Rung 1 capacities that appear in their animal forms in Chapter 3 (temporal comparison in nematodes), Chapter 8 (temporal-difference learning in fish and early vertebrates), and Chapter 6 (pattern recognition in fish).

The capacities that have *never* been extended by any tool in the catalog — that have always remained on the right-hand side of the table — are the capacities that appear late in the phylogenetic tree: Rung 2 and Rung 3 reasoning, metacognitive monitoring, theory of mind, the accountability structure of an agent with stakes. These are the capacities whose neural substrates are documented in Chapters 11 through 16. They are the capacities that the New York Declaration treats as evidence of something worth moral consideration. They are also, not coincidentally, the capacities that no cognitive technology has yet replaced.

I do not think this is an accident. I think it reflects something real about the structure of the problem. The Rung 1 capacities are formalizable because they are, at base, statistical: they involve detecting patterns in data, interpolating across the training distribution, predicting what happens next given what has happened before. Formalization is what you do to statistical patterns. You find the algorithm, specify the objective function, and let the system optimize.

The Rung 2 and Rung 3 capacities are not statistical in the same way. They involve, as Pearl has argued for three decades, something *more* than fitting data: they involve representing the structure of causation, modeling what would happen if the world were different from how it is, and taking actions whose consequences you bear. These are the capacities that the biological tree spent five hundred million years building. They are expensive. They are fragile. They are also — and this is the book's final empirical claim — what the right-hand column of the catalog has always required.

---

## 18.5 Why the Question Mark Stays

Chapter 1 was titled "The Definition Problem." It opened with a simple observation: eight researchers, eight definitions of intelligence, no consensus. The chapter did not try to resolve the dispute. It proposed a working instrument — the ability to achieve goals across a wide range of environments — and used that instrument to take comparative measurements across fourteen capacities in organisms from bacteria to humans. The question mark in the book's title was a substantive thesis: *intelligence is not one thing accumulating across the tree of life. It is a family of distinct capacities, each with its own evolutionary history, each extendable by different tools, and none of them well described by any definition we currently have.*

Chapter 17 showed where AI sits in that family. It has extreme Rung 1 capacities. It has weak to absent Rung 2 and Rung 3 capacities. It does not have stakes, embodiment, a history of consequences, or participation in the cumulative-culture ratchet in the sense that produces genuine understanding rather than compressed recall.

This chapter has shown that AI's position in the family is not historically novel in its *shape*. Every other tool in the catalog has the same shape: strong on the capacity it extends, absent on the direction required to deploy that capacity responsibly. What is novel is the *breadth* and *power* of the capacity extended. The microscope extended one perceptual modality. The printing press extended one communication channel. GPS extended one navigational capacity. AI extends something much closer to *general-purpose Rung 1 reasoning* — not all of it, and not the parts that matter most, but more of it than any prior tool has extended.

This breadth makes the directing layer harder to maintain, not easier. The cases where AI output is most confidently wrong are precisely the Rung 2 and Rung 3 cases — the novel problems, the causal questions, the out-of-distribution situations, the cases where the training distribution provides no reliable guide. These are also the cases where the confident presentation of a Rung 1 answer is most misleading. The Roomba navigated into a corner. The GPS navigated into a lake. The LLM navigated into an authoritative-sounding confabulation. The failure mode scales with the capacity. The directing requirement scales with the capacity.

The question mark stays because intelligence is plural and the pluralism is not going away. The nematode's steering is real intelligence — real goal-directedness, real internal state, real cost-benefit computation under uncertainty. It is not a precursor to human intelligence. It is a solution to a different problem, shaped by three hundred and two neurons and five hundred million years of selection pressure in moist soil. The bee's functional emotion is real — a valenced internal state that biases cognition in ways the Anderson-Adolphs criteria can identify and the cognitive-bias paradigm can test. The crow's causal reasoning, the dolphin's metacognition, the chimpanzee's theory of mind — all real, all distinct, all sitting at specific rungs on a ladder that does not have a top rung marked *done*.

The human sits on that ladder too. The human's position is remarkable in two ways: the breadth of the capacities present, and the existence of the cumulative-culture ratchet that allows the products of individual cognition to survive individual lifetimes and compound across generations. But the human does not sit *off* the ladder, at some point where the ladder ceases to be relevant. The human sits *on* it, connected to the rungs below by every evolutionary continuity this book has traced.

AI sits on the catalog shelf, not on the ladder. It is a tool in the human tradition of extending Rung 1 capacities while requiring Rung 2 and Rung 3 direction. If a system ever appears that genuinely occupies a rung of its own — that formulates problems, audits its own outputs against counterfactuals it generates, calibrates its uncertainty against consequence, and bears accountability for its actions — then we will have a new entry on the ladder, not a new entry on the shelf. The book's framework has a place for that system. It would be the most important cognitive event since the evolution of language. It has not happened yet.

The question mark stays. Not because the questions are unanswerable. Because the answers are plural, and the plurality is what is true.

---

## Chapter Summary

**What you can do now that you could not before this chapter:**

The central skill this chapter adds is the ability to analyze any cognitive technology — from writing to GPS to a large language model — against the capacity/direction distinction and identify, precisely, what the human user must supply that the tool cannot. This analysis requires knowing the tool's capability profile (what it does well, where it fails), knowing the task's structure (which parts are Rung 1, which are Rung 2 or 3), and knowing who bears accountability for the result.

**The one idea that matters most:** The capacity/direction boundary is not a temporary artifact of immature technology. It tracks the boundary between what is formalizable (Rung 1: statistical, pattern-based, prediction from training distribution) and what is not-yet-formalizable (Rung 2 and 3: causal reasoning, problem formulation, plausibility auditing, accountability). Every tool in human history has extended a capacity on the left side of that boundary. Every tool in human history has required a directing contribution from the right side. AI is the most powerful tool yet, but it obeys the same shape.

**The common mistake to watch for:** Concluding from the power of a tool that the directing requirement has diminished. The evidence runs the opposite way: as capacity extends, the cases where the tool runs without direction become more consequential. The Roomba could not do much harm navigating into a corner. A trading algorithm running without direction cascaded the 2010 Flash Crash in twenty minutes. The directing requirement does not shrink as the tool grows. It migrates to a higher level and becomes simultaneously more important and harder to maintain.

**The Feynman test:** Can you take any one chapter's Extension Note from this book and specify, in two sentences, (a) what capacity the tool extends, and (b) what the human must supply that the tool cannot? If yes, you can apply the capacity/direction distinction. If not, reread §18.2 with one chapter's Extension Note open beside it.

---

## Exercises

**Warm-up: Direct Application**

1. Otto's notebook and Rex's nose are the chapter's opening images. Apply the capacity/direction distinction to each. For Otto's notebook: what is the capacity extended, and what does Otto supply that the notebook cannot? For Rex and his handler: what is the capacity extended, and what does the handler supply that Rex cannot? In what sense is Rex's case more complex than Otto's notebook case?

2. Goodhart's Law states that when a measure becomes a target, it ceases to be a good measure. Using the recommendation-engine example from §18.2, explain how Goodhart's Law is a specific instance of insufficient directing capacity. What would an adequate directing layer have needed to specify that the engagement metric failed to capture?

3. The chapter claims that the directing capacity in the catalog's right-hand column maps onto Pearl's Rungs 2 and 3. Select any three entries from the catalog in §18.2 and identify specifically which Rung 2 or Rung 3 activity the directing capacity involves. Are there any entries where the directing capacity involves only Rung 1? If so, what does that imply?

**Application: Translation**

4. A hospital deploys an AI system that flags potential cancer diagnoses in pathology images. The system performs at expert level on the validation set. Describe, using the capacity/direction framework, what the radiologist must supply that the AI cannot. Identify at least two specific failure modes that would arise if the directing layer were reduced or removed.

5. A writing assistant for students provides real-time suggestions, generates draft paragraphs on request, and checks for logical coherence in arguments. A university must decide whether to permit this tool in writing-intensive courses. Frame this debate using the capacity/direction distinction: what capacities does the tool extend? What directing capacities must the student supply? What would a course policy need to specify to ensure the directing layer is actually being exercised?

6. The chapter describes the printing press as extending the capacity for linguistic transmission while leaving the directing requirement unchanged in form but more demanding in practice. How did the Reformation illustrate this pattern? How did the 2016 election disinformation campaigns illustrate the same pattern at the next step change of scale? What does this comparison suggest about whether the directing requirement grows or shrinks as the capacity-extension tool becomes more powerful?

**Synthesis: Combining Concepts**

7. The catalog in §18.2 contains entries from across all seventeen chapters. Select three entries from very different chapters — ideally one from Part One (Chapters 2–4), one from Part Two (Chapters 5–9), and one from Part Three (Chapters 10–16). Show that all three have the same structural shape (capacity offloaded, direction retained) despite being radically different kinds of tools. What does this consistency suggest about the relationship between the structure of the catalog and the structure of the biological cognitive ladder the chapters trace?

8. Chapter 4 described associative learning as the first mechanism for changing what counts as good and bad based on experience. Chapter 8 described temporal-difference learning as the Rung 1 instantiation of prediction. Chapter 18 describes AI as extending Rung 1 capacities. Trace the line from *C. elegans* dopamine signaling (Chapter 3) through the TD-learning account of vertebrate dopamine (Chapter 8) to modern reinforcement learning systems. At each step, identify what is the same (the functional architecture) and what is different (the substrate, the scale, the degree of generalization). Where on this line does Goodhart's Law become a risk?

9. The chapter claims that accountability is "constitutively the kind of thing that requires a subject of experience to bear it." This is a philosophical claim with significant practical implications. Construct the strongest argument against this claim — the argument that accountability could, in principle, be transferred to an artificial system without requiring that system to have subjective experience. Then construct the strongest argument for the claim. Where does the disagreement ultimately turn?

**Challenge: Pushing Forward**

10. *(Open-ended)* The chapter ends with a description of what a system would need to have to cross the boundary from tool to agent: stakes, embodied causal reasoning, calibrated metacognition, and participation in the cumulative-culture ratchet. If such a system existed, where would it sit in the book's comparative framework? Would it be a new entry on the phylogenetic ladder — a genuinely new cognitive type — or would it be a very elaborate instantiation of capacities that already exist somewhere on the ladder? What would the appearance of such a system change about how we should think about the other entries on the ladder, including human cognition? This is the question Chapter 19 approaches. Begin developing your own position here.

---

## Connections Forward

Chapter 18 assembled the catalog. Chapter 19 names what the catalog implies.

**Chapter 19** (*The Extended Mind Returns*) takes the pattern identified here — capacity offloaded, direction retained, the question mark preserved — and asks what it means for practice: how we should educate people to exercise the directing function that no tool can replace; how we should design institutions that preserve the accountability structure that makes the directing function meaningful; and what we owe to the organisms on the biological ladder whose cognitive capacities we have been studying — and, in some cases, replacing.

The book ends where it began: with the question of what intelligence is. The answer the book has built toward is not a single number. It is a map of distinct capacities, distributed across the tree of life, each with its own evolutionary history, each extendable by different tools, and none of them well described by any definition that claims to capture them all at once. The question mark in the title is the thesis. The catalog is the evidence. The direction is what you supply.

---

*Every tool in this catalog extended a capacity. Every tool in this catalog required a direction. The capacity got broader. The direction got harder. The question mark got more important. This is the pattern. It has not yet stopped.*

---

**Chapter Notes and Primary Sources**

The Clark-Chalmers extended mind thesis appeared in *Analysis* in 1998, titled "The Extended Mind." The constitutive versus instrumentalist debate is most clearly laid out in Adams and Aizawa's 2001 paper "The Bounds of Cognition" in *Philosophical Psychology* and in Rupert's 2004 "Challenges to the Hypothesis of Extended Cognition" in *Journal of Philosophy*.

The Javadi-Spiers GPS and hippocampus study was published in *Nature Communications* in 2017. The Flash Crash market disruption on May 6, 2010 is documented in the joint SEC/CFTC report "Findings Regarding the Market Events of May 6, 2010," published September 2010.

Goodhart's Law was articulated by Charles Goodhart in a 1975 paper prepared for a Bank of England conference; the formulation most commonly cited ("When a measure becomes a target, it ceases to be a good measure") is Marilyn Strathern's paraphrase from 1997.

Pearl's three-rung ladder of causation — association, intervention, counterfactual — is developed in *The Book of Why* (Pearl and Mackenzie, 2018) and in the formal framework of *Causality* (Pearl, 2000). Its application to AI limitations is argued in Chapter 7 of *The Book of Why*.

Lisa Feldman Barrett's critique of basic emotion theory and its implications for AI affect-recognition systems appears in *How Emotions Are Made: The Secret Life of the Brain* (2017) and in her 2019 paper "Emotional Expressions Reconsidered: Challenges to Inferring Emotion from Human Facial Movements" in *Psychological Science in the Public Interest*.

The cumulative-culture ratchet is developed in Michael Tomasello's *The Cultural Origins of Human Cognition* (1999) and Joseph Henrich's *The Secret of Our Success* (2015). The relationship between cumulative culture and the extended mind thesis is explored in Kim Sterelny's *The Evolved Apprentice* (2012).
