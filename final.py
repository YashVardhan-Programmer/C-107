import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv('data.csv')

student_df = df.loc[df['student_id'] == 'TRL_zet']

print(student_df.groupby('level')['attempt'].mean())

fig = go.Figure(go.Bar(
    x = ['level1', 'level2', 'level3', 'level4'],
    y = student_df.groupby('level')['attempt'].mean(),
))
fig.show()