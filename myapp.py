from flask import Flask, render_template, request
import difflib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    similarity = None

    if request.method == 'POST':
        code1 = request.form['code1']
        code2 = request.form['code2']
        similarity = difflib.SequenceMatcher(None, code1, code2).ratio() * 100

    return render_template('index.html', similarity=similarity)

if __name__ == '__main__':
    print("RUNNING MYAPP FILE")
    app.run(debug=True)