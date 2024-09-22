from flask import Flask, jsonify, request
from src import LeitnerSystem  # Import your Python Leitner system

app = Flask(__name__)

# Create a new instance of LeitnerSystem
leitner = LeitnerSystem()

@app.route('/')
def index():
    return "Leitner System API"

# Endpoint to add a new card
@app.route('/add_card', methods=['POST'])
def add_card():
    data = request.json
    question = data['question']
    answer = data['answer']
    # Add the card to the Leitner system
    leitner.add_card(question, answer)
    return jsonify({"message": "Card added successfully"})

# Endpoint to review a box
@app.route('/review_box/<int:box_id>', methods=['GET'])
def review_box(box_id):
    result = leitner.review_box(box_id)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
