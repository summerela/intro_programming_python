#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

# import csv from URL as dataframe
url = "http://pbpython.com/extras/sample-salesv2.csv"
sales = pd.read_csv(url)

# update column names to remove spaces
sales.columns = ['acct_num', 'name', 'sku', 'category', 'quantity', 'unit_price', 'ext_price', 'date']

# subset data to contain only belt sales
belt_df = sales[['name', 'category', 'quantity', 'unit_price']]
belt_df = belt_df[belt_df['category']== 'Belt']

# create a new column called belt_sales
belt_df['belt_sales'] = belt_df.quantity * belt_df.unit_price

# group sales by company name
belts_by_company = belt_df.groupby('name').sum()

# subset for top 10 best sellers
top_sellers = belts_by_company.sort_values(by='belt_sales', ascending=False).head(10)

# save top 10 data frame to tsv
top_sellers.to_csv("./top_sellers.tsv", sep="\t", index=None)

# save plot to file
top_sellers.plot()
plt.savefig('./top_sellers.png')

