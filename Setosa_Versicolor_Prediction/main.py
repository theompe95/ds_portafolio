from data_loader import load_and_preprocess_data
from model import train_model
from evaluate import evaluate_model



def main():
    # Step 1: Load and preprocess data
    X_train, X_test, y_train, y_test = load_and_preprocess_data()
    
    # Step 2: Train the model
    model = train_model(X_train, y_train)
    
    
    # Step 3: Evaluate the model
    accuracy = evaluate_model(model, X_test, y_test)
    print("Model Accuracy:", accuracy)
    
    
if __name__ == "__main__":
    main()