from iexfinance.stocks import Stock
import pprint

pp = pprint.PrettyPrinter()

TOKEN = 'pk_76304d9f19524ea6986767564e6c69bb'
aapl = Stock('FB', token=TOKEN)
data = aapl.get_quote()
# print(aapl.get_quote())
pp.pprint(data)
print(data['companyName'], data['latestPrice'])
