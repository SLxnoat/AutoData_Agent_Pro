import pandas as pd

def load_data(file):
    try:
        # Streamlit file object එකේ නම (filename) බලන්න .name පාවිච්චි කරනවා
        file_name = file.name
        
        if file_name.endswith('.csv'):
            return pd.read_csv(file)
        elif file_name.endswith(('.xls', '.xlsx')):
            return pd.read_excel(file)
        else:
            return "Error: Unsupported file format."
    except Exception as e:
        return f"Error: {str(e)}"