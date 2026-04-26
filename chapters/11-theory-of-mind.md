# Chapter 11: Theory of Mind
## The Ape Who Looked at the Wrong Place

---

### Learning Objectives

By the end of this chapter, you should be able to:

1. **Describe** the hierarchy of theory-of-mind capacities — goal attribution, perspective-taking, false-belief reasoning, second-order recursion — and specify what each level requires beyond the level below it
2. **Explain** why the implicit-explicit distinction matters for interpreting comparative results, and apply it to evaluate what the Krupenye 2016 eye-tracking result does and does not establish
3. **Apply** the inverse-reinforcement-learning frame to describe what theory of mind is computing — and use that frame to identify what a system that genuinely passes the false-belief task must be doing internally
4. **Evaluate** the Ullman 2023 fragility result and explain why it distinguishes pattern-matching on canonical narratives from genuine mental-state representation
5. **Analyze** the dog guilty-look result and the corvid re-caching result to illustrate how two very different cognitive operations can produce superficially similar behavioral signatures

**Prerequisites:** Chapter 9's treatment of mental simulation and the hippocampal-cortical model-building system; Chapter 10's account of social intelligence, dominance hierarchies, and the oxytocin-dopamine social-bonding architecture. Theory of mind is the capacity to point the simulation machinery of Chapter 9 at another agent's mind rather than at the physical world.

**Where this fits:** Chapter 9 showed that mammalian brains can simulate trajectories — running the world forward before acting. Chapter 10 showed that primate brains can track who knows what, who outranks whom, and what relations third parties hold to each other. Chapter 11 asks the next question: can an animal not only track social relationships, but represent the *internal states* of the agents it interacts with — their beliefs, desires, intentions — as states that can be correct or incorrect about the world?

---

### Chapter Opening: Before the Actor Moves

In a primate research center in Japan, a chimpanzee is sitting in a quiet room. An infrared eye-tracker is watching her eyes. On the screen in front of her, a video is playing.

The video shows a person searching for an object. A few minutes ago — in the video — the person watched the object get hidden in a particular spot. Then the person left the room. While the person was gone, someone moved the object. In one version, the object was moved to a different location. In another version, it was removed entirely.

The person is now returning. In a few moments, they will begin to search.

The question is not what the chimpanzee knows. She watched the whole sequence. She knows where the object actually is, or that it is gone. The question is what the chimpanzee expects the person to do.

A fraction of a second before the person starts to move, the chimpanzee's eyes shift. They move to a location on the screen. The eye-tracker records exactly where.

They move to the place where the object used to be. The place where the actor falsely believes it still is. Not the place where it now sits. Not the place it was removed to. The place the actor thinks it is.

The chimpanzee is anticipating a *mistake*. She is predicting that the actor will go to the wrong place, based on a belief she knows to be false — and she is doing this before the actor has made any movement that she could simply imitate or track.

Christopher Krupenye and colleagues published this result in *Science* in 2016. It was the first time any non-human animal had passed a version of the false-belief task — the test that, since 1983, had served as the gold standard for theory of mind in comparative cognition. Forty years of prior experiments had found that great apes could not do this. Then eye-tracking showed that they could, or at least that something in their visual anticipation system was doing it implicitly, below the level of any explicit verbal answer.

The ape looked at the wrong place. The wrong place was the right answer.

---

## 11.1 The Task That Defined the Field

To understand why the Krupenye result matters, you need to understand the problem it was trying to solve, and why the previous forty years of attempts had failed to solve it.

The concept of *theory of mind* entered comparative cognition in 1978, in a paper by David Premack and Guy Woodruff in *Behavioral and Brain Sciences*. Their subject was a chimpanzee named Sarah, who had been raised among researchers and trained with plastic symbols to communicate. They showed Sarah short films of a person trying to solve problems — reaching for bananas suspended too high, trying to operate a disconnected heater — and gave her photographs showing various solutions. She consistently chose the correct solution photograph. Premack and Woodruff inferred that Sarah understood the actor's *purpose*, and asked whether this meant she had a theory of mind — a framework for representing other agents as having mental states like goals and intentions.

The philosopher Daniel Dennett read the paper and immediately identified the problem. Sarah might not be attributing anything to the actor at all. She might simply be solving the physical problem in her own head and selecting the photograph that shows the solution, with no reference to what the actor believes or wants. To rule this out, Dennett argued, you need a design in which the *subject's knowledge of the world differs from the actor's knowledge* — a situation where the subject knows something the actor does not, and the test is whether the subject predicts the actor's behavior based on the actor's false belief rather than on the truth.

