from custa.renderer.elements.text import TextRenderer
from custa.renderer.elements.button import ButtonRenderer
from custa.renderer.elements.hr import HrRenderer
from custa.renderer.elements.section import SectionRenderer
from custa.renderer.elements.headings import HeadingRenderer

from custa.renderer.elements.nav.navbar import NavbarRenderer
from custa.renderer.elements.nav.nav_button import NavButtonRenderer
from custa.renderer.elements.nav.nav_footer import NavFooterRenderer

from custa.renderer.elements.tables.table import TableRenderer
from custa.renderer.elements.tables.thead import TheadRenderer
from custa.renderer.elements.tables.tbody import TbodyRenderer
from custa.renderer.elements.tables.tr import TrRenderer
from custa.renderer.elements.tables.th import ThRenderer
from custa.renderer.elements.tables.td import TdRenderer

from custa.renderer.elements.lists.list import ListRenderer
from custa.renderer.elements.lists.item import ItemRenderer
from custa.renderer.elements.lists.term import TermRenderer
from custa.renderer.elements.lists.desc import DescRenderer

renderers = {
    # Navbar
    "navbar": NavbarRenderer(),
    "nav_button": NavButtonRenderer(),
    "nav_footer": NavFooterRenderer(),

    # Table
    "table": TableRenderer(),    
    "thead": TheadRenderer(),
    "tbody": TbodyRenderer(),
    "tr": TrRenderer(),
    "th": ThRenderer(),
    "td": TdRenderer(),

    # List
    "list": ListRenderer(),
    "item": ItemRenderer(),
    "term": TermRenderer(),
    "desc": DescRenderer(),

    "h1": HeadingRenderer(),
    "h2": HeadingRenderer(),
    "h3": HeadingRenderer(),

    "hr": HrRenderer(),

    "text": TextRenderer(),
    "button": ButtonRenderer(),
    "section": SectionRenderer(),
}
