import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Load the data
data = [{"Date": "2030-01-15", "Hospital_Capacity_%": 100, "Food_Reserves_%": 100, "Fuel_Supplies_%": 100, "Healthcare_Workers_%": 100, "Quarantine_Capacity_%": 100}, 
        {"Date": "2030-03-15", "Hospital_Capacity_%": 115, "Food_Reserves_%": 95, "Fuel_Supplies_%": 98, "Healthcare_Workers_%": 92, "Quarantine_Capacity_%": 67}, 
        {"Date": "2030-06-01", "Hospital_Capacity_%": 340, "Food_Reserves_%": 34, "Fuel_Supplies_%": 23, "Healthcare_Workers_%": 66, "Quarantine_Capacity_%": 18}, 
        {"Date": "2030-09-01", "Hospital_Capacity_%": 450, "Food_Reserves_%": 12, "Fuel_Supplies_%": 8, "Healthcare_Workers_%": 45, "Quarantine_Capacity_%": 5}, 
        {"Date": "2031-06-30", "Hospital_Capacity_%": 280, "Food_Reserves_%": 45, "Fuel_Supplies_%": 34, "Healthcare_Workers_%": 58, "Quarantine_Capacity_%": 23}, 
        {"Date": "2032-12-31", "Hospital_Capacity_%": 145, "Food_Reserves_%": 78, "Fuel_Supplies_%": 67, "Healthcare_Workers_%": 72, "Quarantine_Capacity_%": 45}, 
        {"Date": "2033-12-31", "Hospital_Capacity_%": 110, "Food_Reserves_%": 89, "Fuel_Supplies_%": 85, "Healthcare_Workers_%": 83, "Quarantine_Capacity_%": 78}, 
        {"Date": "2034-12-31", "Hospital_Capacity_%": 95, "Food_Reserves_%": 92, "Fuel_Supplies_%": 90, "Healthcare_Workers_%": 89, "Quarantine_Capacity_%": 85}]

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Create the figure
fig = go.Figure()

# Brand colors for different severity levels
colors = ['#DB4545', '#D2BA4C', '#2E8B57', '#5D878F', '#1FB8CD']

# Add traces for each resource
fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Hospital_Capacity_%'],
    mode='lines+markers',
    name='Hospital Cap',
    line=dict(color=colors[0], width=3),
    marker=dict(size=8)
))

fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Food_Reserves_%'],
    mode='lines+markers',
    name='Food Reserves',
    line=dict(color=colors[1], width=3),
    marker=dict(size=8)
))

fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Fuel_Supplies_%'],
    mode='lines+markers',
    name='Fuel Supplies',
    line=dict(color=colors[2], width=3),
    marker=dict(size=8)
))

fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Healthcare_Workers_%'],
    mode='lines+markers',
    name='Healthcare Wkrs',
    line=dict(color=colors[3], width=3),
    marker=dict(size=8)
))

fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Quarantine_Capacity_%'],
    mode='lines+markers',
    name='Quarantine Cap',
    line=dict(color=colors[4], width=3),
    marker=dict(size=8)
))

# Update layout
fig.update_layout(
    title='Resource Strain Analysis 2030-2035',
    xaxis_title='Year',
    yaxis_title='Percentage %',
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5),
    hovermode='x unified'
)

# Update axes
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')

# Add horizontal line at 100% for reference
fig.add_hline(y=100, line_dash="dash", line_color="gray", opacity=0.5)

# Update traces for better visibility
fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image("resource_strain_chart.png")
fig.write_image("resource_strain_chart.svg", format="svg")

print("Chart saved as resource_strain_chart.png and resource_strain_chart.svg")