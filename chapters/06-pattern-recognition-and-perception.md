# Chapter 6: Pattern Recognition and Perception
## The Fish That Picked a Face Out of Forty-Four

---

### Learning Objectives

By the end of this chapter, you should be able to:

1. **Explain** why discrimination and generalization are computationally in tension, and describe how the vertebrate cortex resolves that tension through a single unified architecture
2. **Describe** the three operations — dimensionality expansion, sparse coding with lateral inhibition, and recurrent auto-associative completion — and explain how each one contributes to solving a specific part of the perception problem
3. **Trace** the evolutionary origin of the cortical pattern-recognition architecture from lamprey to fish to mammal and identify what is structurally conserved across that span
4. **Evaluate** the CNN-cortex parallel: identify where the analogy holds, where it breaks down, and why the parts of the brain that engineers did not copy are precisely the parts that explain the remaining performance gaps
5. **Apply** the auto-associative memory framework to analyze a recognition task and predict what would break if any one of the three operations were removed

**Prerequisites:** Chapter 3's treatment of labeled-line sensory encoding and the role of interneurons in suppressing competing signals. Chapter 4's account of Hebbian plasticity and how co-firing strengthens synaptic connections. Chapter 5's concept of neuromodulatory states affecting perceptual interpretation.

**Where this fits:** Chapter 3 showed us how a minimal nervous system converts sensory input into directed behavior. Chapter 6 asks what happens when the nervous system needs to recognize the *kind* of thing producing the input — not just whether it is good or bad, but what object it is, from any angle, in any light. That requires a fundamentally different kind of architecture.

---

### Chapter Opening: A Photograph Over a Tank

The archerfish does not have a face area.

It does not have a neocortex, that six-layered sheet of tissue that neuroscientists sometimes call the seat of intelligence in mammals. It has a brain the size of a pea, organized around a three-layered structure hundreds of millions of years old. It spends its days hovering just below the water surface, watching the overhanging vegetation for insects, calculating the refraction of light through the water-air boundary, and spitting a precision jet to knock its targets down.

In 2016, researchers at the University of Queensland put two photographs of human faces above a tank of archerfish. The faces were unfamiliar — the fish had never encountered them before. One photograph was paired with a small sucrose reward. The other was not. The fish learned which face meant food.

Then the experiment got harder. The researchers replaced the trained face with a lineup. One of the forty-four photographs was the familiar, rewarded face. The other forty-three were new faces the fish had never seen. Which would it spit at?

It spat at the right face. Eighty-one percent of the time. The experimenters controlled for color, overall brightness, and head shape — none of those simpler cues explained the performance. The archerfish was discriminating human faces from a crowd of human faces, using machinery that evolution assembled before the first dinosaur walked on land.

I want to start here because this result is surprising in exactly the right direction. The surprise is not that the fish is clever. The surprise is that we ever thought face recognition required anything the fish does not have. The architecture that does it — the architecture we are about to examine in detail — is not a special innovation of primates, or of mammals, or even of vertebrates with a neocortex. It is the foundational vertebrate solution to a computational problem that appeared the moment the first animal with eyes had to tell apart objects in a visual world.

The fish has been solving this problem for five hundred million years. The chapter is about how.

---

## 6.1 The Central Tension of Perception

Before any architecture can be examined, the problem it solves needs to be stated precisely. Because the central tension of perception is not obvious, and the architecture only makes sense once you see what it has to resolve.

Any perceptual system that acts intelligently in the world has to do two things that pull against each other.

**The first is discrimination.** Two stimuli that are similar but different must be kept distinct. The predator and the harmless decoy have similar silhouettes — but they are not the same thing, and collapsing them into one representation will get you killed. The toxic berry and the edible one look nearly identical. The threatening call and the alarm-free call differ by a few acoustic parameters. A perceptual system that cannot discriminate similar inputs cannot act appropriately — it treats the wrong thing as safe, or the right thing as dangerous, because it cannot tell them apart.

**The second is generalization.** A stimulus encountered in a new form must be recognized as the same kind of thing encountered before. The predator from above and the predator from below cast different silhouettes onto the retina. The mate's call garbled by wind has different acoustic structure from the mate's call in still air. The face in dim light has different luminance values from the face in bright light. A perceptual system that cannot generalize across these variations cannot recognize anything it has not seen in that exact form. It would need to encounter every instance separately, learning nothing about the category it belongs to.

