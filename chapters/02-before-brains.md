# Chapter 2 — Before Brains
### The Decisions That Started Without Us

---

## Chapter Overview

You are about to meet the world's oldest intelligence and probably its most underrated.

It doesn't look like much. It is yellow, roughly the size of a dinner plate, and it has no mouth, no eyes, no neurons, and no brain. It is a single cell — one continuous, pulsing bag of cytoplasm with millions of nuclei sloshing through a network of self-built tubes. In the year 2000, a physicist named Toshiyuki Nakagaki placed a piece of this organism at the entrance of a plastic maze, set food at the exit, and waited. Within hours, the organism had explored every passage, every dead end, every wrong turn. Then it began to withdraw. Branch by branch, the exploratory tubes thinned and disappeared. When the experiment was over, the organism — *Physarum polycephalum*, a slime mold — had concentrated its entire body into a single thick tube that traced the *shortest possible path* between the food sources.

No plan. No map. No nervous system. Just a cell, and a problem solved.

A decade later, Atsushi Tero and colleagues repeated a version of the experiment at a continental scale. They placed oat flakes at the geographic positions of the cities surrounding Tokyo and let *Physarum* connect them. The network the mold built — in its single-organism, brainless way — matched the actual Tokyo rail system in efficiency, cost, and fault tolerance. Human engineers had spent a century designing that system. The mold reproduced its essential structure in a few days.

If that doesn't make you question your assumptions about what intelligence requires, I'm not sure what will.

This chapter is about what happens before brains arrive. It's about the cognitive floor — the minimum viable architecture for something we might honestly call a decision — and about the discovery that this floor is older, simpler, and more widely distributed through life than the neurocentric story of intelligence usually admits. It is also preparation for everything that follows. Every capacity I will trace in the rest of this book — learning, memory, emotion, planning, social cognition — has a pre-neural prototype. Brains did not invent cognition. They industrialized it.

---

## Learning Objectives

By the end of this chapter, you will be able to:

1. **Define** *valence* as a cognitive primitive and explain why it constitutes a genuine decision rather than a reflex.
2. **Trace** the molecular mechanism of bacterial chemotaxis from receptor binding through methylation to the run-or-tumble switch, and identify which steps implement sensing, memory, integration, and variable response.
3. **Distinguish** taxis from tropism and explain why the distinction matters for the definition of intelligence.
4. **Analyze** the *Physarum* maze-solving behavior using the four-ingredient framework for decisions.
5. **Apply** skeptical standards to contested claims in the plant cognition literature, distinguishing what the evidence supports from what it implies.
6. **Explain** the "extension note" logic: how artificial sensors extend valence-detection beyond biological limits, and what they can and cannot yet do.

---

## Prerequisites

Chapter 1 introduced the working definition I'll use throughout this book: *intelligence is the ability of an agent to achieve goals across a wide range of environments.* It also introduced Legg and Hutter's formalization, Gardner's multiple intelligences, and the key observation that every definition we have is either too narrow (excludes organisms we'd intuitively call intelligent) or too broad (includes thermostats). You should be familiar with why we chose the goal-achievement definition as our working instrument, and what it commits us to.

This chapter will strain that definition productively. A bacterium achieves goals in a narrow range of environments — chemical gradients. The range is small. But the goal-achievement is genuine.

---

## Why This Chapter Matters

I need to be honest with you about why this chapter is here at all.

The standard move in books about animal intelligence is to start with vertebrates, or at least with nervous systems. The bacteria and the slime molds get a paragraph in the introduction — "life has always been doing something interesting" — and then we move on to the real story. I am not going to do that, and here is why:

If you do not understand what a decision looks like without neurons, you will not understand what neurons actually added when they arrived. You will assume that brains are *necessary* for decisions rather than *sufficient* for faster, more flexible, more powerful ones. And you will misread the entire subsequent history.

