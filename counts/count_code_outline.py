def import_data():
    """
    for file in directory (60 files = 60 participants):

        - discover whether the file is for "diagnosed" or "control"
        - add participant to appropriate dataset ("diagnosed" or "control")
        - calculate total duration of speech for participant
        - add it to the total duration of the group

    =================================================================================

    Args:
        none

    Return:
        control_data: the collected dataset of control participants. @type array
        depressed_data: the collected dataset of diagnosed participants. @type array
    """


def count_feature(feature, con_data, dep_data, con_duration, dep_duration):
    """
    for each group:
        - count the occurrences of the feature

    compute the total count of feature occurrences

    for each group:
        - compute the expected count of feature occurrences using the total count and durations

    =================================================================================

    Args:
        feature: the feature we want to count (e.g. 'lau'). @type string
        con_data: the dataset of control participants. @type array
        dep_data: the dataset of diagnosed participants. @type array
        con_duration: total time control group spends talking. @type float
        dep_duration: total time diagnosed group spends talking. @type float

    Return:
        observed_f_count: observed feature counts for control and diagnosed groups, [con, diag]. @type array.
        expected_f_count: expected feature counts for control and diagnosed groups, [con, diag]. @type array.
    """


def return_chisquare(observed, expected):
    """
    return the values from the chisquare test

    =================================================================================

    Args:
        observed: observed feature counts for control and diagnosed groups, [con, diag]. @type array.
        expected: expected feature counts for control and diagnosed groups, [con, diag]. @type array.

    Return:
        count_chisquare: values of chisquare and p-value for statistical test, (chisq, p_value). @type tuple
    """