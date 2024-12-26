import pandas as pd

data = pd.Series([100, 200, 'python', 300.12, 400])

print("Series:")
print(data)

newData = pd.Series([500, 'php'])
updatedSeries = pd.concat([data, newData])

print("\nSeries после добавления данных:")
print(updatedSeries)