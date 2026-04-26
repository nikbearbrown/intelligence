# Chapter 9 — Simulation and Planning
### The Rat That Regretted

---

## Chapter Overview

In David Redish's laboratory at the University of Minnesota, a rat is running a circular track called Restaurant Row. Four stations are arranged around the track, each offering a different food flavor — banana, cherry, chocolate, plain. At each station entrance, a chime indicates how long the rat must wait for a reward. The waits range from one second to forty-five. The rat has one hour. It must decide, constantly: stay and collect, or skip to the next station.

The rats develop preferences. Each has a threshold — the longest wait it will accept for each flavor. Below threshold, stay. Above, skip.

Adam Steiner and Redish, in 2014, arranged the track so they could observe what happened when a rat made a costly mistake: skipped a chocolate offer at a wait within its threshold, then arrived at the next station to find a cherry deal at a wait *above* its cherry threshold. A good deal declined, a bad one accepted instead. In a human, we would call the moment that followed regret.

The rat looked back. It turned its head toward the restaurant it had just left, toward the deal it had turned down. The look-back occurred only on regret-eligible trials — only when the rat had passed up a genuinely good offer for a genuinely worse one. While the rat looked back, neurons in the orbitofrontal cortex were firing in the pattern they had previously fired *while the rat was at the chocolate station*. The brain was not encoding the disappointing cherry. It was encoding what the rat should have done a few seconds ago. After the look-back, the rats waited longer at subsequent stations than usual — exactly the behavioral correction that regret produces in human subjects.

A small mammal had just run a counterfactual. It had simulated the alternative it had not taken, compared it to what actually happened, and updated its policy accordingly.

The chapter is the architecture under that look-back — the neural machinery that makes it possible for a brain to run the world forward in its head before acting on it, and backward through the past to recover the better option it missed.

---

## Learning Objectives

By the end of this chapter, you will be able to:

1. **Distinguish** model-free and model-based reinforcement learning as two distinct computational strategies, and explain why model-based RL requires an internal world-model that model-free RL does not.
2. **Explain** how Judea Pearl's three-rung ladder of causation (association, intervention, counterfactual) maps onto these two learning modes, and locate where simulation enters the hierarchy.
3. **Describe** hippocampal forward and reverse replay as the neural substrate of simulation and credit assignment respectively, drawing on the Pfeiffer-Foster and Foster-Wilson evidence.
4. **Analyze** the Steiner-Redish Restaurant Row result as evidence for counterfactual reasoning in rats, distinguishing regret (specific counterfactual comparison) from disappointment (generic prediction error).
5. **Evaluate** the Clayton-Dickinson scrub-jay evidence for episodic-like memory and future planning, and explain what it implies about the evolutionary distribution of simulation — that the capacity evolved at least twice, in mammals and corvids, on different neural substrates.
6. **Apply** the simulation framework to digital-twin technology, identifying what the tool extends relative to the biological simulator, and what the human cognitive contribution remains.

---

## Prerequisites

Chapter 8 introduced model-free reinforcement learning — the dopamine prediction-error signal, the Rescorla-Wagner rule, and the temporal-difference framework for value updating in the basal ganglia. You should be comfortable with the claim that the dopamine signal encodes *prediction error* (the difference between expected and received reward) rather than raw reward, and that this signal drives value updates in striatal circuits. Model-based RL, introduced in this chapter, sits on top of the model-free machinery rather than replacing it; you will need the Chapter 8 foundation to understand what the model-based layer adds.

Chapter 7's hippocampus material is also directly relevant. You know the hippocampus as the seat of the spatial map — the structure that implements allocentric position encoding through place cells and grid cells. This chapter reveals that the same tissue does double duty: it is also the trajectory simulator, running paths forward and backward through the spatial map at speeds far faster than the body can physically move.

---

## Why This Chapter Matters

The question this chapter addresses — whether non-human animals can reason about what would have happened if they had acted differently — was, for most of the twentieth century, treated as obviously answered in the negative. The *Bischof-Köhler hypothesis* held that non-human animals are stuck in time: they can learn from past experience and respond to present conditions, but they cannot plan for future motivational states different from their current ones, and they cannot counterfactually evaluate past decisions they did not make.

