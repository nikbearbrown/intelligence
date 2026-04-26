# Chapter 8: Reinforcement and Prediction
## *The Dip*

---

## Learning Objectives

By the end of this chapter, you should be able to:

1. **Explain** what Wolfram Schultz's monkey experiments actually demonstrated about dopamine, and why "dopamine is the pleasure molecule" is wrong
2. **Derive** the temporal-difference learning update rule and trace its correspondence, step by step, to the phasic firing patterns of midbrain dopamine neurons
3. **Distinguish** between model-free and model-based reinforcement learning, and connect each to specific neural structures in the basal ganglia
4. **Describe** the Adams-Dickinson devaluation paradigm and explain what it reveals about the conditions under which goal-directed behavior becomes habit
5. **Apply** the concept of reward hacking to explain why reinforcement-learning systems optimizing engagement metrics may produce outcomes their designers did not intend
6. **Situate** reinforcement learning within the book's comparative framework: where it fits in the phylogeny, what it adds to the nematode's steering, and what it cannot do that model-based planning can

**Prerequisites:** Chapter 3 (Steering: the nematode, valence, and the minimum architecture for goal-directed behavior), Chapter 4 (Learning and Memory: Hebbian plasticity, CREB, and the credit assignment problem), and Chapter 7 (Navigation and Spatial Intelligence: the hippocampus as model of space). You should be familiar with the Rescorla-Wagner prediction error rule from Chapter 4.

---

## Why This Chapter Matters

In Chapter 4, we established that nervous systems can learn — that experience can modify synaptic weights in ways that persist. In Chapter 7, we established that some nervous systems build internal models of space — maps that allow navigation without retracing every step. This chapter connects those two findings to something deeper: a universal algorithm for learning to act.

The argument is not metaphorical. Richard Sutton published the temporal-difference learning algorithm in 1988. Wolfram Schultz, Peter Dayan, and Read Montague identified its neural implementation in 1997. When you hold the equations next to the electrophysiology, the correspondence is exact, trial for trial, neuron for neuron. It is one of the cleanest alignments between mathematical theory and biological mechanism in the whole of neuroscience.

The algorithm is also ancient. The basal ganglia that implement it appear in essentially modern form in the lamprey, the most primitive living vertebrate, half a billion years before the first transistor. Every fish, reptile, bird, and mammal runs a version of it. You are running it now, in every moment that your dopamine neurons register the difference between what you expected and what you got.

Understanding this mechanism changes how you should think about the reinforcement-learning systems that now run substantial portions of the digital economy. They extend the same algorithm — the same core operation — to scales and speeds no biological agent can match. They share, precisely, the biological system's key limitation: they optimize the reward function they are given, and they cannot ask whether that function is the right one. That question is always on the human side of the loop. This chapter explains why.

---

## 8.1 The Cold Open: The Dip

Fribourg, Switzerland, early 1990s. Wolfram Schultz has lowered a fine electrode into the midbrain of a macaque monkey, into the region called the ventral tegmental area, where dopamine neurons cluster. The monkey is performing a small task: a light comes on, and a few seconds later a drop of sweet juice is delivered to the monkey's mouth. After many repetitions, the monkey has learned what the light means.

While the monkey learns, Schultz watches a single dopamine neuron.

In the first trials, before the monkey understands the task, the dopamine neuron fires a brief sharp burst at the moment the juice arrives. This has been observed many times before in many laboratories. Pleasure causes dopamine. That was the textbook.

After many trials, with the same juice delivered exactly the same way, the dopamine neuron stops responding to the juice. It now fires its burst at the *light*, several seconds before the juice arrives. The same juice. The same intensity. No burst at the moment of delivery. The textbook is already in trouble.

Then Schultz does the experiment that breaks it completely. He lets the monkey see the light — and then withholds the juice. At the exact millisecond the juice would have arrived, based on the timing the monkey has learned over hundreds of trials, the dopamine neuron's firing rate *drops* below its baseline. Briefly. Precisely. Then recovers.

This is not a stimulus the experimenter applied. Nothing is happening in the physical world at that moment. The monkey is simply expecting something that did not arrive, and the dopamine neuron registers the absence as a negative deflection from its resting rate.

