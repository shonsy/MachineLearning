import requests
from lxml import etree
url = 'http://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/stockid/600000/ctrl/1999/displaytype/4.phtml'
r= requests.get(url)
# print(r.text)
s= etree.HTML(r.text)
print(s.xpath('//*[@id="BalanceSheetNewTable0"]/tbody/tr[1]//td/text()'))
# print(s.xpath('//*[@id="BalanceSheetNewTable0"]/tbody/tr[1]/td[3]/text()'))
print

test





