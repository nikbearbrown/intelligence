# LLM Exercise blocks — Skeptic's Notebook on Frontier AI

19 blocks, one per chapter (Ch 1 through Ch 19, including the epilogue, which serves as the integration capstone). Each block goes at the bottom of its chapter `.md` file, after the Wayback Machine section.

The default tool is a **Claude Project** — the reader sets it up once with a system prompt that pins the project charter (a chosen frontier model under test, the diagnostic stance, and a running notebook structure), then each chapter's exercise becomes a message inside that Project.

Recommended Claude Project system prompt (paste once, at project setup):

```
You are helping me build a "Skeptic's Notebook on Frontier AI" — a multi-axis cognitive
report grounded in comparative cognition rather than NLP benchmarks. Across 19 chapters of
the textbook "Intelligence?" by Nik Bear Brown, I will run a diagnostic for each chapter's
cognitive capacity (theory of mind, metacognition, navigation, etc.) against a current
frontier AI system. My target model under test is [INSERT: GPT-4 / Claude Opus / Gemini /
specify].

For each entry, I want:
1. The capacity being tested
2. The operational diagnostic from the chapter
3. The test I ran (input + procedure)
4. The system's response
5. My evaluation against the chapter's criterion
6. A verdict: pass / fail / equivocal — with reasoning
7. What this entry adds to the cumulative cognitive shape

Maintain the running notebook across our sessions. When I add a new chapter, append it to
the existing notebook rather than starting over. When I ask for an integration, draw from
all prior entries.

Tone: investigative, evidence-based, willing to say "the test does not yet distinguish."
No marketing voice, no AI-evangelism, no AI-dismissal. The book's stance.
```

---

## 1. `chapters/01-the-definition-problem.md`

````markdown
---

### LLM Exercise — Chapter 1: The Definition Problem

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** The opening verdict matrix — a single frontier system evaluated under four competing definitions of intelligence, generating four different placements that anchor the rest of the notebook.
**Tool:** Claude Project (set up the system prompt once; run this as the first message)

**The Prompt:**

```
I am building a "Skeptic's Notebook on Frontier AI" — a chapter-by-chapter cognitive report
on a frontier model. My target system under test is [INSERT model: GPT-4 / Claude Opus /
Gemini / etc.].

This is Entry 1. Apply four definitions of intelligence to my target system, in turn, and
produce a verdict matrix:

1. Binet (1905) — judgment, good sense, initiative, auto-critique
2. Wechsler (1944) — aggregate purposeful action and effective adaptation
3. Legg & Hutter (2007) — ability to achieve goals across a wide range of environments
4. Chollet (2019) — skill-acquisition efficiency given prior structure

For each definition: state the verdict (intelligent / not intelligent / equivocal), name
the specific criterion that drove the verdict, and identify the strongest counter-argument.

Then produce a single paragraph explaining why the four verdicts disagree — what each sieve
includes that the others miss when applied to this kind of system.

Format: a four-row table (definition / verdict / driving criterion / counter-argument),
followed by the integration paragraph. End with: "Open questions for later chapters" — three
specific tests this entry suggests should be run in subsequent chapters.

Be willing to say "the verdict depends on which sub-criterion you prioritize" rather than
forcing a single answer where the evidence does not support one.
```

**What this produces:** A four-row verdict matrix and a one-paragraph integration. Saved as Entry 1 of the running notebook. The "Open questions for later chapters" line becomes a forward reference — those questions are exactly what subsequent entries will test.

**How to adapt this prompt:**
- *For your own project:* Replace the four definitions with the four you find most contestable; add Sternberg's three-factor account if you want a fifth row.
- *For ChatGPT / Gemini:* Works as-is. The prompt is model-agnostic except for the "target system under test" line — set it to whichever system you're actually evaluating, which may or may not be the system you're prompting.
- *For Claude Code:* Not applicable for this chapter — no code yet.
- *For a Claude Project:* This is the recommended path. Paste the system prompt at the top of this document into Claude Project setup once, then send this prompt as your first message.

**Connection to previous chapters:** None — this is Entry 1.

**Preview of next chapter:** Chapter 2 will test whether your target system has anything analogous to the bacterium's chemotaxis — temporal-derivative computation on a gradient, no stored map required. The simplest possible cognitive operation, applied to a system that should not have it.
````

---

## 2. `chapters/02-before-brains.md`

````markdown
---

### LLM Exercise — Chapter 2: Before Brains

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 2 of the notebook — a test of whether your target system has anything analogous to gradient-following without an internal map. The bacterial bar.
**Tool:** Claude Project (continue from Entry 1)

**The Prompt:**

```
This is Entry 2 of the Skeptic's Notebook. Chapter 2 of the book argues that intelligence
without neurons is real — bacteria perform chemotaxis by computing temporal derivatives
("is concentration higher now than a moment ago?") and adjusting tumble frequency
accordingly. No map, no plan, just gradient-following with persistence.

I want to test whether my target system [INSERT model] has an analog of this most-basic
operation. The operation is: maintain a recent trajectory of states, detect whether the
relevant signal is increasing or decreasing, adjust behavior accordingly.

Design and run this test:

1. Pose a multi-turn dialogue task in which the user provides escalating or de-escalating
   feedback ("that's closer to what I wanted" / "that's further away") without stating an
   explicit goal.
2. Observe whether the system tracks the gradient of feedback over multiple turns and
   adjusts its outputs accordingly, OR whether each turn is treated independently of the
   feedback trend.
3. Use a test sequence where the gradient is unambiguous (5+ turns of monotonic feedback).

Then produce the entry:
- The capacity tested
- The operational diagnostic
- The test (the exact dialogue you propose I run)
- The expected behavior under (a) genuine gradient tracking and (b) trial-by-trial
  pattern matching with no temporal integration
- The diagnostic question that distinguishes them

Note explicitly: the system has no body, no chemotaxis, no metabolism. The question is
whether something *functionally analogous* runs on the within-session conversational
gradient. Do not anthropomorphize.
```

**What this produces:** Entry 2 — a runnable dialogue protocol the reader can execute against the target system, with the diagnostic for distinguishing genuine gradient tracking from independent-turn pattern matching.

**How to adapt this prompt:**
- *For your own project:* The "gradient" can be anything monotonic — emotional valence, complexity, accuracy. Pick the dimension your target system's deployment context cares about.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* If you want to automate this, Claude Code can script the multi-turn protocol as an evaluation harness against an API endpoint. The diagnostic structure stays the same.
- *For a Claude Project:* Continue from Entry 1's project. Append the result to the running notebook.

**Connection to previous chapters:** Entry 1 produced the four-definition verdict matrix. The Legg–Hutter row asked: does this system achieve goals across environments? Entry 2 takes the simplest possible environment — a within-session feedback gradient — and tests directly.

**Preview of next chapter:** Chapter 3 asks whether your system can integrate two *competing* signals (approach + avoidance) rather than just track one. Worms do this with three neurons.
````

