<!--
    chapters-spec.md
    Blueprint Phase 3: Chapter Specifications. AI FILMMAKING (for trained filmmakers).
    The general-audience course, Agentic Filmmaking, has its own chapters-spec.md in books/agentic-filmmaking-book.
-->

# AI Filmmaking: Chapter Specifications

**Author:** Nik Bear Brown

*Phase 3 output from Blueprint. Written by /scaffold (silent mode) on 2026-11-16 from BLUEPRINT.md, outline.md and pantry/. Revised the same day with Bear's decisions, and on 2026-11-17 for *AI Filmmaking*. Outcomes live in architecture.md. Galen's sessions are written out step by step in outline.md, under each chapter's "On the set"; this file refers to them rather than repeating them. Sidecar unverified until human sign-off.*

---

## Executive summary

- **What this is:** a spec for every chapter, detailed enough that a contributor could start drafting. Each spec gives the opening, the content blocks, the worked example, three exercises and the bridge to the next chapter. After the specs come the case-study plan, contested claims, gaps, hard chapters and how fast each chapter will age.
- **What changed on 2026-11-17:**
  - **Reader:** trained filmmakers with a finished screenplay. Blocks that taught film craft are replaced by blocks that carry the filmmaker's craft to the model: the words it follows, the words it ignores, and the job settings.
  - **Part I:** old Ch 1 to 3 became one chapter, Ch 1, From Screenplay to Shot Table.
  - **Numbering:** old Ch 4 to 15 are now Ch 2 to 13.
  - **Pitching:** moved into Ch 13.
- **Hardest chapters:**
  - Ch 9 (directing dialogue);
  - Ch 12 (compositing generated and live footage);
  - Ch 13 (festival, copyright and disclosure rules);
  - Ch 1 (no pantry source covers converting a screenplay for generation).

  Only Ch 1 has a real run behind it so far.

---

## Chapter Anatomy Template

**TOC stage (now): every chapter has five parts.**

1. **From your craft to the model:** starts from the craft the filmmaker already has and shows what the model needs to produce it:
   - the words it follows;
   - the words it ignores (found by testing, never assumed);
   - the job settings that carry the rest (first frame, references, aspect ratio, length).

   Film craft is not taught again. Every AI term is defined on first use.
2. **The agent does it:** what the model does by default, and how to override it. The agent is the hands; the filmmaker directs it directly. Model and tool names go only in a dated **"Tools as of"** box.
3. **The +1:** where the output departs from what the filmmaker intended. Named failures come from real work. A departure from history or from someone else's taste is not a failure: the agent flags it once, the filmmaker decides, and the decision goes in the production log.
4. **On the set: Galen's opening:** what was really done, with file paths, and whose hands did it (so far, Bear's). Where something has not been run: an exact session for Galen to run (in outline.md), never a description of what he would decide.
5. **Exercises:** at least three; one at Apply or above; one that produces something. Every exercise ends in a file and a line in the production log. Templates have blanks for the filmmaker's own decisions; no finished prompts. Galen's prompts appear only as examples of his decisions.

**Draft stage (required later, per /c2):**
- a one-paragraph overview;
- 3 to 5 objectives;
- the opening case;
- a mid-chapter checkpoint;
- the worked example (part 4);
- a summary written as capabilities gained;
- key terms (AI terms beside the film terms they map to, in plain words);
- 3 to 5 discussion questions, one across chapters;
- further reading with one-line notes;
- the bridge question.

## Keyword Audit (proposed renames, not yet applied)

Most draft titles pass the search test but fail the learner test (they name a topic, not what the filmmaker will do).

