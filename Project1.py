import streamlit as st
from google.api_core import retry
import google.generativeai as palm

# API key configuration
API_KEY = 'AIzaSyBu7_sdYybqqY86rt_XUMg91GpKWcMr5w8'
palm.configure(api_key=API_KEY)

# List available models
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]

# Select a model
model_bison = models[0]

# Retry decorator
@retry.Retry()
def generate_text(prompt, model=model_bison, temperature=0.0):
    return palm.generate_text(prompt=prompt, model=model, temperature=temperature)

# Streamlit web app
st.title("SaM-GPT")

# Get user input
prompt = st.text_input("Enter your prompt:")

# Generate text on button click
if st.button("Generate Text"):
    if prompt:
        st.text("Generating...")
        completion = generate_text(prompt)
        st.success("Generated Text:")
        st.write(completion.result)
    else:
        st.warning("Please enter a prompt.")

# # Display model information
# st.subheader("Selected Model:")
# st.write(f"Name: {model_bison.name}")
# st.write(f"Description: {model_bison.description}")
#
# # Display other available models
# st.subheader("Available Models:")
# for m in models:
#     st.write(f"Name: {m.name}")
#     st.write(f"Description: {m.description}")
#     st.write(f"Supported Generation Methods: {m.supported_generation_methods}")
#     st.write("---")
