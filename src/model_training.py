from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train):
    # Code to train the machine learning model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    # Code to evaluate the model (for simplicity, using accuracy as an example)
    accuracy = model.score(X_test, y_test)
    return accuracy