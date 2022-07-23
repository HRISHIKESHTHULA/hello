import pandas
import seaborn as sns
import matplotlib.pyplot as plt


data = {'name': ['nick', 'david', 'joe', 'ross'],
        'age': [5, 10, 7, 6]}
df = pandas.DataFrame.from_dict(data)
print(df)


sns.set_theme()

# Load the example flights dataset and convert to long-form
flights_long = sns.load_dataset("flights")
flights = flights_long.pivot("month", "year", "passengers")


# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax)

plt.show()
