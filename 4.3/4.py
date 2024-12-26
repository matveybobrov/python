import pandas as pd

data = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])

print("Series:")
print(data)

newOrder = [3, 2, 1]
reorderedSeries = data.reindex(newOrder)

print("\nSeries после изменения индексов")
print(reorderedSeries)