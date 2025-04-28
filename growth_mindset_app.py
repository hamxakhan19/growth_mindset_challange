# growth_mindset_app_advanced.py

import streamlit as st
import random

# -------------- Setup --------------
st.set_page_config(page_title="🌱 Growth Mindset Challenge", page_icon="🌟", layout="centered")

# -------------- Title --------------
st.title("🌱 Growth Mindset Challenge")
st.caption("Develop. Adapt. Thrive. 🚀")

# -------------- Introduction --------------
st.header("What is a Growth Mindset? 🌱")
st.write("""
A **growth mindset** means believing that your **abilities** and **intelligence** can grow through **effort**, **learning**, and **persistence**.
Popularized by psychologist **Carol Dweck**, it teaches us that **challenges are opportunities** to become better.
""")

# -------------- Expandable: Why Growth Mindset? --------------
with st.expander("🌟 Why Adopt a Growth Mindset?"):
    st.markdown("""
    - **Embrace Challenges**: Obstacles are learning opportunities.
    - **Learn from Mistakes**: Every mistake teaches something new.
    - **Persist Through Difficulties**: Tough times build strength.
    - **Celebrate Effort**: Effort matters more than outcomes.
    - **Stay Curious**: An open mind grows faster.
    """)

# -------------- Expandable: How to Practice? --------------
with st.expander("🚀 How Can You Practice a Growth Mindset?"):
    st.markdown("""
    - **Set Learning Goals**, not just performance goals.
    - **Reflect** on both successes and failures.
    - **Seek Feedback** and use it to improve.
    - **Stay Positive** and believe in your potential.
    """)

# -------------- Quotes Carousel --------------
st.subheader("🎯 Motivational Quotes")

quotes = [
    "“It's not that I'm so smart, it's just that I stay with problems longer.” – Albert Einstein",
    "“Challenges are what make life interesting; overcoming them is what makes life meaningful.” – Joshua Marine",
    "“Failure is so important. It is the ability to resist failure or use failure that often leads to greater success.” – J.K. Rowling",
    "“Success is the ability to go from one failure to another with no loss of enthusiasm.” – Winston Churchill",
    "“The only limit to our realization of tomorrow is our doubts of today.” – Franklin D. Roosevelt"
]

if st.button("🌟 Inspire Me!"):
    st.info(random.choice(quotes))

# -------------- Small Quiz --------------
st.subheader("🧠 Quick Quiz: Do You Have a Growth Mindset?")

score = 0

q1 = st.radio("1. When you face a challenge, you:", 
              ["Give up quickly", "See it as a chance to grow"])
if q1 == "See it as a chance to grow":
    score += 1

q2 = st.radio("2. If you fail a test, you:", 
              ["Think you're not smart", "Review mistakes and try again"])
if q2 == "Review mistakes and try again":
    score += 1

q3 = st.radio("3. You believe that talent is:", 
              ["Fixed", "Developed through practice"])
if q3 == "Developed through practice":
    score += 1

# Quiz result
if st.button("🚀 Submit Answers"):
    if score == 3:
        st.success("🌟 Awesome! You have a strong Growth Mindset!")
    elif score == 2:
        st.warning("✨ Good! You’re developing a Growth Mindset.")
    else:
        st.error("💡 Keep working on it! Growth is a journey.")

# -------------- Footer --------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Believe in Your Potential 🌟")
