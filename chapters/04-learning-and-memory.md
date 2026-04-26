# Chapter 4: Learning and Memory
## *Pavlov's Dogs and What They Were Actually Showing*

---

## Learning Objectives

By the end of this chapter, you should be able to:

1. **Explain** what Pavlov's conditioning experiments were actually demonstrating about the cerebral cortex, and why the dog and the drool are the wrong place to look
2. **Distinguish** among habituation, sensitization, and associative learning, and place each in its evolutionary and mechanistic context
3. **Trace** the molecular cascade — from serotonin to cAMP to PKA to CREB to new synaptic structure — that underlies short-term and long-term memory in *Aplysia californica*
4. **Describe** the roles of eligibility traces and prediction error in solving the credit assignment problem, and connect them to the Rescorla-Wagner model
5. **Explain** catastrophic forgetting in artificial neural networks and identify why the architecture of biological learning partially solves the same problem
6. **Apply** the Hebbian principle to the NMDA receptor's coincidence-detection function, and explain what long-term potentiation demonstrates that short-term facilitation does not

**Prerequisites:** Chapter 2 (Before Brains: bacteria, slime molds, valence) and Chapter 3 (Steering: the nematode and the minimum architecture for goal-directed behavior). You should be comfortable with the Legg-Hutter working definition from Chapter 1: intelligence as an agent's ability to achieve goals across a wide range of environments. This chapter adds the question of how goals shift.

---

## Why This Chapter Matters

A nematode steers toward food. A sea slug learns to *expect* a shock and withdraws its gill before it arrives. The gap between those two capabilities is what this chapter is about.

The nematode has a fixed mapping from stimulus to response: salt → move toward it; copper → move away. These mappings were set by evolution. The sea slug has something the nematode largely lacks: the ability to *update* those mappings on the basis of individual experience. What the world teaches it, it keeps.

The mechanism that keeps it is one of the most conserved in all of animal biology. The same molecular cascade that lets a sea slug remember a tail-shock for weeks is recognizably present — elaborated, embedded in more complex circuitry, but structurally the same — in the hippocampus of a rat, a rabbit, and a human. Understanding it from first principles is the most direct path to understanding what memory actually is: not a recording, not a filing cabinet, but a precise and regulated modification of synaptic strength.

Understanding it also illuminates the sharpest current gap between biological and artificial intelligence. Modern neural networks can be trained to superhuman performance on specific tasks. They cannot yet be trained on a sequence of tasks without erasing what they learned before. A sea slug solved that problem five hundred and fifty million years ago. This chapter explains how.

---

## 4.1 The Cold Open: The Towers of Silence

St. Petersburg, sometime in the 1890s. Ivan Pavlov is a physiologist of the digestive system who has just noticed something inconvenient.

He is measuring the composition of gastric secretions in dogs — volume, acidity, enzymatic content, timing — and the data are inconsistent. The dogs secrete differently depending on whether they have seen the food, or only smelled it, or only heard the footsteps of the keeper who usually brings it. The nervous system is anticipating meals that have not arrived. The tubes and glands that Pavlov is trying to study are being pre-tuned by a brain that has read the schedule.

He calls these intrusions "psychic secretions," and he means the term physiologically: there is a mechanism in the cerebral cortex that is forming predictive connections between stimuli — between a sound and what the sound reliably precedes. In 1904, Pavlov receives the Nobel Prize for the digestive work. He then spends the next twenty years not studying digestion.

The building he eventually constructs at the Institute of Experimental Medicine is nicknamed the *Towers of Silence*: a set of chambers within chambers, each isolated from vibration and sound, connected to the outside world only by controlled signals. The isolation is not to protect the dogs. It is to protect the measurements. Pavlov wants to know exactly how much a precisely timed sound, presented a precise number of times before a precise quantity of food, changes a precisely measured response. By 1927, when the English translation of *Conditioned Reflexes* appears, he has a worked-out theory of the cortex as a dynamic system of excitation and inhibition — a system that forms new functional bridges between processing centers when the world repeatedly delivers one event before another.

The dog salivating at a bell is what was visible from the outside. The argument was about what the brain is built to do.

The argument was right.

---

## 4.2 Three Kinds of Learning

Before the mechanism, the taxonomy. Not all learning is the same, and the distinctions matter because they appear in evolutionary order, each building on the last.

