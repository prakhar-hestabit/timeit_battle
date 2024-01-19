from battle_time import BattleTime as bt

def prak(x):
    if x:
        a = 2
    else:
        a = 1
    return a


def sug(x):
    if not x:
        a = 1
    else:
        a = 2
    return a


# Define test cases as a list of values
test_cases = [0, "some_value", None, True, "", 7]

# Create an instance of BattleTime
comparator = bt.BattleTime(func1=prak, func2=sug, test_cases=test_cases)
comparator.compare_and_plot()