The experimental record assembled over the past thirty years has systematically dismantled this hypothesis for mammals and corvids. The Steiner-Redish regret data and the Clayton-Dickinson episodic-memory data are the two clearest empirical cases. Understanding why they matter requires understanding the computational distinction between model-free and model-based processing, which is why this chapter precedes the social cognition chapters rather than following them: the capacity for simulation is the substrate on which social cognition, theory of mind, and planning all build.

For the AI comparison that runs through this book, this chapter establishes something specific. Model-free learning — caching values from experience — is well-represented in current neural networks. Model-based learning — building a world-model and running simulations on it — is an active research area in AI and is not yet reliably present in the systems deployed at scale. Understanding the neural case clarifies what model-based learning actually requires, and why it is harder to build than the model-free version.

---

## Concept 1: Two Modes of Learning, Three Rungs of Causation

### A scene

A rat is in a box with a lever. It presses the lever by accident. A food pellet drops. It presses again. Another pellet. The rat presses many times. The value of pressing the lever has been cached: lever press → reward, cached, retrieve when hungry.

Now the experimenter, without the rat's knowledge, poisons the food pellets. The rat presses the lever. Eats a pellet. Gets sick. One learning system updates: *food pellets → illness, avoid*. But the *lever-press* value was cached separately. When the rat is hungry again the next day, it presses the lever. This is the failure mode of model-free learning, and Bernard Balleine and Anthony Dickinson documented it cleanly in their devaluation paradigm in the 1990s. A model-free agent does not know that lever-pressing leads to the now-aversive food; it only knows that lever-pressing has historically been rewarded. It has to learn the new contingency the slow way, by pressing again.

A model-based agent would not make this mistake. It has a model: lever-pressing → food pellets → currently aversive. It can chain those representations without pressing the lever, compute the expected outcome, and decide not to bother. This is what makes model-based learning qualitatively different from model-free.

### The computational distinction

**Model-free reinforcement learning** caches the *value* of states and actions directly from experience. The agent does not maintain an internal model of what leads to what. It maintains a lookup table: state S has value V, action A in state S has value Q. The cache is updated when the prediction-error signal fires. The advantage is speed: cached values are immediately available, with no simulation required at decision time. The disadvantage is brittleness: the cache reflects the past, and any change in the environment's dynamics requires the agent to collect new experience to update the cache.

**Model-based reinforcement learning** maintains an internal model of the environment's *transition dynamics* — which states lead to which other states, and with what probability — and uses this model to *simulate* action consequences at decision time. Rather than looking up a cached value, the model-based agent runs a mental rehearsal of the trajectory from current state to future outcome and estimates the value by reading off the simulated result. The advantage is flexibility: the agent can reason about novel situations, evaluate options it has never tried, and adapt immediately when the environment changes by updating the model rather than waiting for new cached values. The disadvantage is computational cost: simulation is metabolically expensive and time-consuming.

Real animals use both systems, often simultaneously, with different brain structures mediating each. The basal ganglia — striatum, dopamine system — mediate the model-free cache. The hippocampus-prefrontal-cortex network mediates the model-based simulator. The interaction between them is competitive and context-dependent: under time pressure or cognitive load, model-free habits dominate; given time and a novel situation, model-based planning takes over.

**Pearl's ladder applied to learning.** Judea Pearl's three-rung hierarchy of causal reasoning maps cleanly onto this distinction.

Rung 1 is *association*: A and B co-occur. The rooster crows at sunrise. The lever produces food. Pure Pavlovian conditioning is Rung 1. The model-free cache is Rung 1 applied to action values: *this state-action pair has historically paid off*.

Rung 2 is *intervention*: what happens if I do X? If I press the lever, the food drops. Model-free learning answers this by lookup: the cached value of lever-pressing, acquired from past experience. The agent cannot reason about what would happen if it pressed a lever it has never pressed before.

