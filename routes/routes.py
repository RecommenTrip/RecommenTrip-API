from flask import Flask, request, jsonify
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

from services.db_connection.user_connection import UserConnection
from services.recommendations.recommendByUser import RecommendByUser
from services.db_connection.places_connection import PlaceConnection
from services.recommendations.recommendByPlace import RecommendByPlace

app = Flask(__name__)

@app.route('/recommendation', methods=['POST'])
def receive_data():
    data_rec = request.json  # Accessing JSON data sent in the POST request
    # Process the received data here
    # Perform operations with the received_data

    user_connect = UserConnection('datasets/users.csv')
    added_user = user_connect.add_record(data_rec)
    recommend = RecommendByUser()
    k_neighbors = recommend.find_nearest_neighbors()
    print(k_neighbors)
    places = recommend.get_places(recommend.find_nearest_neighbors())
    print(places)

    # Returning a response
    response = {'message': 'Data received successfully', 'data': places}
    return jsonify(response), 200

@app.route('/recommendation_places', methods=['POST'])
def receive_places():
    
    data_rec = request.json

    place_connect = PlaceConnection('datasets/places.csv')
    update_register = place_connect.update_last_row(data_rec)
    recommend = RecommendByPlace()
    k_neighbors = recommend.find_nearest_neighbors()
    places = recommend.get_places(k_neighbors)
    print(f'Os vizinhos são: \n{places}')

    response = {'message': 'Data received successfully', 'data': places}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application