Discrimination and generalization are in tension because they require opposite operations on the input. Discrimination needs representations that are *far apart* for similar inputs — so that a small difference in the input produces a large difference in the representation, keeping the two stimuli distinct. Generalization needs representations that are *close together* for different instances of the same category — so that the predator from above and the predator from below produce similar representations that lead to the same behavioral response.

There is a name for the difficulty of satisfying both at once: the *stability-plasticity dilemma*. Too much discrimination, and the system cannot generalize. Too much generalization, and the system cannot discriminate. A perceptual system that solves both problems simultaneously — that keeps similar things distinguishable while recognizing different instances as the same kind — is doing something genuinely hard, and the vertebrate cortex has been doing it for longer than the dinosaurs.

There is a third problem that compounds both: **invariance**. Not just discrimination and generalization across instances, but recognition that is *invariant* to changes in viewpoint, scale, rotation, illumination, and partial occlusion. The frog is the frog whether you see it from above, from the side, or upside down. The face is the face in sun or shadow, at forty-four angles and from every demographic. A perceptual system without invariance recognizes only what it has already seen, in the form it has already seen it. It cannot transfer knowledge to new situations.

Invariance is the hardest of the three, and it is where the fish brain still embarrasses our best engineering. I will come back to this.

---

## 6.2 The Blueprint That Survived Five Hundred Million Years

The vertebrate pallium — the cortex's ancestor — has a conserved history that makes everything else in this chapter possible.

In 2017, Shreyas Suryanarayana and colleagues at the Karolinska Institute published the most careful comparison yet of the lamprey pallium to the mammalian cortex. The lamprey split from the rest of the vertebrate lineage approximately five hundred million years ago. It has no jaw, no paired appendages, no bones. It is about as primitive a vertebrate as anything still living. And its lateral pallium, when examined at the level of cellular types, projection patterns, and molecular markers, shows a three-layered structure with glutamatergic projection neurons in an outer layer, a mixed inner layer, and a plexiform zone where incoming inputs meet dendrites — closely matching the organization of the ancient cortical regions in reptiles and mammals.

This is not a superficial resemblance. The lamprey pallium contains cells that are transcriptionally similar to excitatory neurons in mammalian cortex; it receives input from the olfactory bulb with the same topology as the mammalian piriform cortex; and it projects back to the deeper brain structures that execute behavioral output via the same basic route. The blueprint, in the relevant architectural sense, has been preserved.

What the blueprint specifies is a sheet of excitatory neurons — the *pyramidal cells* — embedded in a mesh of inhibitory interneurons, with inputs arriving from the senses and outputs leaving toward motor structures. The neurons are connected to each other by horizontal *recurrent collaterals* — axons that travel sideways through the cortical sheet and synapse on neighboring excitatory cells. The interneurons perform *lateral inhibition* — they suppress activity in neurons that are not the most strongly driven by the current input.

These three features — excitatory projection cells, inhibitory interneurons, recurrent excitatory connections — are the three elements the architecture needs. The magic is in how they interact. Let me build up that interaction one piece at a time.

---

## 6.3 Three Operations, One Architecture

The clearest way to see how the cortex solves discrimination and generalization simultaneously is through the olfactory system, because the olfactory version of the problem is the oldest and most transparent. Most of the vertebrate pallium's deep history is olfactory; vision arrived later and was plugged into hardware originally designed for smell.

The fish has several hundred olfactory receptor types in its epithelium. Each receptor responds to a broad range of odorant molecules with varying affinity; each odorant activates a broad range of receptor types at varying intensities. The signal arriving at the cortex is a high-dimensional pattern of activity across hundreds of receptor channels simultaneously — a *combinatorial code* whose potential diversity, across only a few hundred receptor types, runs into the trillions of distinguishable patterns. The task: identify which patterns belong to known categories (food, predator, mate, competitor), generalize across slight variations within a category, and discriminate between categories even when they overlap.

Here are the three operations that do this.

**Operation 1: Dimensionality expansion.** Fibers from the olfactory bulb project diffusely onto the pyramidal neurons of the lateral pallium — the piriform cortex in mammals, and its equivalent in fish. Each bulb fiber connects to many cortical neurons; each cortical neuron receives inputs from many bulb fibers. The effect is that the high-dimensional input representation at the bulb is projected onto an *even higher-dimensional* representation at the cortex. The cortex has many more cells available to represent the signal than the input pathway had channels to carry it.

