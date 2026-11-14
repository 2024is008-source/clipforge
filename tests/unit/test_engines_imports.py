"""Verify domain engine packages import cleanly and expose core contracts."""
import unittest


class TestEngineModuleBoundaries(unittest.TestCase):
    def test_engine_packages_expose_public_apis(self):
        import engines.video as video
        import engines.vision as vision
        import engines.audio as audio
        import engines.tracking as tracking
        import engines.rendering as rendering

        self.assertTrue(callable(video.decide_scene_layouts))
        self.assertTrue(callable(video.tune_edits))
        self.assertTrue(callable(vision.get_detection_service))
        self.assertTrue(callable(vision.get_segmentation_service))
        self.assertTrue(callable(audio.validate_transcript_words))
        self.assertTrue(callable(tracking.analyze_video_with_openshorts))
        self.assertTrue(callable(rendering.run_render))
        self.assertTrue(callable(rendering.detect_encoder))
        self.assertTrue(callable(rendering.validate_render))


if __name__ == "__main__":
    unittest.main()
