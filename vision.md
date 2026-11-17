<!--
    vision.md
    Blueprint Phase 1: Vision and Positioning. AI FILMMAKING (for trained filmmakers).
    The general-audience course, Agentic Filmmaking, has its own vision.md in books/agentic-filmmaking-book.
-->

# AI Filmmaking: Vision

**Author:** Nik Bear Brown

*Phase 1 output from Blueprint. Written by /scaffold (silent mode) on 2026-11-16 from BLUEPRINT.md, outline.md, pantry/ and the AI Filmmaking notes. Revised the same day with Bear's decisions, and on 2026-11-17 for *AI Filmmaking* after Bear's call with Galen. There is no book.md yet, so Bear's words stand in for it. Sidecar unverified until human sign-off.*

---

## Executive summary

- **What this is:** who *AI Filmmaking* is for, what kind of course it is, what it argues, and how it differs from the three closest alternatives.
- **What is settled:**
  - **Format (Bear, 2026-11-16):** a self-paced online course with no fixed length.
  - **Two courses, two repos (Bear, 2026-11-17):** this one, *AI Filmmaking*, for trained filmmakers with a finished screenplay; and *Agentic Filmmaking*, for a general audience without a film background.
  - **Reader (Bear, 2026-11-17):** a trained filmmaker with a finished screenplay, new to AI. Galen is that reader.
  - **Thesis (Bear, 2026-11-16):** the filmmaker conducts; the agent plays.
- **What is open:** Galen's consent to be the public running case, the cost to students, and fiction only versus documentary too.

---

## Book Concept Summary