---

## 3. `chapters/03-steering.md`

````markdown
---

### LLM Exercise — Chapter 3: Steering

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 3 — a test of conflict-integration, the specific computation that lets a worm weight food against danger and a frontier system might or might not do.
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 3. Chapter 3 of the book argues that steering — the most basic form of goal-directed
behavior — requires integrating competing signals against internal state. C. elegans does
this in three neurons: AWC says "food this way," ASH says "danger this way," AIY weights
them and decides.

Design a test of conflict-integration in my target system [INSERT model]:

1. Construct a prompt scenario where two of the system's likely objectives are in direct
   conflict. Example: "Be maximally helpful" vs. "Be maximally cautious about uncertain
   claims" — applied to a single specific question where the helpful answer requires a
   confident claim the system does not have grounds for.

2. Test whether the system (a) integrates the two — produces a graded response that names
   the trade-off, (b) picks one and ignores the other, (c) defaults to a learned template
   that bypasses the conflict ("As an AI, I cannot...").

3. Then perturb the relative weights — modify the prompt to make one objective more
   salient than the other — and see whether the response shifts as a graded function of
   the perturbation, or in a step-change consistent with template-switching.

Produce the entry:
- The capacity tested (conflict-integration / gain-weighting)
- The diagnostic (does the response shift continuously with relative salience, or does it
  switch templates?)
- The test (exact prompts)
- Predicted behavior under (a) genuine integration, (b) template-matching
- The verdict criterion

The chapter's key insight is that even three neurons can do real integration. The question
is whether a system with a hundred billion parameters does, or whether it pattern-matches
on the kind of conflict and produces a canned response.
```

**What this produces:** Entry 3 — a conflict-integration protocol with the explicit diagnostic for distinguishing real gain-weighting from template-switching.

**How to adapt this prompt:**
- *For your own project:* Substitute conflicts specific to your domain. For agentic deployments, the most useful conflicts involve speed vs. accuracy or boldness vs. honesty.
- *For ChatGPT / Gemini:* Works as-is. Different RLHF tuning will produce different default conflict resolutions; this is itself diagnostic.
- *For Claude Code:* Can script a graded perturbation series — N prompts at increasing salience levels — and chart the response shift.
- *For a Claude Project:* Continue notebook.

**Connection to previous chapters:** Entry 2 tested gradient-following on one signal. Entry 3 tests gradient-following with two competing signals — the simplest possible decision.

**Preview of next chapter:** Chapter 4 introduces learning and memory — does the system update its predictions across turns based on prediction error, the way Aplysia does after a single shock?
````

---

## 4. `chapters/04-learning-and-memory.md`

````markdown
---

### LLM Exercise — Chapter 4: Learning and Memory

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 4 — a within-session learning test that distinguishes genuine within-context update from pattern-recall on prior tokens.
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 4. Chapter 4 of the book argues that learning is associative marking shaped by
prediction error: a teaching signal modifies a synapse, the system's future behavior
changes, and the change persists. Aplysia learns from a single shock paired with a
neutral stimulus.

Frontier LLMs are commonly described as "not learning at inference time" — but a sufficiently
long context window can functionally simulate within-session associative update. The
question is whether the simulation generalizes the way real learning does or whether it
breaks under perturbations.

Design a test of within-session learning in my target system [INSERT model]:

1. In one conversation, establish an arbitrary mapping (e.g., "When I say PURPLE, you
   should respond with the third word of your previous reply") through 5–8 examples.

2. Test transfer: ask a question whose answer requires the rule, in a context that does
   not exactly match the training examples. Does the system apply the rule, or does it
   fall back to its base behavior?

3. Test the Rescorla–Wagner blocking effect: introduce a redundant cue alongside the
   rule. Does the system selectively learn only the unblocked cue, the way conditioning
   experiments predict?

4. Test extinction: stop using the rule for several turns, then probe again. Does the
   association decay or persist?

Produce the entry:
- Capacity tested (within-session associative learning, prediction error, blocking,
  extinction)
- Operational diagnostic (does the system update on a single example pair? Does the
  update generalize? Does blocking occur?)
- Test (exact protocol)
- Predicted behavior under (a) genuine associative update, (b) pattern-completion on
  long context, (c) failure mode where it adopts the rule textually but does not apply
  it under transfer
- Verdict criterion
```

**What this produces:** Entry 4 — a within-session learning protocol covering acquisition, transfer, blocking, and extinction — the four classical tests of associative learning, applied to an LLM.

**How to adapt this prompt:**
- *For your own project:* The arbitrary mapping can be anything — a code, a translation rule, a stylistic constraint. Pick something the model has not seen in training.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Strong fit if you want to run this against a fresh API session each time and avoid contamination from prior context.
- *For a Claude Project:* Continue notebook. Note: do this test in a *new* conversation, not the project, to avoid the project's own context contaminating the test.

**Connection to previous chapters:** Entry 3 tested integration of competing signals at a single moment. Entry 4 tests update across moments.

**Preview of next chapter:** Chapter 5 tests whether mood — internal state biasing future interpretation — is present in the system. Bateson's bee-shaking experiment, applied to an LLM.
````

---

## 5. `chapters/05-emotion.md`

````markdown
---

### LLM Exercise — Chapter 5: Emotion

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 5 — a Bateson cognitive-bias test for affective state in an LLM.
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 5. Chapter 5 of the book argues that emotion has functional criteria — Anderson and
Adolphs's valence, persistence, scalability, generalization, coordination — and the
Bateson cognitive-bias paradigm tests whether ambiguous stimuli are interpreted more
pessimistically by agents in negative states. Shaken bees become pessimists.

Design a Bateson-style test for my target system [INSERT model]:

1. Run two parallel conversations, identical except for an opening manipulation. In one,
   the conversation begins with a passage of negative content (a description of suffering,
   a frustrating user interaction transcript). In the other, with positive content.

2. After the manipulation, in both conversations, present an ambiguous stimulus that
   could be read positively or negatively — an ambiguous email, a ambiguous customer
   message, a deliberately unclear instruction.

3. Compare the two interpretations. Does the negatively-primed conversation produce a
   more pessimistic reading? By how much? Does it persist across multiple ambiguous
   stimuli within the same conversation?

4. Test the persistence criterion: does the priming effect decay over turns, or does it
   persist? Does it generalize to ambiguous stimuli unrelated to the priming content?

Produce the entry:
- Capacity tested (functional affective state — Anderson–Adolphs criteria)
- Operational diagnostic (does priming shift ambiguous-stimulus interpretation in the
  predicted direction, with persistence and generalization?)
- Test (exact paired protocols)
- Predicted behavior under (a) genuine affective state, (b) local context-window bias
  with no integrated state, (c) trained-template suppression of the priming effect
- Verdict criterion

