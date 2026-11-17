# Rules for AI filmmaking (draft 1, from film 1)

## Executive summary

Work from cheap to expensive: script, then stills, then clips, then the cut. Fix problems at the still, because a bad still makes a bad clip. Keep everything that is not picture (arrows, diagrams, titles, narration) out of the generated footage and add it in post.

## Rules

1. **Script first.** One table: shot number, time, picture, narration, reference. Write the look rules once (light, camera, what is banned in frame) and paste them into every prompt.
2. **State the hard constraint in every prompt.** Film 1: black sails, no modern objects, no caps. When a frame breaks it, regenerate that frame; do not hope the video model fixes it.
3. **Stills are cheap, video is not.** Make a photoreal still for every shot before any video. Try several image models on one shot and keep the one that looks like a film, not a 3D render. Film 1 split the stills half Nano Banana, half Cinema Studio.
4. **Match model to subject.** Cinema Studio for ships, hulls, macros. Nano Banana for crowds and interiors with distinct faces. One reference per ship shot keeps the hero object consistent.
5. **Faces must differ.** If every figure is identical, the shot reads as CG. Ask for distinct faces, ages and builds.
6. **Check every still before animating.** Film 1 caught a ghost second sail, a wrong stern ornament, masts with no sails, simplified hulls and a mushy impact. Redo with variants and keep the best.
7. **Animate gently.** Ask for one slow camera move and rigid, plausible motion. Fast, complex motion (many oars in a stroke) smears. A prompt that said the oars never bend or merge, and asked for a moderate pace, fixed it.
8. **Look at several frames per clip,** not one. Make a four-frame contact sheet.
9. **Overlays go in post.** Arrows, dotted routes, labels and grids are added over clean footage.
10. **Sound:** keep the video model's ambient audio. Duck it under narration (Liam, Kokoro am_onyx) when he speaks.
11. **Upscale last.** Topaz Video AI on the clips, per clip rather than on the cut, so cuts do not smear.
12. **Keep the superseded files.** Weak stills and clips go in a `superseded` folder, not the bin.
13. **Credit sources and say it is AI.** Say what the script was adapted from, and that the picture is AI-generated.
14. **Log cost and job IDs** so a shot can be regenerated or used as a reference later.
15. **Narration is fitted to the picture, not the other way round.** Render one Liam line per shot (Kokoro am_onyx, speed 0.95, one pace for the whole film), measure each, and lay them on a timeline: voice starts 0.4 s into its shot, never closer than 0.35 s to the previous line. If a line is longer than its shot, slow that clip by at most 10% (`setpts`), and let the rest spill into the next shot. Film 2: 7 of 25 shots needed it; the voice never lagged its picture by more than 1.8 s.
16. **Level the ambient before ducking it.** Kling clips differ a lot in ambient loudness, so raw ducking leaves some gaps louder than the voice. Even the ambient out first (loudnorm I=-26, LRA 5), then sidechain-compress it under the voice, mix with a fixed gain, and put a limiter on the peaks. Film 2 landed at -16 LUFS, gaps about 5 dB under the speech. A single `loudnorm` over the whole mix pumps the gaps back up. Don't.
17. **Respell unusual words for the voice only.** Kokoro's phonemizer gets Greek terms wrong (trierarch, aphlaston, aulos, diekplous, hypozomata). Give them IPA in a lexicon; captions keep the real spelling.
20. **Characters: give the video model 4 to 5 stills from different angles as references, strip or ban stray background ships, and judge the face on frames across the clip.** Film 3 test: all three video models kept Bear's Aegeus with five references.
19. **Check both ends of the ship.** When the reference hull is asymmetric (curl at the stern only), two of four image models drew a curl at both ends. Compare the ends of the hull with the reference before anything else.
18. **Check `$T[out]` in zsh.** A filter label right after a shell variable is read as an array index. Write `${T}[out]`.
21. **Notes get their own look, and the label sans is Lato Bold.** Filmmaker and reviewer notes are shown as a note card plus a label strip, with Lato Bold for labels (Bear, 2026-11-07, replacing Inter Medium; a first for film labels). Full rule: Brutalist `brutalist.art/CLAUDE.md` rule 12. Paraphrase notes, say whose they are.

## To decide with Bear

- Turn these rules into a skill (his message ended at "Maybe even a ...").
- Whether Galen's scenes get their own folder per film.