Why does this help? Here is the key: when you project a set of points into a higher-dimensional space, points that were close together in the original space tend to spread apart in the new space. Two odors that produced similar patterns across the receptor array — close together in input space — become less similar in the cortical representation, simply because the expanded dimensionality provides more room for the representations to diverge. The cortex does not need to be clever about separating similar inputs; the expansion does it geometrically. This is the mathematical insight underlying the kernel trick in support vector machines, the cover theorem in information theory, and the random projection method in compressed sensing. The brain had it first.

**Operation 2: Sparse coding with lateral inhibition.** The expanded representation is not just big — it is *sparse*. Of all the cortical neurons potentially responsive to a given odor, only a small fraction — a few percent — actually fire. The rest are held silent by the lateral inhibitory interneurons. This happens because inhibitory interneurons receive input from the active excitatory neurons and then broadly suppress the less-strongly driven ones, enforcing a kind of winner-take-most competition. Only neurons that receive particularly strong input survive the suppression.

The sparseness is essential for discrimination. Two odors that produced overlapping sets of active neurons at the input — whose receptor patterns were partially similar — tend to activate *different* sets of sparse cortical neurons after the competition. The inhibitory competition winnows the overlapping representations apart. What was similar becomes distinct. Pattern separation is achieved.

And sparseness has a further virtue: it makes the representations *combinatorially distinct* even when the inputs are not. Two odors with twenty percent input overlap might produce cortical representations with only one percent overlap, because the inhibitory competition amplifies small differences into large ones. The signal-to-noise ratio on the discrimination task improves, at the cost of some information about the details of the input. That is an acceptable tradeoff.

**Operation 3: Recurrent auto-associative completion.** This is the operation that handles generalization, and it is the one that makes the architecture genuinely remarkable.

The pyramidal neurons in the piriform cortex are not just independent feature detectors. They are connected to each other by the horizontal recurrent collaterals I mentioned. These connections are modifiable by Hebbian plasticity — exactly the mechanism characterized in Chapter 4 for *Aplysia* and for hippocampal LTP. When a particular odor is experienced, the set of cortical neurons that fire together strengthen their connections to each other. This happens gradually, across many exposures.

After these connections have been strengthened, something changes about how the cortex processes that odor. If a subsequent presentation of the odor is partial — the concentration is lower, or the wind has blown away some of the volatile compounds, or the odor is partially masked by a background smell — the incoming signal activates some of the learned ensemble but not all of it. The activated neurons fire. Those firing neurons are strongly connected to the other members of the learned ensemble via the strengthened recurrent collaterals. Those connections pull the other ensemble members into firing. The cortex *completes the pattern* — it fills in the missing portions of the representation based on what it has learned about what usually appears with what.

This is *pattern completion*, and it is the generalization operation. The partial or noisy input is resolved into the closest stored template by the auto-associative dynamics of the recurrent network. Two encounters with the same odor, in slightly different forms, produce the same cortical pattern because the recurrent connections enforce convergence.

The full system, combining all three operations, does what no simpler system could. Dimensionality expansion separates similar inputs in representational space. Sparse coding through lateral inhibition enforces discrimination by amplifying the differences. Recurrent connections implement auto-associative memory that generalizes across variations within a category. The same physical structure performs both operations — not by switching between two modes, but by using the *same neurons* for both, with the operations interleaved across the time course of the response.

[FIGURE: The three-operation architecture in a simplified diagram. Left panel: input vectors representing two similar odors as overlapping clusters in a low-dimensional input space. Middle panel: after dimensionality expansion and sparse coding, the clusters are separated in the high-dimensional cortical representation space. Right panel: when a partial version of Odor 1 arrives, the recurrent connections complete the pattern, pulling the representation toward the stored Odor 1 template rather than an ambiguous intermediate. Students should trace how each operation contributes to discrimination (middle panel) and generalization (right panel) and notice that both require the same neurons — they are not separate systems.]

---

## Concept Worked Example: Auto-Associative Memory in Action

Let me make the auto-associative machinery concrete with a specific example.

Suppose a fish has learned to associate a particular complex odor — call it Odor A — with food. Odor A activates a pattern of activity across forty cortical neurons (out of a thousand available). The Hebbian rule strengthens the connections among those forty neurons proportionally to how often they fire together. After many exposures, the forty Odor-A neurons have much stronger mutual connections than they have to other neurons.

