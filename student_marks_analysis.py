import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Iswarya", "Varshini", "Anusha", "Kiranmaye", "Nikhitha"],
    "Marks": [80, 75, 90, 85, 70]
}

df = pd.DataFrame(data)

print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
