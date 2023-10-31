from datetime import datetime
import requests
import pandas as pd
import matplotlib.pyplot as plt
import io
import tabula

with open('file.html', 'w') as f:
    # url = "https://pkgstore.datahub.io/core/nasdaq-listings/nasdaq-listed_csv/data/7665719fb51081ba0bd834fde71ce822/nasdaq-listed_csv.csv"
    # s = requests.get(url).content

    

    # Read remote pdf into a list of DataFrame
    dfs = tabula.read_pdf("https://www.porterco.org/DocumentCenter/View/15171/3-2022-General-Election-OFFICIAL-Summary", pages='all', relative_columns=True, columns=[5, 33, 54, 61 ], guess=False,)
    print('LEN', len(dfs))
    pd.set_option('display.max_columns', None)
    print(dfs[0], dfs[1])

    html = "<img src='my_plot.png'/>"
    for df in dfs:
        try:
            print('good')
            df2 = df.drop(["Unnamed: 0"], axis=1)
        except:
            print('bad')
            df2 = df.drop(index=[0], axis=1)
        df3 = df2.dropna()
        html = html + df3.to_html()
    f.write(f"{html}")
