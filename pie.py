import pandas as pd
from sklearn.metrics import f1_score, make_scorer
from sklearn.model_selection import StratifiedKFold

from sklearn.tree import DecisionTreeClassifier

from pypastry.experiment import Experiment

def get_experiment():
    candidates = pd.read_csv('../data/iris.csv')
    predictor = DecisionTreeClassifier()
    cross_validator = StratifiedKFold(n_splits=5)
    scorer = make_scorer(f1_score, average='micro')
    label_column = 'species'
    return Experiment(candidates, label_column, predictor, cross_validator, scorer)

