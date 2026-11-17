<!--
    outline.md
    TABLE OF CONTENTS: the chapter-level planning document for AI Filmmaking (for trained filmmakers).
    Kept in sync with BLUEPRINT.md. Not the auto-generated EPUB TOC.
    The general-audience course, Agentic Filmmaking, has its own outline.md in books/agentic-filmmaking-book.
    Source keys (BB, BLK, KGB, TB, RMM, CG, FS, CA, VP, CR) are defined in BLUEPRINT.md, "Pantry map".
    RULE n = /Users/bear/Documents/CoWork/bear-textbooks/books/ai-filmmaking/RULES.md
    Model and tool names appear only inside "Tools as of" boxes.
-->

# AI Filmmaking: Outline

**Author:** Nik Bear Brown
**Status:** draft for GATE 0, 2026-11-16, revised the same day with Bear's decisions, and on 2026-11-17 for *AI Filmmaking*. Not signed.

## Executive summary

- **What this is:** the table of contents for *AI Filmmaking*, a self-paced online course with no fixed length: an introduction, 13 chapters in four parts, and a capstone. For each chapter it gives the sections, the pantry sources, and the exact session Galen runs where nothing has been run yet.
- **Who it is for:** a trained filmmaker who already has a finished screenplay and is new to AI. Galen is that reader: a master's degree in film and a full script. The course is technical: how to take that screenplay and turn it into something an agent can make into a film.
- **What changed on 2026-11-17:** the course split into two courses in two repos: *AI Filmmaking* (this one) and *Agentic Filmmaking*. This one skips teaching story, conflict and script writing, so the old Chapters 1 to 3 are now one chapter: Chapter 1, the agent's notes on a finished screenplay and its conversion into a shot table. *Agentic Filmmaking*, for a general audience without a film background, keeps those chapters; its starting outline is [/Users/bear/Documents/CoWork/bear-textbooks/books/agentic-filmmaking-book/outline.md](/Users/bear/Documents/CoWork/bear-textbooks/books/agentic-filmmaking-book/outline.md).
- **How to read it:** every chapter has the same five parts.
  - *From your craft to the model* starts from what the filmmaker already knows and shows what the model needs to produce it. That means the words it follows, the words it ignores, and the job settings that carry the rest.
  - *The agent does it* is what the model does by default and how to override it.
  - *The +1* is where the output departs from what the filmmaker intended.
  - *On the set* is what was really done on Galen's opening, and whose hands did it.
  - Exercises close the chapter.
- **The thesis:** the filmmaker conducts; the agent plays. The course teaches the tech so it stops being the obstacle, and never makes the creative calls for the reader.

**The running case (one thread, whole course):** Galen's opening scene. In this course Galen is both the running case and the target reader. So far the work on his film has been Bear's hands. The course turns on the handoff, when Galen takes over the agent. Each student runs the same steps on the opening of their own screenplay, which becomes the capstone.

**How every Galen session works** (the rules for each "Session for Galen" below):

