from flask import Flask, request, render_template

app = Flask(__name__)

eeg_array = []

@app.route('/', methods=['GET', 'POST'])
def index():

	if(any(request.args) != False):
		eeg_array.append("{}, {}, {}, {}".format(request.args['ch1'],
			 request.args['ch2'],
			 request.args['ch3'],
			 request.args['ch4']
		))

		return render_template('hello.html', eeg_array=eeg_array[0].split(","))
	return render_template('hello.html', eeg_array=eeg_array[-12:])

if __name__ == "__main__":
	app.run(debug=True, server='0.0.0.0')
