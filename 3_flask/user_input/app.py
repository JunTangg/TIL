from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_stock')
def stock():
    return render_template('search_stock.html')


@app.route('/search_result')
def result():
    print('-------'*5)
    print(request.args)
    return render_template('search_result.html')


if __name__ == '__main__':
    app.run(debug=True)

