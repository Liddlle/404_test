import pandas as pd
import numpy as np

def cost_by_month(month='January', year=2019):
    test1 = pd.read_csv('data/test - 1.csv')
    test2 = pd.read_csv('data/test - 2.csv')
    test3 = pd.read_csv('data/test - 3.csv')
    # Соединить таблицы
    df = pd.concat([
        pd.merge(test2, test3, on='id'),
        test1]) \
        .sort_values('date') \
        .reset_index(drop=True)

    # оставить в таблице только строки за определенный месяц
    df.date = pd.to_datetime(df.date)
    df = df[(df.date.dt.year == 2019) & (df.date.dt.month_name() == month)]

    # просуммировать поля invest, registrations, сгруппировав по менеджеру
    df = df.groupby(['id', 'manager'], as_index=False)[['invest', 'registrations']].sum()

    # добавить новый столбец со стоимостью регистрации.
    df['cost'] = round(np.divide(df.invest, df.registrations), 2)

    # учесть возможность того, что количество регистраций может быть 0.
    df.loc[df.registrations == 0, 'cost'] = ''
    return df

print(cost_by_month())