Rung 3 is *counterfactual*: what would have happened if I had done otherwise? This is the rung that requires simulation. The model-based agent can run: *if I had taken the chocolate offer, I would now be satisfied; since I didn't, I am waiting for a worse cherry.* The comparison requires holding two possible world-states in memory simultaneously — actual and counterfactual — and computing the difference. No amount of model-free caching can produce this comparison. It requires a world-model and the ability to run it.

The rat at Restaurant Row was on Rung 3. The chapter is how it got there.

**Trade-off: Speed versus flexibility**

The model-free and model-based systems are not just computationally different; they trade off against each other in a way that determines which dominates in a given behavioral context. Model-free is fast — cached values are retrieved in milliseconds and drive action without deliberation. Model-based is flexible — simulation can evaluate novel situations and adapt to environmental changes — but it requires time and working memory. Under stress, time pressure, or high cognitive load, control shifts toward model-free habits. This is why well-practiced skills become automatic (golf swings, piano fingering, surgical suturing) — not because the model-based simulator stops working, but because the model-free system has enough cached value to produce correct behavior faster than deliberation can. The pathology of addiction is partly the model-free system overcaching a substance value that the model-based system knows is net negative, with the model-free lookup winning under the drug cue because it is faster.

---

## Concept 2: Hippocampal Replay — The Neural Simulator

### A scene

It is 1948. Edward Tolman is watching rats at maze junctions. A rat approaches a T-junction, pauses, and swings its head left, then right, then left again. It looks as if it is weighing its options. Tolman calls this *vicarious trial and error* — VTE — and argues, in his 1948 *Psychological Review* paper, that the rat is trying out the alternatives in its head before committing. His behaviorist colleagues are skeptical. VTE could be an indecisive head-swing with no cognitive content. The claim cannot be adjudicated with 1948 neurophysiology.

Sixty years later, the electrodes are fine enough to settle it.

### How the hippocampus runs the world forward

The hippocampus — which Chapter 7 established as the seat of the allocentric spatial map — turns out to be a *trajectory generator*. The same place cells that fire when the rat is in a particular location also fire, in rapid sequence, when the rat is *not moving*, during brief high-frequency oscillations called *sharp-wave ripples* in the CA1 and CA3 subfields.

Brad Pfeiffer and David Foster, recording simultaneously from many hippocampal place cells in 2013, captured the forward version of this. Just before a rat began moving toward a remembered goal location, a brief sweep of place-cell firing — starting at the rat's current position and ending at the goal, traversing the path in between — occurred in roughly a hundred milliseconds. Far faster than the rat could physically run the path. The sweep predicted which route the rat subsequently took. Sometimes it predicted the route better than the rat's prior behavior would have suggested, as if the simulation had evaluated options and selected the better one. The hippocampus was *pre-experiencing the trajectory* before the body took a single step.

This is *forward replay*. The hippocampal map runs a fast simulation of a candidate future path, on the same neural substrate that encodes the real path when the rat is actually moving.

Foster and Matthew Wilson, working with data from 2006, had documented the complementary phenomenon earlier: after a rat ran a trajectory and arrived at reward, the hippocampal place cells fired in reverse order — from the reward location backward through the path just taken. This *reverse replay* also occurs during sharp-wave ripples, immediately post-reward. Its function is credit assignment: propagating the reward signal backward through the trajectory, so that each step that contributed to reaching the reward gets its value updated. In the language of temporal-difference learning from Chapter 8, forward replay computes $V(s_t)$ for states the animal is about to enter; reverse replay propagates $\delta_t$ backward through the chain of states that produced the outcome.

Together, the two forms of replay give the hippocampus its role as a *planning substrate*. Forward replay evaluates candidate futures. Reverse replay assigns credit to past choices. The animal can sit still and do the mental work of navigation — evaluating paths, updating values — at twenty or thirty times the speed of physical experience, in the gaps between actual movement.

Several additional properties of replay are worth noting. Replay events are *prioritized*: not every past trajectory is replayed with equal frequency. Trajectories toward high-reward locations, novel routes, and recently visited places are replayed more often — the system allocates its simulation budget to the experiences most useful for current decisions. Replay also occurs during sleep, particularly slow-wave sleep, when sharp-wave-ripple events compress entire behavioral sessions into rapid neural sequences. This sleep replay appears to consolidate the day's spatial and episodic memories into the neocortex for long-term storage — the nightly archive of the day's simulations.

