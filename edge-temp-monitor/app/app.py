from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

LOGFILE = "/home/darensalteruk/scripts/pi-temp.log"

@app.route("/")
def index():
	labels = []
	temps = []

	try:
		with open(LOGFILE) as f:
			lines = f.readlines()[-200:]

			for line in lines:	#Last 200 readings
				line = line.strip()
				
				timestamp, temp = line.split(",")
			
				dt = datetime.strptime(timestamp,"%Y-%m-%d %H:%M:%S")
				labels.append(dt.strftime("%H:%M"))
				temps.append(float(temp))
				# print(labels, temps)
	except FileNotFoundError:
		pass

	return render_template("index.html", labels=labels, temps=temps)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)

