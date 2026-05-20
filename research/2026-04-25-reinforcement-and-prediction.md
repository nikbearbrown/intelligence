# Research notes — Chapter 8: Reinforcement and Prediction

**Book:** intelligence (*Intelligence? A Natural History of Mind Across the Animal Kingdom*)
**Chapter slug:** reinforcement-and-prediction
**Date:** 2026-04-25
**Command:** `/chapter`
**Voice anchoring:** `voice-unanchored`. Both `style/` folders empty. Eighth drafted unit.

---

## Concept

Reinforcement learning as the algorithmic core of how vertebrate brains learn from experience. The chapter argues that the dopamine prediction-error signal is not a pleasure broadcast but a teaching signal whose mathematical structure was independently discovered by Sutton in 1988 (TD learning) and identified in midbrain dopamine neurons by Schultz, Dayan, and Montague in 1997. The basal-ganglia actor-critic architecture is conserved back to the lamprey ~560 million years ago.

## Specification move

Three things unbundled before empirical work:

1. **Pleasure vs. teaching signal.** Dopamine has been popularly framed as a pleasure molecule. The Schultz dip experiments and the Berridge wanting-vs-liking work together show this is the wrong frame. Dopamine is a *teaching signal* (TD-error broadcast); the felt experience of pleasure depends on opioid and other systems that the chapter does not deep-dive into.
2. **Pavlovian (predict) vs. Instrumental (control).** Two different problems with related but distinct neural solutions. Pavlovian: cue → outcome (S-S). Instrumental: action → outcome (A-O).
3. **Model-free (cached values) vs. Model-based (simulation).** Same reinforcement-learning machinery; different uses. Model-free is fast and brittle. Model-based is flexible and computationally expensive. The mammalian brain runs both; behavior toggles between them.

## Empirical vs. non-empirical sub-claims

| Sub-claim | Status |
|---|---|
| Schultz's dopamine neurons fire phasic burst at unexpected reward, transfer to predictive cue, dip at expected-but-omitted reward | **Empirical**, settled (Schultz 1990s; Schultz-Dayan-Montague 1997) |
| The dopamine signal matches the TD-error δ_t | **Empirical/theoretical**, settled as the leading model (Schultz-Dayan-Montague 1997) |
| Sutton 1988 introduced the TD-learning algorithm in *Machine Learning* | **Empirical**, settled |
| Adams-Dickinson 1981 devaluation paradigm distinguishes habits (model-free) from goal-directed action (model-based) | **Empirical**, settled |
| The basal-ganglia actor-critic architecture is conserved back to lamprey | **Empirical**, well-supported (Grillner lab and others) |
| Mnih et al. 2015 DQN matched human performance on 49 Atari games | **Empirical**, settled |
| Dopamine encodes a vector RPE rather than a scalar | **Empirical/contested** — current best reading per recent work but not yet textbook consensus |
| Berridge wanting/liking dissociation | **Empirical**, well-supported across rat literature |
| Reinforcement-learning systems are vulnerable to reward hacking and Goodhart's Law | **Empirical**, well-supported in AI-safety literature |

## Primary sources

1. **Thorndike, E.L. (1911).** *Animal Intelligence*. Macmillan. https://archive.org/details/animalintelligen00thor — puzzle-box experiments and Law of Effect.
2. **Sutton, R.S. (1988).** "Learning to predict by the methods of temporal differences." *Machine Learning* 3: 9–44. https://link.springer.com/article/10.1007/BF00115009 — the TD algorithm.
3. **Schultz, W., Dayan, P., Montague, P.R. (1997).** "A Neural Substrate of Prediction and Reward." *Science* 275: 1593–1599. https://www.science.org/doi/10.1126/science.275.5306.1593 — dopamine = TD error.
4. **Adams, C.D. & Dickinson, A. (1981).** "Instrumental responding following reinforcer devaluation." *Quarterly Journal of Experimental Psychology* 33B: 109–121. https://journals.sagepub.com/doi/10.1080/14640748108400816 — habits vs goal-directed action.
5. **Mnih, V. et al. (2015).** "Human-level control through deep reinforcement learning." *Nature* 518: 529–533. https://www.nature.com/articles/nature14236 — DQN on Atari.

