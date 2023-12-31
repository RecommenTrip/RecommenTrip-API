import pandas as pd

class UserConnection:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_record(self, data_dict):
        try:
            # Convert the dictionary to a DataFrame
            new_record_df = pd.DataFrame([data_dict])

            # Append the new record to the CSV file
            new_record_df.to_csv(self.file_path, mode='a', header=False, index=False)

            places_df = pd.read_csv('datasets/places.csv')
            print(len(places_df))
            # Add a row of zeros to the CSV file
            zeros_df = pd.DataFrame([[0] * len(places_df.columns)])
            zeros_df.to_csv('datasets/places.csv', mode='a', header=False, index=False)

            return True  # Indicates successful addition
            
            
        except Exception as e:
            print(f"Error: {e}")
            return False  # Indicates failure