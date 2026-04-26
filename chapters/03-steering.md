# Chapter 3: Steering
## The First Brain, and What It Was Built to Decide

---

### Learning Objectives

By the end of this chapter, you should be able to:

1. **Explain** what makes bilateral body symmetry a cognitive simplification, not just an anatomical one
2. **Describe** the run-and-pirouette navigation system in *C. elegans* and derive how it produces directed movement without a map
3. **Distinguish** between sensory processing, neuromodulation, and labeled-line encoding as three architecturally distinct components of a minimal intelligent system
4. **Apply** the six-component architecture of steering to evaluate whether a given system — biological or artificial — is capable of goal-directed behavior
5. **Critique** the claim that simple systems "just follow rules" using the food-copper trade-off as a test case

**Prerequisites:** Chapter 2's treatment of bacterial chemotaxis and the run-and-tumble mechanism. Familiarity with the concept of a concentration gradient.

**Where this fits:** Chapter 2 showed us the minimum conditions for *sensing and responding*. This chapter asks a harder question: what is the minimum architecture for *changing your mind*?

---

### Chapter Opening: The Petri Dish at 3 A.M.

It is a centimeter of soil. You cannot see it happening. Somewhere inside a circle of damp agar, a worm approximately one millimeter long — pale as glass, moving at speeds measured in fractions of a millimeter per second — is making a decision.

On one side of the dish: diacetyl, a buttery-smelling compound, the chemical fingerprint of the bacteria the worm eats. On the other side: nothing. Down the middle: a thin line of copper sulfate. Poison. Every cell in the worm's body that responds to copper is firing.

The worm approaches the copper line. It recoils. It tries again. Recoils again. Then — if it has not eaten in several hours — it crosses.

I want to stay with that moment. Not because it is spectacular, not because it rivals a chimpanzee solving a puzzle or a crow manufacturing a tool. But because it is the *smallest* version of something that matters enormously: a living thing re-weighting competing information according to an internal state it did not choose, arriving at a decision that could not have been predicted from either signal alone.

The bacterium of Chapter 2 cannot do this. A thermostat cannot do this. A smoke detector cannot do this. But a worm with three hundred and two neurons — a worm that has been described, synapse by synapse, in a 1986 paper that remains one of the most extraordinary documents in the history of biology — can.

This chapter is about what it takes to build that capacity from scratch.

---

## 3.1 The Body Plan as a Cognitive Move

Before there were neurons, there was architecture.

A radially symmetric animal — a hydra, a sea anemone — presents the same face to the world in every direction. Every part of its body is equally exposed. Any decision it makes about which way to move requires integrating information arriving from all sides simultaneously. The computational burden of *choosing a direction* is maximized.

Bilateral symmetry solves this problem by a stroke of architectural genius: it creates a front.

When an animal has a front, its sensors cluster there. The animal moves in the direction the sensors point. The decision problem transforms from *which of three hundred and sixty degrees?* to something much simpler: *keep going forward, or turn?* Forward and turn. That is the navigation problem a bilateral animal has to solve, and it is the navigation problem that the brain — in its first, simplest instantiation — was built to solve.

This simplification was apparently so profound that it appears to have happened only once in the history of life. All bilateral animals — every worm, insect, fish, frog, bird, and mammal alive today — are descended from a single ancestor that crossed this threshold approximately 570 million years ago. Every brain that has ever existed is the elaboration of a solution to a problem that was first posed in some anonymous Ediacaran mud: *front or not front*.

*C. elegans* sits as close to that original solution as anything still living. Its nervous system is organized around a nerve ring that encircles the throat, just behind the head. This is the worm's brain. It is not impressive by vertebrate standards — 302 neurons, 5,000 synapses, 500 gap junctions, the whole circuit mapped and named. But it does something the bacterial chemotaxis system of Chapter 2 cannot: it integrates *multiple, labeled, conflicting signals* and produces a *coherent directional decision* that can be *tuned by internal state*.

Each of those italicized pieces matters. Let me take them in order.

---

## 3.2 Labeled Lines: What It Means to Know What You're Sensing

Smell your coffee. Hear a car alarm. Feel heat from a radiator. You do not experience these as a single undifferentiated stimulus. You know, before you have time to think about it, that one of them is a smell and one is a sound and one is warmth. This is not a learned inference. It is hardwired into the architecture: separate sensors for separate stimulus categories, each connected to circuits that interpret the signal in light of its source.

