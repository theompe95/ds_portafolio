from sklearn.metrics import accuracy_score

def evaluate_model(model, X_test, y_test):
    
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    return accuracy