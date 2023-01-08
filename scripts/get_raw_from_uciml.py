# Short script to download the mtcars dataset

import urllib.request
url_data = 'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
dest_data = '/home/jul-ian/Github/mtcars-practice/data/raw/auto-mpg.data'

url_docs = 'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.names'
dest_docs = '/home/jul-ian/Github/mtcars-practice/data/auto-mpg.names'

urllib.request.urlretrieve(url_data, dest_data)
urllib.request.urlretrieve(url_docs, dest_docs)
