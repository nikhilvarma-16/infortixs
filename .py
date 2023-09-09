from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store messages in memory (replace with a database in production)
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.json.get('message')
    if message:
        messages.append(message)
    return jsonify({"message": "Message sent successfully"})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True)
