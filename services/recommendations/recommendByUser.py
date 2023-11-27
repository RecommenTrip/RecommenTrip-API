import pandas as pd
import numpy as np
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

class RecommendByUser:

    def find_nearest_neighbors(self, k=4):
        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv('datasets/users.csv')

            # Extract values from the last record for specific columns
            last_record_values = df[['idade', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']].iloc[-1].values

            # Calculate Euclidean distance between new record and existing records
            df['euclidean_distance'] = np.linalg.norm(df[['idade', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']].values - last_record_values, axis=1)

            # Get k records with shortest Euclidean distance (excluding the last record)
            nearest_neighbors = df.nsmallest(k, 'euclidean_distance')

            # Return a list of indices of the nearest neighbors
            return nearest_neighbors.index.tolist()[1:]
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def get_places(self, neighbor_ids, threshold=0):
        # Read the CSV file into a pandas DataFrame
        data = pd.read_csv('datasets/places.csv')
        
        df_places = data.loc[neighbor_ids]
        
        df_places['e'] = df_places.gt(0).dot(df_places.columns + ',').str[:-1]

        print(len(df_places['e']))

        all_places = ','.join(df_places['e'].tolist())

        unique_places = set(all_places.split(','))

        unique_places_list = list(unique_places)

        return unique_places_list
        