Tolman's VTE — the head-swing at the junction — is, on this account, the behavioral surface of hippocampal forward replay. When the replay sweep runs down one candidate arm and then the other, the rat's head follows the simulated trajectory, turning toward each option as the simulation visits it. What looked like hesitation is the rat's body partially executing the trajectories that the hippocampus is projecting forward.

**Trade-off: Simulation depth versus computational cost**

Hippocampal replay can project trajectories of limited length — typically a few seconds to a few minutes of future time, depending on the species and task. Deeper planning (evaluating many steps ahead, considering branching possibilities, modeling multi-agent dynamics) requires more computation and more time. The brain allocates sharp-wave-ripple events in the seconds and minutes between movements; longer deliberation requires correspondingly more pause time. This is why decision-making at junctions takes longer when the available options are more numerous or more similar in value — the forward replay is doing real work, and more work takes more time. The computational cost of deep simulation is one reason why model-free caching is adaptive: once a route has been evaluated many times, caching its value eliminates the need to re-simulate.

[FIGURE: Two-panel schematic. Panel 1: A rat at a maze junction, head turned left. Below, a hippocampal place-cell activation sequence sweeping left along the maze arm, then reversing and sweeping right. Caption: Forward replay during vicarious trial and error — the hippocampus pre-experiences each candidate trajectory before the body commits. Panel 2: A rat at a reward location. Below, place-cell activation sequence running in reverse from the reward location back to the starting point. Caption: Reverse replay after reward — the brain propagates the reward signal backward through the trajectory for credit assignment.]

### Worked example: What forward and reverse replay accomplish together

Here is a concrete scenario that illustrates both replay types working in sequence.

**Scenario:** A rat has just arrived at a maze junction it has visited many times. To the left is a food location it has reached before. To the right is a new arm it has not yet explored. It pauses at the junction.

**Forward replay (prospective):** Sharp-wave-ripple events fire. Place cells sweep left along the familiar arm, projecting the trajectory toward the known food location, reading off the cached reward value at the end. The sweep then runs right along the novel arm — the place cells there have weaker representations from less experience, and the sweep terminates without reaching a high-value endpoint. The comparison favors the left arm. The rat turns left.

**Reverse replay (retrospective):** The rat reaches the food, consumes it. The reward signal fires. Sharp-wave-ripple events fire again, this time sweeping backward — from the food location, through each place field on the path, back to the junction. The prediction-error signal at the food location is propagated backward, slightly increasing the cached value of each place field that contributed to reaching the reward. The left arm's value representation is strengthened.

**What this accomplishes:** The forward replay evaluated options without the rat having to physically try both. The reverse replay updated values from a single experience without requiring many repetitions of the full trajectory. Together, they allow the model-based system to behave adaptively after a small number of physical experiences, by supplementing physical experience with simulated experience — both prospective and retrospective.

**Common mistake to watch for:** Students sometimes describe replay as a memory process that is separate from planning. The evidence is that the same neural events serve both functions. Sharp-wave-ripple replay during waking behavior is prospective — it runs forward to plan and backward for credit assignment in real time. Sharp-wave-ripple replay during sleep is retrospective — it consolidates the day's experience. The substrate is the same; the temporal context determines the function.

---

## Concept 3: Regret in a Rat — Counterfactual Reasoning at the Neuron Level

### A scene

The rat has just made a mistake. It skipped the chocolate station at a 12-second wait — within its threshold for chocolate, a deal it should have taken. It walked on to the cherry station and found a 28-second wait — above its cherry threshold. It stays anyway, because there is no better option ahead. It is committed to waiting for a flavor it does not especially want.

It looks back. Toward the chocolate station.

