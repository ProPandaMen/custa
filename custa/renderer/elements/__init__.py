from custa.renderer.elements.text import render_text
from custa.renderer.elements.section import render_section
from custa.renderer.elements.headings import render_heading
from custa.renderer.elements.hr import render_hr
from custa.renderer.elements.button import render_button

renderers = {
    "text": render_text,
    "section": render_section,
    "h1": render_heading,
    "h2": render_heading,
    "h3": render_heading,
    "hr": render_hr,
    "button": render_button,
}