Neuroscientists call this the *labeled-line principle*, and it is one of the oldest organizational features of nervous systems. *C. elegans* has it in its simplest form.

The neuron called ASE-right responds to chloride ions dissolved in water. The neuron called AWC responds to volatile attractants including diacetyl. AWB responds to volatile repellents. ASH is the worm's nociceptor — it fires for nose-touch, high osmolarity, and heavy metals like copper. AFD is a thermometer, calibrated to the worm's cultivation temperature.

Each label carries a default interpretation. When ASH fires, the worm reverses. When AWC senses attractant, the worm runs forward longer. The meaning of a stimulus is not computed de novo in some general-purpose processing region; it is embedded in the neuron that detected it.

This is the design tradeoff a 302-neuron animal makes. You cannot afford a general-purpose cortex that interprets signals flexibly based on context when you have fewer neurons than a silicon chip has transistors in 1970. What you can afford is a set of pre-labeled lines that carry their interpretation with them, connected to a small integration center that weights them against each other.

The integration center — the interneuron AIY, the most heavily connected node in the worm's connectome — receives inputs from multiple sensory lines simultaneously. Its job is not to *understand* the signals. Its job is to *aggregate* them into a decision about whether to keep running or initiate a turn.

Here is the first deep point of this chapter: **labeled lines with hardwired valences are not a limitation of simple nervous systems. They are a design principle that persists at every scale of neural complexity.** Your own brainstem runs on the same logic. Certain stimuli mean bad, via connections that were established before you were born. The labeled line is the cognitive atom.

---

## 3.3 The Run-and-Pirouette: How a Worm Navigates Without a Map

In 1999, Jonathan Pierce-Shimomura, Thomas Morse, and Shawn Lockery published one of the most clarifying papers in invertebrate neuroscience. They wanted to understand, mechanistically, how *C. elegans* climbs a chemical gradient. The answer turned out to be the bacterial trick from Chapter 2, run through bigger machinery.

Recall what the bacterium does. It alternates between running straight and tumbling to reorient. When concentration is rising — when it is heading toward food — it suppresses tumbles and runs longer. When concentration is falling, it tumbles more frequently, reorienting at random until it happens to point back toward the gradient. The result is a biased random walk that drifts uphill.

The worm does the same thing with different vocabulary. Instead of runs and tumbles, it has *runs* — relatively straight bouts with shallow steering corrections — and *pirouettes*: short bursts of tight turning that include reversals and omega bends, where the body folds into the shape of the Greek letter Ω. The pirouette is the worm's tumble.

The rule governing pirouette initiation is, again, the time-derivative of attractant concentration. When the worm is heading up the gradient — when dC/dt is positive — pirouettes are suppressed. When the worm is heading down the gradient — dC/dt negative — pirouettes fire. Each pirouette randomizes the heading, and over many pirouettes, the worm drifts toward the food.

So far this is just a bacterium with better hardware. What makes the worm interesting is what comes next.

**The worm has multiple attractants and repellents, and their signals arrive simultaneously at the same integration center.**

When the worm smells diacetyl *and* detects copper *at the same time*, both labeled lines are firing. AWC says *forward*. ASH says *reverse*. The interneuron AIY has to produce a single output. How does it weigh them?

The answer — and this is the answer that makes everything else in this chapter possible — is that the weighting is not fixed. It depends on internal state.

---

## 3.4 Neuromodulators: The Slow Broadcast That Rewrites the Rules

In 2000, Elizabeth Sawin, Rajesh Ranganathan, and Robert Horvitz published findings in *Neuron* that reframed how biologists thought about dopamine. Not the vertebrate version — the worm's version.

When *C. elegans* encounters a bacterial lawn — food — it slows down. This slowing is mediated by dopamine released from mechanosensory neurons that physically contact the bacteria. Without dopamine, the worm runs straight through excellent food without pausing. With dopamine, it dwells and eats. Dopamine, half a billion years before any vertebrate brain, is already the signal for *food is nearby; shift from searching to exploiting*.

The same paper showed something that is easy to miss on a first read. If the worm is food-deprived for several hours and then placed on food, the slowing response is dramatically enhanced. But the enhancer is not more dopamine. It is serotonin, released from pharyngeal neurons that signal satiety. A starved worm, returned to food, gets a larger serotonergic response than a fed worm. The serotonin translates into longer dwelling, slower locomotion, more eating.