While it looks back, Adam Steiner's electrodes are recording from single neurons in the orbitofrontal cortex. The neurons that are firing right now are the neurons that, in earlier sessions, fired *while the rat was at the chocolate station receiving chocolate rewards*. The brain is not encoding the disappointing cherry situation. It is encoding the missed chocolate situation — the state the rat is *not in*, the counterfactual it failed to take.

This is what makes the Steiner-Redish result philosophically significant.

### Regret versus disappointment — a diagnostic distinction

There is a precise cognitive distinction that the Steiner-Redish data exploits, and it is worth being careful about it because the distinction is usually obscured in everyday language.

*Disappointment* is a generic worse-than-expected signal: the outcome was below what the prediction said it would be. It is a pure prediction error — the dopamine signal we met in Chapter 8. Disappointment does not require any representation of an alternative action. It requires only a representation of expectation and outcome.

*Regret* is more specific: the outcome is worse not because it fell below prediction but because a *better option was available and not taken*. Regret requires the agent to represent the counterfactual — the option it could have taken — and compare its value to the actual outcome. Without the counterfactual representation, there is no regret; there is only disappointment.

Steiner and Redish designed their analysis to separate these two signals cleanly. The critical comparison was between two types of bad outcome:

**Type 1:** The rat skips a bad chocolate offer (long wait, above threshold) and finds a bad cherry offer (long wait, above threshold). Outcome is below expectation, but no better option was passed up. This is disappointment.

**Type 2:** The rat skips a *good* chocolate offer (short wait, within threshold — a deal it should have taken) and finds a bad cherry offer (long wait, above threshold). A better option was available and missed. This is regret-eligible.

The look-back behavior appeared *only in Type 2 trials*. The orbitofrontal neurons representing the missed chocolate option fired *only in Type 2 trials*. The subsequent behavioral correction — longer waits at subsequent stations — appeared *only after Type 2 trials*. The two conditions had similar reward prediction errors (both were below expectation), but only the regret-eligible condition produced the look-back, the counterfactual neural encoding, and the behavioral update.

This is the strongest animal evidence for counterfactual reasoning — Rung 3 on Pearl's ladder — in a non-primate mammal. The computation is not metaphorically similar to counterfactual reasoning; it is structurally identical: represent the alternative action, evaluate it against actual outcome, update policy accordingly.

**The parallel in macaques.** The same paradigm logic has been applied in macaques. Atsushi Fujimoto and Hiroshi Yamada, among others, have recorded from macaque orbitofrontal cortex during tasks with regret-eligible and disappointment conditions, finding the same dissociation: the OFC represents the missed better option during regret-eligible outcomes, not just during any below-expectation outcome. The capacity is not unique to rats; it appears across mammalian species in proportion to their prefrontal elaboration, with the representation becoming richer and more sustained in primates.

**Trade-off: Accurate regret versus regret miscalibration**

Regret is a genuinely useful cognitive signal when it is well-calibrated: identifying cases where a better option was available and the policy needs updating is exactly the feedback a model-based learner needs. But regret can be miscalibrated in ways that impose costs. *Counterfactual upward comparison* — fixating on the missed better option beyond what is needed for policy update — is, in humans, a well-documented contributor to depression and anxiety. The rat's look-back is brief and produces an immediate behavioral correction; it does not persist. Human regret can persist far beyond the behavioral horizon where the policy update would remain useful, producing rumination that costs time and affect without generating additional policy improvement. The same machinery that makes adaptive counterfactual reasoning possible makes pathological rumination possible. The clinical literature on depression suggests that the difference lies partly in the prefrontal regulation of when the simulation is terminated.

---

## Concept 4: The Corvids — A Second Solution to the Same Problem

### A scene

A western scrub-jay is in a testing room in Nicola Clayton's laboratory at Cambridge. It has just been given access to two compartments — one of which it has learned, through several days of training, will not contain breakfast the next morning. The other will. The jay is not hungry right now. It has just eaten.

It caches more food in the compartment where there will be no breakfast tomorrow.

It is planning for a future state — hunger — that it does not currently feel.

This is the result that broke the Bischof-Köhler hypothesis. And it came from a bird.

### Two solutions, one function

