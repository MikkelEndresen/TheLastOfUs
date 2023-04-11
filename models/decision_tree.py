from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def DT(data):
    # Initialize a DecisionTreeClassifier object
    clf = DecisionTreeClassifier(random_state=42,
                                 max_depth=5,
                                 min_samples_split=20,
                                 min_samples_leaf=10,
                                 criterion='entropy')

    # Fit the classifier to the training data
    clf.fit(data.X_train, data.y_train_binary)

    # Use the trained classifier to make predictions on the test data
    y_pred = clf.predict(data.X_test)

    # # Calculate the accuracy of the classifier on the test data
    # accuracy = accuracy_score(data.y_test, y_pred)

    # # Print the accuracy
    # print(f"Accuracy: {accuracy}")

    return y_pred