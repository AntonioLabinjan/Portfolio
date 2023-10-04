import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define user-defined values for initial capital and number of years
initial_capital = 10000  # Replace with your desired initial capital
num_years = 10  # Replace with your desired number of years for the simulation

# Generate random annual growth rates for each year
min_growth_rate = -0.20
max_growth_rate = 0.40
annual_growth_rates = np.random.uniform(min_growth_rate, max_growth_rate, num_years)

# Initialize a list to track portfolio growth over time
portfolio_growth = []

# Simulate portfolio growth
current_capital = initial_capital
for year in range(num_years):
    current_capital *= (1 + annual_growth_rates[year])
    portfolio_growth.append(current_capital)

# Convert annual growth rates to percentages
annual_growth_rates_percent = [rate * 100 for rate in annual_growth_rates]

# Create a DataFrame to store data
data = pd.DataFrame({'Year': range(1, num_years + 1), 'Capital': portfolio_growth, 'Growth Rate (%)': annual_growth_rates_percent})

# Print the data
print(data)

# Visualize portfolio growth
plt.plot(data['Year'], data['Capital'])
plt.xlabel('Year')
plt.ylabel('Capital')
plt.title('Portfolio Growth Simulation with Random Annual Growth Rates')
plt.grid(True)
plt.show()
