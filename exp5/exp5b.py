import statistics
sales = [120, 150, 180, 200, 220, 250, 270, 300, 350, 400]
mean = statistics.mean(sales)
variance = statistics.variance(sales)
std_dev = statistics.stdev(sales)
# Skewness
n = len(sales)
m3 = sum((x - mean) ** 3 for x in sales) / n
m2 = sum((x - mean) ** 2 for x in sales) / n
skewness = m3 / (m2 ** 1.5)
# Kurtosis
m4 = sum((x - mean) ** 4 for x in sales) / n
kurtosis = (m4 / (m2 ** 2)) - 3
print("Sales Data:", sales)
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)
