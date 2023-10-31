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
    dfs = tabula.read_pdf("https://www.porterco.org/DocumentCenter/View/16019/3-2023-Primary-Election-OFFICIAL-Summary-Results", pages='all', relative_columns=True, columns=[5, 25, 50, 70 ], guess=False,)
    print('LEN', len(dfs))
    pd.set_option('display.max_columns', None)
    print(dfs[0], dfs[1])

    html = "<img src='my_plot.png'/>"
    for df in dfs:
        html = html + df.to_html()
    f.write(f"{html}")
