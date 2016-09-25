from flask import Flask, request

app = Flask(__name__)

@app.route('/hey/', methods=['GET', 'POST'])
def index():
	print(request.args)
	return "hey girlll".format()

if __name__ == "__main__":
	app.run(debug=True, port=8000)