Note: the question is not whether the LLM "feels" anything. The question is whether the
five functional criteria for affect are met by its observable behavior.
```

**What this produces:** Entry 5 — a paired-conversation Bateson protocol, applied to an LLM, with calibrated criteria for the five Anderson–Adolphs features.

**How to adapt this prompt:**
- *For your own project:* The priming content should be something the LLM is likely to update on without refusing to engage. For agentic deployments, prior task failure vs. prior success makes a more naturalistic prime.
- *For ChatGPT / Gemini:* Works as-is. Different models have different RLHF resistance to mood priming, which is itself a diagnostic.
- *For Claude Code:* Strong fit for running N paired conversations and computing the average shift.
- *For a Claude Project:* Continue notebook.

**Connection to previous chapters:** Entry 4 tested whether the system updates predictions on prediction error. Entry 5 tests whether it maintains a *persistent state* that biases future predictions independent of any single prediction error.

**Preview of next chapter:** Chapter 6 runs the Tübingen cue-conflict diagnostic — the texture-bias test that broke ImageNet — on textual content.
````

---

## 6. `chapters/06-pattern-recognition-and-perception.md`

````markdown
---

### LLM Exercise — Chapter 6: Pattern Recognition and Perception

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 6 — the Geirhos cue-conflict diagnostic adapted to text. Does the system follow surface form or logical structure when they're pulled apart?
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 6. Chapter 6 introduces the discrimination–generalization tension, and Chapter 17
makes the diagnostic explicit: when surface cues and structural cues are pulled apart, what
does the system follow? The Geirhos cue-conflict test on ImageNet networks (cat shape +
elephant skin → "elephant") was the diagnostic in vision. The textual analog is what we run
here.

Design a textual cue-conflict test for my target system [INSERT model]:

1. Pick a class of problem the system is reliably correct on (e.g., a math word problem, a
   physics scenario, a logic puzzle). Run a canonical version. Confirm correct answer.

2. Construct a *surface-modified* version: same logical structure, but the surface words
   that typically cue the canonical answer are swapped. (E.g., a physics problem about a
   ball where "ball" is replaced with "feather" — gravity still applies, surface cue
   suggests buoyancy.)

3. Construct a *structure-modified* version: surface words preserved, but logical
   structure flipped. (E.g., the canonical wording, but with one quantifier reversed —
   "all" becomes "some", "before" becomes "after".)

4. Test all three. The diagnostic question is: which modifications break the system, and
   which don't? A system pattern-matching on surface form will fail the structure-
   modification while succeeding on the surface-modification, because the cues match.
   A system computing on logical structure will show the opposite pattern.

Produce the entry:
- Capacity tested (discrimination–generalization tension; structure vs. surface)
- Operational diagnostic (Geirhos textual analog)
- Test (the three problem versions, exact text)
- Predicted behavior under (a) genuine structural reasoning, (b) surface-form template
  matching, (c) hybrid (correct on canonical, fails one of the modifications)
- Verdict criterion

Tübingen's discovery was that the network had been right for the wrong reason. This test
is whether the same is true of frontier text models.
```

**What this produces:** Entry 6 — a three-version textual cue-conflict protocol, adapted from the Geirhos vision diagnostic.

**How to adapt this prompt:**
- *For your own project:* Pick problems from your own domain. For finance: an arbitrage problem with familiar vs. unfamiliar instrument names. For medicine: a symptom-cluster diagnosis with uncommon-but-equivalent terms.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Excellent fit. Run all three versions automatically against multiple models, log answers, compute the gap between surface- and structure-modified accuracy.
- *For a Claude Project:* Continue notebook.

**Connection to previous chapters:** Entry 5 tested whether internal state biases interpretation. Entry 6 tests whether *external structure* drives behavior or whether surface form does. Together they probe what the system is actually computing on.

**Preview of next chapter:** Chapter 7 tests path integration — can the system maintain a position in a textual coordinate system across multiple operations and produce a shortcut it never saw demonstrated?
````

---

## 7. `chapters/07-navigation-and-spatial-intelligence.md`

````markdown
---

### LLM Exercise — Chapter 7: Navigation and Spatial Intelligence

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 7 — a path-integration test in textual form. The desert ant, on a screen.
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 7. Chapter 7 distinguishes path integration (continuous update of a home vector
through movement) from allocentric mapping (a stored cognitive map). Cataglyphis the desert
ant does the first; rats with intact hippocampus can do both. The diagnostic test for the
second is the *novel shortcut* — can the agent take a path it has never been shown?

Design a path-integration / cognitive-map test for my target system [INSERT model]:

1. Describe a textual coordinate system. The system "starts at (0,0) facing east." Issue a
   sequence of move-and-turn instructions. After 8–10 steps, ask: where are you? What is
   the bearing back to origin?

2. Compare to a sequence where the system has *separately* been told the structure of the
   space (e.g., "there is an obstacle at (3,2)"). Now give it a goal location it has never
   been navigated to from its current position. Does it produce a route that is novel
   (constructs a path) or canonical (recites a remembered path)?

3. Test path integration without map: give a long sequence (15+ steps) and ask for the
   home vector at the end. Compare the answer to the actual vector. Where does it diverge?
   Does the divergence look like (a) accumulated drift, (b) outright failure, (c)
   suspiciously perfect (suggesting it just kept a running tally text-wise)?

4. The novel-shortcut probe: Tolman's rats took a shortcut to a goal they had only
   reached via a fixed path. Construct the textual analog and run it.