Now the fish encounters a dilute version of Odor A — only enough to activate twenty-five of the forty neurons directly (the others receive weak input below their firing threshold).

Here is what happens next. The twenty-five neurons that fired directly are strongly connected to the other fifteen Odor-A neurons via the strengthened recurrent collaterals. Each of the fifteen receives excitatory input from multiple active neurons in the ensemble. The summed input pushes those fifteen above threshold. They fire. The pattern completes.

The fish's cortex ends up representing the dilute odor with the same forty-neuron pattern it uses for the full odor. The downstream neurons that evaluate the odor — and decide whether to approach — receive the same signal. The fish approaches the food source, even though the odor was faint.

Now consider what would happen if the recurrent connections did not exist.

The fish would represent the dilute odor with only twenty-five active neurons. The downstream evaluator receives a weaker, different pattern. Unless it has been specifically trained on this dilute version, it would not recognize it as Odor A. The fish would fail to approach the food.

The recurrent completion is not a bonus feature. It is the mechanism that makes learned knowledge useful under real-world conditions where inputs are always partial, noisy, and variable.

**Now add the discriminability requirement.** Suppose there is a second odor, Odor B, that activates thirty of the same forty Odor-A neurons plus ten others. At the input level, Odors A and B are very similar. But because sparse coding enforces a competition among cortical neurons, the ten neurons that are most strongly driven by each odor will tend to win. The cortical representation of Odor A and Odor B end up using largely non-overlapping sparse subsets — even if the input patterns overlapped substantially. Pattern separation has occurred. The auto-associative completion then works separately for each stored pattern, reinforcing its own subnetwork without confusing the two.

Discrimination and generalization, in the same architecture, using the same neurons, at the same time.

---

## 6.4 What the Goldfish Knew About Rotation

The olfactory case establishes the architecture. The visual case shows it doing something harder.

Caroline DeLong and her colleagues at the Rochester Institute of Technology trained goldfish on a discrimination task using color photographs of real objects: a plastic toy turtle and a plastic toy frog. The fish learned the discrimination at zero degrees of rotation. Then they were tested at ninety, one hundred eighty, and two hundred seventy degrees of rotation — in three different planes, including depth rotations that showed the objects from entirely different physical viewpoints.

The goldfish were significantly above chance at every rotation. They recognized the objects even when the photograph showed a viewpoint they had never seen during training.

There are two things worth noting about this result. The first is that the goldfish were not simply detecting simple visual features — color alone, or overall shape as seen from the front — because the rotated images differed substantially in exactly those features. A photograph of a frog from below looks different from a photograph of a frog from the front, in overall brightness distribution, in the positions of the major color patches, in the aspect ratio of the body outline. The goldfish was doing something more abstract than feature detection.

The second is the detail I find most interesting: the goldfish were faster on the upside-down (one-hundred-eighty-degree) rotation than on the ninety-degree rotation. This asymmetry is not predicted by pure viewpoint-invariant recognition — if the brain were simply building a viewpoint-independent representation from the start, all rotations should be equally fast. The asymmetry hints at a component of the recognition that is viewpoint-dependent, perhaps a mental-rotation-like process, but one that is cheaper for a one-hundred-eighty-degree flip (which preserves certain bilateral symmetry relationships) than for a ninety-degree turn (which does not). I do not fully understand this asymmetry, and I will say so directly at the end of the chapter. But the existence of it tells us something real about the architecture: viewpoint-invariant recognition is not simply a flat representation; it is built on top of a viewpoint-sensitive substrate, and the two interact in ways our current models have not fully captured.

The archerfish face-recognition result, from the chapter's opening, has the same flavor. Faces at different angles, under different lighting conditions, from different demographics — recognized reliably by a fish that does not have the dedicated cortical regions mammalian neuroscience has spent decades characterizing. The fish's three-layered pallium, with its dimensionality expansion, sparse coding, and recurrent completion, is apparently sufficient for what human neuroscientists once thought required specialized mammalian architecture.

This is not a demolition of mammalian neuroscience. It is a clarification of what the truly foundational operations are, and what the later elaborations (the dedicated face area, the six-layer neocortex, the large temporal lobe) add on top of them.

---

## 6.5 Where the Neural Network Analogy Holds, and Where It Breaks

