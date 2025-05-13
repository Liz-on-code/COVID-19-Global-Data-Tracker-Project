# Step 6: Optional - Choropleth Map
import plotly.express as px

# Prepare data for the map (using the latest date)
latest_data = df_filtered[df_filtered['date'] == df_filtered['date'].max()]

# Create a choropleth map of total cases by country
fig = px.choropleth(latest_data, locations="iso_code", color="total_cases",
                    hover_name="location", color_continuous_scale="Viridis",
                    title="Total COVID-19 Cases by Country")
fig.show()

# Create a choropleth map of vaccination rates by country
latest_data['vaccination_rate'] = (latest_data['total_vaccinations'] / latest_data['population']) * 100
fig = px.choropleth(latest_data, locations="iso_code", color="vaccination_rate",
                    hover_name="location", color_continuous_scale="Viridis",
                    title="COVID-19 Vaccination Rates by Country")
fig.show()