The western scrub-jay (*Aphelocoma californica*) is a corvid — a member of the crow family — and it earns its living partly by caching food and recovering it later. The caching lifestyle places specific demands on memory and planning: to survive, the bird must remember what it cached, where, and when it was cached (so it can prioritize the perishable items before the shelf-stable ones).

Nicola Clayton and Anthony Dickinson's 1998 *Nature* paper established the episodic-like memory component. Jays were given access to both wax-moth larvae (preferred when fresh, inedible when degraded) and peanuts (shelf-stable). After a short delay, jays preferentially recovered the larvae — the fresh ones were still good. After a longer delay, jays shifted to the peanuts — the larvae had degraded. The jays were not simply preferring one food type. They were integrating information about *what* they had cached, *where*, and *when* — and using that integrated memory to make recovery decisions that depended on all three dimensions simultaneously. The combination, which in humans we associate with episodic memory (memory of specific events as coherent what-where-when wholes), was the first clean demonstration of episodic-like memory in a non-mammal.

The future-planning result followed from work by the Clayton lab and others. Jays given experience that breakfast would be absent in one compartment the next morning cached food there in the evening — more food in the no-breakfast compartment than in the breakfast-available one — *while currently sated*. The caching was motivated by anticipated future hunger, not present hunger. The Bischof-Köhler hypothesis predicted this would be impossible. The jays demonstrated it was not.

Subsequent work extended the picture. Jays re-cache food in private after they have been observed caching — they appear to model the knowledge state of potential thieves (who watched the original caching and might steal from it) and act to defeat that knowledge by moving the cache. This is social simulation: the jay is representing what another agent knows about the jay's own past actions, and planning in response to that representation. We will pick up this thread in Chapter 10.

The neural substrate for corvid simulation is not the hippocampus — or rather, not the hippocampus in the mammalian sense. Birds have no six-layered neocortex. What they have, in the telencephalon, is a dorsal pallium with distinct subregions that modern comparative neuroanatomy has mapped onto mammalian cortical areas by connectivity and molecular markers rather than by anatomy. The corvid equivalent of the hippocampus — the hippocampal formation, present in birds as a structure critical for spatial and episodic memory — is engaged during caching and recovery in the same way that the mammalian hippocampus is engaged during navigation and replay. The prefrontal-equivalent regions of the corvid brain — the nidopallium caudolaterale and related areas — appear to be required for the future-planning and social-inference aspects of caching behavior.

The two solutions — mammalian neocortex-hippocampus-prefrontal and corvid dorsal-pallium-hippocampal-formation-nidopallium — are anatomically distinct. They perform the same computation. They evolved independently in lineages that diverged more than three hundred million years ago. The function is the constraint. The substrate is the variable.

**Trade-off: Specialization versus generalization in simulation**

The corvid simulation capacity has been documented most thoroughly in the specific domain of food caching — a biologically relevant, high-stakes planning context that the species evolved to handle. Whether the same capacity generalizes to arbitrary planning problems is less clear. The mammalian model-based system, implemented in a more anatomically generalized prefrontal-hippocampal network, appears to generalize more broadly — humans and other primates can use mental simulation in domains far removed from spatial foraging. This suggests that the depth and generality of simulation capacity may scale with the anatomical generality of the planning network, not just its presence. The corvid has the rung-3 capacity in its ecological niche; the extent to which it can apply that capacity outside that niche is an open question and an active research area.

---

## Integration: What the Simulator Adds to the Legg-Hutter Definition

The book's working definition of intelligence is the ability to achieve goals across a wide range of environments. Chapter 2 established the cognitive floor — valence-based decision-making in pre-neural systems. Each chapter since has added a layer that widens the range of environments an organism can navigate successfully.

Simulation widens that range in a specific and important way. An organism that can only learn from physical experience needs to encounter every relevant situation many times — at full biological cost and risk. An organism that can simulate can rehearse situations it has never physically been in, evaluate options it has not yet tried, and adapt to environmental changes without failing repeatedly first. The range expansion is qualitative: simulating agents can perform adaptive behavior in environments they have never previously experienced, which purely model-free agents cannot.

