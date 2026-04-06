#!/usr/bin/env bash

LOGFILE="/home/darensalteruk/scripts/logs/pi-temp-$(date +%Y-%m).log"
THRESHOLD=60

# Get Temperature
TEMP=$(vcgencmd measure_temp | grep -o  '[0-9]*\.[0-9]*')

# Log Temperature
echo "$(date '+%Y-%m-%d %H:%M:%S'),${TEMP}" >> $LOGFILE

# Convert to Integer for  Comparison
TEMP_INT=${TEMP%.*}

#Run Comparison

if [ "$TEMP_INT" -ge "$THRESHOLD" ]; then
   echo "$(date) WARNING WILL ROBINSON: Pi CPU Temperature is ${TEMP}(c)"
fi
