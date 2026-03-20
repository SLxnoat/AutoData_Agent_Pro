from agents.base_agent import BaseAgent 
import pandas as pd

class ProfilerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Data Profiler")
        
    def process(self, df):
        
        report = {
            "num_rows": len(df),
            "num_columns": len(df.columns),
            "column_names": df.columns.tolist(),
            "data_types": df.dtypes.astype(str).to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
            "unique_values": {col: df[col].nunique() for col in df.columns},
            "duplicates" : int(df.duplicated().sum()),
            "shape" : df.shape
        }
        
        insights = []
        for col, null in report["missing_values"].items():
            if null > 0:
                percent = (null / len(df)) * 100
                insights.append(f"Column '{col}' has {null} missing ({percent:.1f}%) values.")
        
        return report, insights