1. Galen types to the agent directly, in his own words. Nobody relays notes.
2. Draft stills come first. A hero still (the paid, high-quality still that becomes a clip's first frame) only when a session says so. No motion unless a session says so.
3. The agent flags a likely departure from history or from the script once. Galen decides, and the decision goes in the production log.
4. Every keep or reject gets a reason, in his words, in the log.
5. When a picture is wrong, he revises his description. He does not ask anyone to fix the picture.
6. Credit cap per session: [NEEDS HUMAN INPUT: credit cap per session, set by Galen or Bear before it starts].

---

## Front matter

- **Preface:** why this course exists. Many trained filmmakers carry a finished screenplay and a clear picture of the film. What they lack is the technical path from that screenplay to an AI that produces it. This course is that path, without a rabbit hole of bad decisions.

## Introduction: Can You Make Your Film Now?

- **Opening: the handoff.** Galen's small boat has a cabin. Bear found that implausible for the period, but it is Galen's vision. Once it was clear that his vision is not Galen's, Bear stopped before designing it and handed Galen the controls.
- **The thesis:** the filmmaker conducts; the agent plays. Two people with the same screenplay and the same tools make different films, because the difference lives in their decisions. The agent is the hands; the pitch is "direct it yourself", not "do it yourself". Bear's role ends at teaching.
- **What it costs, plainly:** generation costs real money. Words cost almost nothing. A logged still costs about 2 credits, and a logged 8-second clip 26 to 128 credits. The 37-frame draft storyboard cost about 75 credits. [NEEDS HUMAN INPUT: dollar price per credit.] Never pay for motion to find out what something looks like.
- **The Wrong Ship:** a textbook trireme reached two finished films before Galen caught that it was not his ship. A draft still would have shown it for a few credits.
- **The realistic first win:** a finished opening scene that helps raise money for the rest. That is what the capstone builds.
- **Setup:** the agent, the project folder, the production log, accounts and credits. Also the honesty rules: say it is AI, credit sources, log costs and job IDs, and keep superseded files (RULES 12 to 14).
- **On the set:** the Agentic Filmmaking playlist so far shows Bear's hands on the film. The handoff gets its own episode; it is the turning point of the series.
- *Sources:* TB ch 1 (the idea matters more than the gear); CA 1.1 to 1.2 (AI in production; the controversy); the AI Filmmaking README.

> **Tools as of 2026-11-16:** agent, Claude Code or Cowork; generation service, Higgsfield. Logged prices: Kling 4.0 26 credits per 8-second clip at 1080p, Seedance 2.0 96, Seedance 2.5 128; a Nano Banana 2.1 still about 2.

---

## Part I: From Screenplay to Production Plan (the film in words)

### 1. From Screenplay to Shot Table

The filmmaker already knows how films tell stories, how a story is built and how a screenplay is written. This chapter covers only three things: what changes when the camera is a model, what an agent can do for a finished script, and how the script becomes a plan the agent can generate from. (*Agentic Filmmaking* teaches story, conflict and script writing in full, in three chapters. Pitching moves to Ch 13.)

- **What changes when the camera is a model:**
  - A generated image is not a record of a real moment (Bazin's question, asked again).
  - The three ways a clip gets made: from text, from a still, or from other video.
  - The five stages of making a film, mapped onto the agentic studio: text, image, video, voice and music models, plus the agent that runs them and keeps the log.
  - Authorship and the ethics debate.
- **From your craft to the model:** a screenplay is written for a crew that fills in what the page leaves out. A model fills those gaps with its own defaults. So the conversion writes down, for every shot, what the screenplay leaves to the crew: the picture, the sound, the length, the camera, the references and the continuity notes.
  - Scene headings give location and time of day.
  - Action lines become pictures, shot by shot.
  - Parentheticals become performance notes.
  - Transitions become cut notes.
- **The agent does it: notes on a finished script.** What the agent can check:
  - format;
  - continuity inside the script (names, counts, props);
  - likely departures from the period;
  - rights problems (lyrics, quoted text);
  - coverage-style notes.

  Each note is flagged once, the writer decides, and the decision is logged. By default the agent's coverage scores the familiar. To override that, the writer states their intent before asking for notes.
- **The agent does it: the conversion.** The screenplay becomes a scene list, and then a shot table with columns for shot, time, picture, sound and reference. The shot table is the generation plan (RULE 1). Template: a shot table with blank columns for the filmmaker's own decisions.
- **The +1:** voice and subtext are the writer's. When a note would move the script toward the familiar, the writer declines it and logs the reason.
- **On the set (done by Bear):** the agent's notes on Galen's script email flagged five things, once each:
  - a cabin on an open-deck ship;
  - a crew count that differs inside the script;
  - a monocle out of period (flagged as his call);
  - lightning against Bear's storyboard;
  - shanty lyrics still under copyright.
- **Session for Galen: the shot table.**
  1. Give the agent the script.
  2. The agent lists each flag above once.
  3. Galen answers each flag in his own words, and the agent logs each answer.
  4. The agent breaks the script into a shot table, using his answers.
  5. Galen reads the table and corrects any row in his own words.
  - *Output:* the shot table and the log entries. No images.
- *Sources:* FS Module II (Bazin); CA ch 1 to 3; CR week 1; VP ch 1; BB Formatting a Script, Dialog, Exposition; TB Script Format; Galen's SCRIPT-NOTES.

---

## Part II: Pre-production (the film in stills)

Draft stills (fast, cheap models) for exploring; hero stills (one paid, high-quality still per shot) only for frames that will become a clip's first frame.

### 2. The Visual Story

- **From your craft to the model:** contrast and affinity, tone, color and rhythm are planned across a whole film. A model sees one prompt at a time and remembers nothing between shots. So the visual structure has to be written down in two places:
  - look rules carried in every prompt;
  - a note for each sequence saying where the intensity rises and falls.
- **The agent does it:** the model's default look, and look rules that override it. Write the look rules once (light, palette, camera, what is banned in frame) and paste them into every prompt (RULES 1, 2). Template: look rules with blanks.
- **The +1:** a model makes beautiful single frames with no structure. The filmmaker decides where the film gets tense and where it rests.
- **The thesis exercise:** make the same short scene twice under opposite look rules, or have two people make the same script, and show the results side by side. Name the decisions that made the films differ.
- **On the set (done by Bear):** Bear's look for the draft storyboard was a dusk-blue storm with no lightning in frame. Galen's script has lightning in nearly every beat.
- **Session for Galen: his look rules.**
  1. Write his look rules in his own words: light, palette, camera, what never appears in frame.
  2. The agent turns them into the block it pastes into every prompt.
  3. Choose one beat; generate a few draft stills under his rules.
  4. Put them beside the same beat from Bear's draft storyboard.
  5. Write what differs and which decision caused it.
  - *Output:* his look rules, the side-by-side sheet, the log entries. This is the thesis exercise, run for real.
- *Sources:* BLK ch 1 to 9 (core); BB The Art Department, Finding the Look; CR week 2.

### 3. The Frame: Composition, Angle and Lens

- **From your craft to the model:** shot size, camera height and angle, lens, depth of field, objective and subjective shots, aspect ratio and frame rate.
  - Some of these are words in the prompt.
  - Others are settings on the job (aspect ratio, resolution, length).
  - Which words each model follows and which it ignores is found by testing at research, not assumed.
- **The agent does it:** the model's default framing (found by testing at research, not assumed), and camera language that overrides it; which models follow which words; coverage variants of one beat.
- **The +1:** does the frame match the frame in the filmmaker's head? Check every still before it moves (RULE 6).
- **On the set (done by Bear):** for Film 1, one image model for the ship and another for faces and crowds (RULE 4).
- *Sources:* KGB ch 3 to 5; BB Cinematography; BLK ch 3 to 4; TB ch 5; FS shots and angles; CG framing; VP ch 3 to 4.

> **Tools as of 2026-11-16:** Film 1's split was Cinema Studio 2.5 for the ship and Nano Banana 2.1 for faces and crowds.

### 4. Light and Color

- **From your craft to the model:** key, fill and back; hard and soft; motivated light. A model has no lights to place, only a description of the result. Describe each light by its source, direction, quality, time of day and color, and hold that description fixed across a sequence.
- **The agent does it:** the model's default light, and time of day, light quality and palette that override it; relighting a still; holding color across a sequence.
- **The +1:** is the light the light the filmmaker intended, and does it match from shot to shot?
- **On the set (done by Bear):** Bear's storm-light rework of the draft stills, and Bear's storyboard note: later in the day, a little darker, no lightning. These are Bear's choices, shown as an example of decisions, not as Galen's look.
- **Session for Galen: light per scene.**
  1. For each scene of his opening, name in his own words the time of day and where the light comes from.
  2. The agent relights a few draft stills to match.
  3. Keep or reject each, with a reason.
  - *Output:* a light plan, kept drafts, log entries. Stills only.
- *Sources:* BB Lighting and Grip; BLK ch 5 to 6; CG lighting; FS color.

### 5. Designing the World: Sets, Props, Costume and Characters

- **From your craft to the model:** an art department keeps continuity by building a thing once. A model rebuilds it in every shot. So the continuity of a set, prop, costume or face has to be carried shot by shot, by reference images and a fixed description. Period detail is stated, never assumed.
- **The agent does it:**
  - design in rounds on draft stills;
  - character reference sheets from four or five angles;
  - identity models;
  - hero props held steady with one reference per shot (RULES 4, 20).

  The agent flags a likely departure from the period once.
- **The +1:** where the design departs from what the filmmaker intended. Examples: faces that all look alike (RULE 5); a curl drawn at both ends of the hull when the filmmaker asked for one (RULE 19). A departure from history is the filmmaker's choice, recorded in the log. Consent comes before anyone's likeness is cloned.
- **On the set (done by Bear):**
  - **The Wrong Ship:** Films 1 and 2 used a textbook trireme with two sails and banks of oars. Galen's ship, as the later stills show, has a curl, a beak and a single bank of oars. Only he could catch it.
  - The review-slide notes ("whole ship · curl and beak · adults", "warm wood, oars biting, too many aboard", "same hull · no lightning") are the relay loop the course ends.
  - Bear's ship design rounds 1 to 3 (Bear chose ship B), Bear's 19 Aegeus stills, and the likeness test.
  - Bear stopped before designing the cabin.
- **Session for Galen 1: the cabin (the handoff).**
  1. Open the agent in his project folder, with the production log.
  2. Describe the cabin in his own words: what it is, where it sits on the ship, what is in it.
  3. The agent reads it back as a prompt and flags a likely anachronism once, if it sees one. Galen decides. The decision and his reason go in the log; it is also his answer to any reviewer who says boats like that had no cabins.
  4. The agent generates a few draft stills.
  5. Galen rejects or keeps each one, with a stated reason in his own words.
  6. For each rejection he revises his description, rather than asking anyone to fix the picture, and asks for new drafts.
  7. Stop when he keeps one, or when the credit cap is reached.
  - *Output:* his final cabin description, the kept draft stills, the log entries. Stills only; no hero still, no motion.
- **Session for Galen 2: the characters still held by placeholders** (Theseus, the first mate, the guards).
  1. Describe each character in his own words.
  2. The agent makes a four-to-five-angle reference sheet from draft stills.
  3. Keep or reject each angle, with a reason.
  4. Revise the description, not the picture.
  - *Output:* one reference sheet per character, log entries.
- *Sources:* BB The Art Department; RMM ch 6 (casting); CR week 2 (character consistency, reference images); CA 2.3 (ethics).

> **Tools as of 2026-11-16:** the likeness test used Higgsfield Soul ID; the ship and Aegeus stills used Cinema Studio 2.5 and Nano Banana 2.1.

### 6. Storyboards and the Shot List

- **From your craft to the model:** the storyboard and shot list the filmmaker already makes become the generation plan.
  - Each approved panel's description becomes a draft-still prompt.
  - Each approved draft becomes the brief for a hero still, which will be the clip's first frame.
  - The arrows for camera and action become one stated move per clip (Ch 8).
- **The agent does it:** the whole scene in draft stills, on contact sheets. Then hero stills only for the approved frames. Each hero still becomes the first frame of its clip, because the video can only be as clear as the still it starts from (RULE 3).
- **The +1:** the review pass. Every frame is judged against the filmmaker's intent. Superseded frames are kept (RULE 12).
- **On the set (done by Bear):** a 37-frame draft storyboard of Galen's opening, about 75 credits.
  - Two failures against the script were fixed: a lens drawn as a spyglass where the script says monocle, and edge bars.
  - Three items wait on Galen: the cabin, the period of the guards' helmets, and the crew count (his script gives two different numbers).
  - The storyboard's cabin frames are placeholders made before the handoff, not the cabin's design.
- **Session for Galen: storyboard review.**
  1. Go through the 37 frames one by one: keep, reject with a reason, or ask a question.
  2. Answer the three waiting items in his own words.
  3. The agent redoes rejected frames as draft stills from his revised descriptions.
  4. Mark which frames get hero stills.
  - *Output:* the reviewed storyboard, the hero-still list, log entries. No motion.
- *Sources:* KGB ch 2 and ch 13 (shot list and map); BB A Director Prepares; CG storyboards; VP ch 7.

> **Tools as of 2026-11-16:** the draft storyboard was made in Nano Banana 2.1.

### 7. Producing: Budget, Schedule and Crew

- **From your craft to the model:** script breakdown, the budget top sheet and the schedule carry over. Two things change:
  - The unit of cost is now credits per still and per second of motion.
  - Every take costs money, whether or not it is kept.

  A test budget comes before the real one.
- **The agent does it:** the budget in credits and money, with three lines priced separately: draft stills, hero stills, motion. Also a test budget before the real one, a log of every job ID and cost (RULE 14), and agents as crew. Template: a budget sheet with blank lines for the filmmaker's own shots.
- **The +1:** where the money goes, and what stays human (actors, a location day, a composer). Footage as a fundraising tool.
- **The Wrong Ship, in money:** what it cost to find the ship in motion instead of in a draft still. [NEEDS HUMAN INPUT: credits spent on Films 1 and 2 before the ship was caught.]
- **On the set (done by Bear):** the logged prices per still and per clip.
- **Session for Galen: the budget.**
  1. The agent prices his reviewed shot list in the three lines from logged prices.
  2. Galen decides, shot by shot: generate, shoot live, or cut.
  3. The agent writes the budget file.
  - *Output:* the budget, log entries. No generation.
- *This chapter is the gate in the middle of the course: no motion until the stills are approved and the money is planned.*
- *Sources:* BB Production, Safety on the Set; RMM ch 3 to 5 and the sample budgets; VP Preface. [NEEDS HUMAN INPUT: per-tier still prices; dollar price per credit.]

> **Tools as of 2026-11-16:** Kling 4.0 26 credits per 8-second clip at 1080p; Seedance 2.0 96; Seedance 2.5 128; a Nano Banana 2.1 still about 2.

---

## Part III: Production (motion and sound)

### 8. Movement: Camera and Action

- **From your craft to the model:** dolly, pan, tilt, crane and handheld; motivated movement; screen direction. A clip starts from a still and runs a few seconds. It gets one stated camera move, and its length is a setting on the job.
- **The agent does it:** image-to-video from a hero still; the model's default motion, and one stated camera move that overrides it. Animate gently: one slow move, rigid and plausible motion (RULE 7).
- **The +1:** motion that departs from what the filmmaker intended (oars that bend and merge). Judge four frames per clip, not one (RULE 8).
- **On the set (done by Bear):** Film 1, 25 clips of the trireme; the prompt that stopped the oars smearing.
- **Session for Galen: one clip.**
  1. Pick one of his hero stills.
  2. Name one camera move in his own words.
  3. The agent generates one clip and a four-frame contact sheet.
  4. Keep or reject, with a reason. If rejected, revise the move description, not the clip.
  - *Output:* the clip or the rejection, log entries.
- *Sources:* KGB ch 5, 12, 14, 18; BLK ch 7; CR week 3; VP ch 5; CA 5.2.

> **Tools as of 2026-11-16:** Film 1's clips were made in Kling 4.0.

### 9. Directing Performance and Coverage

- **From your craft to the model:** blocking, eyelines, screen direction, the 180- and 30-degree rules, and coverage all carry over, but the model does not know where the axis is.
  - A floor plan and a stated side of the line go into every prompt of the scene.
  - Identity is held by references.
  - Dialogue needs lip sync.
- **The agent does it:** reference-to-video for identity; expression and gesture prompts; lip-synced dialogue; master, singles and reverses. By default the model does not know where the axis is. The override is a floor plan and a stated side of the line.
- **The +1:** performance is the director's call; eyelines and screen direction are checked by hand. Deepfakes and likeness.
- **On the set (done by Bear):** the Aegeus reference-video test: three video models all held Bear's Aegeus face.
- **Session for Galen: one exchange.**
  1. Pick a two-character exchange from his script.
  2. Describe or sketch the floor plan, and say which side of the line the camera stays on.
  3. The agent makes the master, two singles and the reverses as draft stills.
  4. Galen checks eyelines and keeps or rejects each.
  5. Hero stills for the kept frames.
  6. Motion only for those.
  - *Output:* the coverage, a take-choice note, log entries.
- *Sources:* BB Director, Continuity and Coverage; KGB ch 8, 11, 15 to 17; FS 180/30-degree rules; CA 5.5.3; VP case study.

> **Tools as of 2026-11-16:** the Aegeus test used Kling 4.0 (reference-to-video), Seedance 2.0 and Seedance 2.5.

### 10. Sound: Dialogue, Voice, Effects and Music

- **From your craft to the model:** dialogue, room tone, effects, spotting music and the mix carry over. Generated sound adds three things:
  - voice synthesis and cloning;
  - generated ambience, effects and music;
  - a rights record for every source.

  The loudness target and the mix are the filmmaker's spec; the agent runs them.
- **The agent does it:** voice synthesis and cloning; the model's default ambience; effects and music generation. The agent also does the mix:
  - narration fitted to the picture (RULE 15);
  - ambience leveled before ducking (RULE 16);
  - hard words respelled for the voice only (RULE 17).
- **The +1:** the ear check; consent for every cloned voice; music rights (old public-domain verse is safe, modern lyrics are not).
- **On the set (done by Bear):** Film 2's narration, mixed to -16 LUFS (LUFS is the standard measure of loudness), with 7 of 25 shots slowed to fit.
- **Session for Galen: the sound of one scene.**
  1. Describe, beat by beat in his own words, what the audience hears.
  2. The agent turns it into a sound list and generates options for one beat.
  3. Keep or reject each, with a reason.
  4. Record the rights for each kept source.
  5. Listen to the mix himself.
  - *Output:* sound list, kept sounds, rights record, log entries.
- *Sources:* BB Audio Basics; TB ch 6; CG audio and narration; FS sound; CA 5.5.3 to 5.5.4; CR week 2.

> **Tools as of 2026-11-16:** Film 2's narrator voice was Kokoro am_onyx ("Liam").

---

## Part IV: Post-production and Release

### 11. Editing: Continuity, Time and Rhythm

- **From your craft to the model:** the assembly, rough and fine cuts and Murch's rule of six all carry over. What changes is who holds the timeline. The agent assembles from the shot table and applies the filmmaker's cut notes, typed in plain words (trim, swap, hold, cut). A shot missing from the coverage can be generated, at a cost (Ch 7).
- **The agent does it:** the agent's default assembly from the shot table; captions. The filmmaker's cut notes override it.
- **The +1:** the agent assembles; the filmmaker cuts. Emotion first, continuity last.
- **On the set (done by Bear):** Films 1 and 2 and the two design films, assembled by the agent.
- **Session for Galen: the cut.**
  1. The agent assembles his approved clips in shot-table order.
  2. Galen watches and types cut notes to the agent directly (trim, swap, hold, cut).
  3. The agent applies them. Repeat until the cut is his.
  - *Output:* the cut, every note in the log.
- *Sources:* BB The Work of the Editor; KGB ch 6, 7, 9, 10; BLK ch 8; TB ch 7 to 8, 10; FS editing.

> **Tools as of 2026-11-16:** Films 1 and 2 were assembled with ffmpeg build scripts; the two design films with filmkit.py.

### 12. VFX, Compositing and Finishing

- **From your craft to the model:** plates, compositing, clean-up and finishing carry over. Generated elements are composited like any other plate. Upscaling comes last. Titles and overlays are added in post, never generated into the footage (RULE 9). Color grading craft is a research gap.
- **The agent does it:**
  - compositing generated elements into live footage;
  - object removal and replacement;
  - face replacement;
  - frame blending and parallax;
  - video-to-video restyling;
  - upscaling, last and per clip (RULE 11);
  - overlays and titles in post, never in the generated footage (RULE 9).
- **The +1:** what is real and what is not, and saying so; when to stop polishing.
- **On the set (done by Bear):** 4K upscaling on Films 1 and 2; Bear dropped 4K for the later films.
- **Session for Galen: one hybrid shot.**
  1. Shoot one live plate himself, of whatever he chooses.
  2. Describe the generated element to add, in his own words.
  3. The agent composites it.
  4. Keep or reject, with a reason.
  5. Label the shot: what is real, what is generated.
  - *Output:* the shot, the label, log entries.
- *Sources:* CA 1.3 and 5.4 to 5.5; CR week 4; CG effects and green screen; VP ch 6. Color grading: no pantry source (research gap).

> **Tools as of 2026-11-16:** upscaling was Topaz Video AI.

### 13. Distribution, Festivals, Pitching and Disclosure

- **From your craft to the model:** delivery specs, festivals and fundraising carry over. What is new:
  - AI disclosure;
  - each festival's AI rules;
  - rights records for generated material;
  - the synthetic-media flag on video platforms;
  - the open question of who owns generated footage.

  Pitching moves here from the screenplay chapter, because the finished opening scene is the pitch.
- **The agent does it:** delivery files, captions, metadata, synthetic-media flags, festival packages, and a pitch reel for fundraising.
- **The +1:** the signature. Credits, AI disclosure, rights records; festival AI rules; who owns generated footage.
- **On the set (done by Bear):** four films on the Agentic Filmmaking playlist with the synthetic-media flag and captions.
- **Session for Galen: the release.**
  1. The agent prepares a delivery package and a dated list of festivals with their AI rules.
  2. Galen chooses which to enter.
  3. The agent drafts credits and disclosure.
  4. Galen edits them and signs.
  5. For the pitch reel, Galen picks the shots and the agent assembles them.
  - *Output:* the package, the signed credits, the festival list, log entries.
- *Sources:* RMM ch 9 to 10; CG Share; BB Getting Started in the Business, Loglines, Pitching; CA ch 6. Festival and copyright rules: research gap.

---

## Capstone: The Opening Scene

Each student makes the opening of their own screenplay through the whole pipeline:

1. the agent's notes and the shot table;
2. look rules;
3. a reviewed draft storyboard;
4. hero stills;
5. a budget;
6. clips;
7. sound;
8. the cut;
9. the release.

The realistic first win is a finished opening scene that helps raise money for the rest. The capstone is self-paced and ungraded: the student checks the film and the production log against a self-review checklist. The length of the scene is the student's choice.

## Back matter

- **Glossary:** AI terms in plain words, each beside the film term it maps to. Film terms are not taught again in this course.
- **Templates with blanks:** shot table, look rules, cost log, budget sheet, storyboard sheet, release checklist. No finished prompts.
- **Tools as of this edition:** all the boxes gathered, dated, and refreshed each edition.
- **Skills that help filmmakers:** agent skills grouped by the stage they serve, from the catalog at [/Users/bear/Documents/CoWork/bear-textbooks/books/agentic-filmmaking-book/skills-catalog/README.md](/Users/bear/Documents/CoWork/bear-textbooks/books/agentic-filmmaking-book/skills-catalog/README.md) (built 2026-11-17, nothing in it tested yet). Skill names are tool names, so they go in the dated boxes too.
