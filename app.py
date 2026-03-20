import streamlit as st
from utils.data_handler import load_data
from agents.profiler_agent import ProfilerAgent
from agents.cleaner_agent import CleanerAgent

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
            profiler = ProfilerAgent()
            report, insights = profiler.process(df)
            
            st.subheader("🕵️ Profiler Agent Insights")
            for item in insights:
                st.info(item)
            
            st.json(report)
if st.button("🧼 Start Cleaning"):
    cleaner = CleanerAgent()
    cleaned_df, actions = cleaner.process(df)
    
    st.subheader("🧼 Cleaner Agent Action Log")
    for action in actions:
        st.write(f"- {action}")
        
    st.success("Data cleaning complete!")
    st.dataframe(cleaned_df.head(), use_container_width=True)
    
    csv = cleaned_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        "📥 Download Cleaned CSV",
        csv,
        "cleaned_data.csv",
        "text/csv"
    )