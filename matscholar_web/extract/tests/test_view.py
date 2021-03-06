import matscholar_web.extract.view as msweb_eview
from matscholar_web.tests.util import MatScholarWebBaseTest

"""
Tests for the extract app view.
"""

# Functions to exclude from this test
EXCLUDE = ["highlight_entities_html"]


class TestExtractViews(MatScholarWebBaseTest):
    def test_extract_view(self):
        self.run_test_for_all_functions_in_module(msweb_eview, EXCLUDE)

    def test_highlight_entities_html(self):
        f = msweb_eview.highlight_entities_html
        example_1 = [[["PbTe", "MAT"], ["is", "O"]], [["cool", "O"]]]
        example_2 = [[["testing", "APL"]]]
        examples = [example_1, example_2]
        arg_combos = [(e,) for e in examples]
        self.run_test_for_individual_arg_combos(f, arg_combos)