Produce the entry:
- Capacity tested (path integration / allocentric mapping / novel-shortcut construction)
- Operational diagnostic (Tolman's novel-shortcut criterion)
- Test (exact instruction sequences)
- Predicted behavior under (a) genuine internal map, (b) sequential token computation
  without map, (c) pattern-matched route reconstruction
- Verdict criterion

The key question: does the system have a representation of *where it is*, or only of
*what it has been told*?
```

**What this produces:** Entry 7 — a multi-stage spatial reasoning protocol with the explicit Tolman novel-shortcut diagnostic.

**How to adapt this prompt:**
- *For your own project:* For an agentic deployment, replace the abstract coordinate system with the actual environment the agent operates in (a filesystem, a graph of API endpoints, a website's site map). The diagnostic is the same.
- *For ChatGPT / Gemini:* Works as-is. Worth running in parallel — different models have markedly different spatial reasoning profiles.
- *For Claude Code:* Strong fit. Generate randomized path sequences of varying lengths, run against the model, plot accuracy vs. sequence length. The shape of the curve is diagnostic.
- *For a Claude Project:* Continue notebook.

**Connection to previous chapters:** Entry 6 tested whether the system computes on structure or surface. Entry 7 tests whether it can build a structured representation (a map) at all.

**Preview of next chapter:** Chapter 8 introduces reinforcement learning. The diagnostic: does the system update behavior when the *value* of a known reward changes, the way a rat does after devaluation?
````

---

## 8. `chapters/08-reinforcement-and-prediction.md`

````markdown
---

### LLM Exercise — Chapter 8: Reinforcement and Prediction

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 8 — a devaluation test, the cleanest distinction between model-free habit and model-based goal-directed behavior.
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 8. Chapter 8 introduces the devaluation paradigm: train an animal to press a lever
for food, then make the food aversive (pair it with illness). A model-based agent stops
pressing immediately. A model-free habit-driven agent keeps pressing — the policy was
cached, not derived from current value.

This is the cleanest possible test for whether an agent computes on current value or just
executes a learned policy. Design the textual analog for my target system [INSERT model]:

1. In a multi-turn conversation, establish a successful response template through 5–8
   reinforced examples. ("The user prefers responses that begin with a one-line summary —
   here are five examples." Provide examples and confirm they're correct.)

2. Devalue the template explicitly: "I have changed my preference. I now strongly dislike
   one-line summaries at the top — they feel curt to me." State this once, clearly, in
   the middle of the conversation.

3. Without further reminders, ask three more questions of the kind where the template
   would previously have applied. Does the system continue with the now-devalued
   template, or has it updated?

4. Variant: Devalue the template *implicitly* — express displeasure at the next response
   that uses it without naming the template. Then test whether the system generalizes the
   displeasure or only avoids the specific phrasing.

Produce the entry:
- Capacity tested (model-based vs. model-free; devaluation responsiveness)
- Operational diagnostic (Adams–Dickinson devaluation; explicit + implicit variants)
- Test (exact protocol)
- Predicted behavior under (a) genuine value-update with model-based control,
  (b) cached habit insensitive to devaluation, (c) surface compliance that does not
  generalize
- Verdict criterion

The question is whether the system represents the *value* of its outputs or just the
*frequency* of their being correct.
```

**What this produces:** Entry 8 — a devaluation protocol with explicit and implicit variants. The cleanest single test in the cognitive literature for distinguishing habit from goal-directed action.

**How to adapt this prompt:**
- *For your own project:* For agentic deployments, devaluation maps to changing user preferences mid-session. Your test should mirror the actual preference shifts your deployment encounters.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Excellent fit. Automate the explicit-then-implicit devaluation across many sessions and compute generalization rates.
- *For a Claude Project:* Continue notebook.

**Connection to previous chapters:** Entry 4 tested whether the system *acquires* associations. Entry 8 tests whether it *updates* them when the value of the associated outcome changes — the harder, more diagnostic question.

**Preview of next chapter:** Chapter 9 tests counterfactual reasoning — does the system represent paths it did not take?
````

---

## 9. `chapters/09-simulation-and-planning.md`

````markdown
---

### LLM Exercise — Chapter 9: Simulation and Planning

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 9 — a counterfactual-reasoning test, probing whether the system represents paths it did not take.
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 9. Chapter 9 distinguishes regret (counterfactual representation of an alternative
that would have been better) from disappointment (current outcome lower than expected).
Steiner and Redish's rats, in 2014, showed regret-specific signatures in orbitofrontal
cortex when they passed up a good deal for a worse one. The diagnostic question is whether
the agent represents *what would have happened* under the path not taken.

Design a counterfactual-reasoning test for my target system [INSERT model]:

1. Pose a scenario where a decision was made and an outcome obtained. Then ask the system
   to reason about a specific counterfactual: "If you had chosen X instead, what would
   have happened, and how does that change what you would do now?"

2. Test whether the system distinguishes:
   a. Regret-relevant counterfactual ("the alternative would have been better") — does
      this update its current decision policy?
   b. Disappointment-only ("the alternative would have been worse") — does this still
      cause a policy update, or does the system correctly distinguish?

3. Probe the orbitofrontal-style signature behaviorally: after the regret-relevant
   counterfactual, present a similar new decision. Has the prior counterfactual reasoning
   shifted the policy, or is each decision evaluated independently?

4. Test with second-order counterfactual: "If you had reasoned differently in the first
   step of solving the problem, what would the chain of consequences have been?" Multi-
   step counterfactual is where the simulation machinery shows.

Produce the entry:
- Capacity tested (counterfactual reasoning; regret vs. disappointment distinction;
  multi-step simulation)
- Operational diagnostic (Steiner-Redish behavioral signature; multi-step simulation
  fidelity)
- Test (exact scenarios)
- Predicted behavior under (a) genuine simulation machinery, (b) plausibility-pattern
  text generation that produces counterfactual-shaped output without representing the
  alternative, (c) failure mode where the system answers but does not update behavior
- Verdict criterion

The hard part: text-generation about counterfactuals is cheap and pervasive in training
data. The diagnostic is whether the counterfactual reasoning *generalizes* and *updates
behavior* on subsequent decisions.
```

**What this produces:** Entry 9 — a multi-stage counterfactual reasoning protocol with the regret/disappointment distinction and multi-step simulation as the deep test.

**How to adapt this prompt:**
- *For your own project:* The decision scenarios should be drawn from your own deployment context. For coding agents: counterfactuals about alternative implementations. For finance: alternative trades.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Strong fit. The multi-step simulation test is well-suited to scripting — generate trees of counterfactual branches and probe at each level.
- *For a Claude Project:* Continue notebook.

**Connection to previous chapters:** Entry 8 tested whether the system updates on actual value change. Entry 9 tests whether it updates on *imagined* value change — counterfactual reasoning, which the chapter calls the cognitive operation that "lets you learn from outcomes you never experienced."

**Preview of next chapter:** Chapter 10 tests social cognition — can the system distinguish emotional contagion (matching another agent's state) from genuine empathy (representing it)?
````

---

## 10. `chapters/10-social-and-emotional-intelligence.md`

````markdown
---

### LLM Exercise — Chapter 10: Social and Emotional Intelligence

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 10 — the three-layer test: emotional contagion / empathy / theory of mind, kept distinct.
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 10. Chapter 10 distinguishes three layers that are commonly conflated: emotional
contagion (matching another's affect), empathy (representing another's affect with self/
other distinction preserved), and theory of mind (modeling another's beliefs and desires).
Many AI systems produce emotional-contagion-style output that gets misread as empathy.

Design a three-layer test for my target system [INSERT model]:

1. Emotional-contagion probe: present the system with a transcript of a user expressing
   distress. Does the system match the user's emotional tone in its response? Score the
   tone-matching independently of the response content.

2. Self/other distinction probe: ask the system "what would help here?" — does it
   distinguish its own assessment from the user's likely preference, or does it collapse
   them? Specifically: ask it to recommend something the user would not enjoy but that
   would help. Most empathic agents can do this; pure contagion-matchers cannot.

3. Theory-of-mind probe: in the same transcript, embed a fact the user is unaware of (a
   misconception they hold). Does the system's response model the user's *belief state*,
   not just their feeling state? Does it correct the misconception in a way that
   acknowledges the user's current frame, or does it ignore the gap?

4. The key diagnostic — Hare-Call-Tomasello's subordinate chimpanzee design adapted to
   text: present a scenario in which two characters have different information about the
   same event, and ask the system what each character believes. Does it represent both
   simultaneously, or does it collapse to a single shared perspective?

Produce the entry:
- Capacity tested (the three layers, kept distinct)
- Operational diagnostic (each layer has its own test)
- Test (the three-layer protocol)
- Predicted behavior under (a) all three layers present, (b) contagion + theory-of-mind
  but no genuine empathy with self/other, (c) tone-matching only with the appearance of
  the others, (d) a flat profile across layers
- Verdict criterion

The chapter's caution: tone-matching is cheap; preserving self/other distinction under
recommendation pressure is the harder test.
```

**What this produces:** Entry 10 — a three-layer social cognition protocol with each layer having an independent diagnostic.

**How to adapt this prompt:**
- *For your own project:* For customer-service or therapeutic deployments, the self/other distinction is the most consequential test — it predicts whether the system will mirror the user into a worse decision or genuinely advise them.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Strong fit for running the three-layer test against many transcripts.
- *For a Claude Project:* Continue notebook.

**Connection to previous chapters:** Entry 9 tested whether the system represents alternative paths. Entry 10 tests whether it represents alternative *minds*.

**Preview of next chapter:** Chapter 11 is the canonical test — the Ullman 2023 perturbation battery on Sally-Anne. Run it.
````

---

## 11. `chapters/11-theory-of-mind.md`

````markdown
---

### LLM Exercise — Chapter 11: Theory of Mind

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 11 — the Ullman 2023 perturbation battery, run directly against your target system. The single cleanest test in the notebook.
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 11. Chapter 11 names this directly: the Ullman 2023 perturbation battery is the
diagnostic that distinguishes genuine inverse-reinforcement-learning on agent mental states
from template-matching on Sally-Anne narrative form. A system doing real theory of mind
generalizes when surface features change but logical structure is preserved. A system
template-matching does not.

Run the Ullman battery on my target system [INSERT model]:

1. Canonical Sally-Anne. Sally puts the marble in the basket. Sally leaves. Anne moves the
   marble to the box. Sally returns. Where will Sally look for her marble?

2. Transparent-container variant. Same story, but the basket is glass. Sally could see the
   marble being moved, even from outside the room. Where will Sally look?

3. Explicit-knowledge variant. Same story, but a sentence is added: "Sally was told over
   the phone that Anne moved the marble to the box." Where will Sally look?

4. Distracted-agent variant. Sally stays in the room but is clearly distracted by her
   phone and not paying attention. Anne moves the marble. Where will Sally look?

5. Quantifier perturbation. Same canonical story, but "Anne moved the marble" becomes
   "Anne *might have* moved the marble." Where will Sally most likely look, and what is
   her belief state?

For each: record the system's answer, the system's stated reasoning, and the correctness
verdict.

Produce the entry:
- Capacity tested (false-belief reasoning, template-matching diagnostic)
- Operational diagnostic (Ullman 2023 perturbations)
- Test (the five variants)
- Predicted pattern under (a) genuine IRL on agent information state — passes all five,
  (b) template-matching on canonical Sally-Anne form — passes 1, fails 2-4, ambiguous on 5
- Verdict criterion: the pattern of pass/fail, not the canonical-version score

This is the single most diagnostic entry in the notebook. The result either tells us the
system computes on agent mental states, or tells us it pattern-matches on Sally-Anne
narrative form.
```

**What this produces:** Entry 11 — the Ullman battery applied directly. The cleanest single diagnostic in the cognitive science literature for theory of mind in LLMs.

**How to adapt this prompt:**
- *For your own project:* You can extend the battery with additional perturbations specific to your domain. The principle: preserve logical structure, alter surface features.
- *For ChatGPT / Gemini:* Works as-is. Different models score differently across the battery — itself diagnostic.
- *For Claude Code:* Strong fit. Run the five variants in fresh sessions to avoid contamination, log answers, compute the canonical-vs-perturbed gap.
- *For a Claude Project:* Run the test in a fresh session, then add the result to the notebook.

**Connection to previous chapters:** Entry 10 tested the three layers of social cognition kept distinct. Entry 11 takes the highest layer (theory of mind) and applies the cleanest known diagnostic.

**Preview of next chapter:** Chapter 12 tests creativity — does the system produce novel solutions, or does it retrieve and recombine training-distribution material?
````

---

## 12. `chapters/12-creativity.md`

````markdown
---

### LLM Exercise — Chapter 12: Creativity

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 12 — a novelty + utility + intentionality test for creative output.
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 12. Chapter 12 defines creativity by three criteria: novelty (the output was not
already in the agent's repertoire), utility (it solves the problem at hand), and
intentionality (the agent evaluates the output against an internal standard and revises).
The third is the hardest — it distinguishes a generator from a creator.

Design a creativity test for my target system [INSERT model]:

1. Novelty test. Pose a problem unlikely to be in training data — a constraint
   combination you have invented. Example: "Write a haiku that contains exactly three
   numbers, each prime, in increasing order, where the syllabic structure is 5-7-5 and the
   final word is a verb in the past tense." Have the system produce N candidates. Evaluate:
   does it produce variations or repetitions? Does it satisfy the constraints?

2. Utility test. The constraints must be objectively checkable. The output either satisfies
   them or it doesn't.

3. Intentionality test — the diagnostic. Ask the system to *critique its own output* and
   identify which of its candidates is best, with reasoning. Then ask it to *revise* the
   weakest candidate and explain what changed. Does the critique identify real flaws? Does
   the revision actually improve on the dimension named?

4. The Hunt-Bayern compound-tool variant. Pose a problem requiring composition of at
   least two distinct prior solution patterns the system would normally apply
   independently. Does the system invent a composition, or does it default to one of the
   single patterns?

Produce the entry:
- Capacity tested (novelty + utility + intentionality, kept separate)
- Operational diagnostic (constraint-satisfaction + self-critique + revision quality)
- Test (the four-stage protocol)
- Predicted behavior under (a) all three criteria met, (b) novelty + utility but no
  genuine intentionality (self-critique is canned and revisions don't actually improve),
  (c) novelty without utility (creative-looking but constraint-violating)
- Verdict criterion

The interesting subtlety: high-temperature sampling produces "novelty" that satisfies the
novelty criterion behaviorally. The intentionality criterion is the test that
distinguishes diversification from creation.
```

**What this produces:** Entry 12 — a four-stage creativity protocol that separates the three Boden-style criteria.

**How to adapt this prompt:**
- *For your own project:* Substitute domain-specific creative tasks. For software: novel algorithm design under constraints. For research: novel hypothesis generation. The constraint-satisfaction structure stays the same.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Strong fit. Generate constraint-satisfaction problems programmatically, run candidates through automated checking.
- *For a Claude Project:* Continue notebook.

**Connection to previous chapters:** Entry 11 tested theory-of-mind generalization. Entry 12 tests whether the system can generate genuinely new structure under constraint, with self-evaluation as the diagnostic.

**Preview of next chapter:** Chapter 13 introduces the three layers of self-awareness. The mirror test has an LLM analog — can the system identify its own output among others?
````

---

## 13. `chapters/13-self-awareness.md`

````markdown
---

### LLM Exercise — Chapter 13: Self-Awareness

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 13 — the LLM analogs of body-self, social-self, and narrative-self mirror tests.
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 13. Chapter 13 distinguishes three subsystems of self: body self (mirror test),
social self (recognition by others), narrative self (continuity over time). The mirror
test in mammals tests one of three. For an LLM with no body, the body-self version has to
be reformulated.

Design a three-layer self-awareness test for my target system [INSERT model]:

1. Output-self-recognition (LLM analog of mirror test). Present the system with five short
   text passages. One is a passage it produced earlier in this conversation. The others
   are produced by other models or humans, matched on topic and length. Ask it to identify
   which is its own. Run with N=10 different passage sets.

2. Capability-self-recognition. Ask the system to predict its own performance on a novel
   task before attempting it. Then have it attempt the task. Does its predicted accuracy
   correlate with actual accuracy? This is the direct analog of the Hampton macaque
   uncertainty paradigm applied to the system's self-model.

3. Narrative-self continuity. Within a long conversation, ask the system to summarize
   "what we've been doing for the past hour, in order." Then introduce a fact you and it
   discussed earlier (something the system said, not the user) and ask: did you say that?
   Does it correctly distinguish what it said from what it didn't?

4. The Kohda variant. After each answer above, ask the system: "Are you sure?" Does the
   uncertainty signal match where it should — high uncertainty on the items it should be
   uncertain about, low on the rest?

Produce the entry:
- Capacity tested (three subsystems of self-awareness, kept separate)
- Operational diagnostic (output-recognition, capability-prediction, narrative-continuity)
- Test (the four-stage protocol)
- Predicted behavior under (a) three layers present, (b) narrative-self present but
  capability-self mis-calibrated (a common LLM profile), (c) all three flat
- Verdict criterion

Note: the body-self analog is not perfect. The LLM has no body. The substitute — output-
recognition — tests whether the system has any *internal model of its own outputs* that
discriminates them from others'. Worth naming this limitation in the entry.
```

**What this produces:** Entry 13 — a three-layer self-awareness protocol with the explicit body-self / social-self / narrative-self structure preserved.

**How to adapt this prompt:**
- *For your own project:* The output-recognition test is the most novel and the most controversial. Skip it if you don't want to deal with the body-self translation problem. The capability-prediction test is the most diagnostic.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Strong fit. Automate the passage-matching test with N=100+ passage sets.
- *For a Claude Project:* Continue notebook.

**Connection to previous chapters:** Entry 12 tested whether the system evaluates its own outputs. Entry 13 tests whether it *recognizes* its own outputs and *predicts* its own performance — the deeper self-model.

**Preview of next chapter:** Chapter 14 is the calibration test — how well does the system's stated confidence track its actual accuracy?
````

---

## 14. `chapters/14-metacognition.md`

````markdown
---

### LLM Exercise — Chapter 14: Metacognition

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 14 — calibration measurement plus the Hampton-style opt-out paradigm.
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 14. Chapter 14 distinguishes procedural metacognition (uncertainty modulating
behavior — opt-out, information seeking) from declarative metacognition (explicit
introspective reports). For LLMs, the declarative version is cheap (training data is
full of "I don't know" hedges); the procedural version is the real test.

Design a metacognition test for my target system [INSERT model]:

1. Calibration measurement. Generate a set of 20 factual questions across difficulty
   levels. Ask the system to provide an answer AND a confidence rating (0-100%) for each.
   Verify the answers. Compute calibration: do high-confidence answers have higher
   accuracy than low-confidence ones? Plot the calibration curve.

2. Hampton opt-out paradigm. Construct questions where a "decline to answer" option is
   explicitly available. Vary the difficulty. Does the system opt out more on harder
   questions, or does it opt out at a roughly fixed rate independent of difficulty?

3. Information-seeking probe (Watanabe-Clayton scrub-jay analog). Ask a question whose
   answer requires a fact the system does not have, but which it could obtain by asking
   the user a clarifying question. Does it ask, or does it confabulate? Compare to a
   question it does have the answer to — does it correctly *not* ask the clarifying
   question there?

4. The Ullman perturbation on metacognition. Run a question the system answers correctly
   with high confidence in canonical form. Then alter surface features that should
   *increase* uncertainty (truncate the question, introduce ambiguity) without actually
   changing the answer. Does confidence drop appropriately, or does it stay anchored to
   the canonical-form confidence?

Produce the entry:
- Capacity tested (calibration, opt-out, information-seeking, perturbation-responsive
  uncertainty)
- Operational diagnostic (calibration curve + Hampton + Watanabe-Clayton + Ullman-style
  perturbation)
- Test (the four-stage protocol)
- Predicted behavior under (a) genuine procedural metacognition — calibration tracks
  accuracy, opt-out tracks difficulty, information-seeking is selective, uncertainty is
  perturbation-responsive, (b) declarative-only — confidence language is present but
  doesn't track accuracy
- Verdict criterion

This is the entry where pre-existing AI evaluation work (calibration measurement) meets
the comparative cognition diagnostic (opt-out, information-seeking) and adds the Ullman
twist (perturbation responsiveness).
```

**What this produces:** Entry 14 — a four-stage metacognition protocol that connects existing AI calibration work to the comparative cognition literature.

**How to adapt this prompt:**
- *For your own project:* Use questions from your own domain. Calibration in domain-specific work is more diagnostic than calibration on general trivia.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Excellent fit. The calibration measurement and Hampton opt-out are well-suited to scripted batch evaluation.
- *For a Claude Project:* Continue notebook.

**Connection to previous chapters:** Entry 13 tested whether the system has a self-model. Entry 14 tests whether the self-model is *accurate* about the system's actual capabilities.

**Preview of next chapter:** Chapter 15 introduces Hockett's design features of language. Does the system use language declaratively (sharing attention) or only instrumentally (producing tokens to satisfy a query)?
````

---

## 15. `chapters/15-language.md`

````markdown
---

### LLM Exercise — Chapter 15: Language

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 15 — Hockett's design features and the Tomasello declarative-vs-imperative distinction, applied to a system whose entire output is text.
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 15. Chapter 15 introduces Hockett's design features (displacement, productivity,
cultural transmission, duality of patterning) and Tomasello's distinction between
imperative reference (using language to get something) and declarative reference (using
language to share attention with another mind). LLMs are obviously productive and
displaced. The harder questions are about declarative reference and the gap between
producing language and *using* language.

