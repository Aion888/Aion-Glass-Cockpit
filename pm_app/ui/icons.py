from dash_iconify import DashIconify

# Single source of truth for icon usage across the app
ICON_SET = "lucide"  # keep one set for consistent look

def icon(name: str, size: int = 18, rotate: int = 0):
    """
    Usage: icon("activity") -> lucide:activity
    """
    return DashIconify(icon=f"{ICON_SET}:{name}", width=size, height=size, rotate=rotate)
