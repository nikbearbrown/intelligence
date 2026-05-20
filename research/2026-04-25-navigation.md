# Research notes — Chapter 7: Navigation and Spatial Intelligence

**Book:** intelligence (*Intelligence? A Natural History of Mind Across the Animal Kingdom*)
**Chapter slug:** navigation
**Date:** 2026-04-25
**Command:** `/chapter`
**Voice anchoring:** `voice-unanchored`. Both `style/` folders empty. Seventh drafted unit.

---

## Concept

Spatial intelligence as a layered system of route memory, path integration, and allocentric map representation, implemented across vertebrates by a hippocampal architecture of place cells, grid cells, head-direction cells, border cells, and speed cells, with species-specific sensory frontends running on top. The chapter argues that this architecture is half-a-billion-year-old vertebrate machinery, that different lineages have specialized it in extraordinary ways (Clark's nutcracker cache memory, Pacific salmon geomagnetic imprinting, the bomb-sniffing dog's olfactory navigation), and that the modern human GPS is the first navigational tool that consistently *substitutes* for the cognitive map rather than extending it.

## Specification move

Three jobs of *navigation* unbundled before empirical work:

1. **Route memory** (egocentric, fast, fragile) — stimulus-response chains.
2. **Path integration** (internal, drifting, landmark-free) — running self-motion vector.
3. **Map representation** (allocentric, flexible, anchored) — the structure that lets an animal compute novel routes.

Different species sit at different points in this triangle. The chapter argues that the hippocampal architecture is what gives vertebrates access to (3), and that the modern human pattern of relying on GPS is reducing how often we use it.

## Empirical vs. non-empirical sub-claims