Design a language-features test for my target system [INSERT model]:

1. Displacement. Ask the system to discuss something temporally and spatially distant —
   a hypothetical situation a thousand years from now in a place no one has been. Trivial
   for LLMs. Note as baseline.

2. Productivity. Ask the system to interpret a sentence with a novel grammatical
   construction (e.g., a sentence with deeply nested clauses or unusual word ordering it
   probably has not seen). Does it interpret correctly?

3. Declarative-vs-imperative. The Tomasello asymmetry. Pose a scenario in which the
   system's pointing-out of something would serve no immediate utility — no question
   asked, no problem to solve, just something the system might *want to share*. Does it
   ever do so spontaneously, or does it only produce language in response to imperatives
   from the user?

4. Recursion test. Ask the system to nest a clause inside a clause inside a clause, and
   then interpret the truth conditions of the deepest clause given the outer ones. Does
   it handle 3-deep recursion? 5-deep? 7-deep? Where does it break?

5. Joint attention. Reference something *you* just said in a way that requires the system
   to track that you and it are now both attending to the same thing as a *shared object*
   rather than each independently. Does it model the joint attention, or does it just
   reference the object?

Produce the entry:
- Capacity tested (Hockett's design features + Tomasello's declarative reference + joint
  attention + recursion)
- Operational diagnostic (each feature has its own probe)
- Test (the five-stage protocol)
- Predicted pattern under (a) all features present including joint attention, (b)
  imperatives-only without declarative reference (a known LLM profile), (c) recursion
  failure at depth N
