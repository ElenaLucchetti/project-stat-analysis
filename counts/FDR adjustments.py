 from counts.count_analysis import import_data
from counts.count_analysis import count_feature
from counts.count_analysis import return_chisquare
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

control_data, depressed_data, control_duration, depressed_duration = import_data()

for feature in features:
    obs, exp = count_feature(feature, control_data, depressed_data, control_duration, depressed_duration)
    pvalue = return_chisquare(obs, exp)[1]
    pvalues[feature] = pvalue

pvalues = {feature: pvalues[feature] for feature in pvalues.keys() if pvalues[feature] < 0.05}
sorted_pvalues = sorted(pvalues.items(), key=operator.itemgetter(1))
test_count = len(features)

thresholds = {}

for i in range(len(pvalues)):
    threshold = ALPHA * (i+1) / test_count
    thresholds[sorted_pvalues[i][0]] = threshold

for feature, pvalue in sorted_pvalues:
    print('{0} {1} -- threshold: {2}'.format(feature, pvalue, thresholds[feature]))
