from docutils import nodes
from docutils.statemachine import ViewList
from sphinx.util.compat import Directive
from sphinx.util.docstrings import prepare_docstring
from sphinx.util.nodes import nested_parse_with_titles

tpl_package_info_table = """\
+------------+----------------+
| title      | value          |
+============+================+
| replace    | replace        |
+------------+----------------+
"""


class BaseDirective(Directive):

    def _rest2node(self, rest, container=None):
        """ creates a docutils node from some rest-markup
        """
        vl = ViewList(prepare_docstring(rest))
        if container is None:
            node = nodes.container()
        else:
            node = container()
        nested_parse_with_titles(self.state, vl, node)
        return node


class InfoTableDirective(BaseDirective):
    """creates an table with information from setup.py
    """
    def run(self):
        """a table containing base package info

        returns a list of nodes (in this case one node)
        """
        dummy_value = {'foo', 'bar', 'willi', 'wonka'}
        table = self._rest2node(tpl_package_info_table)
        for key, value in dummy_value.items():
            table.children[0].children[0].children[5].append(
                self._make_row(key, value)
            )
        return [table]

    def _make_row(self, key, value):
        table = self._rest2node(tpl_package_info_table)
        row = table.children[0].children[0].children[5].children[0]
        row[0].children = [nodes.paragraph(text=key)]
        row[1].children = [nodes.paragraph(text=value)]
        return row