More concretely: if you accept the evidence in this chapter, you will leave it holding a claim that reshapes how you read every chapter that follows. That claim is this — the cognitive primitive underlying every form of intelligence in this book, including yours, is *valence*: the categorization of the world into things to approach and things to avoid. The amygdala in your brain detects threats and rewards by computing valence. So does the bacterial cell whose memory fits in two enzymes. One is faster, richer, and more context-sensitive. The core computation is the same.

---

## Concept 1: What a Decision Actually Requires

### A scene

Imagine you are swimming in chemical soup. You are one cell. You have no eyes, no nose, no brain, no memory in any structure you might recognize as such. The soup around you contains amino acids — food, in your world — and also copper ions, which will kill you if they accumulate. Both are diffusing toward you from sources you cannot see. You cannot steer. You have no rudder, no fins, no way to directly choose your direction.

You are, in fact, an *E. coli*, and you are about to make a decision.

### The four ingredients

A decision is not a reflex. Before we can understand why the bacterium counts as doing something cognitive, we need to be clear about what distinguishes the two.

A **reflex** is a fixed response to a stimulus. The input determines the output, every time, regardless of context. Your knee jerks when tapped. A plant grows toward light. A Venus flytrap doesn't close when the wind touches it — it closes when a trigger hair is touched. Each of these is a physical mechanism: input in, output out.

A **decision** varies. The same stimulus can produce different responses depending on what has happened before, on the organism's internal state, on competing inputs. A decision *integrates* information across time and across sources. That integration is what makes it non-reflex.

Stripped to essentials, a minimum decision requires exactly four things:

**Sensing** — some access to environmental information. Without sensing, there is nothing to decide about.

**Memory** — some capacity to compare the present to the past. A system that only knows the present cannot detect whether things are getting better or worse. Without memory, even the most sophisticated sensing is frozen at a single moment in time.

**Integration** — the ability to weigh multiple inputs against each other and over time. The sensory reading right now, the sensory reading four seconds ago, competing cues from different receptors — these must be combined into a single output.

**Variable response** — the output must be able to vary. A system that always does the same thing regardless of input isn't deciding; it's executing. Variable response is what allows decisions to be adaptive rather than fixed.

These four requirements are not my invention. They are what the behavioral literature on learning and decision-making has established as necessary conditions. Take any one away and what you have left is something simpler — a sensor, a clock, a classifier, a switch. All four together, organized into a loop that closes on the world, and you have the floor of cognition.

The term for what this cognitive floor computes is **valence**.

Valence — borrowed from chemistry, where it names the combining power of an element — describes the approach-or-avoid property of a stimulus. Serine has positive valence for *E. coli*. Nickel ions have negative valence. The smell of smoke has negative valence for you, and so does the word *vomit*, which I notice you just flinched at. Valence is not a judgment. It is not a feeling, necessarily — though it may be. It is simply a categorization: *for me* or *against me*, approach or avoid.

Without valence, no preference is possible. Without preference, no goal. Without goals, nothing in the rest of this book. Valence is not a refinement of intelligence; it is its foundation.

**Trade-off: Why valence instead of sensation?**

Sensation alone — the bare ability to detect a chemical or a photon — is not a decision. A pH meter senses acidity. It does not decide anything. What turns a sensor into a cognitive system is the addition of a valence assignment: this reading means *move toward*, that reading means *move away*. Positive valence assignments require memory and integration, because positive valence is relational — not "there is sugar here" but "there is more sugar here than four seconds ago." The trade-off organisms face is between the cost of maintaining memory-capable valence machinery (metabolically expensive, subject to error) and the benefit of adaptive, direction-sensitive behavior that simple sensation cannot provide. Every organism in this chapter has struck that trade-off in favor of valence detection. It is the oldest cognitive investment in biology.

---

## Concept 2: How *E. coli* Decides — The Molecular Architecture

### A scene

It is 1972. Howard Berg has built a microscope that nobody thought was possible: a device that can track a single bacterium through three-dimensional space as it swims. He points it at a cell in a chemical gradient. The bacterium runs straight. Tumbles. Runs straight in a new direction. Tumbles again. Over minutes, this drunken walk — run, tumble, run, tumble — produces net motion toward the chemical source. But the cell is not steering. Berg can see that. So what is it doing?

