import pandas as pd
import numpy as np

# Создание Series из листа
print("\nSeries из списка")
listData = [1, 2, 3]
listSeries = pd.Series(listData)
print(listSeries)

# Создание Series из объекта NumPy
print("\nSeries из объекта NumPy")
numpyData = np.array([1, 2, 3])
numpySeries = pd.Series(numpyData)
print(numpySeries)

# Создание Series из словаря
print("\nSeries из словаря")
dictData = {'a': 1, 'b': 2, 'c': 3}
dictSeries = pd.Series(dictData)
print(dictSeries)

# Преобразовать объект Seris в DataFrame
print("\nDataframe")
listSeriesDataframe= listSeries.to_frame(name='Список')
print(listSeriesDataframe)

# Получить элементы объекта Series A, которых нет в объекте Series B
print("\nЭлементы множества A вне B")
seriesA = pd.Series([1, 2, 3, 4])
seriesB = pd.Series([3, 4, 5, 6])
notInB = seriesA[~seriesA.isin(seriesB)]
print("A")
print(seriesA)
print("B")
print(seriesB)
print("A/B")
print(notInB)

# Вертикальное объединение
print("\nВертикальное объединение A и B")
verticalConcat = pd.concat([seriesA, seriesB], axis=0)
print(verticalConcat)
# Горизонтальное объединение
print("\nГоризонтальное объединение A и B")
horizontalConcat = pd.concat([seriesB, seriesB], axis=1)
print(horizontalConcat)

# Преобразовать каждый символ объекта Series в верхний регистр
print("\nПреобразование в верхний регистр")
stringSeries = pd.Series(['яблоко', 'банан'])
upperStringSeries = stringSeries.str.upper()
print(upperStringSeries)

# Евклидово расстояние между A и B
print("\nЕвклидово расстояние между A и B")
euclideanDistance = np.linalg.norm(seriesA - seriesB)
print(euclideanDistance)


# Преобразовать индексы объекта Series в столбец DataFrameA
print("Dataframe с индексами как столбец")
dfWithIndexAsColumn = listSeries.reset_index()
print(dfWithIndexAsColumn)

# Переименовать столбец(-ы) в DataFrame(df)
print("\nОригинальный Dataframe")
df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
print(df)
dfRenamed = df.rename(columns={'a': 'A', 'b': 'B'})
print("\nПереименованный Dataframe")
print(dfRenamed)

# 1 Поменять местами столбцы 'a' и 'c'
print("\nОригинальный Dataframe")
df = pd.DataFrame({'a': [1, 2], 'b': [3, 4], 'c': [5, 6]})
print(df)
dfSwapped = df[['c', 'b', 'a']]
print("\nПоменяны a и c")
print(dfSwapped)

# 2 Написать функцию, которая меняет столбцы местами
def swapColumns(df, col1, col2):
    columns = df.columns.tolist()
    index1, index2 = columns.index(col1), columns.index(col2)
    columns[index1], columns[index2] = columns[index2], columns[index1]
    df = df[columns]
    return df
df = pd.DataFrame({'a': [1, 2], 'b': [3, 4], 'c': [5, 6]})
dfSwappedFunc = swapColumns(df, 'a', 'c')

# 3 Сортировать столбцы по наименованию
print("\nНесортированный Dataframe")
print(dfSwappedFunc)
dfSortedColumns = df.sort_index(axis=1)
print("\nОтсортированный Dataframe")
print(dfSortedColumns)
