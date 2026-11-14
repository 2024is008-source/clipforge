"""ClipForge Audio Processing, Faster-Whisper Transcription & Active-Speaker Attribution Engine."""
from local_worker.whisper_engine import WhisperEngine
from local_worker.transcript_validator import validate_transcript_words
from local_worker.speaker_priority import attribute_Active_speakers if hasattr(__import__("local_worker.speaker_priority"), "attribute_Active_speakers") else __import__("local_worker.speaker_priority").speaker_priority.attribute_windows

__all__ = ["WhisperEngine", "validate_transcript_words"]