Here is what is happening architecturally. Dopamine and serotonin are not fast neurotransmitters that carry specific signals along specific wires. They are broadcast molecules. They are released into the fluid surrounding the worm's neurons and diffuse broadly, binding to receptors on many neurons simultaneously and changing their properties. A neuromodulator does not transmit a message. It *changes the gain* on an entire circuit.

When serotonin is high — when the worm is starving and finally found food — the gain on the AWC attractive pathway increases. The gain on the ASH repellent pathway decreases. The balance tips. The same copper concentration that would turn away a well-fed worm becomes tolerable to a starved one.

**This is what it means to have a mood.** Not a feeling in the subjective sense — I am not claiming that. But a persistent internal state, encoded in the concentration of broadcast molecules rather than in fast synaptic activity, that changes how the nervous system weights information. The worm's mood is real in the only sense that matters for behavior: it changes what the worm does.

And it is, in its molecular particulars, recognizably the same machinery vertebrates use. The dopamine and serotonin systems in the human brain are elaborations of systems that were already doing essentially this job in animals without a cortex, without a spinal cord, without anything a neurologist would call a brain. They are not inventions of intelligence. They are its prerequisites.

---

## Concept Worked Example: The Trade-off Calculation

Let me make the food-copper trade-off concrete with a simplified model, because the intuition here is worth having precisely.

Imagine the worm's decision as a weighted sum:

$$\text{Decision} = w_{\text{food}} \cdot S_{\text{food}} - w_{\text{copper}} \cdot S_{\text{copper}}$$

If Decision > 0: continue forward. If Decision < 0: reverse.

$S_{\text{food}}$ is the AWC signal strength (how strong is the attractant). $S_{\text{copper}}$ is the ASH signal strength (how strong is the repellent). The weights $w_{\text{food}}$ and $w_{\text{copper}}$ are not fixed — they are modulated by the neuromodulator state.

In a well-fed worm, serotonin is low, and the weights reflect a moderate cost-benefit:

$$w_{\text{food}} = 0.4, \quad w_{\text{copper}} = 0.8$$

Strong copper wins. The worm retreats.

In a starved worm, serotonin rises and resets the weights:

$$w_{\text{food}} = 0.9, \quad w_{\text{copper}} = 0.4$$

Now the food signal, even at the same absolute strength, dominates. The worm crosses.

**Nothing changed in the environment. Nothing changed in the sensors. What changed is the weighting function — and the weighting function is the mood.**

This is not a metaphor for the worm's behavior. This is, at a coarse level of abstraction, what the neuromodulator data shows happening. The molecular details are more complex, but the logical structure is this: a slow-timescale internal variable re-weights the integration of fast-timescale sensory signals. That is what a neuromodulatory system does. That is what it is for.

---

## 3.5 Making Decisions Under Conflict: The HEN-1 Finding

In 2002, Toshihiro Ishihara and colleagues published a result that is, to my mind, one of the most philosophically pointed findings in invertebrate neuroscience. They identified a secreted protein called HEN-1, released by certain interneurons in *C. elegans*, that is required for the worm to weigh attractive odors against repellent chemicals correctly.

Without HEN-1, the worm can still smell diacetyl. It still approaches. It can still detect copper. It still recoils from it. What it cannot do is hold both signals simultaneously and produce a coherent trade-off. HEN-1 mutants wander into the copper. They retreat from food. They cannot integrate the conflict.

**The machinery for making decisions under conflict is separable from the sensors that feed it.**

This is a profound architectural observation. It means that sensing and deciding are not the same operation, even in a 302-neuron animal. You can have perfectly functional sensors and still be unable to trade them off against each other. And conversely — if you disable only the integration machinery, you lose the decision without losing the sensation.

This separability is one of the deepest features of nervous systems at every scale. In vertebrates, a massive literature on the prefrontal cortex and its interactions with the limbic system describes essentially the same division: emotional valence signals arrive from one region, integration and trade-off computation happen elsewhere, and damage to the integration region produces the exact dissociation Ishihara described in worms — sensation intact, decision impaired.

The worm showed us this first.

---

## 3.6 Temperature, Conditioning, and the Idea of a Preference