The dip is real. Reproducible. It is a piece of neural activity corresponding to nothing in the environment and everything in the monkey's prediction — a signal that says, in the language of millisecond firing rates: *I was expecting something and it did not come*.

Dopamine is not a pleasure signal.

Dopamine is a prediction-error signal — the brain's precise, continuous record of how much the present moment deviates from what was expected. The chapter explains what that means, where the algorithm came from, and why it matters for everything from the lamprey to the recommendation engine.

---

## 8.2 The Empirical Thread: Thorndike to Rescorla-Wagner

The ground this chapter stands on was laid by two independent traditions.

The empirical tradition begins with Edward Thorndike's puzzle-box experiments in the late 1890s. A hungry cat is placed in a small wooden box; a piece of fish is visible just outside; a latch must be operated to escape. Thorndike measured the time to escape across many trials. The learning curve was not the sudden *aha* moment of insight that popular accounts later imposed. It was a gradual, jagged improvement — the cat tried this, then that, then a third thing, until eventually the right movement produced escape, and that movement became more likely on the next trial. Thorndike called the finding the *Law of Effect*: responses followed by satisfying consequences become more likely; responses followed by discomfort become less likely. He extended the same pattern to dogs, chickens, and killifish. The architecture did not appear to be species-specific.

Thorndike's law is the behavioral foundation of all reinforcement learning. But it is silent on *timing* — on how the brain assigns credit for an outcome to the action that caused it, when the two are separated by seconds or longer. A cat that opens a latch and escapes five seconds later must somehow connect the latch-press with the escape. This is the *temporal credit-assignment problem*, and it is the harder half.

The Rescorla-Wagner model, encountered in Chapter 4, took the first step toward solving it. Their 1972 formulation proposed that learning is driven by surprise: the difference between what the cue predicted and what actually occurred. The model explained *blocking* — the finding that animals do not learn about a redundant cue if the reward is already fully predicted by a cue they have already mastered. If the reward is expected, there is no prediction error, and no learning occurs.

But Rescorla-Wagner was atemporal. It treated each trial as a single event and had nothing to say about what should happen *during* the trial — at the moment the cue appears, at the moment of the gap, at the moment of outcome. Real learning happens in time, step by step, and a real algorithm has to handle time.

That is what Sutton's 1988 paper does.

---

## 8.3 The One Concept: What the TD Algorithm Is and What Dopamine Is Doing

### The Temporal-Difference Update

Richard Sutton, in his 1988 paper "Learning to predict by the methods of temporal differences" in *Machine Learning*, introduced the algorithmic move that makes reinforcement learning work in continuous time. The move is called *bootstrapping*, and it is worth understanding precisely.

The problem: you want to learn the *value* of being in a particular state — meaning the total reward you can expect to accumulate, from now to the end of the episode, if you act optimally. But you cannot wait until the end of the episode to update your estimate, because episodes can be long and the credit-assignment problem grows with the delay.

The solution: update your estimate at every step using the *next* estimate as part of the target. You do not need the final outcome. You need only the reward you just received and your current best guess about what comes next. Information about future reward flows backward through time, one step at a time, without requiring a complete model of the environment.

The update rule for the estimated value $V(s_t)$ of the current state $s_t$ is:

$$V(s_t) \leftarrow V(s_t) + \alpha \left[ r_{t+1} + \gamma V(s_{t+1}) - V(s_t) \right]$$

Read the bracket slowly. The term $r_{t+1}$ is the reward received at the next time step — whatever the world actually delivered. The term $\gamma V(s_{t+1})$ is the discounted estimated value of the next state — what the agent currently believes is coming, discounted by a factor $\gamma < 1$ to account for the fact that future rewards are worth less than immediate ones. Together, $r_{t+1} + \gamma V(s_{t+1})$ is a *better estimate* of the current state's value, because it incorporates one step of actual experience that the older estimate $V(s_t)$ did not have.

The quantity in brackets — the difference between the better estimate and the older one — is the **temporal-difference error**, or TD error:

