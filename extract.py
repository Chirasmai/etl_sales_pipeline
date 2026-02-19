import pandas as pd

def extract_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("✅ Data extracted successfully")
        print("Rows:", df.shape[0])
        print("Columns:", df.shape[1])
        return df
    except Exception as e:
        print("❌ Error in extraction:", e)
