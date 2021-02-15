import requests
from tabulate import tabulate

#assign date and currency base that you need

date="2010-01-15"
base="EUR"

r=requests.get(
    f"https://api.exchangeratesapi.io/{date}", params={"base":base}
)
r.raise_for_status()
print(r.status_code)

dict_day=r.json()
dict_rates=dict_day["rates"]

columns=["Currency", "Exchange Rate (base "+base+")"]
table_list=[]
for key, value in dict_rates.items():
    line=[str(key), str(value)]
    table_list.append(line)


with open("rates.html", "w") as f:
    f.write("<html>")
    f.write("<body>")
    f.write(tabulate(table_list, headers=columns, tablefmt="html", stralign="center"))
    f.write("</body>")
    f.write("</html>")
