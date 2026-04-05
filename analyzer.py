import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("students.csv")

# Calculate average
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

# Topper
topper = df.loc[df["Average"].idxmax()]

# Weak students
weak_students = df[df["Average"] < 50]

print("Topper:\n", topper)
print("\nWeak Students:\n", weak_students)

# Visualization
plt.figure()
plt.bar(df["Name"], df["Average"])
plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.show()

# Machine Learning
df["Result"] = df["Average"].apply(lambda x: 1 if x >= 50 else 0)
X = df[["Maths", "Science", "English", "Attendance"]]
y = df["Result"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
print("Accuracy:", model.score(X_test, y_test))
