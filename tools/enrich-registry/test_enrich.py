import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("enrich.py")
SPEC = importlib.util.spec_from_file_location("enrich_registry", SCRIPT)
enrich = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(enrich)


class SelectFeaturesTests(unittest.TestCase):
    def test_short_description_is_expanded_to_preview_contract(self):
        with tempfile.TemporaryDirectory(dir=enrich.ROOT) as directory:
            bundle_dir = Path(directory)
            (bundle_dir / "tool.md").write_text(
                "---\ntitle: v0\ndescription: Source-aware guidance for v0.\n---\n# v0\n",
                encoding="utf-8",
            )

            features = enrich.select_features(bundle_dir, "tools")

        self.assertEqual(len(features), 1)
        self.assertGreaterEqual(len(features[0]["description"]), 30)
        self.assertIn("evidence and review boundaries", features[0]["description"])


if __name__ == "__main__":
    unittest.main()
