# What is installed locally and how to call it

Checked 2026-11-06 on Bear's Mac (darwin, zsh).

## Executive summary

- Video upscaling is **Topaz Video AI**, installed, working, no extra login needed from the shell. Use its own ffmpeg for `tvai_up`, then pipe into Homebrew ffmpeg to encode.
- Generation is **Higgsfield through MCP** (images, Kling 4.0 video). Editing and assembly is **Homebrew ffmpeg**. Narration is **Kokoro am_onyx** (Liam), free.

## Topaz Video AI

- App: `/Applications/Topaz Video AI.app` (also `Topaz Photo AI.app`, `Topaz Video.app`).
- Binaries: `/Applications/Topaz Video AI.app/Contents/MacOS/ffmpeg` and `ffprobe`. Filters: `tvai_up` (upscale), `tvai_fi` (frame interpolation), `tvai_stb` (stabilize), `tvai_pe`, `tvai_cpe`.
- Models: `/Applications/Topaz Video AI.app/Contents/Resources/models` (154 files, includes `auth.tpz`). Before calling, export `TVAI_MODEL_DIR` and `TVAI_MODEL_DATA_DIR` to that folder.
- Its ffmpeg has **no libx264**. Encode with `prores_ks` (files are huge: 3 s of 4K ProRes HQ = 255 MB) or, better, write `-f yuv4mpegpipe -` and pipe into `/opt/homebrew/bin/ffmpeg` with libx264.
- Tested: `-vf "tvai_up=model=prob-4:scale=2:blend=0.2"` took a 1928x1072 clip to 3856x2144; 3 s took 19 s. Roughly 6 s of compute per second of footage.
- Script: scratchpad `assemble4k.sh` (upscale each clip, normalize to 3840x2160 at 24 fps, concatenate, fade). Copy it into this folder if it proves good.
- Right for photographic or photoreal footage. Wrong for flat vector art, where it degrades the image (see [brutalist.art/RENDER-4K-AND-UPLOAD.md](https://github.com/nikbearbrown/brutalist.art/blob/main/RENDER-4K-AND-UPLOAD.md)).

## Higgsfield (MCP)

- Server id d1912725-aecd-497b-a1dd-81c518cc5d49. Tools: `generate_image(_batch)`, `generate_video(_batch)`, `jobs_wait`, `media_upload` + `media_confirm`, `models_explore`.
- Batches and waits are capped at 12 items. Prior job IDs can be used as reference media. Upload URLs expire after 24 h.
- Models used: `nano_banana_2_1` (crowds, interiors, multi-reference), `cinematic_studio_2_5` (ships, hulls, macros), `gpt_image_2_6` (cheap tests), `kling4_0` (image-to-video, 1080p, 3 to 30 s, outputs an AAC ambient track).
- Costs seen: stills 2 to 4 credits each at 2k and 4k; Kling 6 s about 19.5, 10 s about 32.5 credits. Whole film 1 about 1,000 credits.

## Other

- ffmpeg and ffprobe: `/opt/homebrew/bin`. Python with PIL for contact sheets (use `python3 -I` for scripts that only need the standard library and PIL).
- Narration: Liam, Kokoro `am_onyx`, rules in the Brutalist toolkit (`books/CLAUDE.md`). Not re-asked.
- YouTube: token in `books/youtube/credentials/nikbearbrown` (local, not on GitHub) (channel UCg0cw2ouRhQ8dr114yGp0mA). Upload quota 100 per day. Descriptions cannot contain angle brackets. Needs plain `python3`, not `-I`.
- macOS screenshot names contain U+202F before AM or PM; use globs, never typed names.
