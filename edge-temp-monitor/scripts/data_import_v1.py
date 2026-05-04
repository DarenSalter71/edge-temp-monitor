#!/usr/bin/env python3

import csv
import sqlite3
import argparse
from pathlib import Path
import os

#--- Import Temperature CSV Data Script ---
#--- V1.0 ---

#--- Reslve Base Directory
BASE_DIR=Path(__file__).resolve().parent.parent
DATA_DIR = Path(os.getenv("DATA_DIR", BASE_DIR / "data"))
DB_PATH = Path(os.getenv("DB_PATH", BASE_DIR / "data" / "temperature.db"))

#Debug Only
print("BASE_DIR : ",BASE_DIR)
print("DATA_DIR : ",DATA_DIR)
print("DB_PATH : ",DB_PATH)


#--- Process each row / record
def prepare_row(row):
   return (
       row[0],            #Timestamp
       float(row[1]),     #Temperature
       row[3],            #Pi ID
       row[4],            #Process
       row[2]             #Fan Status
   )


#--- Core Import Logic ---
def import_csv_to_db(input_file, db_path):
   conn=sqlite3.connect(db_path)
   cursor = conn.cursor()

   # Create table if it doesnt already exist
   cursor.execute("""
      CREATE TABLE IF NOT EXISTS temperature_logs (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         timestamp TEXT,
         temperature REAL,
         pi_id TEXT,
         process TEXT,
         fan_status TEXT
         )
      """)

   BATCH_SIZE=1024
   batch=[]

   with open(input_file, newline="") as csvfile:
      reader=csv.reader(csvfile) # List
         
      for row in reader:
         parsed = prepare_row(row)
         batch.append(parsed)

         if len(batch) >= BATCH_SIZE:
            cursor.executemany("""
               INSERT INTO temperature_logs (timestamp, temperature, pi_id,process,fan_status)
               VALUES (?,?,?,?,?)
            """, batch)
            batch.clear()
   if batch:
      cursor.executemany("""
         INSERT INTO temperature_logs (timestamp, temperature, pi_id,process,fan_status)
         VALUES (?,?,?,?,?)
      """, batch)
      batch.clear()
             
      conn.commit()
      conn.close()

# --- Entry Point ---
if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Import CSV Data into SQLite DB")
   parser.add_argument(
      "--input",
      required=True,
      help="Path to input CSV file"
   )
   parser.add_argument(
      "--db",
      default=DB_PATH,
      help="Path to SQLite database (optional)"
   )

   args=parser.parse_args()

   input_path=Path(args.input)
   db_path=Path(args.db)

   if not input_path.exists():
      print(f"Error: Input file does not exist: {input_path}")
      exit(1)

   print(f"Importing {input_path} into {db_path} .")
   import_csv_to_db(input_path, db_path)
   print("Import Completed.")


