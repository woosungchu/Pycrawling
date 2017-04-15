from urllib import request

google_stock_url = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=2&b=15&c=2017&d=3&e=15&f=2017&g=d&ignore=.csv'

def down_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    str_csv = str(csv)
    lines = str_csv.split("\\n")

    dest_url = r'google.csv' #r = raw
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line+ "\n")
    fx.close()

down_stock_data(google_stock_url)
