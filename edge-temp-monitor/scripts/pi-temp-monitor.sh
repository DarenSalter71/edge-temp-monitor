#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LOGFILE="$SCRIPT_DIR/../data/pi-temp-$(date +%Y-%m).csv"

THRESHOLD=60 # Default threshold temperature (60c)
FAN="OFF"  # Default fan settng : OFF.

PI_ID=$(cat /proc/cpuinfo | grep Serial | awk '{print $3}')

TOP_PROCESS=$(ps -eo comm,%cpu --sort=-%cpu | awk 'NR==2 {print $1 " (" $2 "%)"}')

TIMESTAMP="$(date '+%Y-%m-%d %H:%M:%S')"

#echo "Writing to DIR : $SCRIPT_DIR"
#echo "Writing to : $LOGFILE"
#echo "PI_ID is $PI_ID"
#echo "Timestamp is $TIMESTAMP"
echo "Top Process is : $TOP_PROCESS"

# Get Temperature
TEMP=$(vcgencmd measure_temp | grep -o  '[0-9]*\.[0-9]*')

# Set Fan Status
if (( $(echo "$TEMP >= $THRESHOLD" | bc -l) )) ; then
   FAN="ON"
else
   FAN="OFF"
fi

# Log Temperature, dates and fan status
#echo "$(date '+%Y-%m-%d %H:%M:%S'),${TEMP},${FAN}" >> $LOGFILE
echo "$TIMESTAMP,$TEMP,$FAN,$PI_ID,$TOP_PROCESS" >> "$LOGFILE"

# Convert to Integer for  Comparison
TEMP_INT=${TEMP%.*}

#Run Comparison

if [ "$TEMP_INT" -ge "$THRESHOLD" ]; then
   echo "$(date) WARNING WILL ROBINSON: Pi CPU Temperature is $TEMP(c)"
fi
