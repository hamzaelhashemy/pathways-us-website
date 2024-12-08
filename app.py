from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').lower()

    # Basic bot logic
    if "hello" in user_message:
        reply = "Hi there! How can I assist you today?"
    elif "help" in user_message:
        reply = "Sure! I'm here to answer your questions. Ask me anything!"
    elif "bye" in user_message:
        reply = "Goodbye! Have a great day!"
    else:
        reply = "I'm not sure how to respond to that. Could you try rephrasing?"

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