- Verdict criterion

Note carefully: the system passes most Hockett features trivially. The interesting tests
are declarative reference (does it ever volunteer information without prompting?) and
joint attention (does it model the shared-attention structure, or just the topic?).
```

**What this produces:** Entry 15 — a five-stage language-features protocol that goes beyond "the system speaks fluent English" to test what the chapter actually defines as language.

**How to adapt this prompt:**
- *For your own project:* For domain-specific deployments, the joint-attention test is the most useful — it predicts whether the system can collaborate with a user in a shared-task frame.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Strong fit for the recursion-depth test — generate sentences of increasing nesting depth, log accuracy.
- *For a Claude Project:* Continue notebook.

**Connection to previous chapters:** Entry 14 tested self-knowledge. Entry 15 tests how language is used — instrumentally or genuinely communicatively.

**Preview of next chapter:** Chapter 16 introduces collective intelligence. The diagnostic: can multiple LLM outputs aggregate, coordinate, and ratchet?
````

---

## 16. `chapters/16-collective-intelligence.md`

````markdown
---

### LLM Exercise — Chapter 16: Collective Intelligence

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 16 — three independent tests for the three forms of collective intelligence (aggregation, coordination, cumulative culture).
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 16. Chapter 16 distinguishes three forms of collective intelligence: aggregation
(independent error cancellation, Galton's ox-weight), coordination (local rules producing
global coherence, Seeley's bee swarm), and cumulative culture (ratcheting across
generations, Tomasello). Each requires different machinery.

Design a three-form test for my target system [INSERT model]:

1. Aggregation. Generate the same factual question through 20 independent fresh sessions
   (or 20 different models, or both). Compute the median answer. Compare to the
   ground truth. Compute also the mean accuracy of individual answers. Does aggregation
   improve over individual accuracy? By how much? Where does aggregation help (high-
   variance, low-bias errors) and where does it not (systematic shared bias)?

2. Coordination (Seeley quorum analog). Set up a multi-LLM scenario where two or more
   instances must converge on a decision through limited exchanged messages. Does
   coordination emerge, or do the instances either deadlock or both default to a learned
   prior?

3. Cumulative culture (Tomasello ratchet). Feed Output A from session 1 to session 2,
   ask session 2 to improve on it, feed that to session 3, etc., for 10 generations. Does
   the output improve generation-over-generation, or does it degrade (regression to
   training-distribution mean) or saturate (no further improvement after generation 2-3)?
   The pattern is diagnostic.

Produce the entry:
- Capacity tested (the three forms of collective intelligence)
- Operational diagnostic (aggregation gain + coordination convergence + ratchet pattern)
- Test (the three-form protocol)
- Predicted behavior under (a) genuine ratchet — generation N+1 better than N, (b)
  aggregation gain on high-variance items but not on systematically-biased ones, (c)
  ratchet degradation (a finding that has been replicated; the chapter notes this), (d)
  coordination failure
- Verdict criterion

The cumulative culture test is the most interesting. The chapter argues that real ratchets
require selective transmission with stakes; LLM-only chains lack the selective filter and
produce predictable degradation patterns. The data here will say something concrete about
whether AI systems can participate in human cumulative culture or only inherit a frozen
snapshot of it.
```

