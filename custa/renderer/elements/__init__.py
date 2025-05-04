from custa.renderer.elements.text import TextRenderer
from custa.renderer.elements.button import ButtonRenderer
from custa.renderer.elements.hr import HrRenderer
from custa.renderer.elements.section import SectionRenderer
from custa.renderer.elements.headings import HeadingRenderer

from custa.renderer.elements.nav.navbar import NavbarRenderer
from custa.renderer.elements.nav.nav_button import NavButtonRenderer
from custa.renderer.elements.nav.nav_footer import NavFooterRenderer

renderers = {
    "nav_bar": NavbarRenderer(),
    "nav_button": NavButtonRenderer(),
    "nav_footer": NavFooterRenderer(),

    "h1": HeadingRenderer(),
    "h2": HeadingRenderer(),
    "h3": HeadingRenderer(),

    "hr": HrRenderer(),

    "text": TextRenderer(),
    "button": ButtonRenderer(),
    "section": SectionRenderer(),
}