$$\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$$

The update says: nudge $V(s_t)$ in the direction of the better estimate, by a fraction $\alpha$ called the learning rate. Run this long enough and the value function converges on the true expected discounted reward of every state in the environment.

That is the whole algorithm. It is short, it is local (each update requires only the current state, the next state, and the reward), and it is mathematically correct. It is also what the brain does.

[FIGURE: Three-panel diagram showing the TD error at three training stages. Left panel: early training, before learning — dopamine neuron fires at reward delivery (large positive $\delta_t$ at outcome, nothing at cue). Center panel: after training — dopamine neuron fires at cue onset (positive $\delta_t$ at cue), nothing at reward (predicted reward matches received reward, $\delta_t \approx 0$ at outcome). Right panel: reward omission — dopamine neuron fires at cue, then dips below baseline at the moment when reward would have arrived (negative $\delta_t$ at omission). Each panel should show the neural firing rate trace above and the corresponding TD error $\delta_t$ value below, aligned in time. The student should notice that the three panels together constitute a complete demonstration of TD learning: the signal follows prediction error, not reward itself.]

### The Neural Correspondence

Schultz, Dayan, and Montague identified the correspondence in their 1997 *Science* paper "A Neural Substrate of Prediction and Reward." The match is exact.

**Before learning:** Dopamine neurons fire at reward delivery. In TD terms: $V(s_t)$ is small (no prediction yet), so $\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t) \approx r_{t+1} > 0$. Positive error at reward.

**After learning:** $V(s_{cue})$ has grown to anticipate the reward. At the cue, the state transition from a low-value state to the high-value cue state produces a positive TD error, so dopamine neurons fire at the cue. At reward delivery, the better estimate and the older estimate are nearly equal ($\delta_t \approx 0$), so dopamine neurons are silent.

**At omission:** $r_{t+1} = 0$ (no reward) and $V(s_{t+1})$ drops to near zero (the trial has effectively ended without payoff). So $\delta_t = 0 + \gamma \cdot 0 - V(s_t) < 0$. Negative error. The dip in the monkey's dopamine neurons, below baseline firing, at the exact moment the juice would have arrived — that is negative $\delta_t$, implemented in millisecond firing rates.

The dip is the brain admitting that a prediction was wrong in the negative direction. Relief — the surge of dopamine when something unexpectedly good happens — is positive $\delta_t$. Disappointment is negative $\delta_t$. The emotional vocabulary of surprise is the phenomenal correlate of a learning signal encoded in dopamine.

### The Anatomy Fits Too

The correspondence is not only between the algorithm and the firing patterns. The anatomy of the circuit is also the anatomy of an actor-critic architecture.

The **basal ganglia** — a set of subcortical structures including the striatum, globus pallidus, and substantia nigra, found in essentially modern form in the lamprey 560 million years ago — divide into two functional components. The dorsolateral striatum and its outputs to motor systems function as the **actor**: they select and initiate actions based on learned action values. Subpopulations of striatal neurons called *striosomes* project to the substantia nigra dopamine cells and supply the prediction $V(s_t)$ that gets subtracted from the actual outcome to produce $\delta_t$. The dopamine neurons broadcast $\delta_t$ back to the striatum, where it gates plasticity at the corticostriatal synapses — the connections between cortical state representations and striatal action representations.

Plasticity gated by prediction error is what TD learning prescribes. Plasticity gated by prediction error is what corticostriatal synapses do. The algorithm and the anatomy are the same thing, instantiated in tissue that has been conserved for half a billion years.

### Two Clarifications

Two refinements deserve explicit statement, because the popular version of the dopamine story routinely ignores them.

**First:** dopamine does not encode a single scalar signal. The clean TD-error story that Schultz, Dayan, and Montague proposed has held up well for the central case of reward-prediction error, but subsequent work has shown that different dopamine neurons in different midbrain subregions encode different features — position, object identity, movement kinematics, and so on. The current best picture is something like a *vector* of prediction errors, encoded by a population of dopamine neurons, rather than a single number broadcast uniformly. The original story is correct in its bones; the fine structure is richer than the 1997 paper could detect.

