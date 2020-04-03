from scipy import stats
import numpy as np
import os
import csv

path = '/home/elena/Downloads/Uni/Year 4/IndividualProject/Elena-transcriptions/Elena-transcriptions'


def import_data():
    control_data = []
    depressed_data = []

    for filename in os.listdir(path):
        full_file_path = '{0}/{1}'.format(path, filename)
        with open(full_file_path, "rt", encoding="ISO-8859-1") as f:
            reader = csv.reader(f, delimiter=",")

            if filename[0] == 'C':  # control participants
                part_data = np.array(list(reader))
                control_data += [part_data]  # keep data separate by participant
            elif filename[0] == 'P':  # diagnosed participants
                part_data = np.array(list(reader))
                depressed_data += [part_data]  # keep data separate by participant

    return control_data, depressed_data


def durations_feature(feature, con_data, dep_data):
    con_data = np.concatenate(con_data)  # use concatenate instead of array to put all data together
    dep_data = np.concatenate(dep_data)  # use array to keep participants separate

    # filter by feature
    con_data_f = con_data[np.where(con_data[:, 2] == feature)]
    dep_data_f = dep_data[np.where(dep_data[:, 2] == feature)]

    if con_data_f.size == 0 or dep_data_f.size == 0:
        print("No instances of {} in one of the groups".format(feature))
        return None, None

    # list of durations for each group
    con_f_durations = get_duration_list(con_data_f)
    dep_f_durations = get_duration_list(dep_data_f)

    print('Control {0} duration mean: {1}\nDiagnosed {0} duration mean: {2}'.format(
        feature, np.mean(con_f_durations), np.mean(dep_f_durations))
    )

    print('Control {0} duration variance: {1}\nDiagnosed {0} duration variance: {2}'.format(
        feature, np.var(con_f_durations), np.var(dep_f_durations))
    )
    return con_f_durations, dep_f_durations


def return_t(control, depressed):
    # null hypothesis: Diagnosed patients and control patients use feature with similar durations
    duration_t = stats.ttest_ind(control, depressed)
    return duration_t


def get_duration_list(data):
    durations = []

    for entry in data:
        start = float(entry[-2])
        end = float(entry[-1])
        duration = end - start
        durations += [duration]

    return durations