The Hubel-Wiesel hierarchy — simple cells responding to local oriented edges, complex cells pooling across positions to give translation invariance, hypercomplex cells encoding combinations — is the most celebrated empirical result in visual neuroscience, and it is the direct inspiration for the convolutional neural network. The logic of the inspiration is sound: if the brain solves visual recognition by building a hierarchy of increasingly abstract features, building an artificial system with the same hierarchical structure should produce something with the same capabilities.

In one important sense, this prediction has been confirmed. Daniel Yamins, Ha Hong, Charles Cadieu, and James DiCarlo trained a hierarchical CNN on object categorization without any constraint to match neural data, and then asked whether the network's intermediate activations predicted the firing of neurons in macaque inferior temporal cortex on the same images. The top layer of the trained network was the best predictor of IT neuron responses that the field had produced. The architecture and the task, when matched sufficiently, produced matching representations. This is a real and important finding.

In another important sense, the analogy breaks down. CNNs, in the standard feedforward form, are excellent at translation invariance — the convolutional structure builds this in mathematically, by sharing weights across positions. They are poor at rotation invariance, scale invariance, and recognition under unusual viewpoints unless these have been explicitly represented in the training data through augmentation. The goldfish recognizing a rotated frog from a viewpoint it has never seen is doing something the standard CNN cannot do without having been specifically trained on rotated frogs.

The deeper problem is relational reasoning. A test stimulus that asks whether two shapes are the same — abstracting away what the shapes are and caring only about the relation between them — requires a representation of the relation as such. Feedforward CNNs encode features of parts; they do not, in their standard form, encode relations between parts as a distinct representable quantity. Fish, and certainly mammals, can learn same-different relations and apply them to new shapes. Standard CNNs cannot, at least not from the amounts of data that would be plausible in a biological context.

The explanation for this gap takes us back to what the engineers copied and what they left out.

What was copied: the feature hierarchy. Local feature detectors at the bottom, progressive abstraction upward. Pooling to achieve translation invariance. This is the Hubel-Wiesel part.

What was not copied: the recurrent auto-associative completion. The sparse code enforced by lateral inhibition. The modular separation of storage from processing, so that new learning does not overwrite old. The thalamic gating mechanism that controls which input reaches the cortex at all — a selective attention system that filters the information stream before the cortex processes it.

These omitted components are precisely the components that explain the remaining performance gaps. Recurrent completion enables recognition of partial and degraded inputs. Sparse coding enables catastrophic-forgetting resistance by ensuring that new patterns are represented in neurons that were not previously committed to old ones. Thalamic gating enables selective attention that allows the system to process the relevant features of an input while suppressing irrelevant variation.

When you leave out the recurrent completion, you leave out the mechanism that handles novel viewpoints by completing the pattern toward a stored template. When you leave out sparse coding, you get a system that overwrites old knowledge with new learning — the catastrophic forgetting problem. When you leave out gating, you get a system that must process all input features equally, without the ability to focus on the dimensions that carry the diagnostic information.

The engineers took the feedforward recognition path and left the recurrent stabilization path. The result is a system that is extremely good at the specific discrimination task it was trained on, and less robust than biology on everything else.

---

## 6.6 The Architecture Generalized

The three-operation framework — dimensionality expansion, sparse coding, recurrent completion — is not unique to the olfactory or visual cortex. Variants of it appear wherever the vertebrate brain has had to solve a pattern-recognition problem.

The hippocampus, which handles spatial and episodic memory rather than perceptual categories, runs an architecture that exploits the same logic. The dentate gyrus performs pattern separation — it expands the incoming representation from the entorhinal cortex into a very sparse code, pushing similar inputs into distinct neural ensembles. CA3, the next region, performs pattern completion — it has the most recurrent collateral connectivity of any cortical region in the mammalian brain, and it uses this to complete partial spatial or episodic patterns toward stored templates. CA1 then compares the completed pattern from CA3 to the direct cortical input as a check on how close the current situation is to a stored memory. The hippocampal circuit is the cortical architecture specialized for time-extended pattern completion, running the same three operations on sequences of experience rather than simultaneous sensory inputs.

The cerebellum, which handles fine motor coordination, runs a different but related architecture: its granule cells perform massive dimensionality expansion on sensorimotor inputs (more than half of all neurons in the human brain are cerebellar granule cells), and the Purkinje cells perform supervised pattern classification over this expanded representation. The supervised learning rule (driven by climbing fiber error signals from the inferior olive rather than by Hebbian plasticity) is different, but the expansion-then-classify logic is the same.

