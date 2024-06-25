import matplotlib.pyplot as plt
from meteostat import Point, Daily
from datetime import datetime

# Set the location (e.g., New York City)
location = Point(40.7128, -74.0060)

# Set the time period (e.g., January 2021)
start = datetime(2000, 1, 1)
end = datetime(2021, 1, 31)

# Get daily data
data = Daily(location, start, end)
data = data.fetch()

# Print the data
print(data)

# Plot the data
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.title('Daily Weather Data for New York City - January 2021')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.show()
