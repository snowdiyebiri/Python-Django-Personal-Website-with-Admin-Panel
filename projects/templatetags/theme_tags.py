from django import template

register = template.Library()

@register.filter
def hex_to_rgb(value):
    """Converts a hex color string to an RGB comma-separated string."""
    value = value.lstrip('#')
    try:
        if len(value) == 3:
            value = ''.join([c*2 for c in value])
        r = int(value[0:2], 16)
        g = int(value[2:4], 16)
        b = int(value[4:6], 16)
        return f"{r}, {g}, {b}"
    except (ValueError, IndexError):
        return "0, 0, 0"
