from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'utils/index.html')


def artii(request, keyword):
    import art
    result = art.text2art(keyword, 'random')
    context = {
        'result': result,
        'keyword': keyword,
    }
    return render(request, 'utils/artii.html', context)


def stock_input(request):
    return render(request, 'utils/stock_input.html')


def stock_output(request):
    from iexfinance.stocks import Stock
    conpany_code = request.GET.get('company_code')
    TOKEN = 'pk_76304d9f19524ea6986767564e6c69bb'  # https://iexcloud.io/console/tokens

    try:
        stock = Stock(conpany_code, token=TOKEN)
        data = stock.get_quote()
    except:
        return render(request, 'utils/stock_output.html', {
            'is_ok': False,
            'message': '검색할 수 없습니다',
        }
        )
    # print(data['companyName'], data['latestPrice'])

    return render(request, 'utils/stock_output.html', {
        'is_ok': True,
        'data': data
    }
    )


    print(f'==========={request.POST.get("compony_code")}==========')
    return render(request, 'utils/stock_output.html')