The neocortex proper — the six-layered sheet that mammals expanded dramatically — adds layers of hierarchical abstraction and executive control on top of the three-layer base, but it does not replace that base. Layers 2 and 3 of the neocortex are the recurrent horizontal connectivity layers — the layers most involved in auto-associative completion and the integration of information across cortical columns. Layers 4 and 5 handle the input/output interface. The neocortex is the three-layer architecture, elaborated vertically with more stages of processing and more opportunities for top-down modulation.

The bird brain arrived at comparable functional sophistication by a different anatomical route. The avian pallium — the structure where crow and jay cognition lives, the structure we will examine further in Chapter 12 — is organized in a nuclear rather than a laminar architecture. Instead of layers, it has clusters. But within those clusters, the same computational logic applies: cells with overlapping inputs form recurrent ensembles, lateral inhibition enforces sparse coding, and the resulting representations support both discrimination and generalization. Convergent evolution of the same computation in different anatomical implementations.

This convergence is the strongest evidence that the three operations are not an arbitrary design choice. They are the solution to a hard computational problem — how to simultaneously discriminate and generalize — and any nervous system that solves that problem will implement something recognizably similar to them.

---

## 6.7 What the Architecture Cannot Do

It is important to be careful about the limits of the framework, as I have tried to be at the end of every chapter.

The cortical pattern-recognition architecture is very good at recognizing instances of learned categories and at generalizing learned categories to new instances. It is much weaker at several things that the later chapters will need.

It does not easily support *compositional reasoning* — taking known parts and assembling them into a novel whole in a structured way. Recognizing a face is different from understanding that the face is in front of a body that is on a bicycle that is crossing a bridge. The latter requires representing relations between objects, not just the objects themselves. Relational reasoning — the same-different capacity that defeats standard CNNs and seems to require more than feature detection — is a genuine challenge for the cortical architecture as described, and the mechanism by which the primate cortex handles it (working memory systems in the prefrontal cortex, systematic binding through temporal synchrony, or some other mechanism) remains genuinely contested.

It does not easily support *explicit abstraction*. The auto-associative architecture stores patterns by strengthening connections among co-firing neurons. It retrieves patterns by completing partial inputs toward stored templates. It does not, in its basic form, construct a rule that could be stated verbally and applied systematically to new instances that differ in principled ways from training examples. This is fine for perceptual recognition, which does not require explicit rules. It is insufficient for the kinds of reasoning about rules and categories that appear in primate cognition and will be examined in Chapters 11 through 14.

It does not, on its own, produce *invariance to truly novel transformations*. The goldfish's rotated-frog recognition is impressive, but it may rely on having seen a wide variety of natural objects at natural orientations, building up a prior for how objects deform across viewpoints that can be applied to new objects. When the transformation is truly novel — a kind of distortion the animal has never encountered in any domain — the auto-associative completion will produce the wrong stored pattern, because the partial match will be to the wrong stored template. The failure mode is systematic, not random, and it can be difficult to detect.

These limitations are not bugs in the cortical design. They reflect the different problems the brain needed to solve at different evolutionary stages, and the later chapters are about the mechanisms that were added to handle the problems that the basic cortical pattern recognizer cannot solve alone.

---

## Chapter Summary

**What you can do now that you could not before this chapter:**

The central skill this chapter adds is the ability to analyze any pattern-recognition system — biological or artificial — against a three-operation checklist and identify which operations are present, which are absent, and what the absence predicts about performance under challenging conditions.

Dimensionality expansion separates similar inputs in representational space, addressing discrimination. Sparse coding with lateral inhibition amplifies the separation, ensuring that only the most diagnostic features dominate the representation. Recurrent auto-associative completion uses stored co-firing patterns to generalize across partial, noisy, and viewpoint-shifted instances of learned categories. A system with all three operations handles the core perceptual tasks: discrimination, generalization, and a substantial degree of invariance. A system missing any one degrades in a specific, predictable way.

**The one idea that matters most:** The vertebrate cortex solves discrimination and generalization simultaneously using a single unified architecture — not two separate systems with a balance struck between them, but two *complementary operations* (expansion+sparsification for discrimination, recurrent completion for generalization) running on the same neurons. The architecture has been preserved, in recognizable form, from lamprey to fish to mammal, for at least five hundred million years. That conservation is evidence that the architecture is not one solution among many. It is the solution.

