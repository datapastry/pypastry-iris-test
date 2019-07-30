from sklearn.tree import DecisionTreeClassifier


def get_predictor():
    return DecisionTreeClassifier(max_depth=3)