Heinz Wimmer and Josef Perner provided the experimental design in 1983 in *Cognition*. Simon Baron-Cohen, Alan Leslie, and Uta Frith made it canonical in their 1985 paper showing that children with autism spectrum disorder fail the task at rates much higher than neurotypical children. The paradigm they used — Sally-Anne — has since been run in hundreds of variants and across dozens of cultures.

Sally puts a marble in a basket. Sally leaves the room. Anne moves the marble to a box. Sally returns.

Where will Sally look for her marble?

Four-year-old neurotypical children answer correctly: the basket, where Sally left it and where Sally *believes* it still is. Three-year-olds answer incorrectly: the box, where the marble *actually is*. The three-year-old's error is not a failure to remember where the marble is. Ask where the marble is, and the three-year-old knows. Ask where Sally will look, and the three-year-old says the box — their own knowledge of the marble's location overrides the inference about Sally's belief.

What changes between age three and age four is the capacity to hold a representation of a belief *as a representation* — as a mental state that exists in a mind and that can be wrong about the world. This is sometimes called the capacity for *metarepresentation*: representing representations, rather than just representing states of the world. The three-year-old represents the world as it is. The four-year-old can also represent how someone else represents the world, even when that representation is false.

For forty years after the Sally-Anne paradigm was established, great apes failed every version of it. Across multiple laboratories, multiple species, multiple experimental variations, the apes behaved like three-year-olds: they predicted the actor would go to where the object actually was, not where the actor believed it to be. The consensus hardened that great apes could attribute goals and perhaps desires, but not beliefs — that they were perspective-takers but not false-belief reasoners.

Krupenye's result broke the consensus, and it is worth being precise about how.

---

## 11.2 Why Eye-Tracking Changed Everything

The difference between the 2016 result and the previous forty years of experiments is not the species. It is the *measure*.

All previous false-belief tests with non-human animals used behavioral responses: the animal had to select a photograph, press a button, search in a location, or do something that could be scored as a correct or incorrect answer. These *explicit* measures require the animal to produce an *active, controlled, deliberate* response. In humans, we know that the explicit version of the false-belief task recruits substantial executive function, particularly inhibitory control: the child must suppress their own accurate knowledge about where the marble is in order to compute and report what Sally believes.

The implicit version — the version Krupenye used — asks no active response. The animal sits, watches, and the eye-tracker records where it looks in the moments before action begins. Humans show the anticipatory-looking pattern in implicit false-belief tasks as early as fifteen months, more than two years before they can pass the explicit version. The implicit measure is tapping a prediction system that runs earlier, faster, and more automatically than the controlled explicit response.

What Krupenye's experiment found, across chimpanzees, bonobos, and orangutans, was that the anticipatory gaze went to the false-belief location before the actor began to search. The apes were not following the actor's body movement — the gaze shift happened before any movement occurred. They were generating a prediction, based on the actor's mental state, and that prediction registered in their visual anticipation system.

The critics raised the obvious alternative. Cecilia Heyes, the Oxford comparative psychologist who has spent decades pushing back on mentalistic interpretations of animal behavior, argued that the apes could be running *submentalizing* — simple learned rules about where objects last appeared in an actor's view, without any representation of belief as a mental state. The apes had experienced many episodes in which objects got moved; they might have learned a statistical regularity that actors tend to look where they last interacted with an object, without ever computing what the actor *believes*.

Fumihiro Kano and colleagues answered this directly in their 2019 follow-up in *PNAS*. They pre-exposed different apes to the same kind of barrier used in the main experiment — opaque for some apes, transparent for others. Later, all apes watched a video in which an actor stood behind the barrier of the same type they had experienced. The apes' anticipatory gaze depended on their *own past experience* with that specific barrier. Apes who had experienced the barrier as opaque expected the actor to be ignorant of what was on the other side, and their gaze reflected this. Apes who had experienced it as transparent expected the actor to have seen through it, and their gaze reflected that instead.

This is not a statistical regularity about objects in actors' views. The apes were *projecting their own perceptual experience* onto the actor — using their knowledge of what that type of barrier permits or blocks to infer what the actor had been able to see. This is the core operation of visual perspective-taking elevated to a false-belief computation: *the actor's belief depends on what that actor was able to perceive, and I know something about what that barrier allows one to perceive*.

