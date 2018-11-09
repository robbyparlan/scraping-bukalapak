from flask import Flask, jsonify
from bs4 import BeautifulSoup
import MySQLdb as mdb

app = Flask(__name__)

@app.route('/test')
def test():
	conn = mdb.connect('localhost','root','1105boty','scrap')
	cur = conn.cursor(mdb.cursors.DictCursor)
	sql = "SELECT `product_name`,`product_price`,`product_rating`,`product_review` FROM `result`"
	cur.execute(sql)
	conn.commit()
	result = cur.fetchall()
	print(result[2]['product_name'])
	return jsonify({"Result":{"data":result}})
		
if __name__ == '__main__':
	app.run(debug=True)