**Habituation** is the simplest: the gradual weakening of a response to a repeated stimulus that turns out to be irrelevant. The gill-withdrawal reflex in a sea slug, triggered repeatedly by gentle siphon touches that are never followed by anything harmful, shrinks and eventually disappears. No new association is formed. A response is simply turned down.

We met habituation in Chapter 2 in the slime mold that eventually crosses a quinine barrier. It is present in cnidarians, in nematodes, in organisms with no centralized nervous system at all. It requires only one thing: a way to let a repeatedly active connection become less effective. It is the floor.

**Sensitization** is the counterpart: the strengthening of a response after a noxious event. A sea slug that has been shocked withdraws its gill harder and faster at the next gentle touch — even a touch nowhere near where the shock landed. Sensitization is also non-associative; it doesn't bind one stimulus to another. It simply turns up the volume on existing reactivity. The world has signaled danger; be more responsive to everything.

**Associative learning** is different in kind, not just degree. Two events that were previously unrelated become linked by experience, so that the first reliably predicts the second. Pavlov's dogs heard a metronome, and through training the metronome came to predict food, and the dogs salivated at the metronome alone. The structure is: *if A, then expect B*. The organism now has a model of a causal relationship in its local world.

For most of the twentieth century, the assumption was that associative learning required a centralized nervous system. Cnidarians — jellyfish, sea anemones, hydras — were studied extensively and showed habituation and sensitization but had failed, in experiment after experiment, to demonstrate classical conditioning.

In 2023, that assumption broke. Gaëlle Botzer and colleagues at Fribourg and Barcelona trained the starlet sea anemone *Nematostella vectensis* — a creature with only a nerve net, no centralized brain — by pairing light with electric shock over many trials. After training, the anemones retracted their bodies to light alone. Roughly seventy-two percent of them. Well above chance. Well above any unpaired control.

A creature without a brain had learned the *if-then*.

The floor of associative learning is therefore lower than the brain. What that floor requires, biophysically, is a single thing: a way for two near-simultaneous signals at a synapse to leave a longer-lasting mark than either signal alone. That requirement — what it is made of, how it works, and why it is built the way it is — is the deep mechanism this chapter explains.

---

## 4.3 The One Concept: The Molecule That Holds the Past in Place

### Why Eric Kandel Chose a Sea Slug

In 1962, Eric Kandel made the kind of choice that defines a scientific career. He wanted to find the molecular basis of memory. He chose *Aplysia californica*, a marine slug the size of a small dinner plate.

Other neuroscientists thought this was eccentric. They were studying mammalian cortex — thousands of neurons per column, complex circuitry, close relatives of the human brain. Kandel chose a creature with approximately twenty thousand neurons total, some so large they can be seen with the naked eye, repeatable from animal to animal, individually nameable. The bet was deliberate: whatever the molecular mechanism of memory turned out to be, it would be conserved across animal phyla. The way an *Aplysia* remembered would be, in chemistry if not in scale, recognizably the same as the way we remember.

The bet paid the Nobel Prize in 2000.

[FIGURE: Schematic of *Aplysia californica* showing the gill, mantle, and siphon, with the key neural circuit: siphon sensory neuron → motor neuron → gill, with a tail sensory neuron projecting to a serotonergic interneuron that modulates the sensory-to-motor synapse. Label each neuron, each synapse, and each information-flow arrow. Show the gill-withdrawal reflex path as the thickest line. The student should notice that the modulatory input (from tail shock via serotonin) arrives on the sensory terminal, not on the motor neuron directly.]

### The Behavior

The gill-withdrawal reflex is simple and precisely measurable. *Aplysia* breathes through a delicate gill it normally extends from its mantle cavity. Touch the siphon — the small tube that draws water across the gill — and the gill retracts rapidly into the protected space beneath the mantle. This reflex is modifiable by experience.

Touch the siphon repeatedly with no consequence: the retraction shrinks. Habituation.

Deliver a single strong shock to the tail: the retraction at the next siphon touch is dramatically amplified, and stays amplified for hours, sometimes days. Sensitization.

Repeatedly pair siphon touch with tail shock, reliably: the siphon touch alone begins to trigger gill withdrawal that resembles the response to the shock itself. Associative conditioning.

