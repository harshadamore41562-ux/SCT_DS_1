import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file (correct full path)
df = pd.read_csv(
    r"C:\Users\Admin\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_61\API_SP.POP.TOTL_DS2_en_csv_v2_61.csv",
    skiprows=4
)

# Filter for India
india = df[df['Country Name'] == 'India']

# Extract years and population values
years = india.columns[4:]   # first 4 columns are metadata
population = india.iloc[0, 4:].values.astype(float)

# Plot bar chart
plt.figure(figsize=(12,6))
plt.bar(years, population, color='skyblue')

plt.title("India Population Growth (1960–2024)")
plt.xlabel("Year")
plt.ylabel("Population (in billions)")
plt.xticks(rotation=90)

# Format Y-axis to billions
plt.gca().get_yaxis().set_major_formatter(
    plt.FuncFormatter(lambda x, _: f'{x/1e9:.1f}B')
)

plt.show()
