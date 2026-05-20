# Research notes — Chapter 1: The Definition Problem

**Book:** intelligence (*Intelligence? A Natural History of Mind Across the Animal Kingdom*)
**Chapter slug:** what-is-intelligence
**Date:** 2026-04-25
**Command:** `/chapter` (second rewrite — Bear supplied an expanded brief covering Sternberg, the 1994/1995 contrast, Shalizi, de Waal, Chollet)
**Voice anchoring:** `voice-unanchored`. Both `style/` folders empty. Natural-history register from `book.md` carried into this revision.

---

## Concept (as the literature states it)

There is no single statement. The literature holds several layered facts about itself:

1. The Sternberg & Detterman 1986 symposium produced 24 different definitions from 24 prominent theorists.
2. Legg and Hutter (2007) extended the count to 70+ across psychology, philosophy, and AI.
3. The 1994 *Mainstream Science on Intelligence* statement (52 signatories, *WSJ*) and the 1995/1996 APA Task Force *Knowns and Unknowns* (Neisser et al.) — both careful, both honest, both signed by serious researchers — pulled in opposite directions on what is and is not known. The same year produced both.
4. Across the field there is broad descriptive agreement on what intelligence *does* (predicts academic and life outcomes; varies among individuals; has a substantial heritable component in humans) and persistent disagreement on what intelligence *is* (one factor or many; biologically grounded or statistically constructed; substrate-dependent or substrate-neutral).

## Specification move

The chapter does six things in order:

1. **Hook (§1.1):** the 1986 / 1994 / 1995 contrast. Two careful, honest moves in opposite directions in the same year sharpen the puzzle better than the 1986 quote alone.
2. **Survey of seven candidates (§1.2):** Binet (judgment + the lost "mental orthopedics"); Wechsler (aggregate adaptive capacity + deviation IQ); Gardner (multiple intelligences + the eight criteria); Sternberg (triarchic + niche shaping); Legg-Hutter (formal goal-achievement, equation on the page); Wissner-Gross & Freer (causal entropic forces, equation on the page); Chollet (skill-acquisition efficiency, ARC).
3. **Two critiques that cut across (§1.3):** Shalizi on *g* as statistical artifact (algebraic-necessity argument; car-quality analogy used as my own restatement, not a direct quote); de Waal on *Umwelt* and the circularity of human-centered tests (Umwelt term properly attributed to von Uexküll 1909).
4. **Non-neutrality demonstration (§1.4):** walk same organisms through each sieve; show verdicts diverge.
5. **Working instrument (§1.5):** commit to Legg-Hutter with three reasons (operational, substrate-neutral, graded); name the cost (flattens affective and social texture, requires a reward signal that is at best a useful fiction for biological organisms); signal where alternative tools will be borrowed in later chapters.
6. **What stays open (§1.6):** both verdicts informative under different definitions; question mark is the thesis; hand to chapter 2.

## Empirical vs. non-empirical sub-claims

| Sub-claim | Status |
|---|---|
| 24 theorists at the 1986 Sternberg-Detterman symposium gave 24 different definitions | **Empirical**, settled (Neisser et al. 1996 quotation) |
| 52 researchers signed the 1994 *Mainstream Science on Intelligence* statement in WSJ | **Empirical**, settled (Gottfredson 1994; reprinted 1997 in *Intelligence*) |
| Legg & Hutter surveyed 70+ definitions in 2007 | **Empirical**, settled |
| Binet's 1905 list of terms (judgment, good sense, practical sense, initiative, adaptation, auto-critique) | **Empirical** — primary source is Binet 1905 |
| Binet advocated "mental orthopedics" and warned against single-number reduction | **Empirical** — well-attested in Binet's own writings |
| Wechsler's 1944 definition (aggregate or global capacity to act purposefully, think rationally, deal effectively) | **Empirical**, primary source Wechsler 1944 |
| Wechsler scales introduced deviation IQ on N(100,15) | **Empirical**, settled |
| Gardner's 8 criteria for distinct intelligences | **Empirical**, primary source *Frames of Mind* |
| Sternberg's three-component triarchic theory | **Empirical**, primary source *Beyond IQ* (1985) |
| Legg-Hutter formalization captures intelligence in any reasonable sense | **Definitional** — stipulation, evaluated by usefulness |
| Legg-Hutter measure is provably incomputable | **Empirical/mathematical**, settled (the paper proves it) |
| Wissner-Gross simulations exhibited tool-use and social-cooperation analogs | **Empirical**, settled |
| Whether causal entropic forces capture biological intelligence | **Non-empirical / contested** |
| Shalizi's algebraic argument: any positively correlated variables produce a first PC loading positively on all | **Empirical/mathematical**, settled |
| Whether *g* is a "statistical myth" or a real underlying construct | **Non-empirical / contested** — the data does not currently force a unique reading |
| ARC is hard for current LLMs and easy for humans | **Empirical**, settled (Chollet 2019 and follow-ups) |
| Chaser learned 1,022 proper-noun referents | **Empirical**, settled (Pilley & Reid 2011) |
| *C. elegans* does habituation, associative learning, imprinting | **Empirical**, settled (Ardiel & Rankin 2010 review) |
| *Umwelt* is the right frame for cross-species cognitive comparison | **Methodological** — widely accepted in ethology, contested in some quarters of cognitive science |

## Primary sources

