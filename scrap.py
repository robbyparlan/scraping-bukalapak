from bs4 import BeautifulSoup
import requests
import pandas as pd 

keyword = input(" > ")
url = requests.get("https://www.bukalapak.com/products?utf8=✓&source=navbar&from=omnisearch&page=2&search_source=omnisearch_organic&search%5Bhashtag%5D=&search%5Bkeywords%5D="+keyword)
url = url.text
soup = BeautifulSoup(url, "lxml")
produk = soup.find_all("li","col-12--2")
nama_produk = []
harga_produk = []
for p in produk:
		nama = p.find('a','product__name line-clamp--2 js-tracker-product-link qa-list').get_text()
		harga = p.find("span","amount positive").get_text()
		nama_produk.append(nama)
		harga_produk.append(int(harga.replace(".","")))
'''result disimpan pada file csv'''
produk_dict = {"nama":nama_produk,"harga":harga_produk}
df = pd.DataFrame(produk_dict,columns = ["nama","harga"])
df.sort_values('harga',ascending=True)
df.to_csv("result1.csv",sep=",")