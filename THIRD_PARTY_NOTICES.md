# ClipForge Studio — Ownership & Runtime Notices

**ClipForge Studio** is designed, engineered, and maintained by **Minuja Ranthika Amarasekara** (`https://github.com/2024is008-source/clipforge`).

- **Copyright**: (c) 2026 Minuja Ranthika Amarasekara. All rights reserved.
- **Core Modules by Minuja Ranthika Amarasekara**:
  - ClipForge Reframe Engine v2 (Speaker tracking, camera smoothing, split-screen & 3-up grid layout, and active-speaker attribution in `local_worker/` and `src/lib/reframe.ts`).
  - ClipForge Caption & Overlay Engine (Word-level subtitle animation curves, phrase pagination, contextual emoji triggers, and PNG/ASS rendering in `src/lib/subtitles.ts`, `src/lib/render.ts`, and `local_worker/rendering/`).
  - ClipForge 5-Key Gemini Pool & Local Viral Discovery Ranker (`local_worker/gemini_pool.py`, `src/lib/ai.functions.ts`, `src/lib/local-worker.ts`).

---

## Runtime Libraries & Models Used via Standard Dependencies

### 1. faster-whisper / CTranslate2
- **License**: MIT License
- **Description**: Local speech-to-text inference runtime invoked by `local_worker/whisper_engine.py`.

### 2. Meta AI SAM 2 (Optional)
- **License**: Apache License 2.0
- **Description**: Optional video segmentation predictor adapter in `local_worker/segmentation_service.py`.

### 3. Ultralytics YOLO
- **License**: AGPL-3.0 / Enterprise
- **Description**: Local object detection and pose estimation runtime in `local_worker/detection_service.py`.

### 4. OpenCV & YuNet ONNX
- **License**: Apache License 2.0 / MIT
- **Description**: Video frame decoding and face detection model in `local_worker/`.

### 5. Montserrat Font
- **License**: SIL Open Font License 1.1
- **Description**: Primary display typography used for caption rendering and studio UI.
