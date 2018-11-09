from bs4 import BeautifulSoup
import requests
import json
import MySQLdb as mdb

def main():
	conn = mdb.connect('localhost','root','1105boty','scrap')
	cur = conn.cursor()
	#keyword = input("keyword > ")
	base_url = "https://www.bukalapak.com/c/komputer/laptop?search%5Bfilter_attr%5D%5Bbrand%5D%5B%5D=Asus"
	r = requests.get(base_url)
	#print(r.text)
	soup = BeautifulSoup(r.text, "lxml")
	all_product = soup.find_all('div', class_="product-card")
	for item in all_product:
		#if len(item) <= 6:
		data = {}
		#nama produk
		product_name = item.find("a",{"class":"product__name"})
		product_name = product_name.text
		data['product_name'] = product_name

		#harga produk
		product_price = item.find("span", {"class":"amount"})
		product_price = product_price.text
		data['product_price'] = "Rp " + product_price

		#rating produk
		product_rating = item.find("span",{"class":"rating__star"})
		try:
			product_rating = product_rating.text
			data['product_rating'] = product_rating
		except:
			data['product_rating'] = 0

			#review produk
		product_review = item.find("a",{"class":"review_aggregate"})
		try:
			product_review = product_review.text
			data['product_review'] = product_review
		except:
			data['product_review'] = 0
		'''result disimpan pada file json'''
		#jso = json.dumps(data)
		#with open("result.json","a") as f:
		#	f.writelines("%s" % item for item in jso +",\n")
		'''result disimpan pada database'''
		sql = "INSERT INTO `result`(`product_name`,`product_price`,`product_rating`,`product_review`) VALUES ('{}','{}','{}','{}')".format(data['product_name'],data['product_price'],data['product_rating'],data['product_review'])
		#try:
		cur.execute(sql)
		print("sukses")
		conn.commit()
		#finally:
		#conn.close() 		
			 
		


if __name__ == '__main__':
	main()