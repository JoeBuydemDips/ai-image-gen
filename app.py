import streamlit as st
import replicate
import os
import requests
from io import BytesIO

# Set up the page configuration (must be the first Streamlit command)
st.set_page_config(page_title="AI Image Generator", layout="wide")

# Function to download image
def get_image_download_link(img_url, filename, text):
    response = requests.get(img_url)
    img = BytesIO(response.content)
    st.download_button(label=text, data=img, file_name=filename, mime="image/png")

# Initialize session state
if 'generated_image_url' not in st.session_state:
    st.session_state.generated_image_url = None

# Sidebar for inputs
with st.sidebar:
    st.title("AI Image Generator")
    st.write("Generate amazing images using AI!")

    api_key = st.text_input("Enter your Replicate API key:", type="password")
    if api_key:
        os.environ["REPLICATE_API_TOKEN"] = api_key

    prompt = st.text_area("Enter your prompt:", "A beautiful landscape with mountains and a lake", height=150)
    aspect_ratio = st.selectbox("Choose aspect ratio:", ["1:1", "16:9", "4:3", "3:2"])
    output_format = st.selectbox("Choose output format:", ["webp", "png", "jpg"])
    output_quality = st.slider("Output quality:", 1, 100, 80)
    safety_tolerance = st.slider("Safety tolerance:", 1, 5, 4)
    prompt_upsampling = st.checkbox("Enable prompt upsampling", value=True)

    generate_button = st.button("Generate Image")

# Main area for displaying the image
if generate_button:
    if "REPLICATE_API_TOKEN" not in os.environ:
        st.error("Please enter your Replicate API key in the sidebar.")
    else:
        try:
            with st.spinner("Generating image..."):
                output = replicate.run(
                    "black-forest-labs/flux-1.1-pro",
                    input={
                        "prompt": prompt,
                        "aspect_ratio": aspect_ratio,
                        "output_format": output_format,
                        "output_quality": output_quality,
                        "safety_tolerance": safety_tolerance,
                        "prompt_upsampling": prompt_upsampling
                    }
                )
                
                # Store the generated image URL in session state
                st.session_state.generated_image_url = output
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Display the generated image if available
if st.session_state.generated_image_url:
    st.image(st.session_state.generated_image_url, caption=f"Generated Image: {prompt}", use_column_width=True)
    
    # Add download button
    get_image_download_link(st.session_state.generated_image_url, f"generated_image.{output_format}", "Download Image")

# Add a footer
st.markdown("---")
st.write("Created with ❤️ using Streamlit and Replicate API")