**Second:** prediction error and motivation come apart. Kent Berridge's decades of work distinguish *wanting* (the motivational pull toward an anticipated reward) from *liking* (the hedonic experience when the reward arrives). Knock out dopamine signaling in rats and they still show facial pleasure responses to sweet liquid — they still *like* the sucrose. They simply stop *working* for it; the wanting is gone. The TD-error story and the wanting-vs-liking story are not in conflict. They describe two related operations of the same machinery: updating the value of cues, and generating the motivational pull that drives action toward those cues. Dopamine is necessary for the update and for the wanting; it is not necessary for the liking.

---

## 8.4 The Trade-Off: When Prediction Becomes Habit

The reinforcement-learning machinery has a known failure mode, and the failure mode is biologically and computationally fundamental.

### The Devaluation Test

In 1981, Christopher Adams and Anthony Dickinson trained hungry rats to press a lever for sucrose. After moderate training, they paired the sucrose with lithium chloride — a substance that causes nausea — so that the rats developed a taste aversion to the sucrose itself. Then they returned the rats to the lever.

Moderately trained rats stopped pressing. The reward was now disgusting; pressing for it made no sense; the rats did the sensible thing and quit.

Overtrained rats — animals that had pressed the lever many more times before the devaluation — kept pressing. The reward they were earning made them sick. They pressed anyway.

The action had become a *habit*. It was no longer governed by the current value of the outcome. It had become an automatic response to the lever, disconnected from any live representation of what the lever produced and whether that thing was currently worth having.

### Model-Free and Model-Based

The computational interpretation of this finding is sharp and has proven durable.

**Model-free** reinforcement learning learns a *cached value* for each action in each context: this lever, in this setting, has been worth approximately this much in the past. The cached value updates slowly, trial by trial, via TD error. If the world changes — if the sucrose is now noxious — the cached value will eventually update, but only after many post-change trials in which the agent experiences the devalued outcome repeatedly. Until then, the agent presses.

**Model-based** reinforcement learning builds an internal representation of the world's dynamics: pressing this lever produces sucrose; sucrose has these consequences. When sucrose is devalued, the model-based system can re-evaluate the lever's worth *without further experience*, by simulating the new contingency forward: sucrose now → nausea → bad. It stops pressing immediately.

The mammalian brain implements both. The **dorsolateral striatum** and its associated circuitry implement something like model-free control, holding cached action values that update slowly and drive habitual behavior. The **dorsomedial striatum** and regions of prefrontal cortex implement something like model-based control, building and consulting internal world models. Behavior reflects the relative engagement of the two systems depending on training history, time pressure, cognitive load, and stress: extensive practice tilts toward model-free habit; novel situations or devalued outcomes engage model-based reasoning — if the model-based system has capacity to override.

This architecture is not unique to mammals. Fish have rudimentary versions of both. Rats and pigeons have been studied extensively in the devaluation paradigm, and the same habit/goal-directed dissociation appears across species wherever it has been carefully tested. The model-free/model-based distinction is not a cortical elaboration. It is a vertebrate-level property of the basal ganglia system, with cortical amplification added by mammals.

[FIGURE: Schematic of the actor-critic / model-free and model-based architecture in the basal ganglia. Show two pathways. Left pathway: cortical state representation → dorsolateral striatum (actor) → action selection → outcome → TD error $\delta_t$ → dopamine neurons → back to dorsolateral striatum (gating plasticity). Label this "model-free / habit." Right pathway: cortical state representation → dorsomedial striatum / prefrontal cortex → internal world model → simulated outcomes → action selection. Label this "model-based / goal-directed." Show the midbrain dopamine neurons (VTA / SNc) as a shared node that both pathways influence, and label the dopamine broadcast arrow explicitly as $\delta_t$. The student should notice that both pathways share the dopamine teaching signal but differ in what that signal modifies.]

### The Brittleness Problem

The Adams-Dickinson result is not a laboratory curiosity. It names a structural limitation of any system that learns by caching reward values rather than by building a world model: the system will continue doing what worked before, even when the world has changed to make it wrong, until enough new experience has accumulated to overwrite the cached value.

