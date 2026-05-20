"""
Pass 1 — render 35 TABLE comments to populated markdown tables.
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent
CHAPTERS = ROOT / "chapters"

TABLES = {
    # ------------------------------------------------------------------
    # Ch 1 — The Definition Problem
    # ------------------------------------------------------------------
    "Chaser's exclusion-inference task is scored under each major definition": """| Definition | Key criterion | Verdict on Chaser | Reason |
|---|---|---|---|
| Binet (1905) | Judgment, initiative, *auto-critique* | Uncertain | She adapts and shows initiative, but auto-critique — examining her own reasoning — is hard to attribute to a dog fetching by elimination. |
| Wechsler (1944) | Aggregate purposeful action and effective adaptation | Included | She acts purposefully, deals effectively with novel arrangements, and shows referential mapping under varying conditions. |
| Gardner (1983) | Multiple distinct intelligences; linguistic faculty | Included (linguistic) | She has referential mapping over 1,022 names and a syntax-like structure over nouns, satisfying linguistic intelligence's behavioral criteria. |
| Legg–Hutter (2007) | Goal achievement across environments | Included, without qualification | She achieves the retrieval goal across varying object sets and arrangements; the open question is *how* intelligent and *in what shape*, not whether. |""",

    "the same five organisms — nematode, chess engine, bacterium": """| Organism | Binet | Wechsler | Gardner | Legg–Hutter | Chollet |
|---|---|---|---|---|---|
| Nematode | Excluded (no judgment) | Uncertain (modest adaptive capacity) | Excluded (no nameable intelligences) | Included (modest, narrow goals) | Excluded (essentially no skill-acquisition) |
| Chess engine | Excluded (no auto-critique) | Excluded (no broader purpose) | Excluded (single domain) | Included (high in one environment) | Excluded (cannot learn checkers from scratch) |
| Bacterium | Excluded (reflexive) | Excluded (no aggregate) | Excluded | Included (gradient-following is goal-pursuit) | Excluded |
| Border collie | Uncertain (limited auto-critique) | Included (whole-agent) | Included (linguistic, interpersonal) | Included (broad behavioral repertoire) | Uncertain (modest novel-task efficiency) |
| Large language model | Excluded (template-matched judgment) | Uncertain (purposeful action absent) | Uncertain (linguistic strong, embodied weak) | Included in text environments; absent in physical | Low (high-data, low transfer-from-priors) |""",

    # ------------------------------------------------------------------
    # Ch 2 — Before Brains
    # ------------------------------------------------------------------
    "Four-ingredient decision framework — columns: ingredient": """| Ingredient | What it provides | What is missing without it | Biological example in this chapter |
