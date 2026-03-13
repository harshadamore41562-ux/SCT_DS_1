import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv(
    r"C:\Users\Admin\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_61\API_SP.POP.TOTL_DS2_en_csv_v2_61.csv",
    skiprows=4
)

# --- User interaction ---
country = input("Enter the country name: ").strip()
chart_type = input("Choose chart type (bar/line): ").strip().lower()
start_year = int(input("Enter start year (e.g., 1980): "))
end_year = int(input("Enter end year (e.g., 2000): "))

# Filter for chosen country (case-insensitive)
data = df[df['Country Name'].str.lower() == country.lower()]

if data.empty:
    print(f"Country '{country}' not found in dataset.")
else:
    # Keep only columns that are digits (valid years)
    year_cols = [col for col in data.columns[4:] if col.isdigit()]
    years = pd.to_numeric(year_cols)
    population = data[year_cols].iloc[0].values.astype(float)

    # Apply year range filter
    mask = (years >= start_year) & (years <= end_year)
    years_filtered = years[mask]
    population_filtered = population[mask]

    # Plot chart based on user choice
    plt.figure(figsize=(12,6))
    if chart_type == "bar":
        plt.bar(years_filtered, population_filtered, color='skyblue')
    else:
        plt.plot(years_filtered, population_filtered, color='green', marker='o')

    plt.title(f"{country.title()} Population Growth ({start_year}–{end_year})")
    plt.xlabel("Year")
    plt.ylabel("Population (in billions)")
    plt.xticks(rotation=90)

    # Format Y-axis to billions
    plt.gca().get_yaxis().set_major_formatter(
        plt.FuncFormatter(lambda x, _: f'{x/1e9:.1f}B')
    )

    plt.show()
