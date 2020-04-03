from counts.count_analysis import import_data
from counts.count_analysis import count_feature
from counts.count_analysis import return_chisquare

control_data, depressed_data, control_duration, depressed_duration = import_data()
observed, expected = count_feature('lau', control_data, depressed_data, control_duration, depressed_duration)
chisquare = return_chisquare(observed, expected)

print(chisquare)