**The common mistake to watch for:** Concluding from the CNN-cortex parallel that neural networks and biological visual systems are solving the same problem in the same way. The Yamins DiCarlo result is real: trained CNNs predict IT neuron responses better than earlier models. But the analogy is partial. The feedforward feature hierarchy is the part that matches. The recurrent completion, the sparse coding, the thalamic gating — the parts that explain catastrophic-forgetting resistance, viewpoint invariance, and relational recognition — were not included in the original CNN design, and those omissions explain the remaining performance gaps.

**The Feynman test:** Without using the technical terms, can you explain why a goldfish trained to recognize a frog photograph at zero degrees of rotation also recognizes it at one hundred eighty degrees — and why a CNN trained in the same way would fail at the rotated test unless it had also been trained on rotated images? If yes, you understand the auto-associative completion and the inductive bias story. If not, reread §6.4 and §6.5.

---

## Exercises

**Warm-up: Direct Application**

1. A species of fish is discovered that has a pallium with dimensionality expansion and recurrent connections, but no lateral inhibitory interneurons — so sparse coding does not occur. Predict how this fish's perceptual performance would differ from a fish with the full three-operation architecture. Which failure mode would be most prominent: impaired discrimination, impaired generalization, or impaired invariance? Justify your prediction from the function of lateral inhibition described in §6.3.

2. The auto-associative completion mechanism allows the cortex to reconstruct a full pattern from a partial input. This works well when the partial input is most similar to one stored pattern. What would happen if the partial input were equally similar to two stored patterns? Describe the expected behavior of the auto-associative network in this case and explain why this represents a genuine limitation of the architecture.

3. The chapter claims that dimensionality expansion helps separate similar inputs in representational space. This seems counterintuitive — why does adding more neurons help you distinguish between inputs? Explain the geometric logic in your own words without using technical jargon. What condition must be met for the expansion to work as described?

**Application: Translation**

4. A modern deep learning image classifier is trained on a large labeled dataset of animal photographs. It achieves 95% accuracy on the test set. The manufacturer then deploys it in a wildlife monitoring system in a new habitat where the animals are frequently partially occluded by vegetation, and performance drops to 60%. Using the three-operation framework from this chapter, identify which operation is most likely insufficient in this system and explain what architectural change might improve performance in the deployment environment.

5. The archerfish face-recognition result is sometimes described in popular accounts as showing that archerfish are "as smart as humans at face recognition." Evaluate this claim carefully. In what specific sense does the result support a comparison to human face recognition? In what ways is the comparison misleading? What would you need to know to make a fair comparison?

6. In Chapter 4, we discussed how *C. elegans* forms associations between temperature and food through a mechanism that involves Hebbian strengthening of connections between co-active neurons. In Chapter 6, the piriform cortex generalizes across variations of a learned odor through the same Hebbian mechanism operating on recurrent connections. Is this the same mechanism doing two different things, or two different mechanisms that happen to share a molecular substrate? What would distinguish these two interpretations empirically?

**Synthesis: Combining Concepts**

7. Chapter 3 described how the *C. elegans* nervous system uses labeled-line sensors with hardwired valences — each sensory neuron carries a default interpretation of its signal. Chapter 6 describes how the vertebrate cortex learns representations through experience rather than having them hardwired. What does this difference in architecture imply for the flexibility and the speed of development of each system? Under what ecological conditions would the labeled-line approach be superior, and under what conditions would the learned-representation approach be superior?

8. Chapter 5 showed that neuromodulatory state (dopamine, serotonin) changes how bees interpret ambiguous stimuli — a pessimistic bee interprets the same odor as more aversive. The chapter also discussed the piriform cortex as an auto-associative memory for odors. How might neuromodulatory state interact with auto-associative completion? That is, could the state change *which* stored pattern a partial input completes toward, rather than only changing the threshold for extending the proboscis? Design an experiment that would distinguish between these two accounts.

9. The chapter describes two failure modes of CNNs that can be traced to missing architectural components: catastrophic forgetting (linked to the absence of sparse coding) and poor viewpoint invariance (linked to the absence of recurrent completion). The chapter also describes a third performance gap — relational reasoning (same-different). Which architectural component might, if added to a CNN, specifically improve relational reasoning performance? Build your argument from first principles about what relational reasoning requires that the standard feedforward architecture does not provide.