Three behaviors. One animal. One synapse at the center of each.

### Short-Term Memory: The cAMP Cascade

Sensitization begins with what happens at the tail. A noxious shock activates a population of serotonergic interneurons whose job is to release serotonin onto the axon terminals of the siphon's sensory neurons — exactly where those terminals form synapses with the motor neurons.

Here is what serotonin does when it arrives at those terminals:

$$\text{5-HT receptor} \rightarrow \text{adenylyl cyclase} \uparrow \rightarrow \text{cAMP} \uparrow \rightarrow \text{PKA} \uparrow \rightarrow \text{K}^+ \text{ channel phosphorylation} \rightarrow \text{broadened action potential} \rightarrow \text{more Ca}^{2+} \text{ entry} \rightarrow \text{more glutamate per spike}$$

Read that chain slowly. Serotonin is not directly causing the gill to retract harder. It is changing how the *next* spike from the sensory neuron will behave. The action potential, when it next arrives, will last slightly longer. That slightly longer spike admits slightly more calcium. That extra calcium drives slightly more glutamate into the synapse. The motor neuron receives a stronger signal and contracts the gill more forcefully.

The synapse has been *facilitated*. Not by changing its physical structure — nothing has grown or been pruned — but by chemically retuning proteins that already exist. This is short-term sensitization, and it lasts minutes to hours.

### Long-Term Memory: Building It Into Structure

Minutes to hours is useful. Weeks is better. The molecular transition from short-term to long-term sensitization is one of the most elegant mechanisms in neuroscience, and it turns on a single bottleneck: whether the cascade reaches the nucleus.

Short-term sensitization runs entirely in the cytoplasm and at the membrane. It does not require new protein synthesis.

Long-term sensitization does. When training involves *repeated* tail shocks — when serotonin pulses arrive multiple times across hours — enough PKA accumulates and remains active for long enough that some PKA molecules translocate from the cytoplasm into the nucleus. There, PKA phosphorylates a transcription factor called **CREB-1** (cAMP Response Element-Binding protein 1). Phosphorylated CREB-1 binds to specific DNA sequences and initiates transcription of genes whose protein products do something structural: they grow new synaptic connections.

The synapse does not merely become more efficient. It physically expands. The number of active zones — the release sites where vesicles fuse and glutamate escapes — increases. The memory has been committed to structure, where it is far more resistant to erasure.

### The Brake: CREB-2

There is one more piece, and it is the one that matters most for understanding why biological memory is built the way it is.

Dusan Bartsch and colleagues in Kandel's laboratory reported in 1995 that the bottleneck for long-term memory formation is not the activator, CREB-1. It is a *repressor* called **CREB-2**. CREB-2 sits on the same DNA regulatory sites that CREB-1 wants to bind, blocking access. Long-term memory requires both that CREB-1 be activated *and* that CREB-2 be simultaneously deactivated.

The experiment that proved this is striking in its simplicity. Inject anti-CREB-2 antibodies directly into a sensory neuron — releasing the brake — and a single brief pulse of serotonin that would normally produce only short-term facilitation lasting an hour or two is sufficient to drive long-term, structurally stable synaptic growth. Remove the repressor, and a single signal does the work that normally requires many.

Why does this brake exist? Consider the alternative. If every serotonin pulse committed to permanent synaptic growth, the machinery would be saturated within hours. The neuron has finite resources: finite membrane space for active zones, finite vesicle production capacity, finite metabolic budget. An unrestricted CREB pathway would rapidly tile every synapse with maximal connections, filling the system with noise.

CREB-2 is not a redundancy or an error. It is the filter that ensures only sufficiently strong or sufficiently repeated signals cross the threshold to permanent structure. It is the system's quality control for what is worth keeping.

This is the mechanism Hebb predicted without knowing it. His 1949 rule — *neurons that fire together, wire together* — is a behavioral summary of everything above. The molecular details Hebb lacked: the cAMP cascade, the CREB gateway, the new synaptic growth. The principle he had exactly right.