This is, by my reading, the cleanest result in the chapter. The apes are not doing Sally-Anne explicitly. They are doing something structurally equivalent to it, implicitly, in a system that runs before any deliberate response is made. The floor of theory of mind has moved.

---

## 11.3 The Hierarchy

Theory of mind is not one capacity with a sharp boundary. It is a hierarchy of related capacities, each requiring more of the agent than the level below it. Laying out the hierarchy precisely matters for interpreting the comparative evidence, because different experimental paradigms tap different levels.

**Goal attribution** is the foundation. Recognizing that an agent's movement is *directed toward something* rather than random. An infant as young as six months treats a moving shape differently when it moves *toward* a goal object than when it moves in the same physical direction without targeting anything. Goaledness is likely recognized across a wide range of vertebrates — a bird mobbing a snake is implicitly attributing the goal of predation. This is the capacity that Chapter 9's simulation architecture produces naturally: a model-based agent predicting another agent's future trajectory will tend to represent that trajectory as goal-directed.

**Desire attribution** is one step up. Recognizing not just that an agent has a goal, but that the goal reflects a preference — that the agent *wants* something. Wanting can be in tension with the world: the agent may want something it does not have, and this desire can drive search behavior. Chimpanzee tool use for food retrieval and corvid food-caching both implicitly require representing desired-but-not-yet-obtained states, at minimum in the self.

**Perspective-taking** is the first genuinely social layer. Understanding that what someone *sees* shapes what they *know* — that visual access creates epistemic access, and its absence creates ignorance. The competitive-attention results from Chapter 10 — the subordinate chimpanzee taking food the dominant cannot see — require this. Perspective-taking is behavioral and implicit; it does not require representing belief as a propositional state. It requires modeling the other agent's visual field and using that to infer what they know.

**False-belief reasoning** is the layer where Sally-Anne lives. Representing another agent's belief as a state that can be *wrong about the world* — and using that representation to predict behavior even when the predicted behavior is inconsistent with the truth. This is the layer the great apes appear to reach implicitly, in the Krupenye and Kano results.

**Second-order theory of mind** is the recursive extension. I know what Sally believes. But what does Anne *think* Sally believes? Second-order reasoning requires embedding one belief-representation inside another: representing an agent's representation of another agent's representation. Human children reliably pass tasks at this level by age seven. No non-human animal has been shown to do so in any paradigm, and this remains the sharpest behavioral boundary between human and non-human theory of mind.

**Higher-order recursion** — *I think you think she thinks he thinks...* — in principle extends arbitrarily. In practice, human social reasoning operates at three to four levels of recursion in natural conversation; experimental performance degrades reliably above that. The elaborated human capacity for recursive mentalizing is the substrate that makes politics, deception, literature, and complex negotiation possible.

[FIGURE: The theory-of-mind hierarchy as a layered diagram. Bottom layer: goal attribution — species range (most vertebrates, possibly invertebrates in limited contexts). Second layer: desire attribution — species range (great apes, corvids, dogs in limited contexts). Third layer: perspective-taking — species range (great apes, corvids, dogs reading human gaze). Fourth layer: false-belief reasoning — species range (great apes implicitly per 2016-2019 results, corvids in re-caching paradigm). Fifth layer: second-order recursion — species range (human children 7+, no confirmed non-human). Each layer labeled with: what it requires cognitively; the key experimental paradigm that tests it; representative species known to reach that layer. Students should notice that each layer requires representing the *internal state* of another agent at a finer grain than the layer below it, and that the implicit/explicit distinction cuts across multiple layers.]

---

## 11.4 The Corvid That Knew What Thieves Think

The great-ape result is compelling for what it shows about a lineage close to our own. The corvid result is compelling for a different reason: it shows the same functional capacity appearing in a brain built on entirely different principles, in a lineage separated from humans by more than three hundred million years.

Western scrub jays (*Aphelocoma californica*) store food in hundreds of small caches distributed across their territory. They are prodigious thieves — they routinely raid each other's caches, and dominant birds displace subordinate ones from discovered food. The social environment of the scrub jay is one in which knowing who has seen what about where food is cached is survival-relevant information.

