import google.generativeai as genai
from google.generativeai import GenerativeModel, configure
from agents.base_agent import BaseAgent
import re

class LogicAgent(BaseAgent):
    def __init__(self, api_key):
        super().__init__("Logic Agent")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def process(self, df, user_query):
        context = f"Columns: {list(df.columns)}\nSample Data:\n{df.head(2).to_string()}"
        
        prompt = f"""
        You are a Data Science Agent. Given the following dataset info, write ONLY the Python code 
        using pandas to perform the user's request. 
        The dataframe is named 'df'.
        
        Dataset Info:
        {context}
        
        User Request: {user_query}
        
        Return only the python code block. Do not include explanations.
        """
        
        response = self.model.generate_content(prompt)
        code = self.clean_code(response.text)
        
        return code

    def clean_code(self, raw_code):
        code = re.sub(r'```python|```', '', raw_code)
        return code.strip()