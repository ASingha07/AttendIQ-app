import base64
from pathlib import Path

import streamlit as st


ASSETS_DIR = Path(__file__).parent.parent.parent / "assets"


@st.cache_data
def get_image_base64(filename: str) -> str:
    image_path = ASSETS_DIR / filename
    return base64.b64encode(image_path.read_bytes()).decode()


# This is use for HTML img tag
def image_html(filename: str, style: str = "height:100px") -> str:
    encoded = get_image_base64(filename)
    ext = Path(filename).suffix.lstrip(".")
    return f"<img src='data:image/{ext};base64,{encoded}' style='{style}' />"


# This is use for streamlit st.image function
def show_image(filename: str, width: int = 100, custom_style: str = ""):
    encoded = get_image_base64(filename)
    ext = Path(filename).suffix.lstrip(".")

    base_style = f"width:{width}px;"
    final_style = f"{base_style} {custom_style}".strip()
    
    html_str = f"<img src='data:image/{ext};base64,{encoded}' style='{final_style}' />"
    st.markdown(html_str, unsafe_allow_html=True)