**Challenge: Pushing Forward**

10. *(Open-ended)* I described the goldfish's faster recognition of the upside-down image compared to the ninety-degree-rotated image as something I do not fully understand — an asymmetry that current models do not predict. Develop your own hypothesis for why this asymmetry occurs. Your hypothesis should make at least one additional prediction that could be tested in a follow-up experiment. What would the result of that experiment need to be to either support or falsify your hypothesis? This kind of "something I don't understand" disclosure is common in active research areas; identifying and forming hypotheses about such anomalies is a core scientific skill.

---

## Connections Forward

Chapter 6 established the foundational perceptual architecture of the vertebrate brain. The next chapters ask what is built on top of it.

**Chapter 7** (*Navigation and Spatial Intelligence*) examines what happens when the cortical pattern-recognition architecture is specialized for space rather than for objects. The hippocampal place cells and grid cells that map the environment are running the same auto-associative logic introduced here, applied to a continuous geometric domain. The navigation chapter will return to pattern completion as the mechanism by which a partial spatial cue retrieves a full spatial memory.

**Chapter 9** (*Simulation and Planning*) examines what happens when the cortical architecture runs in *reverse* — generating a prediction of what the input *would be* in a hypothetical situation, rather than recognizing what the input *is* in the current situation. The generative model interpretation of cortex — that perception is an act of prediction, not just recognition — connects the auto-associative machinery of this chapter to the planning capacities of mammals.

**Chapter 12** (*Creativity*) returns to the question of relational reasoning, which the chapter identified as a genuine challenge for the auto-associative architecture. The corvid and primate evidence for compositional thought will require an account of how biological systems go beyond feature recognition to represent structured relationships between elements — the step the chapter acknowledged the basic cortical architecture does not easily support.

The question this chapter leaves open: the goldfish's rotated-frog recognition requires the fish to have extracted something more abstract than a viewpoint-specific surface description. What is that more abstract representation, how is it stored, and how is it retrieved? The auto-associative completion mechanism gives us part of the answer. The part it does not give us — the part about how the brain builds object-level representations that persist across the wildly different retinal images that the same object produces — is one of the genuinely open problems in visual neuroscience, and it remains open at every level from fish to human.

---

*The archerfish that picked the right face out of forty-four did not do it because it is remarkable. It did it because it has the standard vertebrate solution to a standard vertebrate problem. We are the ones who thought the problem was hard.*

---

**Chapter Notes and Primary Sources**

The archerfish face-recognition study was published by Newport, Wallis, Reshitnyk, and Siebeck in *Scientific Reports* in 2016. The goldfish rotation-invariance study was published by DeLong and colleagues in *Animals* in 2022.

The lamprey pallium-to-cortex homology was documented by Suryanarayana, Robertson, Wallén, and Grillner in *Current Biology* in 2017. The original discovery of cortical orientation selectivity and the simple-cell/complex-cell hierarchy was published by Hubel and Wiesel in *The Journal of Physiology* in 1962; they received the Nobel Prize in Physiology or Medicine in 1981.

The CNN-to-IT-cortex predictive fit was demonstrated by Yamins, Hong, Cadieu, and DiCarlo in *Proceedings of the National Academy of Sciences* in 2014. LeNet, the foundational convolutional network for visual recognition, was described by LeCun and colleagues in *Neural Computation* in 1989.

The same-different relational reasoning failure in CNNs was documented by Stabinger, Rodríguez-Sánchez, and Piater in the proceedings of the ICDL-EpiRob conference in 2016; subsequent work by Kim and colleagues in NeurIPS 2018 and by Fleuret and colleagues provided more systematic characterization.

The piriform cortex as an auto-associative memory is developed in detail by Edmund Rolls in *Cerebral Cortex: Principles of Operation* (2016) and in the computational work of Amit, Gutfreund, and Sompolinsky on attractor networks in the late 1980s. The hippocampal pattern separation/completion distinction is developed by David Marr in his 1971 *Philosophical Transactions of the Royal Society* paper on the hippocampus and by McNaughton and Morris in their 1987 *Trends in Neurosciences* review.

The catastrophic forgetting problem in artificial neural networks was first systematically described by McCloskey and Cohen in 1989 and has been addressed by a series of biological-inspired approaches summarized in Kumaran, Hassabis, and McClelland's 2016 *Trends in Cognitive Sciences* review.