### The mechanism, from the receptor down

Let me walk you through the machine.

The cell surface is studded with roughly 7,000 receptor proteins called methyl-accepting chemotaxis proteins, or **MCPs**. Each MCP is tuned to a class of molecule: serine, aspartate, certain repellents. When an attractant binds an MCP, the receptor changes shape. Not dramatically — a subtle conformational shift that propagates through the cell membrane.

That shift inhibits a kinase called **CheA**. A kinase is an enzyme whose job is to phosphorylate — attach a phosphate group to — a target protein. CheA's target is a small messenger called **CheY**. Phosphorylated CheY, written CheY-P, diffuses through the cell to the flagellar motors and biases them toward clockwise rotation. Clockwise rotation means tumbling. Counter-clockwise means a smooth run.

More attractant → less CheA activity → less CheY-P → less tumbling → longer runs.

This already explains why the cell runs longer when it detects attractant. But it does not yet explain how the cell *compares present to past*. The mechanism described so far responds to current concentration. A cell that only responds to current concentration would tumble just as readily in the middle of a rich patch as at the edge of it, because the concentration is high in both places. It would lose all directional information.

The memory lives in two more enzymes: **CheR** and **CheB**.

CheR adds methyl groups to the MCP receptors. CheB removes them. Methylation makes receptors *less sensitive* to attractant — it desensitizes them. Crucially, these enzymes work on a slower timescale than the binding-and-signaling cascade. The effect is that the receptor's current sensitivity reflects the average of the *past few seconds* of chemical experience. The receptor has been slowly tuned to the recent baseline. When current concentration exceeds the baseline (things are getting better), net inhibition of CheA is high and the cell runs. When current concentration falls below the baseline (things are getting worse), CheA fires, CheY-P rises, and the cell tumbles.

In 1986, James Segall, Steven Block, and Berg measured the precise time window by pulsing tethered bacteria with attractant and measuring the response. The cell weighs its chemical experience over the past four seconds, with the most recent second given positive weighting and the prior three seconds given negative weighting. The cell computes, in effect:

$$\text{response} \propto \left[\text{chemical experience, last 1 second}\right] - \left[\text{chemical experience, prior 3 seconds}\right]$$

This is a derivative. The cell is responding to the *change* in concentration over time — the gradient of its experience — rather than to concentration itself. It is doing, as I have said before, differential calculus with two enzymes and a methylation rate. The four-second window is not arbitrary: it matches the distance the cell can swim in a single run before Brownian motion randomizes its direction. Memory longer than that would be memory of a self that no longer exists.

**Trade-off: Sensitivity versus adaptability**

The methylation memory creates a fundamental tension. More methylation means faster adaptation to a new baseline — the cell quickly recalibrates after a step change in concentration. But rapid adaptation means the cell stops responding to the new concentration level sooner. Less methylation means slower adaptation — the cell stays sensitive to the gradient for longer, but takes longer to reset when the environment changes abruptly. Real cells are tuned to operate near the middle of this trade-off, with adaptation timescales matched to the typical chemical landscapes they navigate.

[FIGURE: Diagram of *E. coli* chemotaxis cascade from MCP receptor binding through CheA-CheY-P signaling to flagellar motor switching, with CheR/CheB methylation loop shown as the memory arm. Time axis showing the 4-second integration window.]

### Worked example: The knock-out experiment

Here is how we know the methylation memory is doing what I've described, rather than some other explanation.

**Given:** *E. coli* in a gradient of attractant serine.

**Normally:** The cell detects rising concentration → CheA inhibited → CheY-P falls → flagella spin CCW → smooth run. Over many runs and tumbles, the cell drifts up the gradient.

**Now remove CheR and CheB** (the methylation enzymes) via genetic knock-out.

**Prediction from the model:** Without the slow methylation tuning, the receptor's baseline is fixed at the default methylation state. The cell can still respond to concentration (CheA is still inhibited by attractant binding), but cannot compare present to past. It should respond to absolute concentration rather than to change.