I want to add one more layer before assembling the full picture, because it is the most counterintuitive finding in *C. elegans* neurobiology and the most relevant for what this book is ultimately about.

In 1995, Ikue Mori and Yasumi Ohshima published a paper in *Nature* on thermotaxis — the worm's navigation of temperature gradients. The result was strange. When *C. elegans* is grown at a particular temperature *while eating*, and then placed on a thermal gradient, it migrates toward the temperature it was grown at. The thermosensory neuron AFD acts as if it has stored the cultivation temperature as a set-point.

Here is the strange part: if you deprive the worm of food during cultivation at that temperature, the migration disappears. Raise the worm at 20°C with no food, then place it on a gradient — and it no longer seeks 20°C. The thermal set-point did not form.

The temperature memory is *conditional on the food association*. The worm does not learn to want warmth in the abstract. It learns to want the temperature that, in its experience, meant food was available.

This is not just a memory. It is a *preference* — a behavioral disposition toward a value that depends on prior experience and is not reducible to the current sensory state. The worm has not encountered its cultivation temperature in the current trial. There is no current food signal. There is nothing in the present moment that justifies the migration. The worm seeks the temperature because it *remembers* that temperature as good.

The machinery for this associative memory is, at its molecular core, the same CREB-dependent long-term plasticity that Eric Kandel characterized in the sea slug *Aplysia* and for which he received the Nobel Prize in Physiology or Medicine in 2000. We will return to Kandel extensively in Chapter 4. For now, note the continuity: the same molecular pathway that lets a worm form a conditional temperature preference is the same pathway that lets a sea slug associate a neutral stimulus with a shock, which is the same pathway that underlies certain forms of long-term memory in vertebrates including humans.

The worm is not special. It is carrying ancient code.

---

## 3.7 The Six-Component Architecture

I want to now be explicit about what *C. elegans* has assembled — not to be exhaustive, but to give us a checklist we can carry through the rest of the book.

Goal-directed behavior, on the operational definition this book commits to, is the ability to achieve goals across a range of environments. *C. elegans* has a narrow range — a soil patch, a chemical gradient, a temperature plate. But within that range, it is unambiguously goal-directed. It pursues food when hungry, mates when it can, avoids poison when fed, accepts risk when starving. Its behavior cannot be predicted from sensory inputs alone. You need to know its internal state.

The architecture supporting this has six components, each necessary, none sufficient alone:

**1. A bilateral body plan** that simplifies the navigation problem from *which direction?* to *forward or turn?* This is a cognitive simplification achieved through anatomy, before any neuron fires.

**2. A labeled-line sensory array** in which each detector carries a default valence into the integration center. ASH means bad. AWC means good. The interpretation is structural, not computed.

**3. A temporal-comparison rule** — the dC/dt logic the bacterium also uses — that converts the current sensory moment into a direction-of-motion decision. Not where am I? but am I getting closer or farther?

**4. Mutual-inhibition circuits** between competing behavioral programs that produce coherent, all-or-nothing outputs rather than getting stuck in partial execution. The worm either runs or pirouettes; it does not do half of each.

**5. A neuromodulator layer** — at minimum dopamine and serotonin — that encodes internal state on a timescale slower than the neural activity itself. This is the layer that makes the worm's behavior state-dependent. It is the layer that makes the food-copper trade-off possible.

**6. Associative plasticity** — the ability to re-weight labeled lines based on outcomes — so that experience can update the valence of a stimulus. Temperature becomes good because food was there. Neutral becomes aversive because shock followed.

Take any one of these out and the worm degrades in a specific, predictable way. Remove the bilateral body plan and navigation becomes a computationally intractable omnidirectional problem. Disable the labeled lines and the worm cannot interpret its sensors. Eliminate neuromodulation and it becomes a reflex machine — same behavior regardless of internal state. Block associative plasticity and it cannot learn from experience.

This architecture is not unique to *C. elegans*. It is the template. Vertebrate nervous systems elaborate each component — more labeled lines, more complex integration, richer neuromodulatory systems, longer time windows for plasticity — but they do not add new categories. A fish has this architecture. A mammal has this architecture. The human prefrontal cortex is, at a level of appropriate abstraction, an enormously elaborated version of what AIY does in the worm.