Nathan Emery and Nicola Clayton, in their 2001 *Nature* paper, set up the following situation. A jay was allowed to cache food in a specific location. In some trials, another jay had been watching from a nearby cage during the caching. In other trials, no observer was present. Subsequently, the caching jay was given private access to all the cache sites and could move any items it wanted to.

Jays that had been observed during caching moved their caches to new locations. Jays that had cached unobserved did not. The caching jay was responding to whether it had been *seen*, which is perspective-taking. But the result that makes the theory-of-mind case is the next observation: the protective re-caching occurred *specifically in jays that had themselves been thieves in the past*. Naive jays, who had never stolen another bird's cache, did not re-cache even when they had been observed. Only jays with personal theft experience took the protective measure.

The mechanism Emery and Clayton proposed is *self-projection*: the experienced thief knows what it does when it watches another bird cache — it steals — and it projects this behavioral tendency onto the watching observer. The computation is: *this bird was in the same perceptual position I have been in when I have stolen from others; I know what I do in that position; therefore I know what this bird is likely to do*.

This is not the Sally-Anne false-belief task. It does not require representing a false belief. But it requires something that Sally-Anne does not explicitly require: taking one's own mental states as a *model* for another agent's mental states. The jay is using *itself* as a theory-of-mind engine, running its own behavioral propensities forward through the lens of the other bird's perspective.

The behavioral test for this mechanism has a clean prediction: jays who have stolen should re-cache when observed; jays who have not stolen should not; and the *more* experience with theft the caching jay has, the more reliably it should re-cache. The data fit this prediction. It takes a thief, literally and specifically, to know what a thief will do.

Corvids lack a six-layered neocortex. Their executive control runs through the *nidopallium caudolaterale*, a structure that is anatomically distinct from mammalian prefrontal cortex but functionally analogous in its role in working memory and flexible decision-making. The convergent-evolution lesson that runs through this book applies again: the function — modeling another agent's knowledge and behavioral propensities — appears twice, in two lineages, on two different neural architectures. The computation is the constraint. The substrate is not.

---

## Concept Worked Example: What the Dog Is and Is Not Doing

The dog case is the chapter's most instructive contrast, because it demonstrates how two very different cognitive operations can produce the same surface behavior — and how a well-designed experiment disambiguates them.

Dog owners reliably report that their dogs produce a "guilty look" when caught having done something forbidden: cowering, flattened ears, averted gaze, tail tucked. The owner typically interprets this as the dog *knowing it did wrong* — evidence of a moral self-awareness with a social component. This is a theory-of-mind attribution: the dog is attributing to the owner the belief that the dog has misbehaved, and is producing a conciliatory response based on that belief.

Alexandra Horowitz ran the experiment that tests this interpretation. Owners left their dogs alone with a forbidden treat, then returned. But before they returned, the experimenter either told them the truth (the dog had eaten the treat, or had not) or *lied* (the dog had eaten the treat but the owner was told it had not; or the dog had not eaten the treat but the owner was told it had). Owners who were told their dog had misbehaved sometimes scolded the dog before looking at whether the treat was gone. Owners who were told their dog had been obedient did not.

The result: the guilty look was not associated with whether the dog had *actually eaten the treat*. It was associated with whether the *owner was scolding*. Dogs that had been obedient but were scolded under a false impression showed as much guilty-look behavior as dogs that had eaten the treat. Dogs that had eaten the treat but whose owners were told they had been obedient showed no guilty look.

**What this tells us:** The dog's guilty behavior is a response to the owner's *current behavioral cues* — the tone of voice, the posture, the expressions that accompany scolding — not a response to the dog's own knowledge of having done wrong. The dog has learned, through years of living with humans, to read the signals of human displeasure and produce submission behavior that defuses it. This is behaviorally sophisticated. It is not theory of mind.

**What the dog is doing:** Behavioral pattern recognition on current observable cues. Rung 1 of the theory-of-mind hierarchy — goal attribution — combined with learned conditional responses. When human = angry display, produce = submission signal.

**What theory of mind would require:** The dog would need to *represent* that the owner holds the *belief that the dog misbehaved*, and produce the guilty look specifically in response to that represented belief rather than to the observable scolding behavior. To test this, you would need to show the dog a situation where the owner holds a false belief about misbehavior but shows *no behavioral cues* of it, and ask whether the dog produces the guilty look in anticipation of the owner discovering the error. The current evidence does not support this.

