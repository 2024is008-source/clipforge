# ClipForge Studio

**Author:** Minuja Ranthika Amarasekara ([2024is008-source](https://github.com/2024is008-source/clipforge))

GPU-accelerated AI short-form video clipping, active-speaker tracking, adaptive 9:16 reframing (`fill`, `split`, `grid3`, `editorial`, `fit`), dynamic animated captions, and native FFmpeg NVENC/CPU mastering.

## Quick Start (Windows)

Run the one-command launcher from the repository root:

```cmd
run.bat
```

Available launcher options:
- `run.bat --check` — Verify Node, Python, worker packages, FFmpeg, and port availability.
- `run.bat --stop` — Stop running local worker and studio background processes.
- `run.bat --restart` — Cleanly restart the local worker and studio.

See [`docs/SETUP_GUIDE.md`](docs/SETUP_GUIDE.md) for CUDA, Faster-Whisper, YOLOv8, and optional SAM 2 setup details.

## Manual Development

```sh
npm install
python -m pip install -r local_worker/requirements.txt

# Terminal 1: Local FastAPI + FFmpeg/CUDA worker (http://127.0.0.1:8765)
python -m local_worker.main

# Terminal 2: Frontend studio (http://localhost:8080)
npm run dev
```

## Verification

```sh
python -m pytest local_worker/tests
npx vitest run
npx tsc --noEmit
npm run build
```

## Documentation & Notices

- Setup Guide: [`docs/SETUP_GUIDE.md`](docs/SETUP_GUIDE.md)
- Licensing Report: [`docs/LICENSING_REPORT.md`](docs/LICENSING_REPORT.md)
- Project & Third-Party Notices: [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)

## Copyright

Copyright (c) 2026 Minuja Ranthika Amarasekara. All rights reserved.
