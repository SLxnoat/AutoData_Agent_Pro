from agents.base_agent import BaseAgent
import pandas as pd

class CleanerAgent(BaseAgent):
    def __init__(self):
        super().__init__("CleanerAgent")
    
    def process(self, df):
        cleaned_df = df.copy()
        action_taken = []
        
        initial_shape = cleaned_df.shape
        cleaned_df = cleaned_df.dropna()
        
        if cleaned_df.shape [0] < initial_shape[0]:
            action_taken.append(f"Removed {initial_shape[0] - cleaned_df.shape[0]} completely empty rows.")
            
        for col in cleaned_df.columns:
            null_count = cleaned_df[col].isnull().sum()
            if null_count > 0:
                if pd.api.types.is_numeric_dtype(cleaned_df[col]):
                    median_value = cleaned_df[col].median()
                    cleaned_df[col] = cleaned_df[col].fillna(median_value)
                    action_taken.append(f"Filled {null_count} missing values in '{col}' with median ({median_value}).")
                
                else:
                    cleaned_df[col] = cleaned_df[col].fillna("Unknown")
                    action_taken.append(f"Filled {null_count} missing values in '{col}' with 'Unknown'.")
                    
        return cleaned_df, action_taken