**The broader lesson:** Dogs are extraordinarily good at reading *current human behavior* — better than great apes in many studies of human communicative cuing. They have been domesticated over fifteen thousand years specifically in contexts where reading human intentions from observable cues was fitness-relevant. But there is a difference between tracking observable cues and modeling the beliefs that will produce future behavior. Dogs may be the best animals in the world at the first. They have not clearly demonstrated the second.

---

## 11.5 The Inverse Reinforcement Learning Frame

There is a computational frame that clarifies what theory of mind is actually computing, and it connects the biological findings to the AI question.

In ordinary reinforcement learning, reviewed in Chapter 8, an agent is given a reward function and learns a policy that maximizes it. In *inverse reinforcement learning* (IRL), the situation reverses. An observer watches another agent behave and must infer the reward function — the goals and preferences — that explains the behavior. Pieter Abbeel and Andrew Ng introduced IRL as a technique for robot learning from human demonstration, but the cognitive science literature has been converging on the view that it is a general description of what theory-of-mind systems do.

When you watch someone walk toward the kitchen, you do not just represent the trajectory of their body. You infer that they are *hungry* (the reward function) and *believe food is in the kitchen* (the world-model). From the observed behavior, you back-compute a compact set of latent variables — desires, beliefs, intentions — that explains everything the person is doing and that will, if accurate, predict what they do next in situations you have not yet observed.

This compression is what makes theory of mind useful. Without it, social prediction requires memorizing every behavior sequence every individual has ever produced in every context. With it, a small number of attributed mental states (hungry, believes food is here, intends to eat) generalize to predictions about infinitely many novel situations. The attributed reward function is the compact model; the observed behavior is the data that the model is fitted to.

Applied to the comparative hierarchy: goal attribution is IRL that infers only the target state of the agent's policy. Perspective-taking is IRL that includes a representation of the agent's *information state* — what it can see. False-belief reasoning is IRL that represents the agent's *world-model* as something that can be incorrect, and uses the agent's false model rather than the true world to predict the agent's behavior.

The frame also clarifies what is wrong with the LLM theory-of-mind results.

In 2023, Michal Kosinski reported that GPT-3.5 and GPT-4 passed a large battery of standard false-belief tasks — Sally-Anne and variants — with accuracy approaching that of competent human adults. The result attracted substantial attention, and speculation followed that large language models had developed theory of mind as an emergent property of scale.

Tomer Ullman answered this in a 2023 paper by making small modifications to the same tasks. Replace the opaque container in the Sally-Anne story with a transparent one, so that Sally could have seen the marble move even when she was in the room. Add a sentence explicitly granting the actor knowledge of the object's new location. Make changes that preserve the *logical structure* of the false-belief situation while altering the *surface features* of the canonical story.

GPT-4, on the modified versions, continued to predict that Sally would look in the basket — the answer correct for the canonical version — even when the modification made it clear that Sally had seen the marble move and therefore knew where it was. The model was applying the learned template (actor-absent-during-move → actor-has-false-belief) even when the story's explicit content contradicted the template.

Humans do not do this. A human reading the transparent-container version immediately updates their prediction: Sally saw it happen, so Sally knows. The inference generalizes because humans are running an actual model of Sally's information state — a model that takes the story's content as input and outputs a belief-state for Sally. The model is computing something, but it is not doing IRL on Sally's mental states. It is matching the story to training-distribution templates, and the templates break when the stories are modified in ways that preserve logical structure while altering surface form.

The distinction is consequential. IRL-based theory of mind generalizes because the underlying representation — the attributed belief and desire structure — is compositional. New stories produce new inferred belief states by applying the same representational machinery to new content. Template-matching on narrative surface features generalizes only within the training distribution, and the Ullman modifications specifically probe the out-of-distribution edge where the template and the logic come apart.

By the IRL frame, a system genuinely doing theory of mind should pass Ullman's modifications, because it is computing Sally's information state from the story's content rather than from the story's surface resemblance to training examples. The models tested in 2023 did not pass. This is the chapter's strongest evidence that what LLMs do when they appear to pass theory-of-mind tasks is not the same kind of operation that a great ape does when it anticipates an actor's false belief. One is building a model of another mind. The other is matching a template.

---

## 11.6 The Mentalizing Network and Its Limits

The human neural architecture for theory of mind is well-characterized enough to be worth noting, because it extends the book's broader argument that cognitive functions correspond to identifiable mechanisms.