1. **Sternberg, R.J. & Detterman, D.K. (eds.) (1986).** *What Is Intelligence? Contemporary Viewpoints on Its Nature and Definition.* Ablex.
2. **Neisser, U. et al. (1996).** "Intelligence: Knowns and Unknowns." *American Psychologist* 51(2): 77–101. https://psycnet.apa.org/record/1996-02655-001
3. **Gottfredson, L.S. et al. (1994).** "Mainstream Science on Intelligence." *Wall Street Journal*, December 13, 1994. Reprinted 1997 in *Intelligence* 24(1): 13–23. https://www1.udel.edu/educ/gottfredson/reprints/1994WSJmainstream.pdf
4. **Binet, A. (1905/1916).** "New methods for the diagnosis of the intellectual level of subnormals." In *The Development of Intelligence in Children: The Binet-Simon Scale.*
5. **Wechsler, D. (1944).** *The Measurement of Adult Intelligence.* Williams & Wilkins.
6. **Gardner, H. (1983/1993).** *Frames of Mind: The Theory of Multiple Intelligences.* Basic Books. https://archive.org/details/framesofmindtheo00gard
7. **Sternberg, R.J. (1985).** *Beyond IQ: A Triarchic Theory of Human Intelligence.* Cambridge University Press. https://psycnet.apa.org/record/1985-97046-000
8. **Legg, S. & Hutter, M. (2007).** "A Collection of Definitions of Intelligence." Tech Report IDSIA-07-07. arXiv:0706.3639. https://arxiv.org/abs/0706.3639
9. **Legg, S. & Hutter, M. (2007).** "Universal Intelligence: A Definition of Machine Intelligence." *Minds and Machines* 17(4): 391–444. arXiv:0712.3329. https://arxiv.org/abs/0712.3329
10. **Wissner-Gross, A.D. & Freer, C.E. (2013).** "Causal Entropic Forces." *Phys Rev Lett* 110: 168702. https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.110.168702
11. **Chollet, F. (2019).** "On the Measure of Intelligence." arXiv:1911.01547. https://arxiv.org/abs/1911.01547
12. **Shalizi, C.R.** "g, a Statistical Myth." Essay at https://bactra.org/weblog/523.html
13. **de Waal, F. (2016).** *Are We Smart Enough to Know How Smart Animals Are?* W.W. Norton. https://wwnorton.com/books/Are-We-Smart-Enough-to-Know-How-Smart-Animals-Are/
14. **von Uexküll, J. (1909).** *Umwelt und Innenwelt der Tiere* (background for *Umwelt* concept). Not cited directly; named for proper attribution.
15. **Ardiel, E.L. & Rankin, C.H. (2010).** "An elegant mind: Learning and memory in *Caenorhabditis elegans*." *Learning & Memory* 17(4): 191–201. https://learnmem.cshlp.org/content/17/4/191
16. **Pilley, J.W. & Reid, A.K. (2011).** "Border collie comprehends object names as verbal referents." *Behavioural Processes* 86: 184–195. https://www.sciencedirect.com/science/article/abs/pii/S0376635710002925

## Mechanism for the deep-dive

The non-neutrality demonstration in §1.4 — walking the same organisms (worm, dog, chess engine, bacterium, language model) through each definition's sieve — is the chapter's load-bearing argument. The math passages on Legg-Hutter's $\Upsilon$ measure and Wissner-Gross's $F = T \nabla S$ are the visible-mechanism moments per CLAUDE.md §6 and the SKILL's "math on the page" rule. Both equations are explained term by term so the reader sees what "formalized" actually means.

## Central analogy

*Intelligence in 2026 is like* life *in 1850.* Used once briefly in §1.1; reader is trusted to carry it forward. Where it breaks down: the life/non-life boundary admitted of a relatively clean operational answer within a century (autocatalytic self-maintenance, replication-with-variation, etc.); whether intelligence will resolve similarly is open. My private bet is that it won't.

## Voice notes

- Natural-history register, per `book.md`. Closer to Attenborough than to a textbook.
- No textbook scaffolding (Learning Objectives, Prerequisites, "Where this chapter fits").
- Workshop conventions retained: 3 suggested titles, TL;DR, "What would change my mind," "Still puzzling," tags.
- First person used at four points (§1.1 intro, §1.5 commitment, §1.6 closing, "What would change my mind") to label position-taking.
- One short scene at the chapter's open (1986 symposium / 1994 letter / 1995 task force). No additional scenes — this is a survey-and-commit chapter, not a mechanism chapter.
- No Extension Note (Ch. 1's brief description doesn't include one; the device begins in Ch. 2 per the book brief).

## Word count and ceiling note

Final word count 3,913 — within the 4,000 ceiling but tight. The brief was rich; further additions would push the chapter into a two-chapter problem. If review wants more on Sternberg's niche-shaping or on the Shalizi-defenders' counter-argument, those expansions probably have to displace something else (likely the Wissner-Gross or Wechsler treatments).

## Process note

This is the second rewrite. The first draft (also dated 2026-04-25) bundled three jobs into Ch. 1 — definition survey, *C. elegans* mechanism, phylogenetic gradient walk — that the book brief assigns to Ch. 1, Ch. 3, and Ch. 17 respectively. The first rewrite restricted Ch. 1 to its proper job at five candidate definitions. The second rewrite (this one) integrates Bear's expanded brief: adds Sternberg, the 1994 *Mainstream Science* statement, Shalizi, de Waal, and Chollet; adds the formal equations for Legg-Hutter and Wissner-Gross to honor the math-on-the-page rule.