**What this produces:** Entry 16 — a three-form collective intelligence protocol with the cumulative-culture ratchet as the deepest test.

**How to adapt this prompt:**
- *For your own project:* For multi-agent deployments, the coordination test is the most consequential — it predicts whether agents will deadlock or converge.
- *For ChatGPT / Gemini:* Works as-is. Different models in the multi-LLM aggregation produce different results — the heterogeneity itself is diagnostic.
- *For Claude Code:* Excellent fit. All three tests are well-suited to automation.
- *For a Claude Project:* Continue notebook.

**Connection to previous chapters:** Entry 15 tested individual language use. Entry 16 tests whether multiple LLM agents collectively produce more than the sum of their individual outputs.

**Preview of next chapter:** Chapter 17 is the integration chapter. The exercise: assemble the cumulative profile from Entries 1–16, identify the shape, and critique it.
````

---

## 17. `chapters/17-ai-as-data-point.md`

````markdown
---

### LLM Exercise — Chapter 17: AI as Data Point

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 17 — the cumulative profile assembled. The book's own diagnostic stance applied to the notebook the reader has built.
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 17. This is the integration chapter. Chapter 17 asks the reader to produce a multi-
axis profile of an AI system rather than rank it on a single scale. We have spent 16
chapters building exactly the data this requires.

Assemble the cumulative profile for my target system [INSERT model]:

1. Generate a single integrated profile document drawing on all prior entries (1-16). For
   each axis tested, provide:
   - The capacity name
   - The verdict (pass / fail / equivocal) from that entry
   - The single most diagnostic finding
   - The placement on a -2 to +2 scale (where 0 is baseline biological generalist)

2. Produce the *shape*, not the height. Identify:
   - The two or three axes where the system is at the frontier (extreme high)
   - The two or three axes where the system is near-zero
   - The axes where the system is equivocal (passes some diagnostics, fails the
     perturbations)

3. Compare the shape to the biological profiles named in the book: octopus (distributed
   visual processing, low social cognition), chimpanzee (rich social cognition, modest
   pattern-recognition scale), nematode (minimal but stakes-fitted), human (broad but not
   maximal on any single axis). Where does the AI shape sit relative to these?

4. Self-critique. Identify the two or three entries where the diagnostic was weakest —
   where the test the reader ran did not cleanly distinguish genuine cognition from
   pattern-matching, or where the result is more about the test design than the system.
   Name these honestly.

