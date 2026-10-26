# Charge sign, current direction, hand rules, and two-way electromechanical constants

(Research notes compiled by Claude, 2026-10-25, for the report writer. Every claim carries a source; items I could not open or confirm are in the Gaps sections.)

## 1. Franklin's sign choice, the electron, and the history of conventional current versus electron flow

### Takeaway
Franklin introduced "positively or plus" and "negatively or minus" in a letter to Peter Collinson dated 28 July 1747, inside a one-fluid theory where "plus" meant an excess of electrical fire. Which side got "plus" was effectively an accident: his rubbed glass tube actually loses electrons. Current was defined as flow of the positive fluid long before the electron (J. J. Thomson, 1897) showed that the carriers in metal wires move the other way. The convention stuck.

### Cited Findings
- Franklin's wording, verbatim from the Founders Online transcription: the top of the Leyden bottle "is electrised positively or plus, the Bottom of the Bottle is electrised negatively or minus in exact Proportion." Experiment IX in the same letter: "When a Body is electrised plus it will repel an electrified Feather or small Cork Ball"; "When minus (or when in [the] common State) it will attract them." — [Franklin to Collinson, 28 July 1747, Founders Online](https://founders.archives.gov/documents/Franklin/01-03-02-0072)
- Dating and addressee: dated "Philada. July 28. 1747" and addressed to "Peter Collinson Esqr. F. R. S. London." Editorial note 1 confirms the date from Franklin's 14 August 1747 letter. Editorial note 7 says "top" and "bottom" should be read as the inside and outside surfaces of the bottle. — [Founders Online](https://founders.archives.gov/documents/Franklin/01-03-02-0072)
- Jensen's history column: Franklin introduced the terms in 1747 within his single-fluid theory, where positive meant excess fluid and negative meant deficit. "Franklin's original assignment of positive and negative was an accident." Rubbed glass actually loses electrons, so the labels came out reversed relative to electron motion. Du Fay's two-fluid theory (vitreous and resinous) "remained dominant throughout most of the 19th century." Aepinus showed that Franklin's theory required matter to repel matter. Franklin's attempts to detect which way the fluid flowed (paper windmills, the look of discharges) were flawed. And "the negative electrons ... are really flowing in the opposite direction." — [W. B. Jensen, "The Origins of Positive and Negative in Electricity," J. Chem. Educ. 2005, 82, 988 (PDF)](https://homepages.uc.edu/~jensenwb/reprints/125.%20Positive%20&%20Negative.pdf)
- IOP's teacher guidance: conventional current "is defined to be in the opposite direction to the 'real' current of electrons," and the convention "was established before it was known that electrons move through the wires of a circuit." — [IOP Spark, "Many students are confused by the idea of conventional current"](https://spark.iop.org/many-students-are-confused-idea-conventional-current)
- Trade-press account: early pioneers took current to run positive to negative. The 1897 cathode-ray work showed that "current flow was really electrons" (the article spells the name "Thompson"), but professors, textbooks, and standards kept the old direction. — [L. Frenzel, "Which Way Does Current Really Flow?", Electronic Design, 2 Feb 2011](https://www.electronicdesign.com/content/article/21802372/which-way-does-current-really-flow)
- Semiconductor symbols lock conventional current in: arrows in polarized device symbols "all point in the direction of conventional flow, not electron flow." — [Lessons in Electric Circuits (Kuphaldt), ch. 1.7 "Conventional versus electron flow," mirror](https://ecstudiosystems.com/discover/textbooks/lessons/DC/chapter1-7-conventional-versus-electron-flow/)

### Inferences
- The sign convention comes from 1747, and the carrier was identified 150 years later (1897). The "backward" relationship is therefore a fact about history, not about physics. Any choice is as good as any other, as long as it's used consistently (see section 3).
- A toolkit that treats the electron's real motion as primary and reads conventional current as its "backward shadow" reverses the historical order. It matches what the IOP and Jensen say is physically happening in metal wires.

### Gaps
- I didn't open a primary Thomson 1897 source. The 1897 date is standard, but here it rests only on the Frenzel trade article.
- I didn't find a documented "first" electron-flow textbook or a date when electron-flow teaching began. See section 2 for the WWII-era evidence.
- Jensen's piece doesn't mention Lichtenberg's +/− symbols or Watson, so I couldn't source who first used the + and − glyphs.

## 2. Teaching traditions: electron flow with left-hand rules versus conventional current with right-hand rules, and the confusion this causes

### Takeaway
US Navy training used electron flow with left-hand rules (for a conductor, for a coil, and for generators) at least from the 1940s. NAVPERS 10548 (1949) states it outright, and the NEETS modules carry a left-hand generator rule. Technical schools, the military, and "electron flow version" textbooks (Floyd) kept the practice going, while physics and EE use conventional current with right-hand rules and Fleming's left-hand motor rule. Physics education research documents trouble with right-hand rules and with negative charges in particular, but I found no controlled study of electron-flow versus conventional-current instruction.

### Cited Findings
- **Navy, 1949:** *Electrician's Mate 3* (NAVPERS 10548, US Government Printing Office, 1949), chapter 3:
  - "the direction of flow is from NEGATIVE to POSITIVE"; "all explanations are based on the present-day idea"
  - Conductor rule: "THE THUMB POINTING IN THE DIRECTION OF ELECTRON FLOW (NEGATIVE TO POSITIVE) ... THE FINGERS WILL POINT IN THE DIRECTION OF THE MAGNETIC LINES OF FLUX"
  - Coil rule: "Grasp the coil in the left hand with the FINGERS pointing in the direction of the ELECTRON [flow] ... the THUMB will then point in the direction of the NORTH pole end of the coil"
  - — [RF Cafe transcription of NAVPERS 10548, ch. 3](https://www.rfcafe.com/references/electrical/electricians-mate-3-navpers-10548/navy-training-electricians-mate-3-NAVPERS-10548-chapter-3.htm)
- **Navy, WWII era:** "Circa World War II, the military used the convention of both current flow and electron flow" running negative to positive. "If you read through the Navy courses, you will see that the Left-Hand Rule is used to determine electromagnetic induction." Sources named: *Electricity – Basic Navy Training Courses* (NAVPERS 10622) and NAVPERS 10548. — [K. Blattenberger, RF Cafe "Kirt's Cogitations #235"](https://rfcafe.com/miscellany/factoids/more-things-change-kirts-cogitations-235.htm)
- **NEETS:** Module 5, *Introduction to Generators and Motors*, ch. 1, gives a "left-hand rule for generators":
  - "Extend the thumb, forefinger, and middle finger of your left hand at right angles to one another"
  - Thumb: the direction the conductor moves. Forefinger: flux, "from north to south." Middle finger: "current flow in an external circuit."
  - — [NEETS Module 5, pp. 1-1 to 1-10, RF Cafe](https://www.rfcafe.com/references/electrical/neets-modules/NEETS-Module-05-1-1-1-10.htm)
- **NEETS criticized:** On an engineering forum, a user who read a NEETS figure as putting +1 A in the electron direction asked whether NEETS uses I = −dq/dt. An experienced poster (WBahn) answered "NEETS is wrong" and said "virtually no one that uses electron flow does it properly (as evidenced by the NEETS material)," meaning unexplained minus signs patched in. This is forum opinion, not a published critique. — [All About Circuits forum, "NEETS Manual Definitions"](https://forum.allaboutcircuits.com/threads/neets-manual-defintions.171305/)
- **Fleming's rule:** Fleming's left-hand rule for motors (late 19th century, John Ambrose Fleming). Thumb: force or motion. Forefinger: field. Middle finger: current, taken as conventional current. — [Wikipedia, Fleming's left-hand rule for motors](https://en.wikipedia.org/wiki/Fleming%27s_left-hand_rule_for_motors)
- **Trades and military today:** The trade-press author learned electron flow at a technical school and says tech textbooks and "the military" teach negative-to-positive flow. Some publishers print two versions of a textbook because instructors reject the "wrong" direction. — [Frenzel, Electronic Design 2011](https://www.electronicdesign.com/content/article/21802372/which-way-does-current-really-flow)
- **Dual editions exist:** Floyd, *Principles of Electric Circuits: Electron Flow Version* (Pearson/Prentice Hall; a 9th edition is listed) alongside the conventional-current edition. — [UNM Bookstore listing](https://bookstore.unm.edu/p-98860-principles-of-electric-circuits-electron-flow-version.aspx); [AbeBooks, 9th ed.](https://www.abebooks.co.uk/Principles-Electric-Circuits-Electron-Flow-Version/32351520126/bd)
- **Kuphaldt:** *Lessons in Electric Circuits* says electron-flow notation is seen in some introductory texts and among solid-state physicists, while "most electrical engineers" use conventional flow. The author's first instructor was a 20-year US Navy electronics technician who preferred electron flow. — [Lessons in Electric Circuits ch. 1.7, mirror](https://ecstudiosystems.com/discover/textbooks/lessons/DC/chapter1-7-conventional-versus-electron-flow/)
- **An attempt to drop hand rules altogether:** James G. Holbrook proposed an "Electron Orbit Method" as an "easy-to-follow substitute for the left- and right-hand rules," to "make a clean break with the traditional left- or right-hand rules." — [Radio-Electronics, Nov. 1968, via RF Cafe](https://www.rfcafe.com/references/radio-electronics/electrons-magnetic-fields-radio-electronics-november-1968.htm)
- **Conflicting claim to flag:** RF Cafe's own introduction to the Holbrook page says a Navy *Electricity* text gives "the generator rule ... as a left-hand rule with conventional current flow," and that "the modern version for electron current flow uses a right-hand rule (Fleming)." This contradicts the standard pairing: Fleming's generator rule is right-handed for conventional current, so an electron-flow generator rule must be left-handed (as in NEETS Module 5). Treat the RF Cafe remark as likely garbled. — [RF Cafe intro](https://www.rfcafe.com/references/radio-electronics/electrons-magnetic-fields-radio-electronics-november-1968.htm), compared with [NEETS Module 5](https://www.rfcafe.com/references/electrical/neets-modules/NEETS-Module-05-1-1-1-10.htm)
- **Physics education research on right-hand rules** (Mary Bridget Kustusch, DePaul; based on her 2011 NC State dissertation; arXiv:1507.02364):
  - Uncorrected right-hand-rule errors were most often "order" errors (computing B × A instead of A × B). More than 70% of these came on backward-reasoning problems.
  - Magnet (pole) pictures of the field produced more errors than vector pictures.
  - Out-of-plane orientations produced more errors.
  - "Negative charges were a significant source of error, with some students ignoring the sign and others double-counting it."
  - Two participants deliberately used a left-hand rule for a negative charge.
  - Turning the paper and guess-and-check reduced errors; guess-and-check cut order errors on backward problems from 15% to 8%.
  - — [Kustusch, "Assessing the impact of representational and contextual problem features on student use of right-hand rules," arXiv:1507.02364](https://arxiv.org/abs/1507.02364)
- **IOP on confusion:** Conventional current "can lead to confusion in some learners." IOP recommends the EPSE Electric Current diagnostic items (Q25, Q26), the 16-19 Episode 106 on electrical power, and teaching the history of the convention. — [IOP Spark](https://spark.iop.org/many-students-are-confused-idea-conventional-current)

### Inferences
- The two traditions differ in just one place, the sign of the current arrow, and the hand rules absorb that difference. Electron flow plus a left hand gives the same physical prediction as conventional current plus a right hand: a mirror (parity) flip cancels a charge-sign flip.
  - NEETS Module 5's middle finger says "current flow," yet the rule is left-handed for a generator. That only works if "current" there means electron flow. This is my reading; I didn't verify NEETS Module 1's explicit definition (see Gaps).
- The PER evidence suggests the hard part is the sign bookkeeping itself (ignoring or double-counting the negative charge), not which hand is used. A toolkit that attaches one explicit "backward arrow" to every charge targets that error directly. Kustusch's double-counting finding is a warning: a hidden backward arrow must be applied exactly once.
- Neither tradition removes the other's semiconductor symbols, so electron-flow learners meet conventional-current arrows whenever they read a diode or transistor symbol.

### Gaps
- I couldn't open NEETS Module 1 (*Introduction to Matter, Energy, and Direct Current*) to quote its definition of current as electron flow, or its left-hand rule for coils. Its electron-flow stance rests on the forum thread, the Module 5 rule, and the Navy lineage above, not on a direct quote.
- I found no controlled PER study comparing electron-flow and conventional-current instruction, and no study of left-hand-rule learners. The forum polls (Physics Forums "which way were you taught") are anecdotal and weren't fetched.
- I couldn't confirm which current US military schools (Navy "A" schools, Army or Air Force electronics courses) or apprenticeship curricula still mandate electron flow in 2026. The 1950s Air University "Electronics Fundamentals" text shows up in an RF Cafe search result, but I didn't open it.
- Kustusch's journal venue (a Physical Review PER publication, I believe) is unconfirmed; the arXiv record is the citation used here.

## 3. Charge-conjugation symmetry in classical electromagnetism: what flips and what doesn't

### Takeaway
If every charge-borne quantity changes sign (q, ρ, J, φ, A, and so E and B), Maxwell's equations and the Lorentz force law come back unchanged. Mass, time, derivatives, and the circuit constants R, C, and L, which are ratios of two sign-flipping quantities, don't change. Published sources cover the field equations; the R, C, and L point is a direct consequence of their definitions, and I didn't find a textbook passage stating it.

### Cited Findings
- Torromé defines C by C(J) = −J and C(ρ) = −ρ. E, B, φ, and A all flip sign; q flips; mass m, ∇, ∂t, and proper time are unchanged. The Maxwell equations "are invariant under each of P, T, and C independently," and the Lorentz force equation (3-vector and 4-vector forms) is invariant under C. The paper cites Jackson, *Classical Electrodynamics*, 3rd ed. (1998), for the Lorentz equation and for P classification, not for C specifically. — [R. Gallego Torromé, "C, P, T operations and classical point charged particle dynamics," arXiv:1403.5141](https://arxiv.org/abs/1403.5141)
- Kotel'nikov: the e → −e transformation maps (E, H, ρ, J, φ, A) → (−E, −H, −ρ, −J, −φ, −A) and leaves the Maxwell equations "transformed to themselves." He presents it as a discrete symmetry of classical electrodynamics. — [G. A. Kotel'nikov, "'Minus c' symmetry in classical and quantum theories," arXiv:quant-ph/9707003](https://ar5iv.labs.arxiv.org/html/quant-ph/9707003)
- Wikipedia: the laws of electromagnetism, both classical and quantum, "are invariant under the exchange of electrical charges with their negatives." The article carries a "needs additional citations" banner and gives no classical sign table. — [Wikipedia, C-symmetry](https://en.wikipedia.org/wiki/C-symmetry)

### Inferences
- The quantities in a beginner toolkit split into two classes:
  - Flip sign: q, ρ, I, J, E, B, V (a potential difference), φ, A, flux Φ, and flux linkage λ.
  - Unchanged: R = V/I, C = Q/V, and L = λ/I (each a ratio of two flipped quantities); force; energy; power (VI, a product of two flipped quantities); torque; and the motor constant K = τ/I = V/ω.
  - This follows from the definitions above together with the cited sign table. It's my derivation and isn't quoted from a source.
- So a quantity like "capture" (flux linkage per radian, physically the same as K_t = K_e) flips sign under C. Its products with current (torque) and with turn rate (back-EMF times current gives power) behave consistently. Reversing every charge in a motor leaves its mechanical behavior unchanged.
- This is the formal justification that conventional current is a legitimate "shadow": a world with positive carriers moving the other way obeys identical laws. The convention can't be detected by any mechanical measurement; only the Hall effect and similar experiments, which reveal the carrier sign, can tell them apart.

### Gaps
- I couldn't open the Feynman Lectures (caltech.edu isn't on the fetch allowlist) or a Jackson page to quote a textbook statement of C invariance in classical electrodynamics. Jackson 3rd ed., Section 6.10 (on transformation properties of electromagnetic quantities under rotations, P, and T) is the usual reference; I believe its Table 6.1 covers P and T, and I'm unsure whether it covers C. Unverified.
- I found no source explicitly listing R, C, and L as C-invariant; this rests on the inference above.

## 4. One constant read both ways: K_t = K_e, loudspeaker Bl, hydraulic displacement, and hoist braking vocabulary

### Takeaway
In SI units a permanent-magnet DC motor's torque constant (N·m/A) and its back-EMF constant (V·s/rad) are the same number, a direct consequence of power balance (e·i = τ·ω). The loudspeaker force factor Bl is the linear version of the same thing: force per amp equals volts per m/s, with units T·m = N/A = V·s/m. Hydraulic displacement plays the same role on the fluid side: torque per pressure equals volume per radian. Hoist and crane practice has the vocabulary for running this coupling backward: an overhauling load drives the motor as a generator, and the energy is returned to the line (regenerative braking), dumped in resistors (dynamic braking), or turned to heat in an eddy-current brake or retarder.

### Cited Findings
- **Hogan's derivation (MIT notes):**
  - "Pelectrical = e i = (v B l) i = v (B l i) = v f = Pmechanical"
  - A measured motor gives "Kt = 0.0355 N-m/amp" and "Ke = 0.0355 volt-sec/rad."
  - "As required by the physics of electromagnetic power transduction, the constants are in fact identical."
  - — [N. Hogan, "DC permanent-magnet motor basics," MIT OCW 2.141 (Fall 2006), PDF](https://ocw.mit.edu/courses/2-141-modeling-and-simulation-of-dynamic-systems-fall-2006/c91a0747722f114e7d2725fae73fafa3_dcpmm_basics.pdf)
- **maxon, a manufacturer:**
  - Torque constant kM "relates the produced torque to the motor current" (mN·m/A; N·m/A in SI).
  - Speed constant kn "relates the motor speed to the back EMF voltage" (rpm/V; rad/s/V in SI).
  - Generator constant kG = 1/kn.
  - "kn is basically the inverse of kM."
  - — [maxon support, "Motor constants"](https://support.maxongroup.com/hc/en-us/articles/360005873794-Motor-constants)
- **Solo Motor Controllers** (motor-controller vendor blog) states the equality and its practical caveats:
  - "In SI units they are numerically equal, because they are two views of the same electromechanical coupling."
  - Datasheet differences come from peak versus RMS current (a factor of √2), line-to-line versus phase voltage, and a 3/2 factor from the Clarke and Park transforms in some three-phase conventions.
  - — [Solo Motor Controllers, "Back-EMF Constant (Ke) vs Torque Constant (Kt)"](https://www.solomotorcontrollers.com/blog/back-emf-constant-vs-torque-constant/)
- **Loudspeaker Bl:**
  - The BL product, "aka Force Factor," is flux density B times voice-coil length L, "Measured in Tesla-meters (T•m)." Datasheets also quote it as N/A (e.g. "6.6 N/A") or Wb/m.
  - "This back EMF is proportional to the Force Factor (BL) times the velocity of the cone."
  - The page is a secondary explainer and doesn't spell out the equivalence of units.
  - — [My New Microphone, "Full List: Thiele-Small Speaker Parameters"](https://mynewmicrophone.com/full-list-thiele-small-speaker-parameters-w-descriptions/)
- **Klippel** treats "the nonlinear force factor characteristic Bl(x) which is a function of voice coil displacement x," set by pole-tip and coil geometry. "Instantaneous variation of the force factor Bl(x) modulates all signal components," which produces intermodulation distortion. Bl(x) is measured under IEC 62458, and Klippel's LSI module identifies it adaptively with a noise stimulus. — [Klippel, "Transducer Nonlinearities (Curve Shape)"](https://www.klippel.de/know-how/measurements/transducer-parameters/transducer-nonlinearities-curve-shape.html)
- **Hydraulic displacement:**
  - Theoretical motor torque "Tmt = ∆pDm / 2π" (pressure drop times displacement per revolution, divided by a full turn).
  - Theoretical speed Nmt = 1000·Q/Dm (rpm from L/min and cm³/rev).
  - "pumps and motors can often be used interchangeably."
  - — [T. Burks, Univ. of Florida ABE 4171, "Hydraulic Systems 2" lecture PDF](https://abe.ufl.edu/faculty/tburks/Presentations/ABE4171/Hydraulic%20Systems_2.pdf)
  - US customary form: T = PSI × D / (24 × 3.1416) in ft·lb, with D in in³/rev. — [Engineers Edge](https://engineersedge.com/fluid_flow/displacement_torque_hydraulic_motor.htm)
- **Hoist trade literature, Hoist magazine:**
  - Overhauling: "overhauling is the load pulling the motor rotor shaft faster than the motor rotating magnetic field." "An over-hauling hoist load turns the motor into a generator."
  - Regenerative braking: "Regenerative braking meets the OSHA controlled braking requirement"; "The energy generated returns power to the supply line or other type of electrical absorption load."
  - Dynamic braking: power "dumped across dynamic braking resistors."
  - Eddy-current brakes: "Eddy current brakes only retard load lowering speeds, they will not stop a lowering load"; "Retarding torque is only produced with motion and DC excitation."
  - Quadrant language: powered lowering "in the third quadrant," and hoisting as "a first quadrant power torque mode."
  - — [N. Flacco, "Braking: holding and controlling," Hoist magazine, 1 Feb 2002](https://www.hoistmagazine.com/analysis/braking-holding-and-controlling/)
- **Plant Services:**
  - "Dynamic braking exploits the ability of the direct-current drive motor to act as a generator."
  - A motor "operates as a motor when it produces torque in the same direction as shaft rotation."
  - An overhauling load arises "when a load overhauls motor torque, thus reversing shaft rotation."
  - Regeneration "actively pushes power into the ac power system instead of dissipating it as heat."
  - Braking resistors are sized for "lowering the maximum overhauling load through the full length of its travel."
  - — [T. Barkand and W. Helfrich, "Dynamic braking for hoists," Plant Services, 19 Jan 2006](https://www.plantservices.com/articles/2006/023)
- **Konecranes:**
  - An overhauled hoist is one where "the hoist becomes overhauled by the load trying to pull it faster than its rated speed."
  - Regenerative braking is "an inherent function of the squirrel-cage induction motor," acting "as a load brake to keep the load from free-falling."
  - "Some country regulations require each independent hoisting unit of a crane be equipped with two braking systems."
  - — [Konecranes, "The breakdown: holding brakes vs. mechanical load brakes vs. dynamic load brakes"](https://www.konecranes.com/discover/the-breakdown-holding-brakes-vs-mechanical-load-brakes-vs-dynamic-load-brakes)

### Inferences
- K_t (N·m/A), K_e (V·s/rad), Bl (N/A = V·s/m), and hydraulic displacement per radian (m³/rad = N·m/Pa) all have one form: effort per flow on one side equals flow per effort on the other. Energy conservation makes the single number read both ways.
  - A named quantity like "capture" (flux linkage per radian, in Wb/rad = V·s/rad = N·m/A) is exactly K_t = K_e for a rotary machine, and Bl is its linear sibling (Wb/m).
  - Hogan's power-balance line is the cleanest published derivation to cite.
- Displacement divided by a full turn is the hydraulic "per radian" figure: T = Δp·D/2π. That makes it a natural place for a turn-based (τ) presentation: torque equals pressure times displacement per turn, divided by τ.
- The hoist vocabulary maps onto the four quadrants of the torque–speed plane:
  - Motoring (hoisting): torque along the motion.
  - Overhauling or generating (lowering a heavy load): the load drives the machine, and torque opposes the motion.
  - The braking modes differ only in where the generated energy goes: back to the line (regenerative), into resistors (dynamic), or into an eddy-current drum as heat, with no stopping ability at zero speed.
  - This gives crane-operator language for the "read it backwards" side of the constant.

### Gaps
- maxon's exact numeric relation (kM · kn = 30 000/π in maxon units) appears only as an image on the support page and wasn't verified as text.
- I couldn't fetch a primary Thiele (1961/1971) or Small (1972, JAES) paper, an AES or IEC definition of Bl, or a manufacturer Klippel datasheet (the Dayton Audio PDF was behind bot protection). So "Bl = F/i = e/v" rests on secondary explainers and the Hogan derivation (which uses B·l explicitly).
- I didn't fetch ASME B30.16 (overhead hoists) or the OSHA 1910.179 text on "controlled braking," and no CMAA specification was reviewed. The OSHA tie-in is quoted from Hoist magazine only.
- I didn't fetch a truck eddy-current retarder source (Telma). The Telma pages surfaced in search ([Commercial Motor archive, 1993 "How it works"](https://archive.commercialmotor.com/article/14th-october-1993/41/how-it-works)), but I didn't open them.
