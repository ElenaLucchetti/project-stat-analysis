def import_data():
    """
    for file in directory (60 files = 60 participants):

        - discover whether the file is for "diagnosed" or "control"
        - add participant to appropriate dataset ("diagnosed" or "control")

    ===============================================================================

    Args:
        none

    Return:
        control_data: the collected dataset of control participants. @type array
        depressed_data: the collected dataset of diagnosed participants. @type array
        control_duration: total time control group spends talking. @type float
        depressed_duration: total time diagnosed group spends talking. @type float
    """


def durations_feature(feature, con_data, dep_data):
    """
    for each group:
        - filter data by feature
        - get list of feature durations (tmax - tmin)

    ================================================================================

    Args:
        feature: the feature we want to count (e.g. 'lau'). @type string
        con_data: the dataset of control participants. @type array
        dep_data: the dataset of diagnosed participants. @type array

    Return:
        con_durations: list of all durations for the selected feature as they
                        appear in the control dataset. @type array
        dep_durations: list of all durations for the selected feature as they
                        appear in the diagnosed dataset. @type array
    """


def return_t(control, depressed):
    """
    return the values from the t-test

    ================================================================================

    Args:
        control: list of all durations for the selected feature as they
                    appear in the control dataset. @type array
        depressed: list of all durations for the selected feature as they
                        appear in the diagnosed dataset. @type array
    Return:
        duration_t: values of student's t and p-value for statistical test, (t, p_value). @type tuple
    """


def get_duration_list(data):
    """
    for a set of data, compute and return the feature duration and append it to a list

    ================================================================================

    Args:
        data: the (filtered) dataset from which to compute durations. @type array

    Return:
        durations: the compiled list of durations from the dataset. @type list

    """
