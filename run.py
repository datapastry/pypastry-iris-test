import pandas as pd
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold

from pypastry import run_experiment
from sklearn.tree import DecisionTreeClassifier


def run():
    candidates = pd.read_csv('../data/iris.csv')
    predictor = DecisionTreeClassifier()
    cross_validator = StratifiedKFold(n_splits=5)
    metric = f1_score
    label_column = 'species'
    run_experiment(candidates, label_column, predictor, cross_validator, metric)


if __name__ == "__main__":
    run()
