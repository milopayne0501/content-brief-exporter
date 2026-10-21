import unittest
from export_brief import render_brief


class RenderBriefTests(unittest.TestCase):
    def setUp(self):
        self.brief = {
            'title': 'Gold Tips', 'platform': 'TikTok',
            'audience': 'Beginners', 'key_points': ['Check purity'],
            'call_to_action': 'Follow us'
        }

    def test_expected_output(self):
        result = render_brief(self.brief)
        self.assertIn('# Gold Tips', result)
        self.assertIn('- Check purity', result)
        self.assertIn('## Call to Action', result)

    def test_missing_field(self):
        del self.brief['title']
        with self.assertRaisesRegex(ValueError, 'Missing required field: title'):
            render_brief(self.brief)

    def test_invalid_points(self):
        self.brief['key_points'] = []
        with self.assertRaisesRegex(ValueError, 'key_points'):
            render_brief(self.brief)

    def test_wrong_root_type(self):
        with self.assertRaisesRegex(ValueError, 'JSON object'):
            render_brief([])


if __name__ == '__main__':
    unittest.main()
