import streamlit as st

# Set page config
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌷🧠", layout="centered", initial_sidebar_state="auto")

# Title Section
st.markdown("<h1 style='text-align: center;'>🌷🧠 Growth Mindset Challenge!</h1>", unsafe_allow_html=True)

# (Optional) Image Section
# st.image("your_image_path.png", use_column_width=True, caption="Growth Mindset")

# Welcome Message
st.markdown("## 🙌🏼 Welcome to Your Growth Journey!")
st.write(
    "Aims to help individuals develop a positive attitude toward challenges and learning through interactive exercises and reflections."
    " It encourages continuous improvement by fostering resilience, persistence, and self-belief 💪🏼."
)

# Growth Mindset Quote
st.markdown("## 🧑🏻‍🏫 Growth Mindset Quote")
st.success(
    "Success is born from failure, and growth thrives in the face of both. 🛡️ "
    "Every setback teaches us a lesson, and every victory fuels our journey forward."
)

# Challenge Section
st.markdown("## ⚡ What challenge do you have today?")
challenge = st.text_input("Tell me about the challenge you are dealing with:")

st.button("Share the challenge you faced when getting started! ⚖️")

# Reflection Section
st.markdown("## 💡 Reflect on What You Have Learned!")
reflection = st.text_area("Tell your reflections here:")

# Achievement Section
st.markdown("## 🏆 Acknowledge Your Achievements!")
achievement = st.text_input("Share something you have achieved recently:")

st.info("No matter the size, every achievement matters. Share one with us 🤩")

# Upload Section
st.markdown("## 📤 Upload Your File")
st.write("Please upload a CSV file")

uploaded_file = st.file_uploader("Drag and drop file here or browse", type=['csv'])

# Footer
st.write("---")
st.caption(
    "Keep faith in your abilities, growth is a journey, not something you just reach 👊🏿"
)
if st.button("Looking For More Inspiration 🌻"):
    st.balloons()

st.markdown("<p style='text-align: center;'>📍 Created by Saba Ali Zain</p>", unsafe_allow_html=True)