**Observed result (Segall et al., following up on earlier Berg lab work):** Mutant cells lacking CheR and CheB still bias their flagella when placed in attractant — the absolute-level response works. But their random walks are not directed. They run longer in high-concentration zones, but they cannot detect *whether concentration is increasing*, so they do not preferentially run toward the source. The drunkard's walk stays drunk.

**Lesson:** The memory is not just an interesting detail about the mechanism. It is the entire basis of directed behavior. The cell without methylation memory is a sensor without a decision. The cell with it is the simplest thing biology has built that qualifies for the four-ingredient standard.

---

## Concept 3: The Same Logic, Different Substrates — From Cytoplasm to Calcium

### A scene

Imagine that instead of two enzymes and a flagellum, you had a body the size of a dinner plate and a decision about which tube to fatten and which to thin. You are not thinking about it. There is no "you" to think. The decision is happening everywhere in your body at once, written in flow rates and cytoplasm pressure, and when it is over, your body *is* the answer.

### *Physarum*, the maze, and the Tokyo rail system

*Physarum* distributes the bacterial logic across a whole different kind of body. The slime mold is a network of cytoplasmic tubes. Cytoplasm sloshes back and forth through these tubes in rhythmic oscillations, every minute or two. The key rule is simple: tubes through which flow is high and sustained grow thicker; tubes through which flow is low thin and eventually disappear. When food is detected at a network node, local oscillations change phase, flow toward the food source increases, that channel is reinforced, and the network reorganizes.

The maze-solving follows directly. Given a path from food to food through a maze, every route gets explored (the mold fills the maze). Every dead-end branch eventually carries zero net flow, because there is no food at the end of it. Every dead-end tube thins and retracts. The shortest path carries the most sustained flow, because it connects the two food sources with the least detour. The shortest path is the last tube standing.

There is also memory — not internal, but *written into the environment*. *Physarum* leaves a trail of extracellular slime where it has been, and the organism avoids this trail on subsequent exploration. The slime is an external hard drive: memory stored in the substrate, not in the cell. This may be older than molecular memory. Many organisms externalize memory rather than computing it internally — ant pheromone trails, beaver dams, the tools a crow caches — and each is a form of the same trick: encoding past behavior in a physical mark that future behavior can read.

[FIGURE: Series showing *Physarum* filling a maze over 8 hours, then retracting to the shortest path. Inset: the Tokyo oat-flake experiment with the resulting network overlaid on the actual rail map.]

### The Venus flytrap's leaky integrator

The flytrap, *Dionaea muscipula*, solves a different problem with a different piece of chemistry. Its inner surface has trigger hairs. The trap closes only when at least two hairs are touched within approximately thirty seconds — a rule that prevents the trap from snapping shut on rain and wind.

Jennifer Böhm, Sönke Scherzer, Rainer Hedrich, and their colleagues have traced the mechanism to calcium signaling. Each touch generates a calcium spike in the trap's cells. Calcium decays over time — the concentration drops back toward baseline as calcium pumps remove it from the cytoplasm. The crucial point: it does not decay completely before the window closes. A second touch adds its calcium spike to whatever residue remains from the first. Only when the summed calcium exceeds the threshold does the trap close.

The calcium concentration *is* the short-term memory. The threshold *is* the decision rule. The trap counts to two by exploiting the fact that calcium decays slower than the interval between legitimate prey movements.

This kind of mechanism — a signal that accumulates with each event and leaks away between events — is called a **leaky integrator**. It appears throughout neuroscience (it is how some neurons accumulate evidence before firing a decision), and here it is in a plant, implemented in ionic calcium, solving the real engineering problem of distinguishing prey from debris. The trap does not need a nervous system for this. It needs a molecule whose concentration history tracks recent touch events. Calcium works.

**Trade-off: Window length versus missed prey**

