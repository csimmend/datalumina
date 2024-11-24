import plotly.express as px

# Sample data
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14]
}

# Create a scatter plot
fig = px.scatter(data, x='x', y='y', title='Simple Scatter Plot')

# Show the plot
fig.show()