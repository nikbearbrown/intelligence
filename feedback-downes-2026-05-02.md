# Thoughts on the Downes feedback

*Read in light of Ch 1 (definition problem), Ch 11 (theory of mind), Ch 17 (AI as data point).*

Downes is a serious reader and a generous one. The three pushes are not equally weighted. One of them is fully answered by commitments the book has already made, one is partially anticipated but exposes a tension worth tightening, and one lands hard and names a gap the book has not yet closed.

## Point 2 first, because it's the cleanest

Downes asks: "Does it matter if I have a 'theory of mind' that was evolved through the history of my species, as opposed to created artificially in a lab, if both theories of mind are to all intents and purposes identical?"

The book has already answered this. The Legg-Hutter commitment in Chapter 1 is *substrate-neutral* by design — that's named as a feature, not a hedge. Chapter 11 makes the multiple-realizability point explicit on the corvid/primate comparison: "the same functional capacity appearing in a brain built on entirely different principles, in a lineage separated from humans by more than 300 million years… the computation is the constraint. The substrate is not."

So if a lab-built system passes the Ullman perturbation test — generalizes when surface features are altered while logical structure is preserved — it has theory of mind, full stop. The diagnostic is the diagnostic regardless of how the system got there. Downes is naming the assumption you already made, deliberately, in print. The answer to his question is: by the book's own commitments, the method of acquisition does not determine the nature of the function. The test does.

What's worth doing in a reply: thank him for forcing the explicitness, restate the commitment plainly, and note that this is exactly why Chapter 17 leans on the Ullman test rather than on training-history facts.

## Point 1 is partially anticipated, but exposes a real tension

Downes asks whether stakes-based evolution of a function is *necessarily distinct* from the same function developed via pattern recognition — and suggests stakes might uniquely enable something downstream like a sense of self.

Chapter 17's "stakes absent" section is the closest thing the book has to a direct response. It's framed as a *mechanical* claim, not a metaphysical one: stakes-driven evolution lays down architecture in body and reflex and procedural memory that gradient descent on text cannot reach. "A system trained on the outputs of stakes-driven cognition inherits whatever structure is visible in the text." That's the position.

But here is where Downes' Points 1 and 2 collide and the book has to pick a lane more cleanly than it currently does. If you're a substrate-neutral functionalist (Point 2), you cannot also claim stakes are *necessary* for genuine cognition (the way Point 1 reads). The escape is that stakes are *contingently* important — they happen to be the only training process we've seen that reliably produces architectures that pass the Ullman test, but in principle a non-stakes-based training process that produced the same architecture would count. Some passages of Ch 17 read like the stronger ontological claim ("stakes are necessary for cognitive architecture"), and the weaker empirical claim ("stakes-based training is the only training we've seen that produces robust architectures") is what the book's commitments actually license.

A robotic agent with real environmental consequences — a self-driving car whose mistakes cost something, a robot arm that breaks — would be the test case. If such a system developed self-projective theory of mind in the corvid sense, the stakes-as-acquisition-route claim is vindicated empirically. If it didn't, Downes wins and the book has to soften.

What's worth doing in a reply: acknowledge the tension, restate the stakes argument as the weaker empirical claim, and name the test case — what would falsify the stakes-route view.

## Point 3 is where Downes draws blood

He asks how much of what's described as intelligence is acquisition of a (mistaken) folk-psychological theory of mind. The discussion of stakes invokes intentionality, belief, will, desire. The false-belief discussion invests in a mental state "that might not actually exist." The explicit theory-of-mind discussion may require the physical symbol system hypothesis.

Churchland is not in the index. Grep on "Churchland" returns zero hits across the whole manuscript. This is the gap.

Chapter 11's IRL framing is a computational story: the brain infers a compact set of latent variables from behavior, generalizes to novel situations, and the latent variables get *labeled* as beliefs, desires, intentions. The labeling is doing real work. The chapter is implicitly committed to the view that the IRL latent variables vindicate folk-psychological vocabulary — that "belief" picks out a real computational kind, not a phlogiston-like artifact of pre-scientific theorizing. That's a defensible position. It's also a position Churchland has spent fifty years arguing against, and Stich and others alongside him.

The book never says it's taking that position. It just translates IRL outputs into folk vocabulary as if the translation is innocent. It isn't. There's a real philosophical commitment hiding there, and the eliminative-materialist tradition has reasons to think the latent variables of well-fitted social IRL might look more like *trajectory templates* or *policy parameters* than like beliefs in the sense ordinary language attributes — beliefs that are propositional, that have intentional content, that are referred to by pronouns, that can be true or false in the sense Sally-Anne tests.

Downes is right that this commitment is doing work and has not been earned in the text. Three responses are available:

1. **Acknowledge and bracket.** "The IRL framing is computational; the translation to belief/desire vocabulary is notational shorthand for the latent variables, not a substantive claim that folk psychology will be vindicated by neuroscience." This is the cheapest fix.

2. **Defend the vindication.** Argue affirmatively that the IRL latent variables track real computational structure of the kind folk psychology has been pointing at, and that Churchland's pessimism about folk psychology surviving reduction was premature. Bayes-net causal modeling of mental-state attribution (Tenenbaum, Goodman, Baker) is the live research program here — if the book wants to back this, that's the literature to lean on.

3. **Bite the bullet.** Acknowledge that the IRL framing slips into folk psychology in places where it should remain more austere, and edit those passages. This is the most honest move and probably the smallest revision in word count.

What's worth doing in a reply: thank him for the catch, name which response you want to make, and outline the revision — probably a paragraph in Chapter 11 (or a footnote in Chapter 1) that says explicitly what the book is and is not committed to about folk psychology.

## What I'd send Downes

A short letter, two or three paragraphs, doing exactly this:

- Concede Point 3 cleanly. Tell him you're going to add a passage in Chapter 11 that names the Churchland challenge and your position on it.
- For Point 2, restate the substrate-neutral commitment from Chapter 1 and note that the book's diagnostic — Ullman-style content perturbation — is the criterion regardless of acquisition method. The method-of-acquisition question is genuinely settled by the framework.
- For Point 1, distinguish the strong claim (stakes are necessary) from the weaker empirical one (stakes-based training is what we've seen produce robust architecture so far) and name the falsifier — a non-stakes-trained system that passes Ullman, or a stakes-trained robotic agent that doesn't develop self-projective theory of mind.

A reader like Downes is precisely the reader the book wants. The pushback is the kind that sharpens a manuscript rather than redirects it. None of the three points requires reworking the spine; one of them requires naming a commitment you've already made, and one of them requires a paragraph of philosophical clarification that should probably have been in Chapter 11 from the start.