Also referenced without primary URLs:
- Rescorla & Wagner 1972 (already cited in Ch. 4 via Scholarpedia).
- Berridge wanting-vs-liking work (Berridge & Robinson 1998 *Brain Research Reviews* etc.).
- Tesauro TD-Gammon 1995.
- Grillner lamprey basal-ganglia comparative work.

## Mechanism for the deep-dive

*The Schultz-Dayan-Montague identification of dopamine as the TD error signal δ_t.* §8.3 walks the TD update rule on the page: V(s_t) ← V(s_t) + α[r_{t+1} + γV(s_{t+1}) − V(s_t)]. The prediction error δ_t is the bracketed term. Schultz's three-phase result — burst at unexpected reward, transfer to predictive cue, dip at expected-but-omitted reward — is shown to be exactly what the TD algorithm predicts. The basal-ganglia actor-critic anatomy is then mapped: striosomes in the striatum supply V(s_t); dopamine neurons compute and broadcast δ_t; corticostriatal plasticity is gated by δ_t. One sentence: *the algorithm and the anatomy are the same thing.*

## Central analogy

*Dopamine as the universal currency of update.* The "currency" framing lands cleanly because it captures both the broadcast nature of the signal (one neurotransmitter, many target sites) and the value-update function (every transaction in the brain that involves a value gets paid in this currency). Where the analogy breaks: a real currency is conserved across transactions; dopamine is a signal that is generated and consumed, not exchanged. The break is small and the analogy survives.

## Voice notes

- Natural-history register continued. The Schultz monkey scene in §8.1 anchors the chapter, with the *dip* as the load-bearing observation.
- First person used in §8.3 ("by my reading"), §8.5 ("I conclude"), and "What would change my mind." Sparingly.
- Single-sentence paragraphs at three pivots: end of §8.1 ("This is the chapter"), end of §8.3 first major beat ("the algorithm and the anatomy are the same thing" — phrased as the chapter's own conclusion), §8.5 closing ("The dip is the moment to remember").
- Math on the page in §8.3: the TD update equation, with each term explained in plain prose. This is the *math-on-the-page* moment for the chapter per the workshop rules.
- Extension Note (seventh in book): recommendation engines, RL trading, the specification problem. The chapter explicitly names Goodhart's Law and the 6 May 2010 Flash Crash as concrete instances of misspecified reward functions. Reinforces the leitmotif from Ch. 7 (additive vs substitutive extension) by noting that RL systems can extend optimization capacity but cannot specify what to optimize — that is still on the human side.

## Risks flagged

- **Schultz's actual original recordings** are reported across multiple papers (Schultz 1986, 1992, 1993, 1994, 1997). I cite the 1997 Schultz-Dayan-Montague *Science* paper as the synthesis where the TD-error correspondence was made explicit. The original phasic-firing observations are earlier; Schultz's 1986 *J Neurophysiology* paper is the first published.
- **The "actor-critic in basal ganglia" framing is the leading model**, not consensus. Houk-Adams-Barto and the related O'Doherty actor-critic-in-striatum proposal are the standard references. The mapping to striosomes-as-critic vs matrix-as-actor is a model that is well-supported but not airtight; alternative anatomical mappings exist.
- **The vector-RPE picture (Sharpe, Engelhard, et al.) is recent enough** that I describe it briefly in §8.3 without citing a specific paper. The Engelhard 2019 *Nature* paper is the standard reference if review wants it added.
- **Berridge wanting-vs-liking** is presented compactly in §8.3. The full debate has more nuance; if review wants more detail, it would add a paragraph at the cost of trimming elsewhere.
- **The "Flash Crash" framing** in the Extension Note is a popular shorthand for what was actually a more complex sequence of events. The trillion-dollar number is the peak intraday market-cap loss before recovery, not a permanent loss. The chapter is careful in saying "twenty minutes" and "evaporation" without overcommitting to specifics.

## Process note

Eighth drafted unit. The TD-error story is one of the few moments in the book where biology and computation lock together so tightly that the math literally fits the firing rates. The chapter leans into that strength. Voice still flagged `voice-unanchored` — eight units now in the same register; the case for clearing the flag continues to strengthen.