[FIGURE: Two side-by-side panels showing short-term vs. long-term sensitization. Left panel: serotonin → cAMP → PKA → K+ channel phosphorylation; no nuclear involvement; label "minutes to hours." Right panel: same cascade extended, with a PKA arrow entering the nucleus, phosphorylating CREB-1, CREB-2 blockade shown as a barrier that is lifted, gene transcription, and new synaptic terminal growth indicated structurally; label "days to weeks." The CREB-2 repressor should be visually prominent in both panels — present and blocking in the left, displaced in the right. The student should notice that the only structural change in the right panel is CREB-2 displacement and the downstream growth it enables.]

### LTP: The Same Trick, Vertebrate Edition

Twenty-four years after Kandel picked up his first sea slug, Tim Bliss and Terje Lømo were recording from the rabbit hippocampus. In 1973, in *The Journal of Physiology*, they reported that brief high-frequency electrical trains delivered to hippocampal inputs produced **long-term potentiation** — LTP. Synapses that had been stimulated strongly stayed strong. The effect lasted hours in their initial experiments; subsequent work showed it could last days, weeks, and with sufficient training, indefinitely.

The vertebrate version of what Kandel had been studying in a slug.

The mammalian version adds one feature the *Aplysia* circuit does not need. Recall that Hebb's rule requires co-activity: the presynaptic neuron must fire *and* the postsynaptic neuron must be active for the synapse to strengthen. In the *Aplysia* system, this conjunction is enforced by timing — serotonin arrives when the sensory neuron has just been active. In the hippocampus, the conjunction is enforced by a specific protein: the **NMDA receptor**.

The NMDA receptor is a coincidence detector built into the postsynaptic membrane. Its channel is normally blocked by a magnesium ion ($\text{Mg}^{2+}$) that occupies the pore at resting membrane potential. The magnesium is expelled only when the postsynaptic membrane is already substantially depolarized — when the postsynaptic neuron is already receiving strong excitatory input. For the channel to open, two conditions must hold simultaneously:

1. The presynaptic cell must be releasing glutamate (which binds the NMDA receptor's glutamate site)
2. The postsynaptic membrane must already be depolarized enough to have expelled the magnesium block

This is a logical AND gate implemented in a protein. When both conditions are met, calcium pours through the NMDA channel into the postsynaptic cell. That calcium triggers the kinase cascade — including ultimately CREB-mediated transcription — that Kandel described in the slug. The synapse strengthens. The memory forms.

Half a billion years separate the *Aplysia* sensory-to-motor synapse from the hippocampal CA1 pyramidal cell. The molecular elaboration is real and significant. But the trick — two signals arriving together at a synapse cause that synapse to become more likely to transmit those signals in the future — is the same trick.

---

## 4.4 The Trade-Off: Credit Assignment and Prediction

### The Problem of Timing

Learning from experience requires solving a problem that is not obvious until you examine it carefully. Reward and punishment do not arrive at the moment of the action that earned them. The sea slug's tail shock arrives *seconds after* the gill withdrawal that the siphon touch triggered. If that siphon touch is going to be linked to the shock — if the conditioned response is to form — something has to tag the recently-active synapse so that when the serotonin pulse arrives, it finds the right target.

This tag is called an **eligibility trace**. In *Aplysia*, it is implemented in the slow time-course of cAMP and the gating of CREB. When a sensory neuron fires, cAMP does not disappear instantly. It persists, briefly, at slightly elevated levels — marking the synapse as recently active. When serotonin arrives within that window, it finds a synapse already primed, and the cascade runs more efficiently. The eligibility trace is the molecular memory of *I was just used*, persisting long enough to be stamped if a reward signal arrives.

This is not the mathematically optimal solution. The optimal solution for training a feedforward neural network is backpropagation — computing the precise gradient of the error with respect to every weight and adjusting each by exactly the right amount. Backpropagation is elegant. There is no known biological implementation of it. The wiring it requires — every synapse receiving information about the global error and the entire chain of partial derivatives from output back to itself — does not exist in any nervous system we know of.

Real biology uses local rules: eligibility traces, neuromodulators that broadcast a diffuse reward signal, Hebbian co-activity at the synapse. The result is slower and less precise than backpropagation. It has two properties that backpropagation in its standard form lacks. It is local. And it does not catastrophically forget.

### What the Prediction Does

The second constraint on biological learning comes from what the animal does with its predictions.

Leon Kamin observed in 1968 that if you first train an animal that stimulus A predicts reward, then train it on compound A+B predicting the same reward, the animal learns nothing new about B. The reward is already fully predicted by A. B has no informational work to do. This effect — *blocking* — reveals that the animal is not simply recording correlations. It is maintaining a prediction, and it updates only when the prediction is wrong.

Robert Rescorla and Allan Wagner formalized this in 1972:

$$\Delta V_A = \alpha_A \cdot \beta \cdot (\lambda - V_{\text{total}})$$

where $V_A$ is the associative strength of stimulus A, $\alpha_A$ is A's salience, $\beta$ is the learning rate, $\lambda$ is the maximum possible association, and $V_{\text{total}}$ is the total predictive strength of all cues currently present. The key term is $(\lambda - V_{\text{total}})$: the prediction error, the gap between what arrived and what was expected.

When the reward is already fully predicted, $\lambda - V_{\text{total}} = 0$. No learning. Kamin's blocking, derived from first principles.

When something unexpected arrives, $\lambda - V_{\text{total}} > 0$, and learning proceeds in proportion to the surprise.

Wolfram Schultz confirmed the biological implementation of this logic in the 1990s. Dopamine neurons in the midbrain — part of the circuit we will examine fully in Chapter 8 on reinforcement — fire in exact correspondence to prediction error. Unexpected reward: dopamine neurons fire. Predicted reward fails to arrive: they fall silent below baseline. Reward arrives exactly as predicted: their rate does not change. The Rescorla-Wagner prediction error, implemented in dopamine, is what the brain uses to decide when to update what it knows. Learning is gated by surprise, and the gate is a neurotransmitter.

---

## 4.5 The Trade-Off: Why the Sea Slug Doesn't Forget

### Catastrophic Forgetting

Train a modern artificial neural network on Task A until it performs well. Then train it on Task B. Its performance on Task A collapses. The weights that encoded the solution to A have been overwritten by the optimization process for B. This is catastrophic forgetting, documented clearly since the 1980s, and it has not been fundamentally solved in standard architectures.

The reason is structural. Backpropagation adjusts every weight in the network on every training step, nudging each weight toward whatever reduces the current loss. If the current training data is Task B, every weight is nudged toward Task B, regardless of what each weight was previously doing for Task A. There is no protection. There is no gate. The system has no way to say: *this weight matters for something I already know; be careful here*.

### Why Biology Does Not Have This Problem

The *Aplysia* does not do this. Train a sea slug to associate one odor with shock, then train it on a second odor. It retains the first association. Multiple memories coexist in the same nervous system without mutual erasure.

The reason is exactly what Section 4.3 described. Synaptic changes in biological systems are:

**Sparse.** Not every synapse changes for every new experience. Only synapses that were recently active and received a coincident modulatory signal undergo modification. The sensory neurons that respond to odor A are not the same neurons responding to odor B; the modifications for each memory occur in largely non-overlapping sets of synapses.

**Protected by the CREB gate.** Long-term memories are not overwritten by casual experience. The CREB-2 repressor ensures that only repeated or strong signals reach the threshold for structural change. A single encounter with a new stimulus does not wipe out weeks of prior learning.

**Local.** Each synapse decides its own fate based on its own activity and a diffuse neuromodulatory signal. There is no global optimizer sweeping through all connections and nudging them simultaneously toward a new objective.

In 2017, James Kirkpatrick and colleagues at Google DeepMind published "Overcoming catastrophic forgetting in neural networks" in *PNAS*, proposing a fix called **Elastic Weight Consolidation** (EWC). The idea: after training on Task A, measure which weights are most important for that task's performance. When training on Task B, apply a mathematical penalty — a stiffer resistance to change — to those important weights. The paper explicitly cited biological synaptic consolidation as the conceptual model.

EWC works, partially. The state of the art has largely moved to *experience replay* — storing a subset of old training examples and interleaving them with new ones, so the network is perpetually retrained on a mixture of old and new. This is computationally expensive. It is also, tellingly, closer to what the mammalian brain appears to do during sleep: the hippocampus replays recently encoded memories to the cortex, consolidating them into long-term storage rather than allowing them to be overwritten by the next day's new experience.

The problem that occupied hundreds of machine learning researchers across four decades was solved — in a different, slower, less precise, but fundamentally workable way — by *Aplysia* roughly five hundred and fifty million years before the first transistor.

---

## 4.6 The Strange Case of the Headless Worm

Before leaving this chapter I want to include a result I cannot fit cleanly into the story I have been telling, and I include it precisely because the story is not as tidy as this chapter's structure implies.

In 2013, Tal Shomrat and Michael Levin at Tufts University trained planarian flatworms to associate a rough-textured floor with the presence of food. Then they cut off the worms' heads.

After approximately two weeks, each worm had regenerated an entirely new head, including an entirely new brain, from the tail fragment. When returned to the training context, the retrained worms reacquired the food-rough-floor association significantly faster than naive controls that had never been trained.

Some portion of the memory had survived the complete destruction and replacement of the brain.

Where it was stored is not settled. Candidates include bioelectric gradients maintained in non-neuronal cells, patterns of DNA methylation in the body's remaining tissues, or something else we have not yet identified. The CREB cascade described in Section 4.3 operates at synapses that no longer existed after the head was removed. Whatever these worms retained, it was not stored in the synapse — at least not in the synapses that were destroyed.

I present this not as a footnote but as a live scientific question. Either there is a non-synaptic substrate for at least some forms of memory that the field has systematically underexplored, or planarians are doing something genuinely different from the bilateral nervous system lineage that produced *Aplysia* and mammals. Both possibilities deserve serious consideration. Neither has been excluded.

The synaptic account of memory described in this chapter is almost certainly correct for the animals where it has been studied in detail. It may not be complete.

---

## 4.7 What We Have, and Where This Leaves Us

A nervous system that can learn associatively has something no amount of hardwired steering provides: the ability to update what counts as a threat or a reward on the basis of individual experience.

The nematode of Chapter 3 steers beautifully. Its valence assignments — salt is good, copper is bad — were calibrated by evolution and are largely fixed. The sea slug also has hardwired reflexes, but its reflexes exist in a medium that can be modified. Pair siphon touch with tail shock enough times, and the slug treats siphon touch as a threat. Expose it to a reliable food cue, and the slug approaches more eagerly. The animal's map of what the world means has changed: locally, specifically, reversibly.

By the Legg-Hutter definition, this is a meaningful expansion of intelligence. The slug that has learned is better at achieving its goals across a range of environments than the slug that has not, because its predictions about those environments are more accurate. Learning is what makes experience accumulate into improved performance. Memory is what makes learning durable.

The CREB-2-gated transition from short-term facilitation to long-term structural change is the mechanism by which the nervous system decides: *this is worth keeping*. The decision is not made consciously, and not by any central authority. It is made by each synapse, under molecular rules that evolution built to balance two competing pressures: don't overwrite too easily, and don't stay too rigid.

But the organism that emerges from this process does not, as far as we can determine, feel anything about it. The gill-withdrawal reflex getting stronger is not accompanied by anything we would recognize as the experience of fear. The sea slug's nervous system encodes what to do differently, without apparently encoding what it is like to be in danger.

Chapter 5 is about an organism where that line becomes genuinely hard to draw. The bee, whose brain weighs a milligram, may be the first animal in this book where the word *emotion* earns serious scientific consideration.

---

## Summary

**The key mechanism:** Long-term memory is structurally encoded in synaptic weight. The transition from a fleeting chemical change (cAMP, PKA) to a durable structural change (new synaptic terminals, new active zones) is gated by CREB-1 activation and CREB-2 deactivation. This gate protects existing memories while admitting new ones that exceed the threshold.

**The key principle:** Neurons that fire together, wire together — but only when the activity is strong enough, or repeated enough, to clear the molecular threshold for structural change. Hebb's rule is not always on. It is gated, and the gate is CREB-2.

**The key insight about AI:** Catastrophic forgetting in artificial neural networks is the consequence of using a global optimization process that updates all weights simultaneously toward a new objective. Biological learning avoids this through sparse, local, gated modification. The sea slug solved this problem before the Cambrian.

**The common mistake to watch for:** Treating memory as a recording. Memory is not stored information in the sense that a file is stored on a hard drive. It is a modification of synaptic transmission probability, physically instantiated in the structure of the synapse. There is no memory that exists independently of the synapse that holds it — except, unaccountably, in planarians after decapitation.

**What you should now be able to teach someone else:** Why the NMDA receptor is a coincidence detector, and why that makes it the cellular mechanism of Hebbian learning. Why CREB-2 exists, and why an animal without it would have a serious memory problem. Why a neural network trained sequentially on two tasks forgets the first one, and why *Aplysia* does not.

---

## Exercises

### Warm-Up

1. Arrange the following in order of when each likely first appeared in evolutionary history, and briefly explain the evidence for your ordering: long-term potentiation in the hippocampus; habituation in a cnidarian nerve net; associative conditioning in *Nematostella vectensis*; NMDA-receptor-dependent LTP in a vertebrate.

2. In your own words, explain what a CREB-2 repressor does and why its existence is evidence of a design constraint rather than a design flaw. What would you predict would happen to an animal whose CREB-2 gene was silenced in all neurons?

### Application

3. The Rescorla-Wagner model predicts that learning is proportional to prediction error: $\Delta V = \alpha \beta (\lambda - V_{\text{total}})$. Use this model to explain blocking. If stimulus A already perfectly predicts reward ($V_A = \lambda$), what does the model predict will happen to $V_B$ when the compound A+B is reinforced? Is this prediction confirmed by Kamin's experiments?

4. A researcher trains a rat in a water maze, then injects a drug that blocks all NMDA receptors in the hippocampus for 48 hours. Predict, with mechanistic reasoning, what will happen to: (a) the rat's performance on the already-learned maze during the 48-hour window; (b) the rat's ability to learn a new maze during the 48-hour window; (c) the rat's performance on a new maze learned after the drug wears off.

5. A sea slug trained to associate odor A with food reward is then trained, in a separate chamber, to associate odor B with shock. After both training periods, both odors are presented simultaneously. Using what you know about eligibility traces and the Rescorla-Wagner framework, predict the animal's response. What additional information would you need to generate a quantitative prediction?

### Synthesis

6. Elastic Weight Consolidation was explicitly modeled on biological synaptic consolidation. List three specific features of biological memory described in this chapter that EWC attempts to replicate, and for each feature evaluate whether EWC fully replicates it, partially replicates it, or fails to replicate it. What would a more complete biological analog look like computationally?

7. The CREB-2 gate ensures that only strong or repeated signals commit to structural change. But consider an animal that encounters a single, highly salient event — a near-predation experience — that it would be strongly adaptive to remember permanently from one trial. Does the CREB-2 gate create a problem here? How might the nervous system handle this case without relaxing the gate? What evidence bears on your answer?

### Challenge

8. Shomrat and Levin's planarian result — memory surviving complete brain regeneration — presents a genuine puzzle for the synaptic account. Construct two competing hypotheses for where the memory is stored in planarians: one consistent with the synaptic account (memory is preserved in neurons growing from the tail's existing nervous tissue remnants), and one requiring a fundamentally different account (memory is stored in a non-neuronal substrate). Design one experiment that would distinguish between these hypotheses. What result would count as decisive evidence for each?