This course teaches **the technical path from a finished screenplay to a film made by an AI agent**. It is for **trained filmmakers who have a screenplay and a clear picture of the film, and are new to AI**. It does this by **following one real film (Galen's opening scene) from screenplay to release, in the order costs rise: words, draft stills, hero stills, motion, sound, cut**.
- Each chapter starts from craft the filmmaker already has, and shows what the model needs to produce it.
- It fills the gap left by classical filmmaking textbooks, which teach craft with no AI and assume a crew, and by AI filmmaking courses, which start from zero and teach tool by tool.
- It succeeds if the filmmaker can **make and release the opening scene of their own screenplay, with a production log that shows every decision, cost and AI disclosure, without going down a rabbit hole of bad decisions.**

[CONFIRMED: Bear, 2026-11-16, deployment; 2026-11-17, reader and the two courses; the rest follows from BLUEPRINT.md]

**Biggest unresolved structural question:** whether Galen agrees to be the public running case. Every chapter's "On the set" depends on it.

## Book Type and Deployment Specification

**Type:** a self-paced online course, with no fixed length. Not a semester course, not a workshop. [CONFIRMED: Bear, 2026-11-16] Chapters run in sequence, but each chapter's AI half can be re-entered by task ("how do I storyboard with an agent?"), so it also works as a handbook.

**Primary use:** one filmmaker, on their own time, making the opening of their own screenplay.

**Secondary use:** viewers of the Agentic Filmmaking playlist, who see the same running case. [INFERRED FROM: README, "The series and the course"]

**Explicitly NOT designed for:**
- learners who have never made a film (that is *Agentic Filmmaking*);
- teaching story, conflict or script writing;
- semester or workshop delivery;
- studio VFX professionals;
- software training for one editor or compositing package;
- a film theory or history survey;
- prompt engineering for its own sake.

**How the TOC signals the type:** chapter titles use the field's own words (screenplay, storyboard, producing, editing). The course starts from the screenplay, not from the idea. Every chapter ends in a file the filmmaker made. The AI work sits inside every chapter instead of in a separate part.

**Assessment requirements** (self-paced, so nothing is graded; detail in architecture.md):

| Assessment | Status |
|---|---|
| Chapter exercises, each ending in a file | needed |
| Running production log (decisions, costs, job IDs, superseded files) | needed |
| Capstone, checked against a self-review checklist | needed |
| Self-check quizzes | desired |
| Flashcards for the glossary (AI terms beside the film terms they map to) | desired |
| Exam bank | out of scope |
| Semester LMS modules | out of scope |
| Hosting platform | [NEEDS HUMAN INPUT — it decides the quiz format] |

## Learner Profile

Target reader: a trained filmmaker who already has a finished screenplay and is new to AI. They know story, conflict, script format, coverage and storyboards. What they lack is the technical path from that screenplay to something an agent can generate. Galen is both the target reader and the running case: he has a master's degree in film and a full script. The translation from the filmmaker's craft to what a model needs is what separates this course from tool tutorials. [CONFIRMED: Bear, 2026-11-17, after a call with Galen]

In Bear's words (2026-11-17): Galen *"has a screenplay, and he needs to convert that screenplay into a format that can be made into film. So it's more technical."* (2026-11-16): the course is for people who *"have a dream of making films"* and want to start making their vision without *"going down a rabbit hole of bad decisions"*.

**What they reliably know:**
- story, structure and conflict;
- screenplay format;
- shot sizes, lenses and coverage;
- storyboards and shot lists;
- the stages of a production;
- how an edit is built.

**How the craft is handled:** it is not taught again. Each chapter starts from the filmmaker's own terms and shows what the model needs to produce them:
- the words it follows;
- the words it ignores (found by testing, never assumed);
- the job settings that carry the rest.

**Prior misconceptions** (each one is a source's own warning, so the course can quote it):

1. *"The AI makes the film from a prompt."* The Curious Refuge syllabus itself says there is much more to it than typing a prompt (CR week 1).
2. *"The model reads a screenplay the way a crew does."* It does not. A crew fills in what the page leaves out, and a model fills it with its defaults. So the screenplay is converted into a shot table first (Ch 1; RULE 1).
3. *"A beautiful frame is a good shot."* Block and Brine both tie the frame to story structure (BLK ch 9, KGB ch 1).
4. *"The video model will fix a bad still."* It will not: fix it at the still (RULES 2, 3).
5. *"I'll find out what it looks like in the video."* Never pay for motion to find out what something looks like; the Wrong Ship reached two finished films that way.
6. *"Generated footage is cheap."* Testing a video model costs real money; 100 test clips can cost hundreds of dollars (VP Preface).
7. *"Generated footage needs no credit, disclosure or consent."* (CA ch 2.3; RULE 13)
8. *"The AI should make the creative calls."* The agent is the hands; the filmmaker decides.

**Current capability gap:** they cannot yet do these things:
- turn a screenplay into a plan an agent can generate from;
- get a model to produce the frame, light and look they already know how to name;
- hold a look and a face across generated shots;
- budget the expensive steps;
- finish and release a film honestly labelled.

**Motivation:** creative and practical. They want to make *their* film, and footage that helps raise money for the rest.

## Prerequisite Map

Only true prerequisites are listed. Film craft is assumed in this course; AI terms are taught as content.

| Prerequisite | Safe to assume? | Treatment |
|---|---|---|
| Film training (story, script format, coverage, storyboards) | Yes, for this course | none; *Agentic Filmmaking* teaches it |
| A finished screenplay | Yes, required | the input to Ch 1 |
| Chatting with an AI assistant | Yes | none |
| Running a CLI agent | Probably | Introduction setup |
| Keeping a project folder in order (names, superseded files) | Probably | Introduction setup, then embedded |
| An account and credits on a generation service | No | [NEEDS HUMAN INPUT — which service, who pays, is there a free path?] |
| A phone or camera | Probably | needed only for Ch 12's hybrid shot |

**Prerequisite decision:** four items are rated No or Probably, which crosses the threshold of three. Option chosen: **(1) a foundations chapter**, folded into the Introduction, which acts as Chapter 0 (agent setup, project folder, production log, accounts).

## Central Argument

Thesis: the filmmaker conducts; the agent plays. The agent generates, logs and prices options; every choice of what to keep, reject or change belongs to the filmmaker. The proof is that two people can take the same idea, run the same tools and make completely different films, because the difference lives in their decisions, not in the software. The course teaches the tech so it stops being the obstacle, and never makes the creative calls for the reader. [CONFIRMED: Bear, 2026-11-16]

**Two consequences:**
- The agent is the hands. "Direct it yourself", not "do it yourself".
- Bear's role ends at teaching. The course exists so the filmmaker talks to the agent directly, without anyone relaying notes.

**Supporting method:** the cost order. Decide everything you can on cheap draft stills; pay for a hero still only for a clip's first frame; pay for motion last.

**Thesis test:** the TOC reflects it.
- The Introduction opens on the handoff (Bear stopping before the cabin and handing Galen the controls).
- Ch 1 makes the screenplay, not the model, the source of every shot.
- Ch 2's exercise proves the thesis directly: the same scene made under opposite look rules, or by two people.
- Every "On the set" ends in a session Galen runs himself.

## Field Positioning

**1. Blain Brown, *The Basics of Filmmaking* (Routledge, 2020)**
- *Covers that this course also covers:* the whole craft, from screenwriting to editing, by department.
- *Misses:* AI entirely; it predates the tools.
- *What this course changes:* it assumes a crew, a budget and a set. This course is for the trained filmmaker who has the craft but not the crew. It shows how to carry that craft into directions an agent can follow.

**2. Curious Refuge, *AI Filmmaking Course* (four-week syllabus)**
- *Covers:* AI tools across concept, directing, cinematography, VFX and distribution, with an assignment each week.
- *Misses:* a starting point for a filmmaker who already has a screenplay; depth of craft (filmmaking concepts are one goal among many in week 1); an agent that runs the tools and keeps the log.
- *What this course corrects:* it teaches tool by tool, so it ages with the tools. Its week 2 goals include removing watermarks from videos; this course keeps disclosure and credit (RULE 13).

**3. James Hutson and Andrew Allen Smith, *Cinematic Algorithms* (CRC Press, 2025)**
- *Covers:* AI in video production, ethics and authorship, the history of effects, 12 interviews with AI filmmakers, and workflows for each kind of generation.
- *Misses:* converting a screenplay; exercises a filmmaker can complete; cost.
- *What this course corrects:* its tool chapter already names tools that Bear's 2026 runs did not use. Tools belong in dated boxes, not in the spine.

**Positioning statements:**
- *The Basics of Filmmaking* teaches each department of a crewed production. This course takes the same craft to one filmmaker directing an agent, for trained filmmakers with a screenplay and no crew.
- The Curious Refuge course teaches AI tools week by week, from zero. This course starts from the filmmaker's screenplay and craft and has an agent run the tools, for filmmakers who want skills that outlast this year's models.
- *Cinematic Algorithms* surveys AI in film and its debates. This course makes a film from screenplay to release with every cost and failure on the record, for filmmakers who want to make work, not study it.