In biological agents, the model-based system provides the override when it is working well. In artificial reinforcement-learning systems, the equivalent override must be explicitly engineered — and often is not.

The DeepMind deep Q-network that learned to play forty-nine Atari 2600 games at human or superhuman level from raw pixels (Mnih et al., 2015) is a landmark of model-free reinforcement learning. It is also brittle in exactly the ways the Adams-Dickinson result predicts: change the color of the sprites, shift the visual context, or vary the game in any way outside the training distribution, and performance often collapses. The DQN has learned a cached policy valid in the environment it was trained in. It does not have a model of the game that would let it adapt to variants it has never seen.

The fish that learned to navigate by landmarks — described in Chapter 7 — and can solve a detour problem by consulting its spatial map has something the overtrained rat and the DQN do not: a model it can consult when the cached policy fails.

---

## 8.5 The Scale-Up: What Happens When the Algorithm Runs the Economy

The same core operation that explains Schultz's monkey now runs a substantial fraction of the digital economy.

Netflix, YouTube, Spotify, TikTok, and Amazon all deploy reinforcement-learning systems whose job is to predict what content will most increase a measured engagement signal, and then act on the prediction by shaping the next thing the user sees. High-frequency trading firms run reinforcement-learning policies that predict price movements over short horizons and execute in milliseconds. Industrial control systems from data-center cooling to chip floorplan placement use RL to find policies that exceed hand-engineered solutions. These systems extend one cognitive capacity — the optimization of action against a measurable reward — to scales and speeds no biological agent can approach.

They also share the biological system's key vulnerability: they optimize the reward function they are given, and they cannot, on their own, ask whether that function is the right one.

This is not a bug to be fixed in the next architecture. It is a structural property of any optimizer. Give a sufficiently powerful optimization process a reward function and it will find a policy that maximizes that function. If the function is a good proxy for what you actually want, the policy will be good. If the function is a poor proxy — if it can be maximized in ways that diverge from the actual goal — the policy will exploit that divergence.

The technical term in AI safety is *reward hacking*. The economist's version is Goodhart's Law: *when a measure becomes a target, it ceases to be a good measure*. These are the same observation in different vocabularies. The user-engagement metric that recommendation engines optimize is not the same thing as user well-being or epistemic health. The trading-revenue metric that high-frequency systems optimize is not the same thing as market stability. The 2010 Flash Crash — in which automated systems amplified a large sell order into a trillion-dollar evaporation in twenty minutes — is one documented instance of what happens when many powerful optimizers share an environment and act on each other's outputs without any of them having a model of the shared system they are operating in.

The basal ganglia dopamine system that evolution built avoids the worst versions of reward hacking through a combination of features that took hundreds of millions of years to assemble: a model-based system that can inspect the current reward contingencies and ask whether they are still appropriate; a prefrontal regulatory layer that can suppress habitual responses when the context has changed; and an embodied agent with a body and a history whose motivational structure was calibrated over evolutionary time to track actual fitness consequences rather than arbitrary proxy signals.

Artificial reinforcement-learning systems have none of these features by default. They have the actor. They have the TD update. They have, in some architectures, a model. What they do not have — what no optimizer can have from the inside — is the capacity to specify what should be optimized. That capacity is always external to the system. It is the part of the loop that belongs, irreducibly, to the humans who design the reward function, who define the environment, who decide what to optimize and why.

The specification of the reward function requires moral, ethical, and strategic judgment about what kind of future is worth producing. It is the part of the loop that most resembles what the book has been calling intelligence across its full scope — not goal-achievement within a fixed environment, but the capacity to evaluate goals across environments and to ask whether a given goal is worth pursuing at all. No current reinforcement-learning system, biological or artificial, has that capacity in anything like full form. Humans have it, imperfectly, in ways that the rest of this book has been tracing.

---

## 8.6 What We Have, and Where This Leaves Us

Reinforcement learning is the algorithmic core of how vertebrate brains learn to act. It is implemented in dopamine and the basal ganglia in essentially the same architectural form across at least five hundred million years of vertebrate evolution. It is the mechanism by which the lamprey learns that this stretch of water is dangerous, the rat learns that this lever is worth pressing, and the monkey learns that this light predicts juice.

