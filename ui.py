import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="AI Youtube Video Analyzer",
    page_icon="🎥",
    layout="wide"
)

st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:800;
    color:#ff4b4b;
}

.sub-title{
    text-align:center;
    color:#9ca3af;
    font-size:18px;
    margin-bottom:30px;
}

.stButton>button{
    width:100%;
    height:50px;
    border-radius:12px;
    font-size:18px;
    font-weight:600;
}

.result{
    border:1px solid #333;
    border-radius:12px;
    padding:20px;
}

</style>
""", unsafe_allow_html=True)

with st.sidebar:

    st.title("🎯 AI Youtube Video Analyzer")

    st.markdown("---")

    st.markdown("""
### Features

- 📚 Complete Video Analysis
- ⏱ Smart Timestamps
- 🎯 Key Topics
- 📝 Detailed Summary
- 🤖 AI Powered
""")

    st.markdown("---")

    st.warning("""
**⚠️ Note**

- AI-generated analysis may contain mistakes or inaccuracies. Please verify important information before relying on it.
- This application currently uses a **free API tier**, so the quality, speed, and completeness of responses may be limited compared to premium AI models.
""")

st.markdown(
    '<div class="main-title">🎥 AI Youtube Video Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Analyze any YouTube video with AI and get structured insights in seconds.</div>',
    unsafe_allow_html=True
)

url = st.text_input(
    "YouTube Video URL",
    placeholder="https://www.youtube.com/watch?v=..."
)

if st.button("🚀 Analyze Video"):

    if not url.strip():
        st.warning("Please enter a YouTube video URL.")

    else:

        with st.spinner("Analyzing video..."):

            try:

                agent = build_youtube_agent()

                response = agent.run(
                    f"Analyze this YouTube video:\n{url}"
                )

                st.success("Analysis Complete")

                st.markdown("---")

                if hasattr(response, "content"):
                    st.markdown(response.content)
                else:
                    st.markdown(str(response))

            except Exception as e:
                st.error(str(e))