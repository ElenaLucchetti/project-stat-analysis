# Individual-Project
Scripts used to conduct a statistical analysis on the corpus of data of control / diagnosed patients

The directories "counts" and "durations" contain the analyses on frequency and duration respectively.
Each of these directories contains:
* The function definitions needed for data analysis
* The analysis run on each of the 7 selected features (back-channerl, cry, fillers, laughter, lengthenings, overlap, silences).
* False Discovery Rate (FDR) adjustments of the findings
* A file containing the description of each defined function

The directory "tests" contains all the unit test written for the analysis.



**NOTE** run the command

`$ pip install -r requirements.txt`

to install requirements
