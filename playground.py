def clear_df(df):
  import
  for i in range(len(df['message'])):
    df["message"][i] = df["message"][i].lower()
    df["message"][i] = re.sub('[a-zA-Z0-9]', '', df["message"][i])
    df["message"][i] = df["message"][i].replace("\n", " ").replace('~', '').replace('?', '').replace("''", '').replace("'", '').replace("=", '').replace("%", '').replace('→', '').replace('#', '').replace('/', '').replace('-', '').replace(':', '').replace('.', '').replace(';', '')
    df["message"][i] = df["message"][i].replace(" что ", " ").replace(' в ', ' ').replace(' и ', ' ').replace(' с ', ' ').replace(' на ', ' ').replace(' к ', ' ').replace(' от ', ' ').replace(' это ', ' ').replace(' для ', ' ')
    
