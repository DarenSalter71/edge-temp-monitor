from flask import Flask, render_template
from datetime import datetime
from pathlib import Path

import os

app = Flask(__name__)


#--- Reslve Base Directory
#BASE_DIR=Path(__file__).resolve().parent.parent
#DATA_DIR = Path(os.getenv("DATA_DIR", BASE_DIR / "data"))
#DB_PATH = Path(os.getenv("DB_PATH", BASE_DIR / "data" / "temperature.db"))

#print("BASE_DIR : ",BASE_DIR)
#print("DATA_DIR : ",DATA_DIR)
#print("DB_PATH : ",DB_PATH)


#1. Get base folder where this file lives
base_dir = os.path.dirname(os.path.abspath(__file__))

#2. Build path to data folder
data_dir = os.path.join(base_dir,"..","data")

#3. Build data CSV file based on Current Month
current_month = datetime.now().strftime("%Y-%m")
datafile_fname = f"pi-temp-{current_month}.csv"

#4. Add data file to data directory.
datafile=os.path.join(data_dir,datafile_fname)

#5. Number of rows (records) returned 
NO_OF_ROWS = 100 

#6. Grab the CPU "Pi" ID

#7. Grab the Top Process

#Debug ONLY
#print("Current Month : ",current_month)
#print("Data File : ",DATAFILE)

@app.route("/")
def index():
	pi_ids = []
	labels = []
	temps = []
	fan_states = []
	top_processes = []

	try:
		with open(datafile) as f:
			lines = f.readlines()[-NO_OF_ROWS:]

			for line in lines:
				parts = line.strip().split(",")

				if len(parts) >= 2: # Early records do not have pi_id or fan status
					timestamp = parts[0]
					temp = float(parts[1])
					fan =  parts[2] if len(parts) >= 3 else "UNKNOWN FAN STATUS"
					pi_id = parts[3] if len(parts) >= 4 else "UNKNOWN ID"
					top_process = parts[4] if len(parts) >= 5 else "UNKNOWN TOP PROCESS"
				
				dt = datetime.strptime(timestamp,"%Y-%m-%d %H:%M:%S")
				# Build the Data List
				labels.append(dt.strftime("%H:%M"))
				temps.append(float(temp))
				fan_states.append(fan)
				pi_ids.append(pi_id)
				top_processes.append(top_process)

				# print(labels, temps)   #Debug print - comment out if needed.
	except FileNotFoundError:
		pass

	return render_template("index.html",labels=labels,temps=temps,pi_ids=pi_ids,fan_states=fan_states,top_processes=top_processes)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)