If the calcium window were very short (calcium decayed very fast), the trap would almost never close: the second touch would always arrive to an already-zeroed integrator, and the rule would effectively be "two simultaneous touches," which prey never provide. If the window were very long, the trap would close on rain — two drops a minute apart would both register. The thirty-second window is a biological compromise, tuned to the temporal statistics of insect movement versus rainfall. This is exactly the kind of trade-off we see throughout sensory systems: the integration window is calibrated to the signal, not to some abstract optimum.

### A note on plants and caution

I want to name a tension in this literature before you encounter it elsewhere and are misled.

Two of the most-cited demonstrations of plant cognition have not held up cleanly. Monica Gagliano's 2014 study reported that *Mimosa pudica* — the sensitive plant — habituated to repeated drops and remembered the lesson for a month. It was challenged by Robert Biegler, who argued the data could be explained by sensory adaptation or motor fatigue. The dispute has not been resolved by replication, and until it is, I cannot cite the study as established.

Gagliano's 2016 study claiming that pea plants could learn to associate the direction of a fan with the direction of a light — associative learning, the kind we will examine in depth when we reach Chapter 4 — failed to replicate under blinded experimental conditions. Kasey Markel repeated the protocol with improved methodology and found no effect. The original team has argued that Markel's protocol differed in relevant ways. The disagreement continues.

The responsible position, which I hold here and throughout this book, is: *habituation is cleanly demonstrated in Physarum, and is not yet cleanly demonstrated in plants*. The flytrap's calcium-counting is a real mechanism. The sagebrush volatile communication is a documented phenomenon. But the stronger claims — plant "learning," plant "memory" in the sense we reserve for animals — are not established to the standard this book is applying.

The general lesson is precise. For any organism and any capacity, there is a careful version of the claim (the organism produces the *behavior* characteristic of X) and an inflated version (the organism *experiences* X the way we do). For pre-neural cognition, the careful version is often well-supported. The inflated version is almost never established, and stating it as fact is not courage — it is a failure to distinguish evidence from enthusiasm.

---

## Concept 4: The Extension — Artificial Valence Detection

### A scene

In 1906, the Danish chemist Søren Sørensen needed to measure the acidity of his fermentation vats to keep the process stable. He had no automated sensor. He dipped a piece of litmus paper, watched it change color, compared it to a reference card. This was, functionally, a one-point measurement of valence: this batch is *okay* or *too acidic*, approach or stop. It worked. It told him nothing about *whether acidity was changing*, nothing about the trend, nothing that the bacterium's four-second temporal integration would have told it.

The modern pH electrode does a little better. It converts hydrogen ion concentration into a voltage, continuously. Still no trend. Still no comparison to the recent past. Still, essentially, a sensor without a decision.

### What sensors extend and what they cannot do

The instruments human beings have built to detect chemicals — pH meters, gas sensors, smoke detectors, blood-glucose monitors, explosives-detection systems — are all, at their core, artificial MCPs. They implement the sensing step of the bacterium's four-ingredient decision. Some of them add a threshold rule (the smoke detector: accumulate particles, fire when you cross the line). A few add something like integration (environmental monitoring systems that flag *trends* in pollutant concentration, not just instantaneous readings). None of them, as of this writing, implements the full four-ingredient architecture in a way that produces flexible goal-directed behavior across varying environments.

The smoke detector on your ceiling is not stupid. It is a very good one-step sensor with a good threshold rule, and it saves lives. But it would tumble randomly in a chemical gradient. It cannot find the shortest path through a maze. It cannot distinguish the smell of a cooking accident from the smell of a fire in a useful way (which is why your smoke detector went off the last time you made toast). It does not have the memory that makes those distinctions possible.

This is the extension note's argument: every instrument we have built to detect the chemistry of the world is a piece of the same trick the bacterium is running. We have built excellent pieces. We have not yet built the trick. What the bacterium does with its methylation memory — compare the present to the recent past and respond to the *derivative* rather than the *level* — is the step that turns a sensor into a decision-maker. Most of our instruments still stop one step short.

**Trade-off: Precision versus generalization**

