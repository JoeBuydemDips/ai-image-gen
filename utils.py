import streamlit as st
import requests

def get_image_download_link(img_url, filename, text, mime_type="image/png"):
    response = requests.get(img_url)
    response.raise_for_status()
    st.download_button(label=text, data=response.content, file_name=filename, mime=mime_type)
