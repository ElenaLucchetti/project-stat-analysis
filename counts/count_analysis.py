from scipy import stats
import numpy as np
import os
import csv

path = '/home/elena/Downloads/Uni/Year 4/IndividualProject/Elena-transcriptions/Elena-transcriptions'


def import_data():
    control_data = []
    depressed_data = []

    control_duration = 0
    depressed_duration = 0

    for filename in os.listdir(path):
        full_file_path = '{0}/{1}'.format(path, filename)
        with open(full_file_path, "rt", encoding="ISO-8859-1") as f:
            reader = csv.reader(f, delimiter=",")

            if filename[0] == 'C':  # control participants
                part_data = np.array(list(reader))
                control_data += [part_data]  # keep data separate by participant
                control_duration += float(part_data[-1][-1])    # the final max time is the total duration
            elif filename[0] == 'P':  # diagnosed participants
                part_data = np.array(list(reader))
                depressed_data += [part_data]  # keep data separate by participant
                depressed_duration += float(part_data[-1][-1])

    print("Control duration: {0}\nDiagnosed duration: {1}".format(control_duration,depressed_duration))

    return control_data, depressed_data, control_duration, depressed_duration


def count_feature(feature, con_data, dep_data, con_duration, dep_duration):
    con_data = np.concatenate(con_data)  # use concatenate instead of array to put all data together
    dep_data = np.concatenate(dep_data)  # use array to keep participants separate

    # filter by feature
    con_data_f = con_data[np.where(con_data[:, 2] == feature)]
    dep_data_f = dep_data[np.where(dep_data[:, 2] == feature)]

    # count feature for each group
    con_f_count = con_data_f.shape[0]
    dep_f_count = dep_data_f.shape[0]
    print('Control observed feature count {0}\nDiagnosed observed filler count {1}\n\n'.format(
        con_f_count, dep_f_count)
    )
    tot_f = con_f_count + dep_f_count
    observed_f_count = [con_f_count, dep_f_count]

    # expected feature count for each group
    con_exp_f = tot_f * (con_duration / (con_duration + dep_duration))
    dep_exp_f = tot_f * (dep_duration / (dep_duration + con_duration))
    expected_f_count = [con_exp_f, dep_exp_f]
    print('Control expected feature count {0}\nDiagnosed expected filler count {1}\n\n'.format(
        con_exp_f, dep_exp_f)
    )

    return observed_f_count, expected_f_count

def return_chisquare(observed, expected):
    # null hypothesis: Diagnosed patients and control patients use feature with the same frequency
    count_chisquare = stats.chisquare(observed, f_exp=expected)

    return count_chisquare
  