|---|---|---|---|
| Sensing | Detection of relevant environmental signal | The agent cannot tell what state it is in | *E. coli* membrane chemoreceptors; Venus flytrap trigger hairs |
| Memory | A trace of recent state for comparison | The agent cannot detect change over time | CheR/CheB methylation trace; cytoplasmic flow patterns in *Physarum* |
| Integration | Combination of present and remembered state | The agent cannot decide; it can only react | *Physarum* network self-pruning; flytrap calcium summation |
| Variable response | Output that differs as a function of integration | The agent's behavior is fixed and signal-independent | Run-vs-tumble switching; trap closure thresholding |""",

    "Memory substrate comparison across three organisms": """| Organism | Memory substrate | Timescale | What is encoded | Internal or external |
|---|---|---|---|---|
| *E. coli* | Methylation of chemoreceptors (CheR/CheB) | ~1 second | Recent attractant concentration | Internal (cytoplasmic) |
| *Physarum* | Cytoplasmic flow channels + extracellular slime | Minutes to hours | Where the organism has already explored | Both (channels internal, slime external) |
| Venus flytrap | Cytoplasmic calcium concentration | ~20 seconds | Recent count of trigger-hair stimulations | Internal |""",

    "Contested vs. established claims in pre-neural cognition": """| Claim | Organism | Study | Status | What the evidence actually shows |
|---|---|---|---|---|
| Maze-shortest-path solving | *Physarum polycephalum* | Nakagaki 2000 (*Nature*) | Established | Reproducible across labs; mechanism (network pruning by flow optimization) understood. |
| Habituation to mechanical stimulation | *Physarum* | Boisseau et al. 2016 | Established | Habituation to bromide solution shows both stimulus-specific and dishabituation behavior. |
| Habituation in *Mimosa pudica* | *Mimosa pudica* | Gagliano 2014 | Established | Repeated drops produce reduced leaf-folding, persistent across days. |
| Pavlovian-style associative learning in pea | *Pisum sativum* | Gagliano 2016 | Contested | Original result has not cleanly replicated; methodological objections about light-cue confounds remain unresolved. |
| Calcium-counting of trigger-hair touches | Venus flytrap (*Dionaea*) | Hedrich lab 2016 onward | Established | Two-touch threshold mechanism mapped to specific calcium signaling and gene expression. |""",

    "Artificial sensors mapped to the four-ingredient framework": """| Device | Sensing | Memory | Integration | Variable response |
|---|---|---|---|---|
| Litmus paper | Yes | No | No | No (single readout) |
| pH electrode | Yes | No | No | No |
| Smoke detector | Yes | No | Yes (threshold) | Yes (alarm above threshold) |
| Blood-glucose monitor | Yes | Yes (logged history) | Partial (trend display) | No (reports, does not act) |
| Environmental trend monitor | Yes | Yes | Yes | No (no agent that acts on the integration) |""",

    # ------------------------------------------------------------------
    # Ch 3 — Steering
    # ------------------------------------------------------------------
    "labeled-line summary for C. elegans": """| Neuron | Stimulus detected | Default valence | Modifiable by internal state? |
|---|---|---|---|
| AWA, AWC | Volatile attractant odors (food cues) | Approach | Yes — neuromodulators (dopamine, serotonin) reset its effective weight in AIY. |
| ASH | Mechanical and high-osmolarity insults; copper | Avoid (sharp pirouette) | Yes — sustained starvation gates ASH down so the worm crosses copper barriers. |
| ASE (left/right) | Salts (Na⁺, Cl⁻) | Approach (asymmetrically tuned by L/R pair) | Less so; ASE encoding is largely structural. |
| AFD | Temperature gradient relative to cultivation T | Approach toward T<sub>cult</sub> | Modifiable on long timescales by experience. |""",

    "the food-copper trade-off under two neuromodulator states": """| Worm state | Serotonin level | w<sub>food</sub> | w<sub>copper</sub> | Decision (equal S<sub>food</sub>, S<sub>copper</sub>) | Predicted behavior |
|---|---|---|---|---|---|
| Fed | High | Low (~0.3) | High (~1.0) | Negative | Stays on safe side; does not cross copper |
| Starved | Low | High (~1.0) | Low (~0.3) | Positive | Crosses copper barrier toward food |""",

    "C. elegans vs. Roomba mapped against the six-component architecture": """| Component | C. elegans | Roomba |
|---|---|---|
| 1. Sensors | Present — chemo-, mechano-, thermo-, osmoreceptors | Present — bumper, cliff, dust, IR |
| 2. Labeled lines | Present — each sensory neuron carries its valence structurally | Present — each sensor has a fixed handler in firmware |
| 3. Integration | Present — AIY weights inputs against internal state | Present — controller arbitrates by priority rules |
| 4. Motor output | Present — locomotion modulated by tumble/run policy | Present — drive wheels and brush motor |
| 5. Neuromodulation (gain-resetting) | Present — dopamine/serotonin reset weights with state (fed/starved) | **Absent** — gain weights are fixed by code; no state-dependent re-weighting |
| 6. Internal state coupling to weights | Present — hunger, fatigue, prior experience | **Absent** — battery is sensed but does not change behavior weights, only triggers a return-to-dock policy |""",

    # ------------------------------------------------------------------
    # Ch 4 — Learning and Memory
    # ------------------------------------------------------------------
    "side-by-side comparison of biological vs. artificial neural network memory": """| Property | Biological neural network | Artificial neural network (standard backprop) |
|---|---|---|
| Update scope | Local — synapse changes when its pre- and post-synaptic neurons are co-active | Global — every weight in every layer is updated on every batch |
| Protection mechanism | CREB-1 / CREB-2 gate; only surprise-tagged events become permanent | None — recent gradients overwrite older representations |
| Forgetting behavior | Sparse and gated; old skills persist through new learning | Catastrophic — prior tasks degrade rapidly when new ones are learned |
| Engineering fix | — | Elastic weight consolidation (EWC); experience replay buffers |
| Biological analog of the fix | — | EWC ↔ synaptic consolidation; replay ↔ hippocampal sharp-wave ripples during sleep |""",

    # ------------------------------------------------------------------
    # Ch 5 — Emotion
    # ------------------------------------------------------------------
    "Three definitions of emotion side by side": """| Definition | What it describes | How it is measured | What it can and cannot settle |
|---|---|---|---|
| Definition Y — feeling / phenomenology | The felt, subjective experience of an emotion | Verbal report only (in humans); inaccessible elsewhere | Cannot be settled by any third-person measurement; not the working definition of this chapter |
| Emotion as behavior | A pattern of observable response (e.g. flight, freeze, approach) | Direct observation of behavior | Settles only what the organism *does*; cannot distinguish reflex from state |
| Definition X — functional state (Anderson–Adolphs) | An internal state with valence, persistence, scalability, generalization, and coordination | Cognitive-bias paradigm, persistence assays, dose–response, cross-modality probes | Settles whether the organism has the *functional architecture* of emotion; remains silent on phenomenology |""",

    "Mood vs. appetitive motivation — two competing explanations for the Perry result": """| Test | Mood interpretation predicts | Appetitive-motivation interpretation predicts |
|---|---|---|
| Does the bias generalize to non-food ambiguous stimuli? | Yes — mood is a global state | No — appetitive motivation is reward-specific |
| Does dopamine antagonist affect all approach-related behaviors? | Yes — across-the-board attenuation | Only food-related approach is attenuated |
| Does the bias persist after the surprise reward is consumed? | Yes — mood persistence | No — return to baseline as motivation discharges |
| Open empirical question | Run a non-food generalization probe (e.g. shelter approach) under the same dopamine manipulation | The same experiment distinguishes the accounts |""",

    "Anderson-Adolphs criteria applied across four organisms": """| Criterion | Shaken honeybee (Bateson 2011) | Surprised bumblebee (Perry 2016) | Hermit crab (Elwood) | Headless cockroach (Horridge) |
|---|---|---|---|---|
| Persistence | ✓ — pessimistic bias outlasts the shaking | ✓ — optimism outlasts sucrose surprise | ✓ — withdrawal preference persists after shock | ? — duration not characterized |
| Scalability | ✓ — graded by shake intensity | ✓ — graded by sucrose magnitude | ✓ — graded by shock intensity | — |
| Valence | ✓ — negative | ✓ — positive | ✓ — negative | ? |
| Generalization | ? — limited cross-modal testing | ? — limited cross-modal testing | ✓ — preference shifts across new shells | — |
| Coordination | ✓ — physiological + behavioral | ✓ — dopamine-mediated multi-system | ✓ — multi-system | — |""",

    # ------------------------------------------------------------------
    # Ch 6 — Pattern Recognition
    # ------------------------------------------------------------------
    "what CNNs copied from the cortex vs. what they left out": """| Component | Standard CNN | Vertebrate cortex | Performance consequence of absence |
|---|---|---|---|
| Feature hierarchy | Yes | Yes | — (this part transferred well) |
| Sparse coding | Partial (ReLU) | Strong (lateral inhibition) | Reduced disentanglement; representations less robust under occlusion |
| Recurrent completion | Mostly absent (until transformers) | Present in CA3, neocortex | Poor partial-input completion; brittle to noise |
| Thalamic gating | Absent | Present (LGN, pulvinar) | Inability to selectively pass behaviorally relevant information; attention has to be bolted on |""",

    "the three-operation framework across brain regions": """| Region | Dimensionality expansion | Sparse coding | Recurrent completion | Primary function |
|---|---|---|---|---|
| Piriform cortex | Olfactory glomeruli → broad cortical projection | Lateral inhibition between principal cells | Recurrent collaterals among pyramidal cells | Odor discrimination + completion |
| Hippocampus (DG / CA3) | Mossy-fiber expansion in DG | Strong DG sparsity | CA3 recurrent network | Episodic-memory pattern completion |
| Cerebellum | Mossy-fiber → granule cell expansion (~10⁵×) | Granule cells fire sparsely | None (feedforward) | Motor pattern timing and prediction |
| Neocortex | L4 → L2/3 expansion | Local inhibitory interneurons | Lateral cortico-cortical loops | General-purpose pattern recognition |
| Avian pallium | Nidopallium expansion | Inhibitory networks present | Recurrent connections present | Functional analog of mammalian cortex |""",

    # ------------------------------------------------------------------
    # Ch 7 — Navigation
    # ------------------------------------------------------------------
    "three-species comparison — columns: species, primary navigation strategy": """| Species | Primary navigation strategy | Sensory modality | Hippocampal elaboration | Failure mode when key modality is removed |
|---|---|---|---|---|
| Clark's nutcracker | Allocentric memory of cache locations | Visual landmarks | Greatly enlarged hippocampus | Cannot recover caches when landmarks are altered |
| Pacific salmon | Magnetic + olfactory sequence memory | Geomagnetic + chemical | Modest, but salient olfactory memory | Returns to wrong river when olfactory imprint is disrupted |
| Desert ant *Cataglyphis* | Path integration (home vector) | Polarized sky light + step counter | Small, no map elaboration | Walks the integrated vector even when displaced — terminates in the wrong place |""",

    # ------------------------------------------------------------------
    # Ch 8 — Reinforcement and Prediction
    # ------------------------------------------------------------------
    "Model-free vs. model-based reinforcement learning — columns: property": """| Property | Model-free | Model-based |
|---|---|---|
| What is stored | Cached action values per state | A model of world dynamics + reward function |
| Devaluation handling | Requires post-change experience to update | Immediate re-evaluation by simulation |
| Behavioral signature | Habit — overtrained rats keep pressing the lever | Goal-directed — immediate suppression after devaluation |
| Neural substrate | Dorsolateral striatum | Dorsomedial striatum + prefrontal cortex |
| Phylogenetic appearance | Lamprey onward | Lamprey onward (basic); cortical amplification mammalian |""",

    # ------------------------------------------------------------------
    # Ch 9 — Simulation and Planning
    # ------------------------------------------------------------------
    "model-free vs. model-based reinforcement learning — rows: what is stored": """| | Model-free | Model-based |
|---|---|---|
| What is stored | Cached action values | World-model + reward function |
| How decisions are made | Lookup of cached value | Forward simulation through the model |
| Speed at decision time | Fast | Slow |
| Cost of environmental change | High — old cache is wrong | Low — re-simulate |
| Failure mode | Habit, devaluation-insensitive | Compute cost; model errors propagate |
| Neural substrate | Dorsolateral striatum | Dorsomedial striatum + prefrontal cortex; hippocampus for spatial models |""",

    "the regret vs. disappointment experimental design": """| | Type 1 (disappointment) | Type 2 (regret-eligible) |
|---|---|---|
| Offer skipped | Bad (the rat correctly skipped a low-value option) | Good (the rat skipped a high-value option) |
| Offer encountered next | Bad (also low-value) | Bad (and now committed to it) |
| Prediction error present | Yes | Yes |
| Look-back behavior | Absent | Present — rat orients backward toward the skipped offer |
| OFC neurons encoding the missed option | Absent | Present |
| Subsequent behavioral correction | Absent | Present — rat takes the next good offer that arises |""",

    # ------------------------------------------------------------------
    # Ch 10 — Social and Emotional Intelligence
    # ------------------------------------------------------------------
    "comparison of small-group biological reputation tracking vs. digital reputation systems": """| | Small-group biological tracking | Digital reputation system |
|---|---|---|
| Information modality | Direct observation, gossip, repeated interaction | Aggregated ratings, reviews, scores |
| Embeddedness in ongoing relationships | Strong — tracker and tracked are in continued contact | Weak — rater and rated rarely meet again |
| Skin-in-the-game for accuracy | High — false reputations cost the tracker socially | Low — false reviews cost almost nothing |
| Gamability | Low — falsehoods detected by repeated interaction | High — review fraud, sock puppets, brigades |
| Scale | ~150 (Dunbar) | Millions |
| Depth of relational texture | Rich — context, history, motive | Thin — a star count and a sentence |""",

    # ------------------------------------------------------------------
    # Ch 11 — Theory of Mind
    # ------------------------------------------------------------------
    "Kano 2019 barrier-experience design": """| Pre-exposure condition | What the ape learned | Submentalizing prediction | Perspective-projection prediction | Observed result |
|---|---|---|---|---|
| Opaque-barrier group | Barriers of this type block vision | Actor will not have seen → look at false-belief location | Actor will not have seen → look at false-belief location | Anticipatory gaze to false-belief location |
| Transparent-barrier group | Barriers of this type are see-through | Actor will not have seen (same surface cue) → look at false-belief location | Actor *did* see through → look at true location | Anticipatory gaze to true location — distinguishes the two accounts |""",

    "Horowitz guilty-look experiment": """| | Owner told *misbehaved* (scolds) | Owner told *obedient* (no scolding) |
|---|---|---|
| Dog actually misbehaved | High guilty-look rate | Low guilty-look rate |
| Dog was obedient | High guilty-look rate | Low guilty-look rate |""",

    "Ullman 2023 fragility result": """| Task version | Logical structure | Surface form matches training distribution? | GPT-4 prediction | Correct prediction |
|---|---|---|---|---|
| Canonical Sally-Anne (opaque container, actor absent) | False-belief at original location | Yes | Original location | Original location ✓ |
| Transparent-container modification (actor present, can see through) | True-belief at new location | No (logical structure changed despite similar wording) | Original location | New location ✗ |
| Explicit-knowledge modification (actor told over phone) | True-belief at new location | No | Original location | New location ✗ |""",

    # ------------------------------------------------------------------
    # Ch 12 — Creativity
    # ------------------------------------------------------------------
    "the four cases evaluated against the three creativity criteria": """| Case | Novelty | Utility | Intentionality | Product/process gap |
|---|---|---|---|---|
| New Caledonian crow compound tool | Strong — composition not seen in training | Strong — solves the problem | Weak — selection process not directly observed | Whether the bird *intended* the composition or assembled by trial and error remains unobservable |
| Fongoli chimpanzee spear | Strong — population-level innovation in tool use | Moderate — hunts succeed at low rates | Moderate — repeated, refined production over years | Whether each maker invented or learned culturally is hard to disentangle |
| Veined octopus coconut transport | Strong — coconut-shell carry is novel | Strong — defensive shelter on demand | Weak — single observed case; selection process unclear | Whether the octopus *planned* the shelter use or stumbled into it cannot be distinguished |
| Great bowerbird forced-perspective court | Strong — graded stone arrangement is non-trivial | Strong — inflates apparent body size to females | Strong — males adjust placement after viewing from female position | Process is partially observable in the male's repeated viewing-and-adjusting behavior |""",

    # ------------------------------------------------------------------
    # Ch 13 — Self-Awareness
    # ------------------------------------------------------------------
    "passer catalog — columns: species, brain structure": """| Species | Brain structure | Relative brain size | Year of first confirmed pass | Key behavioral evidence | Primary contested alternative |
|---|---|---|---|---|---|
| Chimpanzee | Six-layered neocortex | Large for body | 1970 (Gallup) | Mark-directed touching of own face | None still serious — replicated widely |
| Bottlenose dolphin | Six-layered neocortex (different organization) | Very large | 2001 | Use of mirror to inspect novel marks | Memory and visual habituation accounts |
| Asian elephant | Six-layered neocortex | Largest among terrestrial mammals | 2006 | Trunk-directed touching of marked spot | Pass rate is low (one individual of three) |
| Eurasian magpie | Pallial (no neocortex) | Large for bird | 2008 | Foot-directed scratching at marked throat | Replication contested in some labs |
| Cleaner wrasse | No cortex | Modest | 2019 | Throat-mark inspection and scraping | Active dispute — alternative accounts in olfactory and tactile cuing remain on the table |""",

    # ------------------------------------------------------------------
    # Ch 14 — Metacognition
    # ------------------------------------------------------------------
    "Three distinctions that structure the metacognition literature": """| Distinction | Lower-demand form | Higher-demand form | Distinguishing evidence |
|---|---|---|---|
| Procedural vs. declarative metacognition | Procedural — uncertainty modulates behavior | Declarative — explicit verbal report of certainty | Whether the agent can report confidence outside of an action context |
| Uncertainty monitoring vs. information seeking | Monitoring — opt out of hard trials | Seeking — actively sample more information before committing | Whether the agent voluntarily expends effort to reduce uncertainty before deciding |
| Learned stimulus avoidance vs. genuine uncertainty | Avoidance — opt-out becomes associated with hard stimuli per se | Genuine — opt-out tracks the agent's *actual* accuracy on novel stimuli | Whether opt-out generalizes to never-before-seen items where the agent will in fact fail |""",

    "Pearl's ladder applied to metacognition": """| Rung | Internal operation | Species with demonstrated capacity | Key paradigm | What the higher rung adds |
|---|---|---|---|---|
| Rung 1 — Association | Internal state correlates with task accuracy | Macaques, dolphins, some corvids, bees (debated) | Hampton 2001 memory delay; Smith 1995 dolphin opt-out | — |
| Rung 2 — Intervention | Agent acts on its own knowledge state to change it (information seeking) | Macaques, scrub jays | Watanabe-Clayton 2016 information seeking | Requires modeling that more sampling will change *one's own* state |
| Rung 3 — Counterfactual | Reasoning about alternative cognitive histories ("if I had paid attention then...") | Humans (only clear case) | Self-report under structured introspection | Requires representing alternative *internal* trajectories, not just alternative external actions |""",

    "Institutional metacognitive tools as additive extensions": """| Tool | Individual analog | What it extends beyond the individual | Failure mode |
|---|---|---|---|
| Confidence intervals | Subjective certainty | Forces explicit, calibrated uncertainty across observers | Misinterpretation as guarantees rather than ranges |
| Peer review | Self-checking | Recruits independent error-detectors with skin in the game | Reviewer bias, novelty penalty, slow turnaround |
| Replication studies | Re-checking one's own work | Distributes the verification across labs and time | Replication failure misread as the original being false |
| Prediction markets | Self-calibrated forecast | Prices aggregate decentralized confidence | Thin liquidity, manipulation, regulatory limits |""",

    # ------------------------------------------------------------------
    # Ch 15 — Language
    # ------------------------------------------------------------------
    "the double dissociation between emotional expression and language": """| Condition | Lesion location | Grammatical speech | Spontaneous emotional vocalization | What remains | What is lost |
|---|---|---|---|---|---|
| Broca's aphasia | Left inferior frontal gyrus | Impaired (effortful, agrammatic) | Intact (laughter, crying, swearing under emotion) | Emotional vocal system | Symbolic syntactic production |
| Pseudobulbar affect | Bilateral corticobulbar lesions (often brainstem) | Intact | Impaired (uncontrolled or mismatched laughter/crying) | Symbolic language | Volitional control over emotional vocalization |""",

    "comparison of language-learning trajectories": """| Measure | Human child at 18 months | Nim Chimpsky at equivalent training | Kanzi (best ape-language subject) |
|---|---|---|---|
| Vocabulary size | ~50–200 words | ~125 signs after years | ~400 lexigrams |
| Self-initiated utterances | Most are spontaneous | Mostly prompted | Substantial spontaneous use, but mostly imperative |
| Question forms produced | Yes | No | No |
| Displacement (talk about absent things) | Yes | Limited | Partial |
| Recursive structure | Emerging | No | No |
| Trajectory | Continuing growth | Plateaued | Plateaued |""",

    "five communication systems evaluated against Hockett's key design features": """| System | Displacement | Productivity / recursion | Cultural transmission | Duality of patterning | Declarative reference |
|---|---|---|---|---|---|
| Human language | Present | Present (recursive) | Present | Present | Present |
| Chimpanzee gestural communication | Absent or rare | Absent | Partial (some local conventions) | Absent | Absent (almost entirely imperative) |
| Honeybee waggle dance | Present (food at distance) | Limited (no novel meanings) | Partial (regional dialects) | Absent | Absent (functional, not declarative) |
| Vervet alarm calls | Absent (calls about present threats) | Absent | Absent | Absent | Absent |
| Large language model text output | Present | Present (productivity) | Inherits human written record | Present (tokens compose into words) | Contested — produces declarative-shaped text without joint-attention machinery |""",

    # ------------------------------------------------------------------
    # Ch 16 — Collective Intelligence
    # ------------------------------------------------------------------
    "explicit vs. tacit knowledge comparison across three domains": """| Domain | Explicit (transmissible by text) | Tacit (requires apprenticeship) | Failure mode of text-only transmission |
|---|---|---|---|
| Science | Hypotheses, methods sections, results, equations | Bench technique, reagent intuition, calibration habits, judgment about which experiments are worth running | Replication failure — papers describe what was done, not what was *needed* to make it work |
| Surgery | Anatomy, decision criteria, written protocols | Tissue handling, pacing, micro-judgments under bleeding | Trainees who pass exams cannot operate; outcomes depend on hours of supervised practice |
| Skilled craft | Patterns, materials specs, written instructions | Tool feel, error recovery, sense of when a piece is "right" | Apprenticeship cannot be skipped; written guides produce mechanically correct but qualitatively poor work |""",

    # ------------------------------------------------------------------
    # Ch 17 — AI as Data Point
    # ------------------------------------------------------------------
    "Three questions inside \"is AI intelligent?\"": """| Question | What it assumes | Evidence that would answer it | Evidence that cannot |
|---|---|---|---|
| (1) Is intelligence a height or a shape? | A single ranking exists across all systems | Multi-axis profile across cognitive capacities | Performance on one benchmark, however high |
| (2) Is the system *doing* the thing or *buying* the output? | Skill and skill-acquisition efficiency are separable | Performance on novel tasks given few examples (Chollet ARC) | Performance on tasks similar to training distribution |
| (3) Is the function running or just the language? | Surface output and underlying operation can be separated | Ullman-style perturbations that preserve logic and alter surface | Fluent text production on canonical templates |""",

    "AI placement under four definitions of intelligence from Chapter 1": """| Definition | What it measures | AI placement | What drives the placement |
|---|---|---|---|
| Legg–Hutter | Goal achievement across environments | Strong in narrow digital, text-structured environments; absent in most physical | Stakes-absent training produces high in-distribution performance, not broad transfer |
| Sternberg | Analytic + creative + practical | High analytic, mixed creative, weak practical | Practical intelligence requires environment-shaping, which a textless agent cannot do |
| Wechsler | Purposeful action and effective adaptation | Weak | Purposes in the biological sense require stakes; the system has none |
| Chollet | Skill-acquisition efficiency given priors | Much lower than the human child | High-data, low-prior; biological priors are the gap |""",

    # ------------------------------------------------------------------
    # Ch 18 — Extended Mind
    # ------------------------------------------------------------------
    "the catalog as a two-column table": """| Extension technology + capacity it extends | Directing capacity required (not supplied by the tool) |
|---|---|
| pH meter — extends *E. coli*'s gradient detection | Choosing what to measure; interpreting the reading in context |
| Microscope — extends visual pattern recognition | Choosing the field, framing the question, judging what is artifact |
| GPS — extends path integration / cognitive maps | Choosing the destination; recognizing when the route is wrong |
| Calculator — extends working memory and computation | Setting up the calculation; auditing the result for plausibility |
| Written records — extend memory across generations | Selecting what is worth recording; reading critically |
| Clinical decision support — extends diagnostic pattern matching | Specifying the case; cross-checking against the patient in front of you |
| Recommendation engine — extends preference matching | Setting goals beyond engagement; auditing for Goodhart drift |
| Apollo 13 digital twin — extends simulation and planning | Formulating the right counterfactual to simulate; deciding which simulation to act on |
| Detection dog — extends olfactory pattern recognition | Selecting the search; calibrating false-positive tolerance |
| Large language model — extends pattern recognition + language production | Goal-setting, plausibility-auditing, causal reasoning, accountability |""",
}


def apply():
    pat = re.compile(r'<!--\s*→\s*\[TABLE:(.+?)-->', re.DOTALL)
    total_replaced = 0
    for f in sorted(CHAPTERS.glob('*.md')):
        text = f.read_text()
        replaced = 0

        def replacer(m):
            nonlocal replaced
            body = m.group(1)
            for key, table in TABLES.items():
                if key in body:
                    replaced += 1
                    return table
            return m.group(0)

        new_text = pat.sub(replacer, text)
        if replaced:
            f.write_text(new_text)
            print(f"  {f.name}: {replaced} tables")
            total_replaced += replaced
    print(f"\nreplaced: {total_replaced} tables")


if __name__ == "__main__":
    apply()
