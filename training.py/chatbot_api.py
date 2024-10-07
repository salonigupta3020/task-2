from flask import Flask, request, jsonify
from gpt2_generator import generate_article_gpt2
from bert_generator import generate_article_bert
from T5_generator import generate_article_t5

app = Flask(__name__)

@app.route('/generste', methods=['POST'])
def generate_article():
    date = request.json
    model = date.get('model', 'gpt2')
    prompt = date.get('prompt', ' ')

    if model == 'gpt2':
        article = generate_article_gpt2(prompt)
    elif model == 'bert':
        article = generate_article_bert(prompt)
    elif model == 't5':
        article = generate_article_t5(prompt)
    else:
        return jsonify({"error": "Invalid model selected"}), 400

    return jsonify({"article": article})

if __name__ == '__main__':
    app.run(debug=True)       