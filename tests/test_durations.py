import unittest
import numpy as np
from durations.duration_analysis import import_data
from durations.duration_analysis import get_duration_list


class TestDataDurationAnalysis(unittest.TestCase):

    def test_import_control_data(self):
        control_data = np.array([
            ['line', 'subject', 'tier2', 'tier3', 'tier1', 'tmin', 'tmax'],
            ['1', 'CF61WOM_47', 'noise', '?', '{noise}', '0', '1.375'],
            ['2', 'CF61WOM_47', 'clause1_exp-s1', 'exp', '"allora parlaci un poco di te e della tua famiglia?" ', '1.375', '4.046'],
            ['3', 'CF61WOM_47', 'sil_exp', '?', '(.)_exp', '4.046', '4.214'],
            ['4', 'CF61WOM_47', 'clause2_exp-s1', 'exp', '"quanti componenti sono" ', '4.214', '5.469'],
            ['5', 'CF61WOM_47', 'clause3_exp-s1', 'exp', '"e cosa fa"', '5.469', '5.867'],
            ['6', 'CF61WOM_47', 'ove', '?', '[]', '5.867', '6.137'],
            ['7', 'CF61WOM_47', 'clause1-s1', 'sub', 'quindi', '6.137', '6.633']
        ])

        imported_control_data, imported_depressed_data = import_data()
        np.testing.assert_array_equal(control_data, imported_control_data[0][:8])

    def test_import_depressed_data(self):
        depressed_data = np.array([
            ['line', 'subject', 'tier2', 'tier3', 'tier1', 'tmin', 'tmax'],
            ['1', 'PM33ATR_66', 'noise', '?', '{noise}', '0', '1.739'],
            ['2', 'PM33ATR_66', 'clause1_exp-s1', 'exp', '"raccontamo un po\' come"', '1.739', '3.059'],
            ['3', 'PM33ATR_66', 'len', 'f', ':::e', '3.059', '3.375'],
            ['4', 'PM33ATR_66', 'fil', '?', ':m', '3.375', '4.046'],
            ['5', 'PM33ATR_66', 'clause1_exp-s2', '?', '"hai passato quest\'ultima settimana"', '4.046', '5.727'],
            ['6', 'PM33ATR_66', 'silV-s', '?', '(.)v', '5.727', '6.659'],
            ['7', 'PM33ATR_66', 'clause1-s1', 'sub', "allora quest ultima settimana l'ho passata", '6.659', '9.187']
        ])

        imported_control_data, imported_depressed_data = import_data()
        np.testing.assert_array_equal(depressed_data, imported_depressed_data[0][:8])

    def test_get_duration_list(self):
        data = [
            ['1', 'CF61WOM_47', 'sil', '?', '{noise}', '0', '1.375'],
            ['2', 'CF61WOM_47', 'clause1_exp-s1', 'exp', '"allora parlaci un poco di te e della tua famiglia?" ', '1.375', '4.046'],
            ['3', 'CF61WOM_47', 'sil', '?', '(.)_exp', '4.046', '4.214']
        ]

        real_durations = [1.375, 2.671, 0.168]
        print(get_duration_list(data))

        np.testing.assert_almost_equal(real_durations, get_duration_list(data), 2)
