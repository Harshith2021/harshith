import pandas as pd
import numpy as np
import plotly.graph_objects as go
path_to_data = 'C:\\Users\\M Harshith\\OneDrive\\Documents\\Olympics\\Data Set'
df_athletes = pd.read_excel(path_to_data + '\\Athletes.xlsx')
df_gender = pd.read_excel(path_to_data + '\\EntriesGender.xlsx')
df_medals = pd.read_excel(path_to_data + '\\Medals.xlsx')
df_teams = pd.read_excel(path_to_data + '\\Teams.xlsx')
print('Missing values on Athletes.xlsx column NOC: {}'.format(
    df_athletes['NOC'].isna().sum()))
print('Missing values on Athletes.xlsx column Discipline: {}'.format(
    df_athletes['Discipline'].isna().sum()))
print('Missing values on EntriesGender.xlsx column Discipline: {}'.format(
    df_gender['Discipline'].isna().sum()))
print('Missing values on EntriesGender.xlsx column Female: {}'.format(
    df_gender['Female'].isna().sum()))
print('Missing values on EntriesGender.xlsx column Male: {}'.format(
    df_gender['Male'].isna().sum()))
print('Missing values on Medals.xlsx column Team/NOC: {}'.format(
    df_medals['Team/NOC'].isna().sum()))
print('Missing values on Medals.xlsx column Gold: {}'.format(
    df_medals['Gold'].isna().sum()))
print('Missing values on Medals.xlsx column Silver: {}'.format(
    df_medals['Silver'].isna().sum()))
print('Missing values on Medals.xlsx column Bronze: {}'.format(
    df_medals['Bronze'].isna().sum()))
fig = go.Figure([go.Bar(x=df_athletes['NOC'].value_counts().index[:20],
                        y=df_athletes['NOC'].value_counts().values[:20],
                        text=df_athletes['NOC'].value_counts().values[:20],
                        textposition='auto')
                 ]
                )

fig.update_layout(
    title_text="Top 20 country with the most athletes in the competition")

fig.show()
fig = go.Figure([go.Bar(x=df_athletes['Discipline'].value_counts().index[:20],
                        y=df_athletes['Discipline'].value_counts().values[:20],
                        text=df_athletes['Discipline'].value_counts(
).values[:20],
    textposition='auto')
]
)

fig.update_layout(
    title_text="Top 20 disciplines with the most athletes in the competition")

fig.show()
fig = go.Figure(data=[
    go.Bar(name='Male', x=df_gender['Discipline'], y=df_gender['Male']),
    go.Bar(name='Female', x=df_gender['Discipline'], y=df_gender['Female']),
])
# Change the bar mode
fig.update_layout(
    barmode='group', title_text="Gender distribution on each discipline")
fig.show()
fig = go.Figure()
fig.add_trace(go.Bar(name='Male',
                     x=df_gender['Male'] / df_gender['Total'],
                     y=df_gender['Discipline'],
                     orientation='h'
                     ))

fig.add_trace(go.Bar(name='Female',
                     x=df_gender['Female'] / df_gender['Total'],
                     y=df_gender['Discipline'],
                     orientation='h'
                     ))

fig.update_layout(barmode="relative",
                  width=1000,
                  height=1000,
                  bargap=0.30,
                  title_text="Gender distribution on each discipline",
                  legend_orientation='h')
fig.show()
fig = go.Figure()
fig.add_trace(go.Bar(name='Gold',
                     x=df_medals[df_medals['Rank'] <= 20]['Gold'],
                     y=df_medals[df_medals['Rank'] <= 20]['Team/NOC'],
                     orientation='h',
                     marker_color='gold'
                     ))
fig.add_trace(go.Bar(name='Silver',
                     x=df_medals[df_medals['Rank'] <= 20]['Silver'],
                     y=df_medals[df_medals['Rank'] <= 20]['Team/NOC'],
                     orientation='h',
                     marker_color='silver'
                     ))

fig.add_trace(go.Bar(name='Bronze',
                     x=df_medals[df_medals['Rank'] <= 20]['Bronze'],
                     y=df_medals[df_medals['Rank'] <= 20]['Team/NOC'],
                     orientation='h',
                     marker_color='brown'
                     ))

fig.update_layout(barmode="stack",
                  width=1000,
                  height=1000,
                  bargap=0.30,
                  legend_orientation='h')
fig.show()