The core structure is the *mentalizing network*, identified through neuroimaging by Rebecca Saxe and colleagues at MIT. The temporo-parietal junction (TPJ), particularly in the right hemisphere, is the most consistent hub: it is selectively active when human subjects are reasoning about other agents' beliefs, and its activity scales with the *degree of recursion* in the mentalizing task (first-order belief versus second-order belief versus third-order). Damage to the right TPJ — from stroke or lesion — produces specific deficits in false-belief reasoning without impairing other aspects of social cognition or general intelligence.

The medial prefrontal cortex contributes what appears to be the self-other integration component: the system that keeps track of which mental states are mine and which are attributed to another agent. When subjects fail to maintain this distinction — attributing their own knowledge to another agent — the medial PFC activity is typically dysregulated relative to successful mentalizing trials. The posterior superior temporal sulcus parses biological motion as goal-directed, providing the input to the mentalizing network: the system needs to recognize that the entity it is modeling is *an agent moving intentionally*, not a rock falling.

Together these regions run the inverse-reinforcement-learning inference that theory of mind requires. The TPJ does the belief attribution proper; the mPFC maintains the self-other boundary; the pSTS provides the prior that the entity in question has goal-directed behavior to model.

The homologs of this network in great apes are not fully characterized — the comparative neuroimaging literature is thin because scanning an unanaesthetized great ape in an MRI machine is practically very difficult. What is known is that the basic cortical regions are present, and that the functional connectivity patterns that support mentalizing in humans appear to have close counterparts in chimpanzee cortex. The divergence, on current evidence, appears to be in the degree of elaboration, the density of the connections, and particularly the capacity for *language-mediated* recursive mentalizing that makes the human second- and third-order reasoning possible.

What language adds to theory of mind is its own chapter — Chapter 15. For now, mark the point: the neural substrate for theory of mind is present in a graded form across the primate phylogenetic tree, consistent with the behavioral evidence that the capacity is graded rather than all-or-nothing.

---

## 11.7 Where the Line Now Sits

I want to be direct about what the chapter has established and what it has not.

**What is established:** Implicit false-belief reasoning in great apes, supported by the Krupenye 2016 and Kano 2019 results. The implicit result is replicable and survives the strongest submentalizing alternative tested so far. Self-projective perspective attribution in corvids, supported by the Emery-Clayton re-caching result. Both species are doing something that satisfies the logical requirements of false-belief reasoning, using mechanisms that are not simply explained by associative learning on behavioral regularities.

**What is contested:** Whether any non-human animal does *explicit* false-belief reasoning — controlled, verbalized, deliberate — comparable to what four-year-old humans do. The implicit/explicit distinction is real, and the gap between them matters for understanding the recursive human capacity for mentalizing. Whether the Ullman result generalizes to other LLM families and later model generations (the 2023 result applies to GPT-3.5 and GPT-4; subsequent models have not been as thoroughly probed with the same paradigm as of my writing).

**What is not established:** Second-order recursive false-belief reasoning in any non-human animal. The corvid re-caching result is self-projective, not explicitly recursive. The great-ape eye-tracking results are at the first-order level. The line between humans and non-human animals, in theory of mind, now sits at *explicit, second-order, recursive* mentalizing — not at any form of mental-state attribution per se.

This boundary matters for the book's argument. By the operational definition — ability to achieve goals across a wide range of environments — theory of mind is valuable across a wide range of its levels. A social environment is navigable with perspective-taking alone. It is navigable better with first-order false-belief attribution. It is navigable best with the recursive structure that allows strategic deception, coalition-building, political maneuvering, and the transmission of cultural knowledge through deliberate teaching. The richer levels produce a qualitatively different range of achievable goals, not just a quantitatively better performance on the same ones.

The ape who looked at the wrong place has something real. The four-year-old who said "the basket" has something more of the same kind. What exactly the "more" consists of, and how much of it is specifically enabled by language, is the question Chapter 15 approaches.

---

## Chapter Summary

**What you can do now that you could not before this chapter:**

The central skill this chapter adds is the ability to evaluate a claimed theory-of-mind result — whether in an animal experiment, a human developmental study, or an AI benchmark — against the IRL frame and the implicit/explicit distinction. A result is evidence for theory of mind only if: (1) the subject's knowledge of the world differs from the target agent's knowledge, (2) the subject's behavior is predicted by the *target's* world-model rather than the subject's own, and (3) the result generalizes across surface variations in the scenario, not just across repetitions of the canonical form.

