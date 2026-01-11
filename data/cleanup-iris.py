import polars as pl

pl.read_csv("./IRIS.csv").select(
	pl.exclude('species'),
	pl.col('species').str.split('-').list.get(1)
).write_csv("./IRIS-clean.csv")