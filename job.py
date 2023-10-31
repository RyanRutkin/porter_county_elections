from datetime import datetime
import requests
import pandas as pd
import matplotlib.pyplot as plt
import io

with open('file.html', 'w') as f:
    url = "https://pkgstore.datahub.io/core/nasdaq-listings/nasdaq-listed_csv/data/7665719fb51081ba0bd834fde71ce822/nasdaq-listed_csv.csv"
    s = requests.get(url).content
    companies = pd.read_csv(io.StringIO(s.decode('utf-8')))
    lot_size = companies['Round Lot Size'].tolist()
    symbols = companies['Symbol'].tolist()

    fig, ax = plt.subplots()
    ax.bar(symbols[:5], lot_size[:5])
    fig.savefig('my_plot.png')

    html = "<img src='my_plot.png'/>"
    f.write(f"{html}")
