# Step 3: Data Cleaning

# Filter the data for selected countries
countries_of_interest = ['Kenya', 'USA', 'India']
df_filtered = df[df['location'].isin(countries_of_interest)]

# Convert the 'date' column to datetime
df_filtered['date'] = pd.to_datetime(df_filtered['date'])

# Drop rows with missing 'date' or critical columns
df_filtered = df_filtered.dropna(subset=['date', 'total_cases', 'total_deaths', 'total_vaccinations'])

# Fill or interpolate missing values for numerical columns (like new cases, new deaths, etc.)
df_filtered['new_cases'] = df_filtered['new_cases'].fillna(0)
df_filtered['new_deaths'] = df_filtered['new_deaths'].fillna(0)

# Check the cleaned data
print(df_filtered.head())
