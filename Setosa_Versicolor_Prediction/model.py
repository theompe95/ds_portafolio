from sklearn.linear_model import LogisticRegression

def train_model(X_train, y_train):
    
    # Initialize the Logistic Regression model
    model = LogisticRegression(random_state=42)
    
    
    # Train the model on the training data
    model.fit(X_train, y_train)
    
    return model