import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    "Name": ["John", "MARY", "aDE", "Bola"],
    "Email": ["john@gmail.com", "mary3yahoo.com", "ade@outlook.com", "bola@gmail.com"],
    "Math": [80, 55, 70, 90],
    "Science": [75, 60, 68, 95]
}

df = pd.DataFrame(data)

# Convert names to lowercase
df["Name"] = df["Name"].str.lower()

# Extract domain names
df["Domain"] = df["Email"].str.split("@").str[1]

print(df)

# Line plot
plt.plot(df["Name"], df["Math"])
plt.title("Math Scores Over Students")
plt.xlabel("Name")
plt.ylabel("Math Score")
plt.show()

# Histogram
plt.hist(df["Math"])
plt.title("Distribution of Math Scores")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.show()

# Scatter plot
plt.scatter(df["Math"], df["Science"])
plt.title("Math vs Science Scores")
plt.xlabel("Math")
plt.ylabel("Science")
plt.show()