The mammalian and corvid cases together establish something essential: this capacity is not tied to any single neural architecture. The hippocampus-prefrontal system in mammals and the pallial-hippocampal-nidopallial system in corvids are anatomically distinct implementations of the same abstract function — run the world forward in the head, compare actual to counterfactual, update policy from the difference. The capacity evolved at least twice because the function is valuable enough to be worth reaching independently, from whatever neural starting materials each lineage had available.

The digital twin is the external version of the same function — a fast, cheap rehearsal of trajectories that the operator has not yet taken, run to inform the choice about to be made. The simulator's reach is wider and its time horizon longer than what any biological brain can hold. The choice of what to simulate, what the answer means, and what to do with it remains on the human side — which is the part that does not extend.

---

## Exercises

### Warm-Up (Direct Application)

**1.** Explain, in your own words, what makes model-based reinforcement learning qualitatively different from model-free. Use the food-devaluation paradigm — where a rat is trained to press a lever for a food that is later poisoned — to illustrate the difference. Which mode of learning would immediately stop pressing the lever after the food is devalued, and why?
*(Tests Learning Objective 1; difficulty: accessible)*

**2.** Place each of the following behaviors on Pearl's three-rung ladder and justify your placement: (a) a rat presses a lever that has historically produced food; (b) a rat evaluates a novel lever by simulating what will happen if it presses it; (c) a rat looks back at a restaurant it just left and encodes the value of the option it should have taken.
*(Tests Learning Objective 2; difficulty: accessible)*

**3.** What is the functional difference between forward replay and reverse replay in the hippocampus? Which one corresponds to prospective planning, and which to credit assignment? Describe the specific behavioral context in which each typically occurs.
*(Tests Learning Objective 3; difficulty: accessible)*

### Application (Translation Required)

**4.** Steiner and Redish designed their analysis to distinguish regret from disappointment using a specific comparison between two trial types. Describe the two trial types, explain why only one is regret-eligible, and explain what finding — behavioral or neural — would be expected if the orbitofrontal cortex were encoding *disappointment* rather than *regret* in the regret-eligible trials. What specific result ruled out the disappointment explanation?
*(Tests Learning Objective 4; difficulty: moderate)*

**5.** Clayton and Dickinson's scrub-jay experiment is often described as evidence for episodic-like memory. Explain what "episodic-like" means in this context — what three dimensions must be integrated simultaneously — and explain why the experimental design demonstrates integration of all three rather than simple preference for one food type over another.
*(Tests Learning Objective 5; difficulty: moderate)*

### Synthesis (Combining Multiple Concepts)

**6.** The chapter argues that simulation evolved at least twice — in mammals and in corvids — on anatomically distinct neural substrates. Write an analysis that: (a) identifies the specific neural structures that mediate simulation in each lineage; (b) explains what the convergence tells us about the relationship between the function (simulation) and the substrate (neural architecture); and (c) evaluates what the convergence evidence implies for the claim that Pearl's Rung 3 counterfactual capacity requires a specific brain structure, such as the mammalian prefrontal cortex.
*(Tests Learning Objectives 3, 4, and 5 in combination; difficulty: challenging)*

### Challenge (Open-Ended, Points Forward)

