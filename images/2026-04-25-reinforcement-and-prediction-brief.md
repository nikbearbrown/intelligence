# Hero image brief — Chapter 8: Reinforcement and Prediction

**Book:** intelligence (*Intelligence? A Natural History of Mind Across the Animal Kingdom*)
**Chapter slug:** reinforcement-and-prediction
**Date:** 2026-04-25

---

## Concept

A composition that visualizes the chapter's central observation — *the dopamine dip at the moment of expected-but-omitted reward* — by showing the three-phase transformation of dopamine neuron activity across learning, in the same format Schultz himself used to communicate the result.

## Composition options

**Option A — The three-phase transition.** A clean three-panel raster plot. Each panel shows time on the x-axis, with the cue marked at one point and the (actual or expected) reward marked at another. Each panel has many trial rows of dopamine-neuron spikes. Panel one (early training): a dense burst of spikes at the *reward*, nothing at the cue. Panel two (after learning, reward delivered): a dense burst at the *cue*, nothing at the reward. Panel three (after learning, reward omitted): a burst at the cue, then a *gap* — silence below baseline — at the moment the reward should have been. Caption: *the dip at the bottom-right is the brain admitting that the future arrived differently than predicted*.

**Option B — The actor-critic anatomy.** A schematic of the basal ganglia with three colored regions: the striatal striosomes (the *critic* supplying V(s_t)), the striatal matrix and output nuclei (the *actor* selecting actions), and the substantia nigra dopamine neurons (broadcasting the TD error δ_t). Cortical inputs come in from the top. Arrows trace the loop: cortex → striatum → SNr/GPi → thalamus → cortex; striosomes → dopamine → striatum (the teaching feedback). Caption: *the algorithm is the anatomy*.

**Option C — The TD update rule on the page.** A clean typesetting of the equation V(s_t) ← V(s_t) + α[r_{t+1} + γV(s_{t+1}) − V(s_t)] with arrows from each term to a small drawing of what it represents in the brain. The reward term r_{t+1} maps to a drop of juice. The next-state value γV(s_{t+1}) maps to the cue light. The current-state value V(s_t) maps to the pre-cue waiting period. The bracketed difference δ_t maps to a small dopamine-neuron spike-or-dip indicator.

## Style

- Natural-history register, but for this chapter the register can lean a bit more technical to match the deep-dive's mathematical content.
- Honor the lineage of Schultz's original raster plots from his 1990s papers.
- Restrained palette. Black-and-white-and-one-color (red for the dopamine-spike marks, blue for the dip).
- Avoid: glowing-brain icons, "AI" tropes, neural-net diagrams as decoration.

## Caption (Option A)

*Three rasters from the same dopamine neuron. Before learning: spikes at reward. After learning, reward delivered: spikes at cue. After learning, reward omitted: a dip at the moment the reward should have come. The dip is the brain registering that the future arrived differently than predicted.*

## Caption (Option B)

*The basal-ganglia actor-critic. Striosomes in the striatum supply the predicted value V(s); dopamine neurons in the substantia nigra compute the prediction error δ_t and broadcast it back to the striatum, where it gates plasticity at corticostriatal synapses. The algorithm Sutton wrote down in 1988 was already running in this anatomy half a billion years before he wrote it.*

## Caption (Option C)

*The TD update rule, with each term mapped to its experimental analog. The bracketed difference is the prediction error δ_t — what dopamine neurons phasically encode.*

## Note

Do not generate the image automatically. Brief is for human image direction. My recommendation: **Option A**, because the three-panel raster is the chapter's central evidence — the dip is the moment that broke the pleasure-signal account of dopamine, and the visual lands the argument cleanly without requiring the reader to track the math.
