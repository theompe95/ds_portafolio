from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

import pandas as pd

def load_and_preprocess_data(test_size=0.3, random_state=42):
    # Load the dataset
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target)
    
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    return X_train, X_test, y_train, y_test