By the Legg-Hutter framework, an agent with only a model-free reinforcement-learning system is intelligent in a narrow, brittle way: it learns policies that work in training environments and fails in environments that differ. An agent that adds a model-based system is intelligent across a wider range, because it can simulate novel contingencies and adapt without further experience. An agent that adds metacognitive oversight of both systems — the capacity to notice when it is acting out of habit rather than judgment — is more intelligent still.

The phylogeny is clear. The lamprey already has the basal ganglia, the direct and indirect pathways, the dopamine neurons, the striosomal microcircuitry. Fish and reptiles inherit it. Mammals add the cortical elaboration that lets model-based reasoning live on top of the model-free core. Primates and humans add prefrontal regulation that lets the model-based system override habit on demand. The ladder is built on the floor the lamprey already had.

The dip in Schultz's monkey is not a small finding. It is the brain's precise admission that something it predicted did not happen. Disappointment is the felt version of negative $\delta_t$. Relief is the felt version of positive $\delta_t$ when something unexpectedly good arrives. We have, in five hundred million years and one Swiss laboratory in the early 1990s, located the neural currency of prediction.

The next chapter is about what happens when you use that currency to run a simulation *before* the action is taken — when the brain, instead of updating values after experience, runs experience forward in imagination and acts on the result. That is the capacity we will call planning, and it is where the gap between fish and mammal becomes most visible.

---

## Summary

**The key mechanism:** Phasic dopamine firing in midbrain neurons encodes the temporal-difference prediction error $\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$. Before learning, dopamine fires at reward. After learning, dopamine fires at the predictive cue. When reward is omitted, dopamine dips below baseline at the expected moment of delivery. This is not a pleasure signal. It is a teaching signal.

**The key distinction:** Model-free reinforcement learning caches action values and updates them slowly via TD error; it produces habit and is brittle to environmental change. Model-based reinforcement learning builds a world model and consults it to simulate outcomes before acting; it produces flexible, goal-directed behavior and adapts to devaluation immediately. Both systems are implemented in the basal ganglia, and behavior reflects their relative engagement.

**The key application:** Reinforcement-learning systems deployed in the digital economy extend the TD algorithm to scales and speeds no biological system can match. They share the biological system's structural vulnerability: they optimize the reward function they are given and cannot evaluate whether that function is appropriate. Reward specification is always external to the optimizer.

**The common mistake to watch for:** Treating dopamine as a reward signal. It is not. A dopamine burst means "this is better than I expected." A dopamine dip means "this is worse than I expected." Absence of dopamine response to a predicted reward means "this is exactly what I expected." The signal is always relative to a prediction, never absolute.

**What you should now be able to teach someone else:** Why Schultz's monkey's dopamine neuron dips when the juice is withheld, what that dip corresponds to in the TD update equation, and why an overtrained rat keeps pressing a lever even when the food it earns makes it sick.

---

## Exercises

### Warm-Up

1. A monkey is trained that a blue light predicts a juice reward one second later. After extensive training, the blue light is replaced by a green light that also predicts juice one second later. Using the TD framework, predict: (a) what happens to dopamine neuron firing at the green light on the first trial; (b) what happens at the blue light on the first trial after the switch; (c) how firing patterns at both lights change over subsequent trials. Explain each prediction with reference to the TD error equation.

2. In your own words, explain the difference between Berridge's "wanting" and "liking," and explain why the existence of this distinction does not contradict the TD-error account of dopamine. What would you predict about the behavior of a rat with dopamine neurons destroyed, if you placed food directly in its mouth?

### Application

3. A rat is trained for 200 trials to press lever A for sucrose and lever B for food pellets. After training, sucrose is devalued (paired with lithium chloride). The rat is then tested with both levers present, but no rewards delivered. Predict, with mechanistic reasoning, the rat's behavior on lever A and lever B in the test phase. How would your prediction change if the rat had been trained for 2,000 trials rather than 200?

