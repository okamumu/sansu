from flask import Flask, render_template
app = Flask(__name__)

import warisan

@app.route('/')
def hello_world():
    problems = warisan.gen_warisan()
    return render_template('index.html', problems = problems)

if __name__ == '__main__':
    app.run(debug=True)