[FIGURE: The six-component architecture of steering. A diagram showing the causal flow from bilateral body plan → labeled-line sensor array → temporal comparison rule → mutual inhibition → neuromodulator state layer → associative plasticity, with arrows showing how each feeds into the next and how internal state modulates the processing at multiple points. The student should notice that neuromodulator state is not a step in the processing chain but a context that affects the weights throughout.]

---

## 3.8 The Roomba Is Not a Worm

I want to be precise about something, because I think a confusion lurks here.

When Rodney Brooks proposed the subsumption architecture in 1986, he was reacting to decades of AI research that had tried to build robots by giving them internal world models — symbolic maps, formal reasoning over those maps, explicit planning. The robots had been mostly catastrophic. Brooks's response was to throw out the map and build control systems from stacked sensory-motor reflexes, each one simple, with higher layers able to suppress lower ones when their conditions were met.

The architecture he described is, at the level of behavioral organization, remarkably similar to the worm's. Obstacle avoidance as a base layer. Wandering as a layer above that. Exploration above that. Each layer handles its own sensing and acting. The world is its own best model.

The first commercially successful descendant of this idea was the Roomba, which since 2002 has cleaned tens of millions of rooms by doing exactly what *C. elegans* does in a petri dish: react to local stimuli, run a small number of behavioral states, persist in each until interrupted.

The Roomba is not, however, a worm. And the gap is not a matter of scale or sophistication. It is a matter of architecture.

The Roomba does not have a neuromodulator equivalent — no slow-timescale internal state that re-weights its sensory integration. When its bin is full, it stops and signals for help; it does not *change its behavior across the board* in response to internal depletion the way a hungry worm changes every aspect of its cost-benefit calculus. The Roomba does not form associative preferences. If it repeatedly fails to clean a certain corner, it does not learn to try harder there; it does not update the valence of that corner in any enduring way.

Most importantly: the Roomba has no trade-off resolution machinery. It does not cross the copper line. It cannot hold two conflicting signals simultaneously and decide, on the basis of internal state, which to honor. Its behaviors are mutually exclusive by design: it either cleans, or avoids, or docks. There is no HEN-1 equivalent that lets it weigh *clean this area* against *avoid this obstacle* according to how dirty it already is.

I say this not to dismiss Brooks — his work was correct and important, and the worm-shaped architecture he intuited is a genuine insight about how much intelligent-seeming behavior can be produced without a map. I say it because the gap between the Roomba and *C. elegans* is the gap between the second and fifth items on my six-component list. The worm has neuromodulatory state and associative plasticity. The Roomba does not. These are not implementation details. They are the difference between a system that *responds to stimuli* and a system that *makes decisions* in any sense of the phrase worth preserving.

---

## 3.9 What the Worm Cannot Do

It is also worth being careful — very careful — about the worm's limits.

*C. elegans* does not build a spatial map. It navigates gradients, not spaces. If you remove the gradient and put food at a fixed location, the worm cannot learn to go to that location from memory. It will find the food each time by running the temporal-comparison algorithm from scratch.

The worm's memory windows are short. Working comparisons run over seconds to minutes. The longest forms of associative learning — the temperature conditioning — operate over hours to a day. There is nothing in the worm's repertoire that resembles episodic memory, the capacity to remember a specific past event and use it to plan a specific future action. The worm does not plan.

The worm does not imitate. It cannot learn a behavior by watching another worm perform it. Imitation requires a model of another agent's intentions, and there is no evidence — none — that *C. elegans* represents other agents as agents.

The 302-neuron count is, I should add, not a magic floor. You could build a device with fewer functional units that navigates a chemical gradient. The reason the worm has 302 neurons is not that 301 would fail. It is that the worm has to do many things simultaneously — forage, mate, lay eggs, escape predators, survive desiccation, navigate five or six sensory modalities in an unpredictable environment — and the count reflects that multifunctionality, not some minimal threshold.

What I am claiming is not that the worm has the smallest possible nervous system that can produce goal-directed behavior. I am claiming that the worm's nervous system, as studied, represents the earliest evolutionary instance of the full six-component architecture I described in §3.7 — and that the six components together define a category of capacity that is qualitatively different from anything in Chapter 2.

---

## 3.10 The Deepest Lesson

The worm at the copper line is making a decision. Not a rich, conscious, deliberate decision — I am not suggesting that, and I want to be precise about what I am not saying. But a decision in the operationally meaningful sense: a behavioral output that cannot be predicted from sensory inputs alone, that requires knowledge of internal state, and that represents a weighting of competing information according to a cost-benefit calculation that is genuinely dynamic.

