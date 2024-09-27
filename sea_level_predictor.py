import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


data = pd.read_csv('/Users/a1/Downloads/epa-sea-level.csv')


plt.figure(figsize=(10, 6))
plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Sea Level Data', color='blue')


slope_full, intercept_full, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])

# Generate x values from 1880 to 2050
years_full = pd.Series(range(1880, 2051))

# Predict sea level for the full range using the line of best fit
sea_level_full = intercept_full + slope_full * years_full

# Plot the line of best fit
plt.plot(years_full, sea_level_full, label='Fit: 1880-2050', color='red')

# Step 4: Perform linear regression on data from 2000 onwards
recent_data = data[data['Year'] >= 2000]
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

# Generate x values from 2000 to 2050
years_recent = pd.Series(range(2000, 2051))

# Predict sea level for the recent period using the line of best fit
sea_level_recent = intercept_recent + slope_recent * years_recent

# Plot the recent line of best fit
plt.plot(years_recent, sea_level_recent, label='Fit: 2000-2050', color='green')

# Step 5: Customize the plot with labels, title, and legend
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Save and show the plot
plt.savefig('sea_level_plot.png')
plt.show()
