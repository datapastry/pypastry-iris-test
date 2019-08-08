import pandas as pd
from sklearn.metrics import f1_score, make_scorer
from sklearn.model_selection import StratifiedKFold

from pypastry import run_experiment
from sklearn.tree import DecisionTreeClassifier


def run():
    candidates = pd.read_csv('../data/iris.csv')
    predictor = DecisionTreeClassifier()
    cross_validator = StratifiedKFold(n_splits=5)
    scorer = make_scorer(f1_score, average='micro')
    label_column = 'species'
    run_experiment(candidates, label_column, predictor, cross_validator, scorer)


if __name__ == "__main__":
    run()
