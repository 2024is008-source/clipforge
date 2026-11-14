"""ClipForge Audio Processing, Faster-Whisper Transcription & Active-Speaker Attribution Engine."""
from local_worker.whisper_engine import WhisperEngine
from local_worker.transcript_validator import validate_and_normalize_transcript
from local_worker.speaker_priority import evaluate_speaker_priority

__all__ = ["WhisperEngine", "validate_and_normalize_transcript", "evaluate_speaker_priority"]
