# MIMS unit treadmill dataset

This dataset includes data of treadmill walking and running from 10 participants wearing Actigraph devices (Some with GT3X+ and others with GT9X) on non dominant wrist and dominant waist.

## files in the data folder

1. `sessions.csv`

This file includes the corresponding sensor file (based on date in the file name), the time segmentation of walking and running episodes of differrent speeds for each participant.

2. `*RAW.csv(.gz)`

These files are the raw accelerometer data files stored in Actigraph csv format. If it ends with `.gz`, please decompress the file at first.

3. `*RAW.sensor.csv`

These files are the raw accelerometer data files stored in mhealth format.

4. `*RAW.sensorEpoch.csv`

These files are the processed ENMO values.

5. Other files

Intermediate files when generating ENMO values.

## Generate Actigraph count and MIMS unit value

Please use Actilife software and `*RAW.csv` files to generate actigraph counts.  
Please use MIMSunit R package and `*RAW.sensor.csv` files to generate MIMS unit values.

You may then use the information in the `sessions.csv` file to find out the corresponding ENMO, actigraph counts and MIMS unit values for walking and running of different speeds for each participant.