| # | Draft title | Proposed title | Why |
|---|---|---|---|
| Intro | Can You Make Your Film Now? | keep | an introduction may pose a question |
| 1 | From Screenplay to Shot Table | Converting the Screenplay: AI Script Notes and the Shot Table | names both actions |
| 2 | The Visual Story | Planning the Visual Story: Look Rules for Every Prompt | names the action and the output |
| 3 | The Frame: Composition, Angle and Lens | Composing the Shot: Framing, Camera Angle and Lens | field keywords |
| 4 | Light and Color | Lighting and Color for the Frame | names the action |
| 5 | Designing the World | Production Design: Sets, Props, Costume and Characters | "designing the world" is metaphorical |
| 6 | Storyboards and the Shot List | Storyboarding and Shot Lists | names the action |
| 7 | Producing: Budget, Schedule and Crew | Producing: Budgeting, Scheduling and Crewing | names the actions |
| 8 | Movement: Camera and Action | Camera Movement and Animating the Shot | adds the AI action |
| 9 | Directing Performance and Coverage | Directing Performance, Dialogue and Coverage | dialogue is the hard case |
| 10 | Sound: Dialogue, Voice, Effects and Music | Sound Design: Dialogue, Voice, Effects and Music | field keyword |
| 11 | Editing: Continuity, Time and Rhythm | Film Editing: Continuity, Time and Rhythm | field keyword |
| 12 | VFX, Compositing and Finishing | Visual Effects, Compositing and Finishing | spells out VFX for search |
| 13 | Distribution, Festivals, Pitching and Disclosure | Distribution, Film Festivals, Pitching and AI Disclosure | field keywords |

## Chapter Specifications

**Introduction: Can You Make Your Film Now?**
*Problem it solves:* "I have a finished screenplay and I'm lost on the tech. Is this real, and what will it cost?"
*Opening:* the handoff. Bear stopped before designing Galen's cabin once it was clear his vision is not Galen's, and handed Galen the controls. (Galen opening 1 of 3.)
*Blocks:*
1. The thesis: the filmmaker conducts, the agent plays.
2. The agent is the hands: direct it yourself, without a translator.
3. What it costs, plainly, with the logged figures.
4. The two still tiers, and never paying for motion to find out what something looks like.
5. The first win: a finished opening scene that helps raise money.
6. Setup and the honesty rules (RULES 12 to 14); the pebble, made from a few lines of the filmmaker's own screenplay.
*Worked example:* the Wrong Ship. A textbook trireme reached two finished films before Galen caught it.
*Exercises:* set up the project and the log; make the pebble film; write a half-page note on where it departed from what you intended.
*Bridge:* the pebble came from three lines of your script, and the model filled in the rest. What does it need from the whole screenplay?
*Contributor notes:* TB ch 1; CA 1.1 to 1.2; the AI Filmmaking README. Common mistake: selling AI as effortless, or as the one making the calls.

