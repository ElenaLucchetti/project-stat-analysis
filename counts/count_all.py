from counts.count_analysis import import_data

control_data, depressed_data, control_duration, depressed_duration = import_data()

relevant_feaures = [
    'bac',
    'cry',
    'fil',
    'lau',
    'len',
    'ove',
    'sil'
]


def count_others(data):
    count = 0
    for part in data:
        for line in part:
            feature = line[2]
            if feature not in relevant_feaures:
                if 'exp' not in feature and 'clause' not in feature:
                    print(feature)
                    count += 1
    return count


#control_data = control_data[0]
print("Other for controls: ", count_others(control_data))

#depressed_data = depressed_data[0]
print("Other for depressed: ", count_others(depressed_data))


