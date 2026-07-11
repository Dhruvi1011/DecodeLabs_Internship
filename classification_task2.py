import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix,ConfusionMatrixDisplay

# Load dataset
df = pd.read_csv(r"D:\Internships_2ndYear\DecodeLabs_AI\Iris_dataset.csv")

# Remove Id column if present
if 'Id' in df.columns:
    df = df.drop('Id', axis=1)


print("Dataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# Features and Target
X = df.drop('Species', axis=1)
y = df['Species']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train logistic regressionmodel
lr_model = LogisticRegression(max_iter=200)

lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)

lr_accuracy = accuracy_score(y_test, lr_pred)

print("\n===== LOGISTIC REGRESSION =====")
print("Accuracy:", round(lr_accuracy * 100, 2), "%")
print(classification_report(y_test, lr_pred))

# Confusion Matrix - Logistic Regression
lr_cm = confusion_matrix(y_test, lr_pred)

ConfusionMatrixDisplay(
    confusion_matrix=lr_cm,
    display_labels=lr_model.classes_
).plot()

plt.title("Confusion Matrix - Logistic Regression")
plt.show()

#train knn model
knn_model = KNeighborsClassifier(n_neighbors=3)

knn_model.fit(X_train, y_train)

knn_pred = knn_model.predict(X_test)

knn_accuracy = accuracy_score(y_test, knn_pred)

print("\n===== KNN CLASSIFIER =====")
print("Accuracy:", round(knn_accuracy * 100, 2), "%")
print(classification_report(y_test, knn_pred))

# Confusion Matrix - KNN
knn_cm = confusion_matrix(y_test, knn_pred)

ConfusionMatrixDisplay(
    confusion_matrix=knn_cm,
    display_labels=knn_model.classes_
).plot()

plt.title("Confusion Matrix - KNN")
plt.show()

#model comparision
print("\n===== MODEL COMPARISON =====")
print(f"Logistic Regression Accuracy : {lr_accuracy*100:.2f}%")
print(f"KNN Accuracy                 : {knn_accuracy*100:.2f}%")

if lr_accuracy > knn_accuracy:
    print("Best Model: Logistic Regression")
elif knn_accuracy > lr_accuracy:
    print("Best Model: KNN")
else:
    print("Both models performed equally well.")



# input from user

print("\n--- Predict Iris Flower Species ---")

sl = float(input("Enter Sepal Length: "))
sw = float(input("Enter Sepal Width: "))
pl = float(input("Enter Petal Length: "))
pw = float(input("Enter Petal Width: "))

sample = pd.DataFrame({
    'SepalLengthCm': [sl],
    'SepalWidthCm': [sw],
    'PetalLengthCm': [pl],
    'PetalWidthCm': [pw]
})

lr_result = lr_model.predict(sample)
knn_result = knn_model.predict(sample)

print("\nLogistic Regression Prediction:", lr_result[0])
print("KNN Prediction:", knn_result[0])

