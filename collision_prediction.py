# Vehicle Collision Detection (Simple Version)
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data.csv")
X = data[['speed', 'distance']]
y = data['risk']

# Train ML model
model = DecisionTreeClassifier()
model.fit(X, y)

# Take user input
speed = float(input("Enter vehicle speed: "))
distance = float(input("Enter distance between vehicles: "))

# Predict collision risk
risk = model.predict([[speed, distance]])[0]

if risk == 1:
    print("Collision Risk Detected!")
else:
    print("Safe Distance")

# Optional: visualize dataset
plt.scatter(data['distance'], data['speed'], c=data['risk'], cmap='coolwarm', s=100)
plt.xlabel("Distance")
plt.ylabel("Speed")
plt.title("Collision Risk Plot")
plt.show()