**Ch 1: From Screenplay to Shot Table**
*Problem:* "I have a finished screenplay. How does it become something an agent can make?"
*Opening:* the agent's notes on Galen's script, each flagged once (Galen opening 2 of 3):
- a cabin on an open-deck ship;
- a crew count that differs inside the script;
- a monocle out of period (his call);
- lightning against Bear's storyboard;
- lyrics still under copyright.
*Blocks:*
1. What changes when the camera is a model: a generated image records no real moment (Bazin's question, asked again); text, still or video as the starting point; the five stages mapped onto the agentic studio.
2. What a model needs that a screenplay leaves to the crew: picture, sound, length, camera, references, continuity.
3. The agent's notes on a finished script: format, continuity inside the script, period, rights, coverage-style notes. Flag once, decide, log.
4. The default pull toward the familiar, and the override: the writer's intent, stated before the notes.
5. The conversion: screenplay to scene list to shot table, the generation plan (RULE 1), as a template with blanks.
6. Authorship and the ethics debate, briefly.
*Worked example:* the flags above as examples of flag-once-and-log, not as failures. Galen's shot-table session is in outline.md.
*Exercises:* state your intent for one scene, then get the agent's notes on it and log a decision for every note; convert one scene of your screenplay into the shot-table template; a 300-word position on Bazin and generated images.
*Bridge:* the table says what is in each shot. What should the film look like?
*Contributor notes:* FS Module II (Bazin); CA ch 1 to 3; CR week 1; VP ch 1; BB Formatting a Script, Dialog, Exposition; TB Script Format; Galen's SCRIPT-NOTES. No pantry source covers the conversion itself; Bear's run on Galen's script is the evidence. Common mistakes: treating the shot table as paperwork instead of the plan every prompt comes from; accepting notes that rewrite the writer's voice.

**Ch 2: The Visual Story**
*Problem:* "I know the look I want. Every frame the model gives me is pretty, and none of them belong together, or to me."
*Opening:* one film's visual-structure graph from BLK ch 9. [example chosen at research]
*Blocks:*
1. Visual structure across a film, and why a model breaks it: one prompt at a time, no memory between shots.
2. The model's default look.
3. Look rules that override it in every prompt (RULES 1, 2).
4. The intensity note for each sequence.
5. Judging frames against the look rules.
*Worked example:* Bear's look for the draft storyboard (no lightning), set against Galen's script (lightning in nearly every beat). This shows two people's decisions, not a right answer. Galen's session is in outline.md.
*Exercises:* write your look rules (template with blanks); write the intensity note for your opening; **the thesis exercise:** make the same short scene twice under opposite look rules, or with a second person from the same script, and show the results side by side with the decisions that made them differ.
*Bridge:* the look is yours. Will the model frame each shot the way you would?
*Contributor notes:* BLK ch 1 to 9 (core); BB Finding the Look; CR week 2. Common mistake: a mood board with no story attached.

**Ch 3: The Frame: Composition, Angle and Lens**
*Problem:* "I can name the shot. Will the model give it to me?"
*Opening:* one frame spec, written the way a cinematographer would say it, and what the model returned. [example built and tested at research]
*Blocks:*
1. Prompt words and job settings: which is which (aspect ratio, resolution and length are settings).
2. Shot size and angle in words the model follows.
3. Lens and depth of field: what the model follows and what it ignores, tested.
4. Objective and subjective shots.
5. The model's default framing, and the override.
6. The still check (RULE 6).
*Worked example:* in Film 1, Bear matched the model to the subject: one for the ship, another for faces and crowds (RULE 4).
*Exercises:* specify and generate one beat three ways (size, angle, lens) in draft stills; run one spec through two models and record which words each followed; keep-or-reject notes on ten stills, each reason stated against your intent. Then revise your shot table's frame words with what you found.
*Bridge:* the frame is right. Is the light?
*Contributor notes:* KGB ch 3 to 5; BB Cinematography; BLK ch 3 to 4; TB ch 5; VP ch 3 to 4. Common mistake: trusting lens words the model ignores.

**Ch 4: Light and Color**
*Problem:* "My stills change light from one shot to the next."
*Opening:* one still described two ways, by the lighting setup and by the light it produces, with what the model returned for each. [example built and tested at research]
*Blocks:*
1. A model has no lights to place: describe the result, not the setup.
2. Source, direction, quality, time of day and color.
3. The model's default light, and the override.
4. Holding one fixed light description across a sequence.
5. Color as continuity; relighting a still.
*Worked example:* Bear's storm-light rework and his note (later in the day, a little darker, no lightning), shown as Bear's decisions. Galen's session is in outline.md.
*Exercises:* a lighting plan for your scene, written as fixed descriptions; generate the sequence in draft stills and mark every frame that drifts from your plan; repair the drifters, and revise your shot table's light words.
*Bridge:* light and frame hold. Now the things and people in them.
*Contributor notes:* BB Lighting and Grip; BLK ch 5 to 6; CG lighting. Common mistake: light with no source in the world. Needs a cinematographer's review.

**Ch 5: Designing the World: Sets, Props, Costume and Characters**
*Problem:* "My hero looks different in every shot, and the ship isn't the one in my head."
*Opening:* the deepfake and likeness debate (CA 2.3).
*Blocks:*
1. Continuity without a built set: reference images and a fixed description, shot by shot.
2. Design in rounds on draft stills.
3. Reference sheets and identity models (RULE 20).
4. Period detail stated, never assumed: the agent flags a departure once, and the filmmaker's choice is logged.
5. Consent for likeness.
*Worked example:*
- the Wrong Ship, with the review-slide notes as the relay loop the course ends;
- Bear's ship rounds, including the curl drawn at both ends when one was asked for (RULE 19);
- Bear's own Aegeus, which replaced the agent's first tries.

Then **the cabin, the handoff:** Galen's first session, step by step in outline.md.
*Exercises:* a character sheet in four or five angles; a hero-prop sheet; a log of every period departure in your designs, each recorded as your choice.
*Bridge:* the world exists. Lay out the whole scene before anything moves.
*Contributor notes:* BB The Art Department; RMM ch 6; CR week 2. Common mistake: one great portrait and no reference set; or "correcting" the filmmaker's world to match history.

**Ch 6: Storyboards and the Shot List**
*Problem:* "How do I see the whole film before I pay for it?"
*Opening:* Galen's 37-frame draft storyboard. (Galen opening 3 of 3.)
*Blocks:*
1. From shot table to draft-still prompts.
2. The whole scene as draft stills on contact sheets (RULE 3).
3. Numbering, labels and maps, carried over from paper boards.
4. The review pass and the superseded folder (RULE 12).
5. Hero stills for approved frames only; each becomes a clip's first frame.
6. The arrows on a board become one stated move per clip (Ch 8).
*Worked example:*
- Two failures against the script were fixed: a spyglass where the script says monocle, and edge bars.
- Three items wait on Galen: the cabin, the period of the helmets, the crew count.
- The cabin frames are placeholders made before the handoff.
- Galen's review session is in outline.md.
*Exercises:* a numbered draft storyboard of your scene; a review log with keep, reject or question for every frame; a hero-still list and the shot list linked to it.
*Bridge:* every frame is approved. What will it cost to move them?
*Contributor notes:* KGB ch 2, 13; BB A Director Prepares; CG storyboards; VP ch 7. Common mistake: paying for hero stills before the drafts are reviewed.

**Ch 7: Producing: Budget, Schedule and Crew**
*Problem:* "How much will this really cost, and what do I spend it on?"
*Opening:* testing one video model properly can cost hundreds of dollars before a single real shot (VP Preface).
*Blocks:*
1. The breakdown, priced in credits per still and per second of motion.
2. The budget in three lines: draft stills, hero stills, motion.
3. Every take costs money: budgeting retries.
4. Test budget first.
5. Job and cost log (RULE 14).
6. What stays human, and footage as a fundraising tool.
*Worked example:* the logged prices, and the Wrong Ship in money. [NEEDS HUMAN INPUT: credits spent on Films 1 and 2 before the ship was caught.] Galen's budget session is in outline.md.
*Exercises:* break down your script in credits; fill the budget template with the three lines priced separately, plus a test budget; a generate, shoot or cut decision for every shot, with reasons.
*Bridge:* the money is planned. Make the stills move.
*Contributor notes:* BB Production; RMM ch 3 to 5 and the sample budgets; Safety on the Set. Common mistake: budgeting finals and forgetting retries. [NEEDS HUMAN INPUT: per-tier still prices; dollar price per credit.]

**Ch 8: Movement: Camera and Action**
*Problem:* "My clips move, but not the way I meant."
*Opening:* the filmmaker's own pebble clip from the Introduction, replayed: why does the camera move?
*Blocks:*
1. A clip starts from a still and runs a few seconds; its length is a setting on the job.
2. Image-to-video from a hero still, and the model's default motion.
3. Camera-move words the model follows, tested.
4. One stated move per clip (RULE 7).
5. Motivated movement and screen direction, carried over.
6. Four-frame contact sheets (RULE 8).
*Worked example:* Film 1's trireme clips and the prompt that stopped the oars bending and merging. Galen's one-clip session is in outline.md.
*Exercises:* animate three approved hero stills, one stated move each; contact sheets for every clip; a reject log with each departure from your intent named.
*Bridge:* the camera moves. Can the people act?
*Contributor notes:* KGB ch 5, 12, 14; BLK ch 7; CR week 3; VP ch 5. Common mistake: judging a clip by its first frame.

**Ch 9: Directing Performance and Coverage**
*Problem:* "Two characters talk, and the scene falls apart."
*Opening:* a generated shot-reverse-shot that crosses the line. [example built at research]
*Blocks:*
1. Coverage, carried over: master, singles, reverses.
2. The model's default axis, and the floor plan that overrides it.
3. Eyelines and screen direction stated in every prompt of the scene.
4. Reference-to-video for identity.
5. Expression, gesture and lip sync.
6. Choosing takes.
*Worked example:* the Aegeus reference-video test (three models held Bear's Aegeus face). **Not run yet:** a two-character dialogue scene. Galen's session is in outline.md.
*Exercises:* a coverage plan with a floor map; generate master, two singles and reverses (drafts, then hero stills, then motion); a take-choice note.
*Bridge:* the picture plays. What does it sound like?
*Contributor notes:* BB Director, Continuity and Coverage; KGB ch 8, 11, 15 to 17; FS 180/30-degree rules; CA 5.5.3. Common mistake: trusting the model with screen direction. Needs a working director's review.

**Ch 10: Sound: Dialogue, Voice, Effects and Music**
*Problem:* "Half the film is sound, and I don't yet know what a model can give me."
*Opening:* one clip played silent, with its ambient sound, and with music. [demonstration built at drafting]
*Blocks:*
1. The sound list as the spec the agent works from.
2. Voice synthesis and cloning, with consent.
3. The model's default ambience; effects and music.
4. The agent's mix to the filmmaker's loudness target (RULES 15 to 17).
5. The rights record.
6. The ear check.
*Worked example:* Film 2's narration: one line per shot, 7 of 25 shots slowed to fit, ambience leveled then ducked, -16 LUFS. **Not run yet:** a score. Galen's session is in outline.md.
*Exercises:* a sound list for your scene; build and mix the soundtrack to your target; a rights and consent record for every source.
*Bridge:* every piece exists. Now cut it.
*Contributor notes:* BB Audio Basics; TB ch 6; CG audio; CA 5.5.3 to 5.5.4. Common mistake: no ear check. Needs a sound editor's review.

**Ch 11: Editing: Continuity, Time and Rhythm**
*Problem:* "The agent assembled it. Why doesn't it feel like mine?"
*Opening:* two cuts of the same scene, judged by Murch's rule of six (BB).
*Blocks:*
1. Who holds the timeline: the agent assembles from the shot table.
2. Cut notes typed in plain words (trim, swap, hold, cut).
3. Continuity, time and rhythm, judged by the filmmaker.
4. Generating a missing shot, at a cost (Ch 7).
5. Captions.
6. When the cut is yours.
*Worked example:* the agent's assemblies of Films 1 and 2 and the two design films, and what the filmmaker's cut notes would change. Galen's cut session is in outline.md.
*Exercises:* have the agent assemble your scene; cut it to a fine cut with your own notes; a cut-by-cut justification against the rule of six.
*Bridge:* the cut works. Is it finished?
*Contributor notes:* BB The Work of the Editor; KGB ch 6, 7, 9, 10; BLK ch 8; TB ch 7, 8, 10. Common mistake: accepting the assembly as the cut. Needs an editor's review.

**Ch 12: VFX, Compositing and Finishing**
*Problem:* "I shot one real thing. Can it live in the generated world?"
*Opening:* the history of effects from matte paintings to CGI (CA 1.3), or a hybrid VFX practitioner from CA ch 4. [chosen at research]
*Blocks:*
1. Generated elements treated as plates.
2. Compositing into live footage.
3. Object removal and replacement; video-to-video restyling.
4. Consistency across real and generated shots.
5. Titles and overlays in post (RULE 9).
6. Upscaling last, per clip (RULE 11).
*Worked example:* 4K upscaling on Films 1 and 2, then dropped by Bear for later films. **Not run yet:** a generated element in a live-action plate. Galen's session is in outline.md.
*Exercises:* composite one hybrid shot; finish your cut (titles, overlays, upscale); a shot-by-shot real-or-generated label sheet.
*Bridge:* the film is done. Who sees it, and what do you tell them?
*Contributor notes:* CA 1.3, 5.4, 5.5; CR week 4; CG effects; VP ch 6. Common mistake: polishing past the point anyone can see. Color grading has no pantry source.

**Ch 13: Distribution, Festivals, Pitching and Disclosure**
*Problem:* "How do I release this honestly and get it seen, or funded?"
*Opening:* the festival programmer's view of a submission (RMM ch 10).
*Blocks:*
1. Delivery files, captions and metadata.
2. Festivals and their AI rules, dated.
3. Synthetic-media disclosure and credits.
4. Who owns generated footage.
5. Pitching: the logline and the pitch, moved here from the screenplay chapter.
6. The pitch reel and fundraising.
*Worked example:* four films posted to the Agentic Filmmaking playlist with the synthetic-media flag and captions. **Not run yet:** a festival submission and a pitch reel. Galen's session is in outline.md.
*Exercises:* a delivery package for your scene; a festival list with each festival's AI rule, dated; a credits-and-rights audit of your own film.
*Bridge:* the capstone.
*Contributor notes:* RMM ch 9 to 10; CG Share; BB Getting Started in the Business, Loglines, Pitching; CA ch 6. Common mistake: stating a festival or copyright rule without a date. Needs a legal reviewer.

**Capstone: The Opening Scene**
*Capability:* the whole pipeline on the filmmaker's own screenplay, checked against a self-review checklist.
*Deliverables:*
- the agent's notes, answered, and the shot table;
- look rules;
- the reviewed draft storyboard;
- hero stills;
- the budget;
- clips;
- the soundtrack;
- the cut;
- the release;
- the production log.
*Length:* the filmmaker's choice. Self-paced and ungraded.

## Case Study Strategy

**Domain coverage map**

| Domain | Chapters | Concepts illustrated |
|---|---|---|
| Galen's opening (period drama at sea) | worked example in Intro and Ch 1 to 13; openings in Intro, 1, 6 | everything; the running case |
| The filmmaker's own screenplay | exercises everywhere; Ch 8 opening (the pebble clip) | transfer to their own work |
| Classic narrative film (Brine's examples) | opening in 11 | cutting |
| Model tests built at research | openings in 3, 4, 9 | what the model follows and ignores |
| Visual design theory (Block) | 2 | visual structure |
| AI practitioners (CA ch 2.3 and ch 4 interviews) | openings in 5, 12 | likeness ethics, hybrid VFX |
| Cost of testing (VP Preface; logged prices) | 7 | budgeting |
| The festival circuit (Munroe) | 13 | distribution |

**Over-representation flag:** Galen's film appears in far more than 30 percent of chapters. That is by design (it is the running case and, in this course, the target reader), so the rule is applied to chapter openings instead: Galen opens only three chapters.

**Failure cases** (all real, all departures from intent):
- the Wrong Ship (Ch 5, Intro, Ch 7);
- the spyglass where the script says monocle (Ch 6);
- the curl drawn at both ends of the hull (Ch 5);
- the agent's rejected first-try kings (Ch 5);
- the oars that smeared (Ch 8).

Departures from history (helmets, the monocle, the cabin) are taught as flags and logged choices, not failures.

**Escalation:**
- *Act One* cases have one concept and a clear answer: does this note fit my intent? does each row say what the page means?
- *Act Two* cases need judgment: does this still or this take match what I intended?
- *Act Three* cases are synthesis with no single answer: is this cut mine? is this release honest enough?

**The thesis case:** Ch 2's side-by-side (the same scene made under opposite look rules, or by two people) is the direct evidence for the thesis. Bear's draft storyboard and Galen's own look rules become a real pair once Galen runs his session.

**Concepts with no case yet:**
- dialogue lip sync (Ch 9);
- a composed score (Ch 10);
- compositing into live footage (Ch 12);
- color grading (Ch 12);
- a festival submission (Ch 13);
- the model tests behind the openings of Ch 3, 4 and 9.

No hypotheticals are planned: each gets a real session, or the chapter says "not run yet".

## Contested Claims Audit

| Claim | Status | How the course handles it |
|---|---|---|
| A generated film is authored by the filmmaker | Disputed | Present both sides (CA 1.2, 2.3). The course argues that authorship lives in decisions: the filmmaker conducts, the agent plays. The filmmaker writes their own position (Ch 1). |
| Generated footage can be copyrighted | Emerging, varies by country | Dated sources only; no assertion. A "rules as of" box in Ch 13. |
| Festivals accept AI films | Emerging, varies by festival | A dated table, built at research and refreshed each edition. |
| Voice cloning and likeness use are lawful with consent | Emerging, varies by jurisdiction | Teach consent records as practice; point to law with dates; no legal advice. |
| AI makes filmmaking cheaper | Emerging | Show only logged numbers. No claims about the cost of a whole feature. |
| Models obey camera, lens and light words | Emerging, model-specific | Tested in exercises (Ch 3, 4, 8), never asserted. |
| AI will replace film crews | Disputed | Acknowledge the labor debate (CA 1.2); the course claims only that one person can now direct a short. |
| The photograph has a special claim on reality (Bazin) | Disputed in film theory | Pose it as a question in Ch 1, with formalist replies. |

## Coverage Gaps

| Gap | Why excluded | Name in preface? |
|---|---|---|
| Story, conflict, structure and script writing | the reader already has them; taught in *Agentic Filmmaking* | yes |
| Documentary | [NEEDS HUMAN INPUT — open decision 4]; the pantry is fiction-centred | yes, either way |
| Animation as a form | outside the thesis (a live-action look) | yes |
| Operating a real camera and grip | only hybrid plates in Ch 12 | yes |
| Training in one editing or compositing program | ages fast; the agent assembles | no |
| Film history and theory beyond Ch 1 | covered better in film studies courses | no |
| Composing music | Ch 10 covers selection, spotting and generation only | yes |
| Color grading | research gap; may enter Ch 12 | yes, if still missing |
| Contracts and legal clearance | not legal advice; Ch 13 points to rules | yes |
| Interactive and immersive media | CA covers it; out of the short-film scope | no |

## Hard Chapters

1. **Ch 9, Directing Performance and Coverage.**
   - *Why hard:* models are weakest here, and no dialogue scene has been run.
   - *If written poorly:* it teaches filmmakers to accept dead performances and broken eyelines.
   - *Ideal author:* Bear, with a working director as reviewer. [NEEDS HUMAN INPUT — who reviews?]
2. **Ch 12, VFX, Compositing and Finishing.**
   - *Why hard:* hybrid work needs real footage and VFX skill, and no hybrid shot exists yet.
   - *Ideal reviewer:* a compositor; CA ch 4's hybrid-VFX interview is a lead.
3. **Ch 13, Distribution, Festivals, Pitching and Disclosure.**
   - *Why hard:* the rules change monthly and differ by festival, platform and country.
   - *If written poorly:* it gives filmmakers wrong legal-sounding advice.
   - *Ideal reviewer:* an entertainment lawyer or a festival programmer.
4. **Ch 1, From Screenplay to Shot Table.**
   - *Why hard:* no pantry source covers converting a finished screenplay for generation. Bear's run on Galen's script is the only evidence.
   - *If written poorly:* the chapter rewrites the filmmaker's script instead of converting it.
   - *Ideal reviewer:* a screenwriter or script supervisor.

## Aging Risk Audit

| Chapter | Stable core | Current-state content | Ages in 3 yrs / 5 yrs |
|---|---|---|---|
| Intro, 1 | who decides; what a model needs from a screenplay; the shot table | the tool map, prices, script-note features | low / medium |
| 2, 3, 4 | visual structure, frame, light | model defaults, the words each model follows | medium / high |
| 5 | the art department, consent | identity models, reference limits | high / high |
| 6 | storyboard practice, the two tiers | which models fill each tier | low / medium |
| 7 | breakdown, budgeting | prices per tier and per second | high / high |
| 8, 9 | movement, coverage, the axis | video models, lip sync | high / high |
| 10 | sound craft, mixing | voice and music models | medium / high |
| 11 | editing grammar | agent assembly | low / medium |
| 12 | compositing principles | specific VFX tools | high / high |
| 13 | festivals, credits, pitching | AI rules, copyright, disclosure flags | high / high |

**Structural fix (in the anatomy):** the craft-to-model translation, defaults-and-overrides and judgment live in the running text; tools, prices and rules live in dated boxes. The evidence that this is needed is in the pantry itself: the 2025 tool chapter in *Cinematic Algorithms* already names tools Bear's 2026 runs did not use. The words each model follows age fastest of all, so they are recorded as dated test results, not as rules.
