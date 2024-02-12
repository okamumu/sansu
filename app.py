from flask import Flask, render_template, request
app = Flask(__name__)

import sansuu
import random

@app.route('/tashisan1')
def show_tashisan1():
    num = request.args.get('num', default=10, type=int)
    seed = request.args.get('seed', default=random.seed(), type=int)
    problems = sansuu.tashisan1(num, seed)
    return render_template('keisan1.html', problems=problems, seed=seed)

@app.route('/hikisan1')
def show_hikisan1():
    num = request.args.get('num', default=10, type=int)
    seed = request.args.get('seed', default=random.seed(), type=int)
    problems = sansuu.hikisan1(num, seed)
    return render_template('keisan1.html', problems=problems, seed=seed)

@app.route('/kakesan1')
def show_kakesan1():
    num = request.args.get('num', default=10, type=int)
    seed = request.args.get('seed', default=random.seed(), type=int)
    problems = sansuu.kakesan1(num, seed)
    return render_template('keisan1.html', problems=problems, seed=seed)

@app.route('/warisan1')
def show_warisan1():
    num = request.args.get('num', default=10, type=int)
    seed = request.args.get('seed', default=random.seed(), type=int)
    problems = sansuu.warisan1(num, seed)
    return render_template('keisan1.html', problems=problems, seed=seed)

if __name__ == '__main__':
    app.run(debug=True)
