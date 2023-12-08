import streamlit as st
import pandas as pd
import altair as alt

# Load data
file_path = r'C:\Users\Zaki\Desktop\streamlitint\experiment\indian-cities-dataset.csv'
data = pd.read_csv(file_path)

# Sidebar for filtering
st.sidebar.header("Filter Data")

# Calculate average distance
avg_dis = data['Distance'].mean()

# Display average distance
st.sidebar.write(f"Average Distance: {avg_dis:.2f} units")

# Calculate maximum and minimum distances
max_dis = data['Distance'].max()
min_dis = data['Distance'].min()

# Display maximum and minimum distances
st.sidebar.write(f"Maximum Distance: {max_dis} units")
st.sidebar.write(f"Minimum Distance: {min_dis} units")

# Identify city pairs with the highest and lowest distances
max_distance_row = data[data['Distance'] == max_dis]
min_distance_row = data[data['Distance'] == min_dis]

# Display city pairs with maximum and minimum distances
st.sidebar.write(f"City Pair with Maximum Distance: {max_distance_row['Origin'].values[0]} to {max_distance_row['Destination'].values[0]}")
st.sidebar.write(f"City Pair with Minimum Distance: {min_distance_row['Origin'].values[0]} to {min_distance_row['Destination'].values[0]}")

# Display the first 30 rows of the dataset
st.write("Top 30 Rows of the Dataset:")
st.write(data.head(30))

# Create a bar chart for distances using Streamlit
st.subheader("Distances Between Cities (Top 10)")
top_cities = data.groupby(['Origin', 'Destination']).mean().sort_values(by='Distance', ascending=False).head(10)

# Reset index before using st.bar_chart
top_cities_reset_index = top_cities.reset_index()
st.bar_chart(top_cities_reset_index['Distance'])

# Create a pie chart for distance distribution using Altair
st.subheader("Distance Distribution")
distance_distribution = data.groupby('Destination')['Distance'].sum().sort_values(ascending=False).head(5)

# Create Altair chart
chart = alt.Chart(distance_distribution.reset_index()).mark_bar().encode(
    x='Destination',
    y='Distance',
    color='Destination'
).properties(width=500, height=300)

# Display the Altair chart in Streamlit
st.altair_chart(chart, use_container_width=True)