**The one idea that matters most:** Theory of mind is inverse reinforcement learning — the brain's algorithm for inferring the reward function (desires) and world-model (beliefs) of another agent from observed behavior, producing a compact internal representation that generalizes across novel situations. A system genuinely doing this generalizes when the scenario is modified. A system pattern-matching on narrative templates does not. The Ullman 2023 result is the clean test, and it separates the two.

**The common mistake to watch for:** Treating behavioral evidence for perspective-taking as evidence for false-belief reasoning. The subordinate chimpanzee taking food the dominant cannot see is doing perspective-taking. The chimpanzee anticipating that an actor will search in the wrong place is doing false-belief reasoning. The behaviors can look similar from outside. The cognitive operations are distinct, and the experimental designs that test them are different. Know which level a given paradigm actually probes.

**The Feynman test:** Without using the words "theory of mind," explain why the Kano 2019 goggles experiment defeats the submentalizing alternative for great apes. If you can give that explanation — including what the submentalizing alternative predicts and why the goggles result differs from that prediction — you understand what the Krupenye-Kano body of work actually established.

---

## Exercises

**Warm-up: Direct Application**

1. A vervet monkey gives an alarm call when it spots a hawk. Other monkeys in the group hear the call and run into the bushes. A different alarm call, used for ground predators, causes the monkeys to climb trees. Does this behavior require theory of mind? If so, at what level of the hierarchy? If not, what does it require instead? What additional observation would establish that the calling monkey is *attributing* knowledge or fear to its audience rather than simply producing a context-specific vocalization?

2. The Sally-Anne task is modified as follows: Sally puts the marble in the basket. Sally remains in the room, but she is looking at her phone and clearly not paying attention when Anne moves the marble to the box. Where will Sally look? Apply the IRL frame to explain how a genuine theory-of-mind system would approach this modification. What would a template-matching system predict, and how does it differ?

3. The chapter describes how the Kano 2019 goggles experiment was designed to defeat the submentalizing alternative for great apes. Apply the same logic to design a follow-up experiment for the Emery-Clayton corvid re-caching result that would specifically test whether the jays are doing self-projection versus simply responding to the *presence of an observer* as a learned cue for theft risk.

**Application: Translation**

4. A company asks you to evaluate an AI assistant's capacity for user modeling. The assistant is given transcripts of user interactions and asked to predict what a user will do next in a new scenario. It performs well on scenarios similar to those in the training transcripts and poorly on scenarios that are logically equivalent but phrased differently. Using the IRL frame and the Ullman result, explain what this performance pattern tells you about the mechanism the system is using. What would the system need to demonstrate to establish genuine user-model inference rather than template matching?

5. The Extension Note describes Cambridge Analytica as "population-scale pseudo-theory-of-mind." Explain precisely what makes it *pseudo* rather than genuine theory of mind, using the IRL frame. What specific inference does Cambridge Analytica's approach replace with a statistical approximation, and what are the failure modes of that approximation compared to genuine mental-state attribution?

6. A developmental psychologist proposes that the transition from failing to passing the Sally-Anne task at age four is explained by *inhibitory control development* — the child's ability to suppress their own knowledge of the marble's location has improved, not their ability to represent false beliefs. Construct the strongest version of this argument, then identify one experiment that would distinguish the inhibitory-control account from the metarepresentation account.

**Synthesis: Combining Concepts**

7. Chapter 9 described how the hippocampal-cortical system simulates future trajectories before acting. Chapter 11 describes theory of mind as inverse reinforcement learning — inferring another agent's goals and beliefs from behavior. How might the simulation machinery of Chapter 9 be *repurposed* for theory of mind? What would the rat's hippocampal-cortical simulator need to do differently to model another agent's trajectory rather than its own? What additional components would be required?

8. The chapter argues that the Ullman 2023 result shows that LLMs are doing template-matching rather than genuine IRL on mental states. But one might respond that the Krupenye apes are also, in some sense, running learned behavioral templates — they have experience with many scenarios in which absent actors have false beliefs, and their eye-tracking reflects that experience. What is the specific difference between the ape's "template" and the LLM's "template" that makes one evidence for genuine theory of mind and the other evidence against it? Use the IRL frame to make the distinction precise.

