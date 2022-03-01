import pandas as pd


ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.info())
print(ad_clicks.head())

utm_source_count = ad_clicks.groupby('utm_source').user_id.count().reset_index()

print(utm_source_count)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

print(ad_clicks)

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(
    columns = 'is_click',
    index = 'utm_source',
    values = 'user_id')\
    .reset_index()

print(clicks_pivot)

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

print(clicks_pivot)

clicks_by_ad = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(clicks_by_ad)

clicks_by_ad_with_click= ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

print(clicks_by_ad_with_click)

a_clicks = ad_clicks[(ad_clicks.experimental_group == 'A')]
print(a_clicks)
b_clicks = ad_clicks[(ad_clicks.experimental_group == 'B')]

a_clicks_pivot = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()\
    .pivot(
    index = 'day',
    columns = 'is_click',
    values = 'user_id').reset_index()
print(a_clicks_pivot)
a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True] / (a_clicks_pivot[True]+ a_clicks_pivot[False])
print(a_clicks_pivot)

b_clicks_pivot = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()\
    .pivot(
    index = 'day',
    columns = 'is_click',
    values = 'user_id').reset_index()
b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True] / (b_clicks_pivot[True]+ b_clicks_pivot[False])
print(b_clicks_pivot)

# A is better because it has a higher click rate on every day apart from tuesday
# A also has a higher click rate percentage overall