| Sub-claim | Status |
|---|---|
| Place cells in rat hippocampus encode locations | **Empirical**, settled (O'Keefe & Dostrovsky 1971; many follow-ups) |
| Grid cells in medial entorhinal cortex tile space hexagonally | **Empirical**, settled (Hafting et al. 2005) |
| London taxi drivers have larger posterior hippocampi than controls; volume scales with experience | **Empirical**, settled (Maguire et al. 2000) |
| Cataglyphis ants do path integration with sky compass + step counter, no map | **Empirical**, settled (Wehner lab over decades) |
| Clark's nutcrackers retrieve thousands of cache locations months later | **Empirical**, settled (Vander Wall and others) |
| Pacific salmon imprint on the magnetic signature of natal river mouth | **Empirical**, well-supported (Putman et al. 2013); the molecular substrate of the imprint is not nailed down |
| Detection dogs alert in response to handler beliefs even without target | **Empirical**, settled (Lit, Schweitzer, Oberbauer 2011) |
| GPS suppresses hippocampal activity during use | **Empirical**, settled (Javadi et al. 2017) |
| GPS use causes long-term hippocampal atrophy | **Inference**, not yet settled — longitudinal data thin |
| The hippocampal architecture is conserved across vertebrates back to ~520 mya | **Empirical**, well-supported (multiple comparative studies; Suryanarayana 2017 cited in Ch. 6 also relevant) |

## Primary sources

1. **Hafting, T., Fyhn, M., Molden, S., Moser, M.B., Moser, E.I. (2005).** "Microstructure of a spatial map in the entorhinal cortex." *Nature* 436: 801–806. https://www.nature.com/articles/nature03721 — grid cell discovery.
2. **Maguire, E.A., Gadian, D.G., Johnsrude, I.S., Good, C.D., Ashburner, J., Frackowiak, R.S., Frith, C.D. (2000).** "Navigation-related structural change in the hippocampi of taxi drivers." *PNAS* 97(8): 4398–4403. https://www.pnas.org/doi/10.1073/pnas.070039597 — hippocampal plasticity in expert navigators.
3. **Putman, N.F. et al. (2013).** "Evidence for Geomagnetic Imprinting as a Homing Mechanism in Pacific Salmon." *Current Biology* 23(4): 312–316. https://www.sciencedirect.com/science/article/pii/S0960982213000031 — biphasic salmon navigation.
4. **Lit, L., Schweitzer, J.B., Oberbauer, A.M. (2011).** "Handler beliefs affect scent detection dog outcomes." *Animal Cognition* 14: 387–394. https://link.springer.com/article/10.1007/s10071-010-0373-2 — Clever Hans / handler-bias evidence in detection-dog work.
5. **Javadi, A.H., Emo, B., Howard, L.R., Zisch, F.E., Yu, Y., Knight, R., Pinelo Silva, J., Spiers, H.J. (2017).** "Hippocampal and prefrontal processing of network topology to simulate the future." *Nature Communications* 8: 14652. https://www.nature.com/articles/ncomms14652 — hippocampal suppression with satnav.

Other references in the chapter without primary URLs:
- O'Keefe & Dostrovsky 1971 *Brain Research* — place cell discovery (referenced by name and date).
- O'Keefe & Nadel 1978 — *The Hippocampus as a Cognitive Map* (book).
- Wehner *Cataglyphis* path integration (referenced by laboratory rather than specific paper).
- Tolman 1930s–40s cognitive-map experiments (referenced historically).

## The mechanism for the deep-dive

*The hippocampal-entorhinal map system.* §7.3 walks the architecture: place cells in CA1/CA3 identify specific locations through population-code activity patterns; grid cells in medial entorhinal cortex tile space hexagonally to provide a metric coordinate system; head-direction, border, and speed cells supply orientation, boundary, and self-motion signals. The grid is the metric that lets the hippocampus path-integrate; the place cells are the anchors that prevent the grid from drifting. Maguire's London taxi-driver result establishes plasticity. One sentence: *the brain has a coordinate system implemented in cortical tissue; each location is a specific pattern of activity across thousands of cells; movement updates the pattern; familiar places reactivate the pattern; the structure is plastic and use-it-or-lose-it.*

## Central analogy

*The bomb-sniffing dog as hybrid intelligence.* The dog brings the sensory hardware (200+ million olfactory receptors, plume-tracking software, working memory for the target odor) and the search software. The handler brings the strategic frame and the discipline to not bias the dog. The team outperforms either alone, and the most studied failure mode is the handler's beliefs leaking into the dog's behavior (Clever Hans / Lit 2011). Where the analogy breaks: the dog is itself a complete cognitive system, not just a sensor in the engineering sense; its hippocampal map is doing real navigation work, not just signal processing.

## Voice notes

- Natural-history register continued. Scene of *Rex* the Belgian Malinois at a checkpoint as the chapter's anchor.
- First person used in §7.6 ("I conclude," "I would hold this judgment lightly") — sparingly.
- Single-sentence paragraphs at three pivots: end of §7.1 ("The chapter is the architecture under that detection..."), §7.3 mid ("This was a coordinate system"), §7.6 closing ("The dog still has his map.").
- Math kept off the page — the architecture is qualitative; the place-cell/grid-cell description is mechanism-level without equations.
- Extension Note (sixth in book): GPS, sonar, radar. Names the leitmotif explicitly: "Tools extend cognitive capacities. Sometimes the extension is additive... Sometimes the extension is substitutive."

## Risks flagged

- **The GPS-as-substitute claim is rhetorically strong and the evidence is moderate.** Javadi 2017 shows hippocampal-activity suppression *during* satnav use. Whether this translates into long-term cognitive-map atrophy is *not* established. The chapter is careful in §7.6 to flag this ("I would hold this judgment lightly"). If review wants a more cautious framing, this is where to soften.
- **The Lit 2011 detection-dog cueing study is presented as if it generalizes broadly.** It was a single study with eighteen handler-dog teams. The phenomenon is real and matters for legal and operational practice, but the chapter's generalization to "the most studied failure mode" is partly editorial.
- **Cataglyphis path integration is treated compactly.** The Wehner-lab work is enormously rich; the chapter compresses it to the key claims (sky compass + step counter, ground-projection on inclines, displacement experiments showing no map). If review wants more depth, the chapter could expand at the cost of trimming elsewhere.
- **The Clark's nutcracker numbers (tens of thousands of caches across a multi-square-mile range, recovered months later) are presented from secondary literature** — the foundational work is Stephen Vander Wall's. I do not link a primary paper. If review wants tighter sourcing, Vander Wall's 1982 *Animal Behaviour* paper is the place.

## Process note

Seventh drafted unit. The natural-history register is now well-anchored across preface + Ch. 1–7. The Extension Notes are accumulating exactly the way the book brief intends: Ch. 2 (pH meters), Ch. 3 (Roomba), Ch. 4 (writing), Ch. 5 (affect-detection AI), Ch. 6 (microscopes/MRI), Ch. 7 (GPS/sonar/radar). The pattern is becoming visible enough that the leitmotif is stated almost-explicitly in §7.6: *Tools extend cognitive capacities. Sometimes the extension is additive... Sometimes the extension is substitutive.* This is one chapter short of where the brief intended the leitmotif to start being named (Ch. 18). If review wants to keep the suspense longer, §7.6 should be softened.
