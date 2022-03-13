import urllib
import numpy as np
import pandas as pd

def boston():
	data_url = "http://lib.stat.cmu.edu/datasets/boston"

	raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
	data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
	target = raw_df.values[1::2, 2]

	file = urllib.request.urlopen(data_url)
	columns = list(map(lambda x: x.split(' ')[1], [line.decode('utf-8') for line in file][7:20]))
	data = pd.DataFrame(data=data, columns=columns)
	data["PRICE"] = target
	return data