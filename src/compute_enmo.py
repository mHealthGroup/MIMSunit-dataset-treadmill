
from glob import glob
import os
import re
from subprocess import call
import pandas as pd
import sys

enmo_script = sys.argv[1]

csv_files = glob('../data/*RAW_2g.sensor.csv')
for csv in csv_files:
	print(csv)
	if 'TAS' in csv:
		gr = 2
		sr = 100
	elif 'CLE' in csv:
		gr = 2
		sr = 80

	if 'TAS' in csv and 'Waist' in csv and '2017-03-22' in csv and 'TT2' in csv:
		sr = 80
	
	if 'TAS' in csv and 'Wrist' in csv and '2017-03-22' in csv and 'TT2' in csv:
		sr = 80
	# para_file = csv.replace('.csv', 'Calibration.csv')
	print(gr)
	print(sr)
	# print(os.path.exists(para_file))

	call(['python', enmo_script, '-range', str(gr), '-sr', str(sr), csv])

	# convert to mhealth feature file
	print("convert to mhealth feature file")
	enmo_input_file = csv.replace('.csv', 'Epoch.csv')
	enmo_output_file = csv.replace('.sensor.csv', '-enmo.feature.csv')
	enmo_df = pd.read_csv(enmo_input_file)
	enmo_df = enmo_df.iloc[:,[0, 1]]
	enmo_df.columns = ['HEADER_TIME_STAMP', 'ENMO']
	enmo_df.to_csv(enmo_output_file, float_format='%.3f', index=False)
	