# titanic_predictor.py or in a Jupyter cell

import pandas as pd

# Load dataset
df = pd.read_csv("data/train.csv")

# Basic overview
print(df.head())
print(df.info())
print(df.describe())