---

## Connections Forward

Chapter 5 introduces an animal — the honeybee — whose neural circuits have been analyzed in comparable mechanistic detail to *Aplysia*, but whose behavioral repertoire includes something the sea slug arguably lacks: a state that modulates behavior globally, persists beyond the stimulus that caused it, and has a valence that colors its subsequent choices.

The technical term for that state is a functional analog of emotion. Chapter 5 will ask whether that term describes what's happening or tracks something real about what it is like to be a bee. The CREB cascade does not settle that question. Neither does the Rescorla-Wagner model. That is where the book's central problem — the gap between mechanism and experience — begins to feel genuinely acute.

---

*What would change my mind on the deep mechanism: a demonstration that one of the core molecular components of long-term memory in the bilaterian lineage — CREB-1, CREB-2, the cAMP–PKA axis, NMDA-mediated coincidence detection — is absent in an animal that nonetheless reliably forms long-term associative memories. The conservation of this cascade from sea slug to mammal is among the strongest evidence in all of neuroscience. A clean exception would require substantial revision.*

*Still puzzling: the planarian result. Shomrat and Levin's finding holds up well enough that I cannot dismiss it, and I cannot, at the level of the molecular cascade described in Section 4.3, explain how an environmental association would survive the complete loss and regeneration of every synapse in the head. Either there is a non-synaptic substrate for memory that the field has systematically underexplored, or planarians are doing something genuinely different. Both options are worth taking seriously.*

---
