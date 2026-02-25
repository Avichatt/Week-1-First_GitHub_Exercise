import statistics

# Sample weather data for Gandhinagar (last 10 days)
# Replace with actual values if available
temperature = [28, 30, 29, 31, 32, 33, 29, 30, 31, 28]  # in °C
humidity = [45, 50, 48, 52, 55, 53, 47, 49, 51, 46]     # in %
aqi = [85, 90, 88, 95, 100, 92, 87, 89, 93, 91]         # AQI values

def calculate_stats(data, label):
    avg = sum(data) / len(data)
    median = statistics.median(data)
    print(f"{label} - Average: {avg:.2f}, Median: {median}")

def main():
    print("Weather & AQI Data Analysis for Gandhinagar (Last 10 Days)")
    calculate_stats(temperature, "Temperature (°C)")
    calculate_stats(humidity, "Humidity (%)")
    calculate_stats(aqi, "Air Quality Index (AQI)")

if __name__ == "__main__":
    main()
    