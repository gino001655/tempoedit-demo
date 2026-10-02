from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.meta = {}
        self.h1_count = 0
        self.title_parts = []
        self.text_parts = []
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            self.ids.add(attributes["id"])
        if tag == "link":
            self.links.append(attributes)
        if tag == "meta":
            key = attributes.get("name") or attributes.get("property")
            if key:
                self.meta[key] = attributes.get("content", "")
        if tag == "h1":
            self.h1_count += 1
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        text = data.strip()
        if not text:
            return
        self.text_parts.append(text)
        if self._in_title:
            self.title_parts.append(text)


class TempoEditSiteTests(unittest.TestCase):
    def parse_page(self):
        self.assertTrue(INDEX.is_file(), "index.html must exist at the repository root")
        source = INDEX.read_text(encoding="utf-8")
        parser = SiteParser()
        parser.feed(source)
        return source, parser

    def test_identity_and_social_metadata_are_complete(self):
        _, parser = self.parse_page()
        title = "TempoEdit | Training-Free Temporal Audio Editing"
        description = (
            "TempoEdit explores training-free temporal audio editing with "
            "pretrained text-to-audio models."
        )
        self.assertEqual("".join(parser.title_parts), title)
        self.assertEqual(parser.meta.get("description"), description)
        self.assertEqual(parser.meta.get("og:title"), title)
        self.assertEqual(parser.meta.get("og:description"), description)
        self.assertEqual(
            parser.meta.get("og:url"),
            "https://gino001655.github.io/tempoedit-demo/",
        )
        self.assertEqual(parser.meta.get("og:type"), "website")
        self.assertEqual(parser.meta.get("twitter:card"), "summary")
        self.assertEqual(parser.h1_count, 1)

    def test_research_content_is_semantic_and_honest(self):
        source, parser = self.parse_page()
        visible_text = " ".join(parser.text_parts)
        self.assertTrue({"overview", "approach", "status"}.issubset(parser.ids))
        for expected in (
            "Chih-Yao Chen",
            "Department of Electrical Engineering",
            "National Taiwan University",
            "Ongoing Research Project",
            "Relocate",
            "Extend",
            "Shorten",
        ):
            self.assertIn(expected, visible_text)
        for forbidden in (
            "TBD",
            "TODO",
            "PLACEHOLDER",
            "DATASET OR BENCHMARK",
            "PRIMARY METRIC",
        ):
            self.assertNotIn(forbidden, source)

    def test_local_assets_work_under_a_github_project_path(self):
        _, parser = self.parse_page()
        stylesheets = [
            link.get("href", "")
            for link in parser.links
            if "stylesheet" in link.get("rel", "").split()
        ]
        self.assertEqual(stylesheets, ["style.css"])
        self.assertFalse(stylesheets[0].startswith("/"))
        canonical = [
            link.get("href", "")
            for link in parser.links
            if "canonical" in link.get("rel", "").split()
        ]
        self.assertEqual(
            canonical,
            ["https://gino001655.github.io/tempoedit-demo/"],
        )


if __name__ == "__main__":
    unittest.main()
