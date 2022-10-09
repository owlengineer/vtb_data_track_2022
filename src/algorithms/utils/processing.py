import pandas as pd


def clear_df(df):
    import re
    for i in range(len(df['message'])):
        df["message"][i] = str(df["message"][i]).lower()
        df["message"][i] = re.sub('[a-zA-Z0-9]', '', df["message"][i])
        df["message"][i] = df["message"][i].replace("\n", " ").replace('~', '').replace('?', '').replace("''",
                                                                                                         '').replace(
            "'", '').replace("=", '').replace("%", '').replace('→', '').replace('#', '').replace('/', '').replace('-',
                                                                                                                  '').replace(
            ':', '').replace('.', '').replace(';', '')
        df["message"][i] = df["message"][i].replace(" что ", " ").replace(' в ', ' ').replace(' и ', ' ').replace(' с ',
                                                                                                                  ' ').replace(
            ' на ', ' ').replace(' к ', ' ').replace(' от ', ' ').replace(' это ', ' ').replace(' для ', ' ')


def get_data():
    df = pd.read_csv('src/algorithms/utils/tg.csv')
    clear_df(df)
    print(df.head())
    return df
