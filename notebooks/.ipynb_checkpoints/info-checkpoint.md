## Stats
Originally, it took me over 30 minutes (maybe provide %timeit data) to just gather 3 stats

df.iterrows(): --> df.itertuples(): --> df.groupby()

df.iterrows():
11min 49s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)

df.itertuples():
10min 11s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)

df.groupby():
