# Import pandas for data manipulation, matplotlib for plotting graphs, and seaborn for enhanced graph visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the file path for the CSV file with stock data
csv_file_path = 'C:/Users/unfaz/Downloads/AAPL.csv'

# Read the stock data from the CSV into a pandas DataFrame object
data_frame = pd.read_csv(csv_file_path)

# Compute moving averages over the last 100 and 200 days for the 'Close' price
data_frame['100_MA'] = data_frame['Close'].rolling(window=100).mean()  # 100-day moving average
data_frame['200_MA'] = data_frame['Close'].rolling(window=200).mean()  # 200-day moving average

# Convert string dates to DateTime objects to facilitate plotting
data_frame['Date'] = pd.to_datetime(data_frame['Date'])

# Create a new figure for plotting with a set size (width, height in inches)
plt.figure(figsize=(12, 6))

# Plot closing price and moving averages with labels for each line
plt.plot(data_frame['Date'], data_frame['Close'], label='Closing Price', color='blue')  # Plot closing price
plt.plot(data_frame['Date'], data_frame['100_MA'], label='100-day MA', color='orange')  # Plot 100-day MA
plt.plot(data_frame['Date'], data_frame['200_MA'], label='200-day MA', color='red')     # Plot 200-day MA

# Label the x-axis and y-axis, and add a title to the plot
plt.xlabel('Date')  # X-axis label
plt.ylabel('Price')  # Y-axis label
plt.title('AAPL Stock Price Analysis')  # Plot title

# Show the legend to identify which line is which
plt.legend()

# Add a grid for easier reading of the plot
plt.grid(True)

# Display the matplotlib plot to the user
plt.show()

# Set the aesthetic parameters for seaborn plots
sns.set(style="whitegrid")

# Create another figure for the seaborn plot with a specified size
plt.figure(figsize=(12, 6))

# Use seaborn to create a line plot for closing prices and moving averages
sns.lineplot(data=data_frame, x='Date', y='Close', label='Closing Price')  # Seaborn plot for closing price
sns.lineplot(data=data_frame, x='Date', y='100_MA', label='100-day MA')    # Seaborn plot for 100-day MA
sns.lineplot(data=data_frame, x='Date', y='200_MA', label='200-day MA')    # Seaborn plot for 200-day MA

# Labeling and title for the seaborn plot
plt.xlabel('Date')  # X-axis label
plt.ylabel('Price')  # Y-axis label
plt.title('AAPL Stock Price Analysis using Seaborn')  # Plot title

# Show the legend and display the seaborn plot
plt.legend()
plt.show()
