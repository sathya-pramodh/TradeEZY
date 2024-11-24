from flask import Flask, jsonify, request
from rag.langchain_loader import generate_data_store
from rag.query_data import generate_answer

app = Flask(__name__)


@app.route("/api/load-data", methods=["POST"])
def load_data():
    try:
        # Check if files are included in the request
        if 'files' not in request.files:
            return jsonify({'error': 'No files part in the request'}), 400

        # Get the uploaded files from the frontend
        uploaded_files = request.files.getlist('files')  # Get multiple files if sent

        # Call the generate_data_store script with uploaded files
        generate_data_store(uploaded_files=uploaded_files)
        
        return jsonify({'result': 'Data has been loaded and processed successfully.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route("/api/answer", methods=["POST"])
def get_answer():
    try:
        # Get the data from the request
        data = request.json
        if not data or 'prompt' not in data or 'userID' not in data:
            return jsonify({'error': 'Missing prompt or userID in request body'}), 400
        
        prompt = data['prompt']
        user_id = data['userID']

        # Call the generate_answer function
        answer = generate_answer(user_id=user_id, prompt=prompt)

        if not answer:
            return jsonify({'error': 'No answer could be generated'}), 500

        return jsonify({'answer': answer}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)