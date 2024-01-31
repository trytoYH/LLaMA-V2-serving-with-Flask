from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def llmama_server(question):
    data = {
        "prompt" : question,
        "n_predict" : 128
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post("http://localhost:8080/completion", json=data, headers=headers)
    answer = response.json().get("content", "API 응답 없음")

    return jsonify({"answer" : answer})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/model_output', methods=['POST'])
def model_output():
    if request.method == 'POST':
        qusetion = request.form['question']
        answer = llmama_server(qusetion)
        return answer

if __name__ == '__main__':
    app.run(debug=True)  