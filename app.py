import streamlit as st
from utils.data_handler import load_data
from agents.profiler_agent import ProfilerAgent

st.set_page_config(page_title="AutoData Agent Pro", layout="wide")
st.title("🤖 AutoData Agentic Pipeline")

uploaded_file = st.file_uploader("Upload your Dataset (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file:
    df = load_data(uploaded_file)
    
    if isinstance(df, str):
        st.error(df)
    else:
        st.success("File uploaded successfully!")
        st.dataframe(df.head(), use_container_width=True)
        
        if st.button("🚀 Start Profiling"):
            # Profiler Agent ව පාවිච්චි කරනවා
            profiler = ProfilerAgent()
            report, insights = profiler.process(df)
            
            st.subheader("🕵️ Profiler Agent Insights")
            for item in insights:
                st.info(item)
            
            st.json(report)