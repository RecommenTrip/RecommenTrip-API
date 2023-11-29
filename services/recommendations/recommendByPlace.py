import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class RecommendByPlace:
    def find_nearest_neighbors(self, k=3):
        df = pd.read_csv('datasets/places.csv')

        # Get the last row as the reference row for comparison
        reference_row = df.iloc[-1:].values.reshape(1, -1)

        # Exclude the last row for comparison
        data = df.iloc[:-1].values

        # Calculate cosine similarity between the last row and other rows
        similarities = cosine_similarity(reference_row, data)

        # Get indices of k nearest neighbors
        nearest_indices = similarities.argsort(axis=1)[0][-k:][::-1]

        return nearest_indices
    
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

    
