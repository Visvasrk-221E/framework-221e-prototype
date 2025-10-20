import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Create the data
data = [
    {"Date": "2030-01-15", "Day": 0, "Phase": "Laboratory Accident", "Cumulative_Cases": 1, "Daily_Deaths": 0, "Active_Cases": 1, "GDP_Loss_%": 0, "International_Conflicts": 0},
    {"Date": "2030-03-15", "Day": 59, "Phase": "Community Recognition", "Cumulative_Cases": 47, "Daily_Deaths": 12, "Active_Cases": 35, "GDP_Loss_%": -2, "International_Conflicts": 0},
    {"Date": "2030-06-01", "Day": 137, "Phase": "National Emergency", "Cumulative_Cases": 19648, "Daily_Deaths": 1200, "Active_Cases": 12500, "GDP_Loss_%": -34, "International_Conflicts": 2},
    {"Date": "2030-09-01", "Day": 229, "Phase": "International Crisis", "Cumulative_Cases": 45000000, "Daily_Deaths": 340000, "Active_Cases": 23000000, "GDP_Loss_%": -47, "International_Conflicts": 8},
    {"Date": "2031-06-30", "Day": 531, "Phase": "Vaccine Development", "Cumulative_Cases": 78000000, "Daily_Deaths": 45000, "Active_Cases": 8900000, "GDP_Loss_%": -52, "International_Conflicts": 12},
    {"Date": "2032-12-31", "Day": 1080, "Phase": "Containment", "Cumulative_Cases": 89000000, "Daily_Deaths": 2300, "Active_Cases": 450000, "GDP_Loss_%": -38, "International_Conflicts": 6},
    {"Date": "2033-12-31", "Day": 1445, "Phase": "Recovery", "Cumulative_Cases": 92000000, "Daily_Deaths": 120, "Active_Cases": 23000, "GDP_Loss_%": -18, "International_Conflicts": 3},
    {"Date": "2034-12-31", "Day": 1810, "Phase": "New Normal", "Cumulative_Cases": 94000000, "Daily_Deaths": 12, "Active_Cases": 2100, "GDP_Loss_%": -8, "International_Conflicts": 1}
]

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Normalize metrics to 0-100 scale for visualization
df['Cases_Norm'] = (df['Cumulative_Cases'] / df['Cumulative_Cases'].max()) * 100
df['Deaths_Norm'] = (df['Daily_Deaths'] / df['Daily_Deaths'].max()) * 100
df['Active_Norm'] = (df['Active_Cases'] / df['Active_Cases'].max()) * 100
df['GDP_Norm'] = (abs(df['GDP_Loss_%']) / abs(df['GDP_Loss_%']).max()) * 100
df['Conflicts_Norm'] = (df['International_Conflicts'] / df['International_Conflicts'].max()) * 100

# Create the figure
fig = go.Figure()

# Add traces for each metric
fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Cases_Norm'],
    mode='lines+markers',
    name='Cumulative Cases',
    line=dict(color='#1FB8CD', width=3),
    hovertemplate='<b>%{fullData.name}</b><br>Date: %{x}<br>Value: %{customdata:,.0f}<extra></extra>',
    customdata=df['Cumulative_Cases']
))

fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Deaths_Norm'],
    mode='lines+markers',
    name='Daily Deaths',
    line=dict(color='#DB4545', width=3),
    hovertemplate='<b>%{fullData.name}</b><br>Date: %{x}<br>Value: %{customdata:,.0f}<extra></extra>',
    customdata=df['Daily_Deaths']
))

fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Active_Norm'],
    mode='lines+markers',
    name='Active Cases',
    line=dict(color='#2E8B57', width=3),
    hovertemplate='<b>%{fullData.name}</b><br>Date: %{x}<br>Value: %{customdata:,.0f}<extra></extra>',
    customdata=df['Active_Cases']
))

fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['GDP_Norm'],
    mode='lines+markers',
    name='GDP Loss %',
    line=dict(color='#5D878F', width=3),
    hovertemplate='<b>%{fullData.name}</b><br>Date: %{x}<br>Value: %{customdata}%<extra></extra>',
    customdata=df['GDP_Loss_%']
))

fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Conflicts_Norm'],
    mode='lines+markers',
    name='Intl Conflicts',
    line=dict(color='#D2BA4C', width=3),
    hovertemplate='<b>%{fullData.name}</b><br>Date: %{x}<br>Value: %{customdata}<extra></extra>',
    customdata=df['International_Conflicts']
))

# Add phase markers
colors_cycle = ['#B4413C', '#964325', '#944454', '#13343B', '#DB4545', '#1FB8CD', '#2E8B57', '#5D878F']
for i, (_, row) in enumerate(df.iterrows()):
    fig.add_vline(
        x=row['Date'], 
        line_dash="dash", 
        line_color=colors_cycle[i % len(colors_cycle)],
        opacity=0.6,
        line_width=2
    )

# Update layout
fig.update_layout(
    title='Rabrid-X133 Outbreak Timeline 2030-2035',
    xaxis_title='Date',
    yaxis_title='Normalized Metrics (%)',
    hovermode='x unified',
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

fig.update_traces(cliponaxis=False)

# Save as both PNG and SVG
fig.write_image("rabrid_outbreak_timeline.png")
fig.write_image("rabrid_outbreak_timeline.svg", format="svg")