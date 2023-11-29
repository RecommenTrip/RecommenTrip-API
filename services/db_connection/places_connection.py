import pandas as pd

class PlaceConnection:
    def __init__(self, file_path):
        self.file_path = file_path

    def update_last_row(self, search_string):
        df = pd.read_csv(self.file_path)

        if search_string in df.columns:
            last_row_index = df.index[-1]
            df.loc[last_row_index, search_string] += 1

            df.to_csv(self.file_path, index=False)
            return f"Updated last row in '{search_string}' column."
        else:
            return f"No column named '{search_string}' found."