The bacterium's MCP receptors are tuned to specific chemical classes. They are extremely sensitive within those classes — *E. coli* can detect one molecule of aspartate in a concentration as low as 3 nM — but they are blind to everything else. This is the trade-off between sensitivity and generalization that runs through sensory biology: a system optimized to detect one signal will be deaf to others. Human-designed sensors face the same trade-off: a carbon monoxide detector is exquisitely sensitive to CO and insensitive to almost everything else, including the ozone that would tell it the building has a different kind of air-quality problem. Building general-purpose chemical intelligence — the kind that can flexibly reassign which chemicals mean "approach" and which mean "avoid" based on context — is a problem that has not been solved in either biological or artificial systems below the vertebrate level.

---

## Integration: The Floor of Cognition

Let me collect what the evidence shows.

Decisions — real ones, with all four ingredients — appear in systems with no neurons: bacteria, slime molds, Venus flytraps. In each case, the system computes valence: this is what to approach, that is what to avoid. In each case, the computation involves memory, whether molecular (methylation), ionic (calcium), or physical (slime trails). In each case, the output is variable: the same stimulus does not always produce the same response, because past experience has already altered the machinery.

None of these systems is impressively intelligent in the sense we will develop through the rest of this book. The bacterium handles a small range of chemical gradients. The slime mold finds paths in mazes, but cannot hunt prey. The flytrap counts to two. The range of environments each handles is narrow; the goals they pursue are fixed. But they satisfy the working definition — *achieving goals across the environments they encounter* — and they satisfy it with no neurons.

What neurons will add, beginning in Chapter 3, is speed, flexibility, and range. The nematode *C. elegans*, with 302 neurons, can hold valence in a network instead of a single cell, can update it from experience, can suppress it in the presence of competing needs. That is a genuine advance. But it is advance along the same dimension. The bacterium did not fail to build a mind; it built the minimum viable component of one, and every more elaborate cognitive system in this book will have that component somewhere in it.

---

## Exercises

### Warm-Up (Direct Application)

**1.** *E. coli* navigating toward serine produces longer runs when serine concentration is increasing. Using the CheA-CheY-P cascade, trace the molecular steps that produce this behavior, from receptor binding to flagellar switch. Which step implements memory?
*(Tests Learning Objective 2; difficulty: accessible)*

**2.** Define taxis and tropism. A sunflower turns toward the sun (phototropism). A moth flies toward a lamp (phototaxis). Which of these requires the four-ingredient decision architecture, and why?
*(Tests Learning Objective 3; difficulty: accessible)*

**3.** The Venus flytrap closes only when two trigger hairs are touched within ~30 seconds. Using the calcium leaky integrator mechanism, explain what would happen to the trap if the calcium decay rate were ten times faster (calcium concentration dropped in 3 seconds instead of 30). Would the trap be more or less likely to catch prey? What would it become better at instead?
*(Tests Learning Objective 4; difficulty: accessible)*

### Application (Translation Required)

**4.** An engineer proposes to improve a smoke detector by adding a "trend sensor" — rather than firing when particle concentration exceeds a threshold, it fires when particle concentration *has been rising for more than ten seconds*. Using the bacterial chemotaxis framework, explain what cognitive function this would add. What would the smoke detector now be doing that it was not doing before? What would it still not be doing?
*(Tests Learning Objective 6; difficulty: moderate)*

**5.** The sagebrush volatile communication system (Karban et al.) shows that damaged plants release VOCs that prime defenses in neighboring plants. Evaluate this system against the four-ingredient decision framework: which of the four ingredients does the *receiving* plant satisfy? Which is it missing or unclear on? Write one sentence identifying the most important claim that would need to be demonstrated to upgrade the receiving plant from "sensor" to "decision-maker."
*(Tests Learning Objectives 1 and 5; difficulty: moderate)*

### Synthesis (Combining Multiple Concepts)

**6.** I described the *Physarum* maze-solving and the *E. coli* chemotaxis as implementing "the same logic in different substrates." Write a brief analysis (one paragraph) identifying: (a) what is structurally identical between the two systems, (b) what is genuinely different, and (c) whether these differences are differences in *kind* (one is doing something fundamentally different) or differences in *degree* (one is doing more of the same thing).
*(Tests Learning Objectives 2, 4, and 6; difficulty: challenging)*