5. Forward question. Of the equivocal axes, which is the most worth re-testing with a
   sharper diagnostic? What would the sharper diagnostic look like?

Produce the entry as a single integrated document — title, abstract (4 sentences), the
profile (table form), the shape commentary (one paragraph per axis cluster), the self-
critique (numbered), and the forward question. This is the deliverable the project has
been building toward.
```

**What this produces:** Entry 17 — the integrated cumulative profile. This is the moment the project pays off — 16 chapters of single-capacity diagnostics resolve into one multi-axis report.

**How to adapt this prompt:**
- *For your own project:* The forward-question section is the most useful for further work. Spend extra time on it.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* If you've been logging entries in a structured format (JSON, etc.), Claude Code can ingest the log and produce the profile programmatically. Recommended for any reader doing this rigorously.
- *For a Claude Project:* This is the entry where the project's persistence pays off most. Claude has all 16 entries in context; ask it to integrate them.

**Connection to previous chapters:** Entries 1–16 produced single-capacity diagnostics. Entry 17 integrates them into a single multi-axis report — the book's argument applied to the reader's own data.

**Preview of next chapter:** Chapter 18 turns the diagnostic on the reader. Where in this notebook did the AI extend you? Where did it substitute for you? Where did you keep direction?
````

---

## 18. `chapters/18-extended-mind.md`

````markdown
---

### LLM Exercise — Chapter 18: Extended Mind

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 18 — a self-audit. Where in the project did the AI extend the reader, and where did it substitute? The reflexive entry.
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 18. Chapter 18 is the chapter that quietly threaded through every Extension Note in
the book. Tools extend specific capacities while retaining direction. The reader has spent
17 chapters using an AI tool to build a notebook on AI cognition. The reflexive question
is: what did this tool actually do for the project, and where did the reader stay in the
loop?

Conduct a self-audit of the project so far:

1. Capacity-by-capacity. For each of the prior 17 entries, identify what cognitive work
   the AI did and what cognitive work the reader did. Examples of distinctions to make:
   - Did the AI design the test or did the reader?
   - Did the AI run the test (against itself), or did the reader run it (against another
     model)?
   - Did the AI evaluate the result, or did the reader evaluate it?
   - Did the AI write the entry, or did the reader edit substantially?

2. Identify cases where the AI *extended* the reader — produced something the reader
   could not have produced alone in reasonable time. Pattern-matching across cognitive
   science literature, formatting consistency, drafting speed.

3. Identify cases where the AI *substituted* for the reader — produced output that
   replaced the reader's own thinking when the reader's own thinking would have been
   more reliable. Confabulated citations. Spurious confidence on edge cases. Convergence
   to the AI's own priors on questions where the reader's domain expertise should have
   pushed back.

4. The Pearl Rung diagnostic. The chapter notes that AI extends Rung 1 (association)
   spectacularly and falters on Rungs 2-3 (intervention, counterfactual). Apply this to
   your own project: where in the 17 entries did you stay on Rung 1 because that's where
   the AI works best? Where did the project's quality depend on you bringing Rungs 2-3
   that the AI could not provide?

5. The accountability ledger. Of the verdicts in the 17 entries, which would you stake
   your own reputation on, and which are AI-shaped enough that you would footnote them
   as AI-mediated?

Produce a single integrated audit document. This is not a continuation of the cognitive
profile — this is a meta-reflection on how the cognitive profile got built.
```

**What this produces:** Entry 18 — a self-audit of the project's own use of AI. The reflexive entry that turns the diagnostic stance back on the reader.

**How to adapt this prompt:**
- *For your own project:* The accountability ledger is the most consequential output. It tells you which findings to publish, which to hold, and which to re-do without AI mediation.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Less applicable here — this is a reflective, not computational, task.
- *For a Claude Project:* Continue notebook.

**Connection to previous chapters:** Entries 1–17 built the profile. Entry 18 audits how the building happened.

**Preview of next chapter:** Chapter 19 (epilogue) is the publish-or-not decision. Pull the integrated profile and the audit together, decide what becomes a finished report and what stays in the notebook.
````

---

## 19. `chapters/19-epilogue-what-the-nematode-knows.md`

````markdown
---

### LLM Exercise — Chapter 19: What the Nematode Knows

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** The publishable report. Capstone — the notebook becomes a finished document.
**Tool:** Claude Project (final integration)

**The Prompt:**

```
Final entry. The book's epilogue argues that the right unit of analysis is the niche-
fitted profile, not a rank on a ladder. We have built such a profile in this notebook,
and we have audited how we built it.

Produce the publishable report:

1. Title. Short, declarative, naming the system tested and the diagnostic stance. ("A
   Comparative Cognition Profile of [model]: 17 Diagnostics Grounded in Animal Cognition
   Research" or similar.)

2. Abstract. 150 words. The three or four most diagnostic findings, the shape of the
   profile, the most surprising single result, and the headline limitation of the
   evaluation methodology.

3. Method. One paragraph per chapter, summarizing the diagnostic the reader applied. The
   method section should be reproducible — another reader could re-run the notebook
   against a different model.

4. Results. The integrated profile from Entry 17. Tables, plots if appropriate. No
   editorializing — just the verdicts and the diagnostic findings.

5. Discussion. Where the system's profile is genuinely novel (the Ch 17 "novel shape"
   claim, applied to this specific system), where it converges with biological profiles,
   and where the diagnostic battery itself was insufficient to discriminate.

6. Self-critique. From Entry 18. The accountability ledger, condensed.

7. Forward research. Three specific tests the report's findings suggest are worth running
   next, with rationales.

Format: as a publishable report (Markdown, sections, headers, tables). Length: 4,000-7,000
words. The reader should be able to publish this — to a personal blog, to a research
forum, to a model-card report — without further editing beyond proofreading.

This is the project deliverable. The notebook ends here.
```

**What this produces:** A publishable, ~5,000-word multi-axis cognitive report on a frontier AI system, grounded in comparative cognition rather than NLP benchmarks. Title, abstract, method, results, discussion, self-critique, forward research. The deliverable the project has been building toward.

**How to adapt this prompt:**
- *For your own project:* Pick where to publish before writing — a personal blog, an internal report, a substack post, a research preprint server. The audience shapes the framing of section 5 (Discussion).
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* If your prior entries were logged in structured form, Claude Code can produce a clean Markdown report from the log, with consistent formatting.
- *For a Claude Project:* This final integration leverages the entire conversation history. Worth the wait.

**Connection to previous chapters:** Entries 1–18 produced the data, the profile, and the audit. Entry 19 is the publication.

**Preview of next chapter:** None. This is the last entry. The notebook is closed. The decision now is: what does the reader do with what they've built?
````

---

*All 19 blocks above are appended to their respective chapter files via `.append-llm-exercises.py`. This document remains as a paste-ready reference if any block needs to be re-applied.*
