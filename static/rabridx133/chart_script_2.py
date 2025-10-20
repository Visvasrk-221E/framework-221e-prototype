import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Load the data
data = [
    {"Date": "2030-01-15", "Borders_Closed": 0, "Military_Incidents": 0, "Severed_Relations": 0, "Refugees_Millions": 0, "Nuclear_Alert_Level": 1},
    {"Date": "2030-03-15", "Borders_Closed": 12, "Military_Incidents": 0, "Severed_Relations": 0, "Refugees_Millions": 0.5, "Nuclear_Alert_Level": 1},
    {"Date": "2030-06-01", "Borders_Closed": 89, "Military_Incidents": 2, "Severed_Relations": 3, "Refugees_Millions": 2.3, "Nuclear_Alert_Level": 2},
    {"Date": "2030-09-01", "Borders_Closed": 234, "Military_Incidents": 8, "Severed_Relations": 12, "Refugees_Millions": 23, "Nuclear_Alert_Level": 3},
    {"Date": "2031-06-30", "Borders_Closed": 267, "Military_Incidents": 15, "Severed_Relations": 18, "Refugees_Millions": 67, "Nuclear_Alert_Level": 4},
    {"Date": "2032-12-31", "Borders_Closed": 198, "Military_Incidents": 6, "Severed_Relations": 12, "Refugees_Millions": 89, "Nuclear_Alert_Level": 2},
    {"Date": "2033-12-31", "Borders_Closed": 123, "Military_Incidents": 2, "Severed_Relations": 6, "Refugees_Millions": 78, "Nuclear_Alert_Level": 1},
    {"Date": "2034-12-31", "Borders_Closed": 67, "Military_Incidents": 1, "Severed_Relations": 3, "Refugees_Millions": 45, "Nuclear_Alert_Level": 1}
]

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Scale refugee data to tens of millions for better visualization
df['Refugees_10M'] = df['Refugees_Millions'] / 10

# Create the line chart
fig = go.Figure()

# Define colors from the theme - using more contrasting colors
colors = ['#1FB8CD', '#DB4545', '#2E8B57', '#964325', '#13343B']

# Add each metric as a separate line with improved styling
fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Borders_Closed'],
    mode='lines+markers',
    name='Borders Closed',
    line=dict(color=colors[0], width=3),
    marker=dict(size=8),
    hovertemplate='<b>Borders Closed</b><br>Date: %{x}<br>Count: %{y}<extra></extra>'
))

fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Military_Incidents'],
    mode='lines+markers',
    name='Military Inc.',
    line=dict(color=colors[1], width=3),
    marker=dict(size=8),
    hovertemplate='<b>Military Incidents</b><br>Date: %{x}<br>Count: %{y}<extra></extra>'
))

fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Severed_Relations'],
    mode='lines+markers',
    name='Severed Rel.',
    line=dict(color=colors[2], width=3),
    marker=dict(size=8),
    hovertemplate='<b>Severed Relations</b><br>Date: %{x}<br>Count: %{y}<extra></extra>'
))

fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Refugees_10M'],
    mode='lines+markers',
    name='Refugees (10M)',
    line=dict(color=colors[3], width=3),
    marker=dict(size=8),
    hovertemplate='<b>Refugees</b><br>Date: %{x}<br>Millions: %{customdata}<extra></extra>',
    customdata=df['Refugees_Millions']
))

fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Nuclear_Alert_Level'] * 20,  # Scale up for visibility
    mode='lines+markers',
    name='Nuclear Alert',
    line=dict(color=colors[4], width=4, dash='dash'),
    marker=dict(size=10, symbol='diamond'),
    hovertemplate='<b>Nuclear Alert Level</b><br>Date: %{x}<br>Level: %{customdata}<extra></extra>',
    customdata=df['Nuclear_Alert_Level']
))

# Update layout with better formatting
fig.update_layout(
    title='Geopolitical Crisis Escalation 2030-34',
    xaxis_title='Timeline',
    yaxis_title='Crisis Metrics',
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5),
    hovermode='x unified'
)

# Format x-axis to show month/year
fig.update_xaxes(
    tickformat='%b %Y',
    dtick='M6'  # Show every 6 months
)

# Update traces for better hover display
fig.update_traces(cliponaxis=False)

# Save the chart as both PNG and SVG
fig.write_image("crisis_escalation.png")
fig.write_image("crisis_escalation.svg", format="svg")

fig.show()