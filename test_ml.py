import pytest
# TODO: add necessary import
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.data import process_data
from ml.model import train_model, inference, compute_model_metrics

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # add description for the first test
    Test the inference funciton returns a numpy array
    """
    # Your code here
    X_mock = np.random.rand(10,5)
    model_mock = RandomForestClassifier().fit(X_mock, np.random.randint(0, 2, size=10))
    preds = inference(model_mock, X_mock)
    assert isinstance(preds, np.ndarray)


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # add description for the second test
    Test train_model returns a RandomForestclassifier instance.
    """
    # Your code here
    X_mock = np.random.rand(10, 5)
    y_mock = np.random.randint(0, 2, size=10)
    model = train_model(X_mock, y_mock)
    assert isinstance(model, RandomForestClassifier)
    


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    Test compute_model_metrics returns expected metric values
    """
    # Your code here
    y_true = np.array([1, 0, 1, 1, 0])
    y_pred = np.array([1, 0, 1, 0, 0])
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    assert np.isclose(precision, 1.0)
    assert np.isclose(recall, 0.6667, atol=0.01)
    assert np.isclose(fbeta, 0.8, atol=0.01)