This is the floor of goal-directed behavior. Not a floor I am inferring — a floor I am reading from a documented architecture. A nervous system that does everything the worm does, in the ways the worm does it, is a system that makes choices. A nervous system that lacks any one of the six components I have listed does not make choices in the same sense.

The rest of this book is the elaboration of what happens when you scale each component. Add more labeled lines, longer memory windows, richer integration, more neuromodulators, more flexible plasticity, and eventually you get mammals. Add language and recursive self-modeling and you get, at some point yet to be precisely determined, something like human cognition.

But the worm came first. And the worm is not a stepping stone to something more important. It is the worked example of the foundation. When I get to language in Chapter 15, the core architecture we will need to understand will be recognizable from here — the same six components, scaled and elaborated, running in a brain that weighs sensory signals against internal state and produces behavior that cannot be predicted from either alone.

The worm showed us how. In a centimeter of soil, a millimeter at a time, billions of years before anyone was watching.

---

## Chapter Summary

**What you can do now that you could not before this chapter:**

The central skill this chapter adds is the ability to analyze any behavioral system — biological or artificial — against a specific architectural checklist and determine whether it is capable of *state-dependent goal-directed behavior* or merely *stimulus-response processing*.

The six-component architecture of steering: bilateral body plan, labeled-line sensors with hardwired valences, temporal comparison rule, mutual inhibition between competing programs, neuromodulatory state encoding, and associative plasticity. These are not arbitrary categories. Each one is derived from a specific experimental dissociation in *C. elegans* research: remove the component, and a specific capacity disappears while others are preserved.

**The one idea that matters most:** A system can have perfect sensors and still fail to make trade-offs, if it lacks the integration machinery for resolving conflict under conditions of internal state change. This is what HEN-1 mutants show. This is what the food-copper experiment shows. Sensing and deciding are separable, and the deciding layer is what determines whether a system is goal-directed or merely responsive.

**The common mistake to watch for:** Confusing behavioral complexity with architectural sophistication. The worm's behavior is not complex by vertebrate standards — but its architecture instantiates every component necessary for goal-directed behavior. Conversely, a complex-seeming AI behavior planner might be running on an architecture that lacks neuromodulatory equivalents and cannot actually trade off competing goals in response to internal state. Behavior is evidence about architecture, but it is not the architecture.

**The Feynman test:** Can you explain why a well-fed *C. elegans* turns back from a copper line, but a starved one crosses it, using only the words "gain," "signal," "weight," and "broadcast molecule"? If yes, you understand the chapter's core mechanism. If not, reread §3.4.

---

## Exercises

**Warm-up: Direct Application**

1. A *C. elegans* mutant is created in which the dopamine system is entirely non-functional. The worm can still detect food odors (AWC neurons fire normally) and can still detect copper (ASH neurons fire normally). Predict what you would expect to observe when this mutant is placed on a food lawn after several hours of food deprivation. Which component of the six-part architecture has been disrupted?

2. The run-and-pirouette navigation strategy requires that the worm compute dC/dt — the time-derivative of attractant concentration. What sensory information is the worm actually sampling at each moment, and why is comparing two time points sufficient to approximate a derivative? What would break if the worm could only sample concentration at a single instant?

3. In the labeled-line architecture, sensory neurons carry "default valences" into the integration center. What does "default" mean here, and under what circumstances might a stimulus override its default valence?

**Application: Translation**

4. A Roomba and a *C. elegans* are both placed in environments with attractants (food, clean-floor region) and repellents (obstacle, copper line). Both exhibit approach-avoidance behavior. List two behavioral tests you could run to determine which system has neuromodulatory state and which does not. What results would you expect from each test for each system, and why?

5. Consider an AI recommendation system that suggests content based on a user's click history. Map this system against the six-component architecture of steering. Which components are present? Which are absent? Is the system goal-directed in the sense defined in this chapter? Justify your answer.

6. The HEN-1 protein is required for *C. elegans* to correctly weigh attractive odors against repellent chemicals in a conflict situation. If you were designing an AI agent for autonomous decision-making in environments with conflicting objectives, what would a functional equivalent of HEN-1 need to do? What would break in the agent's behavior if that component were missing?

