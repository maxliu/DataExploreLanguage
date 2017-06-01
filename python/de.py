
#import os
import pandas
import numpy as np

fn = "auto-mpg2.csv"

df = pandas.read_csv(fn)

#print df
print len(df)

print list(df.columns)

colx = 'manufacturer'

uq_colx =  set(df[colx].values)

print len(uq_colx)
print uq_colx

print df.dtypes

print df['displ', 'hwy'].apply([np.sum,np.std, np.mean])


from bokeh.charts import Bar, output_file, show, Histogram

#p = Bar(df, label=colx, values='displ', agg='mean', title="Total MPG by CYL")

#p = Histogram(df, values='displ', color='cyl', title="displ Distribution")
p = Bar(df, label=colx, values='displ', agg='count', title="Total MPG by CYL",
        legend=None)


output_file("bar.html")

show(p)
