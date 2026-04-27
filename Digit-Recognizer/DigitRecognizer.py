import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")