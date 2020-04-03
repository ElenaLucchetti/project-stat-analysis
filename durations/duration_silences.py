from durations.duration_analysis import import_data
from durations.duration_analysis import durations_feature
from durations.duration_analysis import return_t

control_data, depressed_data = import_data()
control, expected = durations_feature('sil', control_data, depressed_data)

if not control or not expected:
    print("Analysis not run due to lack of feature instances")
else:
    stud_t = return_t(control, expected)
    print(stud_t)
