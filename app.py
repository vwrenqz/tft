from flask import Flask, render_template, request
from classical_methods import methods

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html')

@app.route('/calculate', methods=["GET", "POST"])
def calculate():
	if request.method == "POST":
		angle_phi = float(request.form["angle_phi"])
		method = request.form["method"]
		if method in methods:
			results = methods[method](angle_phi)
			return render_template('index.html', results=results)
		else:
			return "Invalid method", 400
	return render_template('index.html')

if __name__ == "__main__":
	app.run(host="127.0.0.1", port=8080)