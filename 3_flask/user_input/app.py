from flask import Flask, render_template, request
from iexfinance.stocks import Stock


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_stock')
def stock():
    return render_template(
        'search_stock.html',
        is_first_search=True,
    )


@app.route('/search_result')
def result():
    user_input = request.args.get('keyword')        # request.args['keyword']로 할 수도 있지만, 해당경우 keyword가 없으면 오류발생 => 서버 다운
    TOKEN =

    stock = Stock(user_input, token=TOKEN)

    try:
        data = stock.get_quote()
    except:
        return render_template(
            'search_stock.html',
            is_success=False,
        )
    # print(data['companyName'], data['latestPrice'])

    return render_template(
        'search_stock.html',
        is_success=True,
        c_name=data['companyName'],
        l_price=data['latestPrice'],
    )


if __name__ == '__main__':
    app.run(debug=True)

