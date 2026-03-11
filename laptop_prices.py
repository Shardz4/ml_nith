
import pandas as pd

# Create a dictionary of mock laptop data
data = {
    'cpu_cores': [4, 6, 8, 8, 12, 16, 4, 16, 6, 12],
    'ram_gb': [8, 16, 16, 32, 32, 64, 16, 32, 8, 64],
    'gpu_memory_gb': [0, 4, 4, 8, 8, 16, 0, 12, 6, 8], 
    'sticker_count': [3, 1, 0, 5, 2, 10, 0, 1, 4, 2],  # The useless feature!
    'price_usd': [450, 850, 950, 1400, 1800, 3200, 500, 2500, 900, 2100]
}

# Convert to a Pandas DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv('laptop_prices.csv', index=False)

print("Dataset successfully saved as 'laptop_prices.csv'!")
print(df.head())