4. A reinforcement-learning system is deployed to recommend videos to users. Its reward function is defined as time-on-platform per session. After six months of deployment, users report feeling worse after using the platform, though they spend more time on it than before deployment. Using the concepts of reward hacking and Goodhart's Law, explain what has likely happened. What alternative reward function might have prevented this outcome, and what would be the challenges in implementing it?

5. The TD update discounts future rewards by a factor $\gamma < 1$: a reward arriving in $k$ steps is worth $\gamma^k$ of the same reward arriving immediately. In biological systems, individual differences in $\gamma$ (sometimes called temporal discounting) are associated with differences in impulsivity and in outcomes like addiction vulnerability. Using the TD framework, explain mechanistically what a low $\gamma$ (steep discounting) implies about the value estimates an agent builds, and why it might produce preference for small immediate rewards over large delayed ones.

### Synthesis

6. The Adams-Dickinson devaluation result distinguishes goal-directed from habitual behavior. Design an experiment that would test whether a fish (from Chapter 7) shows goal-directed behavior — that is, whether it would immediately stop responding to a trained cue if the reward that cue predicted were devalued. What result would indicate goal-directed control? What result would indicate purely habitual control? What does the answer tell you about the evolution of model-based reinforcement learning?

7. The chapter argues that the reward specification problem — deciding what to optimize — cannot be solved from inside the optimizer. Consider a hypothetical reinforcement-learning system that has been given access to human feedback as its reward signal (human raters assess whether outputs are good or bad). Does this approach solve the specification problem, partially solve it, or simply relocate it? Defend your answer with specific reference to the structural vulnerability described in Section 8.5.

### Challenge

8. The chapter claims that the correspondence between the TD algorithm and dopamine neuron firing is "one of the cleanest correspondences between a computational theory and a piece of biological mechanism" in neuroscience. A skeptic might respond: "The correspondence is compelling but could be coincidental — evolution might have arrived at the same functional outcome by a completely different mechanism, and the mathematical framing might be post-hoc description rather than genuine explanation." Construct the strongest version of this skeptical argument. Then construct the strongest response to it, using evidence from the anatomy (actor-critic architecture, basal ganglia conservation), the pharmacology (Berridge's wanting-vs-liking dissociation), and the specificity of the predictions the theory makes (the dip timing, the cue-transfer pattern). What would constitute decisive evidence that the correspondence is genuine rather than post-hoc?

---

## Connections Forward

Chapter 9 examines simulation and planning — the capacity to run actions forward in imagination before executing them in the world. It will argue that this capacity is what distinguishes the mammalian model-based system from the simpler model-free systems that the lamprey and fish already possessed, and that it is implemented in the hippocampus and prefrontal cortex through a specific architectural move: the replay of stored trajectories to update value estimates without acting in the world.

The connection to this chapter is precise. TD learning updates values from experience after it occurs. Planning updates values from *simulated* experience before it occurs. Both use the same update rule; what differs is the source of the transitions being learned from. Chapter 9 will ask what architectural additions are required to make that simulation possible, and what behavioral consequences follow — including the counterintuitive finding that the most powerful planning systems are the ones most likely to construct incorrect simulations and act on them.

---

*What would change my mind: a demonstration that the dopamine-RPE model breaks down for a class of learning that the basal ganglia clearly performs — a rigorously controlled showing that delay-conditioned avoidance learning in a vertebrate occurs without any phasic dopamine signature at all. The Schultz-Dayan-Montague correspondence has held up across decades and species, but it is a model, and the dopamine literature has grown more complicated rather than simpler over time. The vector-RPE picture, with different dopamine neurons encoding different features of the prediction error, is the current best account. A systematic breakdown of the correspondence in a well-studied preparation would force substantial revision.*

*Still puzzling: why dopamine neurons appear to encode several things at once — reward prediction error, salience, novelty, movement vigor — in ways not always reducible to a single scalar signal. The relationship between the high-dimensional dopamine code that more recent recordings reveal and the elegant scalar TD-error story remains an active open problem. Both may be right; they may be describing the same computation at different levels of analysis. I am not yet confident which.*

---