### Challenge (Open-Ended, Points Forward)

**7.** The bacterium's memory lasts approximately four seconds, matched to the distance it can swim before Brownian motion randomizes its direction. *C. elegans* — which you will meet in Chapter 3 — navigates on a surface, has 302 neurons, and appears to maintain chemical preferences for hours after conditioning. What *additional* memory structure would you predict *C. elegans* must have, that *E. coli* does not, given that its behavioral window is roughly 1,000 times longer? What constraints would you place on where that memory is stored?
*(Tests Learning Objectives 2–4 in combination with forward-looking inference; difficulty: advanced)*

---

## Chapter Summary

Here is what you can now do that you couldn't before:

You can look at any organism — regardless of whether it has neurons — and ask the four-question test: does it sense, remember, integrate, and respond variably? If yes, it makes decisions. If no, it has reflexes. This is not a soft philosophical position; it follows from the functional requirements for goal-directed behavior.

You have a precise molecular story for how a single cell implements all four of those requirements: receptor binding implements sensing; methylation implements memory; the kinase cascade implements integration; the flagellar switch implements variable response. This is among the best-understood decision systems in all of biology, and it does everything in a cell that weighs one picogram.

You can apply genuine skepticism to the frontier claims in this literature. Habituation in *Physarum*: demonstrated. Associative learning in peas: contested, failed to replicate under blinding. Plant "intelligence" as a research program: promising but requires careful distinction between the careful claim (this behavior pattern) and the inflated one (this subjective experience).

And you are holding the concept of valence — approach-or-avoid as a cognitive primitive — as the through-line that connects *E. coli* to your amygdala. Every chapter from here to the end is about what it takes to make valence faster, more flexible, more social, more predictive, more abstract. But valence is where it starts.

The common mistake to watch for, going forward: assuming that a capacity we first clearly see in complex organisms must have *originated* in complex organisms. It never does. Search for the prototype. It is almost always older, simpler, and stranger than you expected.

**The Feynman test for this chapter:** Can you explain to someone who has never taken a biology course why the bacterium's temporal comparison requires two enzymes instead of one, and why the window is four seconds instead of four minutes? If you can, you understand the mechanism.

---

## Connections Forward

This chapter has established the floor. The next chapter builds the first real room above it.

*C. elegans*, the nematode, has 302 neurons and 7,000 synapses. It handles the same basic valence computations the bacterium handles — move toward food, move away from toxin — but it now has a *network* to run them through. That changes two things immediately. First, different neurons can specialize for different valence categories: some detect food, some detect noxious chemicals, some integrate both. Second, the same sensory signal can trigger different behavioral responses depending on the nematode's internal state — hunger suppresses toxin avoidance; satiation suppresses food-seeking. This is the beginning of something that will become, much further up the ladder, what we recognize as *motivation*. The bacterium has no internal states to speak of; the nematode has the first functional analogs of them.

Chapter 3 also introduces the two key neuromodulators that will appear in every subsequent chapter: dopamine, which encodes reward prediction and drives approach; and serotonin, which encodes consumption and satiation. Both are present in the nematode. Both are present in you. The molecular conversation between hunger and behavior turns out to have been running, with relatively few changes, for 600 million years.

The question Chapter 3 asks is not "does *C. elegans* have a brain?" — it doesn't, not in any useful sense — but "what does a first nervous system actually add, and was that addition worth the metabolic cost?"

Spoiler: it was.

---

*Tags: before-brains, aneural-cognition, valence, E-coli-chemotaxis, CheA-CheY, methylation-memory, run-and-tumble, Physarum-polycephalum, Venus-flytrap, leaky-integrator, calcium-signaling, taxis-vs-tropism, Nakagaki, Berg, sagebrush-volatiles, plant-cognition-skepticism, artificial-sensors, cognitive-floor*
