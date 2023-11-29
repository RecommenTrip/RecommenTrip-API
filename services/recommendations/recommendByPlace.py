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

