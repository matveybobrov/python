import pandas as pd

# 1. Чтение файла train.csv в DataFrame
df = pd.read_csv('train.csv')

# 2. Отображение первых 10 строк таблицы
print("Первые 10 строк таблицы:")
print(df.head(10))

# 3. Общая информация о таблице
print("\nОбщая информация о таблице:")
print(df.info())

# 4. Проверка на дубликаты и их удаление
duplicates = df.duplicated().sum()
print(f"\nКоличество дубликатов: {duplicates}")
df = df.drop_duplicates()

# 5. Количество отсутствующих значений
missing_values = df.isnull().sum().sum()
print("\nКоличество отсутствующих значений:")
print(missing_values)

# 6. Процентное количество отсутствующих значений
missing_percentage = (df.isnull().sum().sum() / df.size) * 100
print("\nПроцентное количество отсутствующих значений:")
print(missing_percentage)

# 7. Замена отсутствующих значений на 0
df = df.fillna(0)

# 8. Приведение категориальных значений к нижнему регистру
print("\nПриведение населённых пунктов к нижнему регистру")
print(df['sub_area'])
df['sub_area'] = df['sub_area'].str.lower()
print(df['sub_area'])

# Проверка результата
print("\nТаблица после обработки:")
print(df.head())