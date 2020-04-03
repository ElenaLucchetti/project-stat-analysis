from durations.duration_analysis import import_data
from durations.duration_analysis import durations_feature
from durations.duration_analysis import return_t
import operator

ALPHA = 0.05

features = [
    'bac',
    'cry',
    'fil',
    'lau',
    'len',
    'ove',
    'sil'
]

pvalues = {}

control_data, depressed_data = import_data()

for feature in features:

    con, dep = durations_feature(feature, control_data, depressed_data)

    if not con or not dep:
        continue
    pvalue = return_t(con, dep)[1]
    pvalues[feature] = pvalue

pvalues = {feature: pvalues[feature] for feature in pvalues.keys() if pvalues[feature] < ALPHA}
sorted_pvalues = sorted(pvalues.items(), key=operator.itemgetter(1))
test_count = len(features)

thresholds = {}

for i in range(len(pvalues)):
    threshold = ALPHA * ((i+1) / test_count)
    thresholds[sorted_pvalues[i][0]] = threshold

for feature, pvalue in sorted_pvalues:
    print('{0} {1} -- threshold: {2}'.format(feature, pvalue, thresholds[feature]))