9. Chapter 10 described how chimpanzee coalitions require tracking third-party relationships — knowing not just what A thinks of B, but what A thinks B's relationship with C is. Is coalition-tracking a form of second-order theory of mind? Argue that it is, and then argue that it is not. What experiment would distinguish coalition-tracking based on second-order mentalizing from coalition-tracking based on first-order behavioral prediction?

**Challenge: Pushing Forward**

10. *(Open-ended)* The chapter's "still puzzling" note raises the question of why the temporo-parietal junction specifically hosts theory-of-mind computation — why *this* cortical location, adjacent to regions involved in attention, biological motion, and self-location, came to host false-belief attribution. Develop a hypothesis for the developmental and evolutionary origin of TPJ specialization for mentalizing. Your hypothesis should: (a) explain why the location makes sense given the neighboring functions; (b) make a prediction about the developmental order in which TPJ sensitivity to goal attribution, perspective-taking, and false-belief reasoning should emerge in infants; and (c) identify what you would need to measure, in either developmental neuroimaging or comparative neuroimaging of great apes, to test your hypothesis.

---

## Connections Forward

Chapter 11 established that the capacity to model other agents' beliefs — not just their goals or visible behavior — has appeared independently in at least two distant lineages, and runs on a neural architecture whose computational function the IRL frame can describe precisely. The next two chapters trace what this capacity makes possible at larger scales.

**Chapter 12** (*Creativity and Insight*) returns to the question of what mental simulation can produce when there is no physical object to manipulate and no specific other agent to model — when the simulation is purely generative, and the question is how novel solutions emerge from the combination of existing concepts.

**Chapter 15** (*Language*) takes up the question deferred from this chapter: what recursive second-order mentalizing adds when it is mediated by language. The jump from implicit first-order false-belief attribution (where great apes are) to explicit recursive mentalizing (where seven-year-old humans are) appears to depend critically on the capacity to embed propositions about propositions — to say and think *Sally thinks that Anne thinks that the marble is in the box*. How language enables this recursion, and what it means for the human cognitive niche, is the chapter's subject.

The question this chapter leaves open: the mentalizing network and its great-ape homologs run on cortical tissue that the basic vertebrate plan includes. The recursive elaboration appears to require something extra — either a quantitative expansion (more cortical tissue, more connectivity) or a qualitative addition (language). Whether the recursive capacity is a matter of degree or a matter of kind is the question that comparative neuroscience and developmental psychology have not yet jointly resolved. The answer will determine how many places on the biological ladder are, in principle, occupied by full recursive mentalizing — and how many are occupied by something real but more limited.

---

*The ape looked at the wrong place. She knew the right place. She looked at the wrong one because the actor was going to the wrong one, and she knew that too. That is a great deal of cognition for a gaze to carry — and the forty years of experiments that failed to find it were not wrong to look. They were looking in the right direction with the wrong instrument.*

---

**Chapter Notes and Primary Sources**

The original theory-of-mind concept was introduced by Premack and Woodruff in *Behavioral and Brain Sciences* in 1978. The false-belief task was introduced by Wimmer and Perner in *Cognition* in 1983. The Baron-Cohen, Leslie, and Frith autism-and-theory-of-mind paper was published in *Cognition* in 1985.

The Krupenye, Kano, Hirata, Call, and Tomasello great-ape anticipatory-looking result was published in *Science* in 2016. The Kano, Krupenye, Hirata, Tomonaga, and Tomasello opaque/transparent barrier follow-up was published in *PNAS* in 2019.

The Emery and Clayton scrub-jay re-caching result was published in *Nature* in 2001. The Hare, Call, and Tomasello competitive-food-access paradigm with chimpanzees was published in *Animal Behaviour* in 2000.

The Horowitz guilty-look disambiguation experiment was published in *Behavioural Processes* in 2009.

The Kosinski LLM theory-of-mind result was posted as a preprint in 2022 and published in 2023 in *Psychological Science*. The Ullman fragility result was published as a preprint in 2023; "Clever Hans" title, preprint available at arxiv.org/abs/2302.08399.

Rebecca Saxe's characterization of the mentalizing network and the TPJ's role is reviewed in Saxe and Kanwisher's 2003 *NeuroImage* paper and developed across subsequent publications through 2013. The inverse reinforcement learning frame for theory of mind is developed in Baker, Jara-Ettinger, Tenenbaum, and Saxe's *PNAS* paper from 2017.

Cecilia Heyes' submentalizing critique is developed in her 2014 *Animal Behaviour* paper "Animal mindreading: What's the problem?"