**7.** Chapter 10 on social intelligence will argue that theory of mind — modeling another agent's beliefs and intentions — is built on the same simulation substrate introduced in this chapter. Using the hippocampal replay framework, propose a hypothesis about what changes when the simulation runs a model of another agent rather than a model of the physical environment. What neural structures, in addition to the hippocampus, would you expect to be recruited? What behavioral signature — analogous to the look-back in the Steiner-Redish paradigm — would distinguish genuine social simulation (modeling another's mental state) from behavioral contagion (automatically mirroring another's visible behavior)? Use the framework from this chapter to design one experiment that would test your hypothesis.
*(Tests Learning Objectives 1–4 combined with forward-looking design; difficulty: advanced)*

---

## Chapter Summary

Here is what you can now do that you couldn't before.

You can distinguish model-free and model-based reinforcement learning at the level of what each requires neurally — the model-free system caches action values in the basal ganglia and retrieves them under the dopamine prediction-error signal; the model-based system maintains an internal world-model in the hippocampal-prefrontal network and evaluates candidate trajectories by simulation before acting.

You can place this distinction on Pearl's ladder: model-free learning operates on Rung 1 (association) and Rung 2 (intervention by lookup); model-based learning enables Rung 3 (counterfactual — what would have happened if I had acted otherwise). The rat's look-back is Rung 3 implemented in OFC neurons.

You have a cellular account of how the hippocampus implements the simulator: forward replay sweeping candidate trajectories at twenty-to-thirty times physical speed during sharp-wave ripples before movement, and reverse replay propagating the reward signal backward through completed trajectories immediately after reward.

You can apply the regret-versus-disappointment distinction to evaluate any putative evidence for counterfactual reasoning: disappointment is a generic prediction error; regret requires neural representation of the missed better option, and the within-trial comparison to distinguish the two is the design the Steiner-Redish study used.

You can evaluate the corvid evidence for episodic-like memory and future planning as convergent evidence that simulation is a function rather than a substrate — reached independently in mammals and corvids from anatomically distinct neural architectures, for the same computational reason.

**The most important claim:** The hippocampus is not just a spatial memory organ. It is a trajectory generator — a structure that runs the world forward in fast neural sequences, in the gaps between physical experience, to allow the animal to plan and assign credit without requiring full physical exposure to every relevant situation. Everything the chapters that follow build on social cognition, theory of mind, and language is downstream of this capacity to run mental simulations of states and transitions that are not currently being physically experienced.

**The Feynman test for this chapter:** Can you explain to someone who has never studied neuroscience why forward replay during a sharp-wave ripple is the brain running a simulation, and why this is different from just remembering where the food was? If you can explain why the replay is prospective (about where the animal is about to go) rather than retrospective (about where it has been), and why that distinction matters for what the animal can do that a purely habit-based system cannot, you understand the chapter's central mechanism.

---

## Connections Forward

Chapter 10 on social and emotional intelligence picks up the simulation substrate directly and asks what happens when the world-model that the hippocampal-prefrontal system runs contains *agents with mental states* rather than just physical environments. Theory of mind is, in this framework, social simulation: running another agent's decision process forward in one's own brain to predict what they will do and plan accordingly. The same neural substrate — the hippocampus generating trajectories, the prefrontal cortex evaluating and selecting among them — is recruited for social prediction, with additional structures (the temporoparietal junction, medial prefrontal cortex) added to handle the specifically social content of the simulated agent's states.

Chapter 14 on metacognition closes a loop with this chapter's Pearl's-ladder framework. Metacognition is simulation applied to one's own cognitive processes: running the question "how confident am I in this answer?" requires modeling one's own knowledge state, which is a simulation problem of the same logical type as modeling the physical or social environment. The scrub-jay that approaches the peephole when it does not know where the food is — Chapter 14's Rung 2 example — is running a simulation of its own knowledge state and acting to close the gap. The rat that looks back at the chocolate station is running a simulation of its own past decision. Both are the hippocampal-prefrontal simulator directed inward.

The digital-twin extension note anticipates Chapter 16 on collective intelligence, where externalized simulation tools — from computational fluid dynamics to simulated patient cohorts to city-scale earthquake models — are examined as components of the collective scientific and engineering practice that constitutes human cumulative culture. The digital twin is the rat's replay sweep, externalized and made durable across generations. Understanding what it can do that the biological simulator cannot — and what it cannot do that the biological simulator still must — is part of what Chapter 16 requires.

---

*Tags: simulation, planning, hippocampal-replay, forward-replay, reverse-replay, sharp-wave-ripples, vicarious-trial-and-error, Tolman, Pfeiffer-Foster, Foster-Wilson, regret, Restaurant-Row, Steiner-Redish, orbitofrontal-cortex, counterfactual-reasoning, Pearl-ladder, model-free-RL, model-based-RL, Bischof-Köhler-hypothesis, scrub-jays, Clayton-Dickinson, episodic-memory, corvids, digital-twins, Balleine-Dickinson, devaluation-paradigm*