**Synthesis: Combining Concepts**

7. The temperature conditioning experiment (§3.6) shows that *C. elegans* forms a thermal preference only when the temperature is associated with food. Design a follow-up experiment to test whether this preference can be *extinguished* if the worm is subsequently exposed to its cultivation temperature without food. What result would demonstrate that extinction is possible? What result would suggest the preference is permanent once formed?

8. Chapter 2 described bacterial chemotaxis as a biased random walk driven by dC/dt. Chapter 3 describes *C. elegans* chemotaxis as a run-and-pirouette system also driven by dC/dt. In what structural sense are these the same algorithm? In what structural sense are they different? What specific capability does the worm's version enable that the bacterium's version does not?

9. Consider the claim: "Goal-directed behavior is just a very complex stimulus-response system, and the distinction between 'decision-making' and 'reflex' is a matter of degree, not kind." Using specific evidence from this chapter, construct the strongest case you can *for* this claim, then construct the strongest case you can *against* it. Where does the argument finally turn?

**Challenge: Pushing Forward**

10. *(Open-ended)* I argued in §3.7 that the six-component architecture is a *template* — that vertebrate nervous systems elaborate each component without adding new categories. A critic might respond: "Consciousness is a genuinely new category that appears in vertebrates and is absent in *C. elegans*, and this represents a real architectural discontinuity, not just elaboration." How would you evaluate this objection? What evidence would, in principle, be sufficient to settle whether consciousness represents a new architectural category or an elaboration of existing ones? This question will recur throughout the book; begin developing your position here.

---

## Connections Forward

This chapter established the architecture of steering. The next three chapters trace what happens when each component is scaled and supplemented:

**Chapter 4** (*Learning and Memory*) takes the associative plasticity component — present in *C. elegans* in its simplest form — and asks what happens when memory extends from hours to a lifetime, and from single-stimulus associations to causal chains. The molecular machinery we introduced in §3.6 (CREB-dependent plasticity) becomes the central actor.

**Chapter 5** (*Emotion*) takes the neuromodulatory layer and asks: when do diffuse broadcast signals become something we should call emotions, rather than just moods? The functional definition this chapter used — a persistent internal state that changes behavioral weighting — turns out to apply surprisingly far up the phylogenetic tree.

**Chapter 9** (*Simulation and Planning*) revisits the one thing the worm definitively cannot do: build a model of a place it has not been, run that model forward in time, and choose an action based on the simulated outcome. That capacity requires a different kind of brain — but you now know what it must build on.

The question this chapter leaves open: if the six-component architecture is sufficient for goal-directed behavior, what is *not* sufficient for consciousness? I do not propose to answer that here. But I want you to hold the question. The worm makes choices, in a defensible operational sense, but I would not claim the worm has experiences. Where is the line? What, architecturally, would cross it?

We are building toward that question. We are not there yet.

---

*The worm is not a tour stop on the way to humans. The worm is the first chapter of the book the rest of the animal kingdom is still writing.*

---

**Chapter Notes and Primary Sources**

The complete connectome of *C. elegans* was published by White, Southgate, Thomson, and Brenner in 1986 in the Philosophical Transactions of the Royal Society. It remains one of the most extraordinary documents in the history of biology — 340 pages mapping every neuron and synapse in a living organism by hand, from electron micrographs. Sydney Brenner's original proposal for *C. elegans* as a model system appeared in 1974 in the journal Genetics.

The run-and-pirouette navigation strategy was characterized by Pierce-Shimomura, Morse, and Lockery in the Journal of Neuroscience (1999). The dopamine and serotonin modulation of food-related behavior was characterized by Sawin, Ranganathan, and Horvitz in Neuron (2000). The HEN-1 conflict-resolution findings appeared in Cell (2002) from Ishihara and colleagues. The temperature conditioning work was published by Mori and Ohshima in Nature (1995).

The subsumption architecture was proposed by Rodney Brooks in an MIT AI Lab technical report in 1986. The Roomba, first commercialized by iRobot in 2002, is the most widely distributed consumer implementation of subsumption-style control.

Developmental variability in the *C. elegans* connectome was documented by Witvliet and colleagues in Nature (2021), showing that while physical contacts between neurons are nearly invariant across individuals, synaptic strengths vary — a finding that complicates the older picture of a perfectly fixed wiring diagram.
