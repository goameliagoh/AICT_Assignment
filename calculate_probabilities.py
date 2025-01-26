import json
from collections import Counter # so can count how many times a value shows up (eg counter will count how many times "afternoon" occurs in data collected)

# collected data from the apis.. (this is considered historical congestion level)
data = [
    {
        "time_period": "Morning",
        "weather": "Clouds",
        "congestion_level": "Low"
    },
    {
        "time_period": "Morning",
        "weather": "Clouds",
        "congestion_level": "Low"
    },
    {
        "time_period": "Morning",
        "weather": "Clouds",
        "congestion_level": "Medium"
    },
    {
        "time_period": "Morning",
        "weather": "Clouds",
        "congestion_level": "High"
    },
    {
        "time_period": "Morning",
        "weather": "Clear",
        "congestion_level": "High"
    },
    {
        "time_period": "Morning",
        "weather": "Clear",
        "congestion_level": "High"
    },
    {
        "time_period": "Morning",
        "weather": "Clear",
        "congestion_level": "Low"
    },
    {
        "time_period": "Morning",
        "weather": "Clear",
        "congestion_level": "Low"
    },
    {
        "time_period": "Morning",
        "weather": "Clear",
        "congestion_level": "Low"
    },
    {
        "time_period": "Morning",
        "weather": "Clear",
        "congestion_level": "Low"
    },
    {
        "time_period": "Afternoon",
        "weather": "Clear",
        "congestion_level": "Low"
    },
    {
        "time_period": "Afternoon",
        "weather": "Clear",
        "congestion_level": "Low"
    },
    {
        "time_period": "Afternoon",
        "weather": "Clear",
        "congestion_level": "Low"
    },
    {
        "time_period": "Afternoon",
        "weather": "Rain",
        "congestion_level": "Medium"
    },
    {
        "time_period": "Afternoon",
        "weather": "Rain",
        "congestion_level": "High"
    },
    {
        "time_period": "Afternoon",
        "weather": "Rain",
        "congestion_level": "High"
    },
    {
        "time_period": "Afternoon",
        "weather": "Rain",
        "congestion_level": "High"
    },
    {
        "time_period": "Afternoon",
        "weather": "Clouds",
        "congestion_level": "Low"
    },
    {
        "time_period": "Afternoon",
        "weather": "Clouds",
        "congestion_level": "Low"
    },
    {
        "time_period": "Afternoon",
        "weather": "Clouds",
        "congestion_level": "Low"
    },
    {
        "time_period": "Afternoon",
        "weather": "Clouds",
        "congestion_level": "Medium"
    },
    {
        "time_period": "Afternoon",
        "weather": "Rain",
        "congestion_level": "High"
    },
    {
        "time_period": "Evening",
        "weather": "Rain",
        "congestion_level": "High"
    },
    {
        "time_period": "Evening",
        "weather": "Rain",
        "congestion_level": "High"
    },
    {
        "time_period": "Evening",
        "weather": "Rain",
        "congestion_level": "High"
    },
    {
        "time_period": "Evening",
        "weather": "Rain",
        "congestion_level": "High"
    },
    {
        "time_period": "Evening",
        "weather": "Clear",
        "congestion_level": "Medium"
    },
    {
        "time_period": "Evening",
        "weather": "Clear",
        "congestion_level": "Low"
    },
    {
        "time_period": "Evening",
        "weather": "Clear",
        "congestion_level": "Low"
    },
    {
        "time_period": "Evening",
        "weather": "Clear",
        "congestion_level": "Low"
    },
    {
        "time_period": "Evening",
        "weather": "Clear",
        "congestion_level": "Low"
    }
]


# to calculate probabilities from the data obtained
def calculate_probabilities(data):
    # count occurrences of each value for time_period (eg morning, afternoon), weather, and congestion_level
    time_period_counts = Counter(item["time_period"] for item in data)
    weather_counts = Counter(item["weather"] for item in data)
    congestion_level_counts = Counter(item["congestion_level"] for item in data)

    # ** TESTING TO SEE WHAT THE OUTPUT
    # print(time_period_counts) -- output: Counter({'Afternoon': 12, 'Morning': 10, 'Evening': 9})
    # print(time_period_counts.items()) -- output: dict_items([('Morning', 10), ('Afternoon', 12), ('Evening', 9)])

    # calculate probabilities by dividing by total number of entries
    total_entries = len(data)
    time_period_probs = {key: value / total_entries for key, value in time_period_counts.items()} # <-- basically for the kvp in time_period_counts.items(), replace the key with "key"(aka no change), and the value with "value / total_entries" 
    weather_probs = {key: value / total_entries for key, value in weather_counts.items()}
    congestion_level_probs = {key: value / total_entries for key, value in congestion_level_counts.items()}


    # ** TESTING TO SEE WHAT THE OUTPUT
    # print(time_period_probs) -- output: {'Morning': 0.3225806451612903, 'Afternoon': 0.3870967741935484, 'Evening': 0.2903225806451613} <-- aka key = time period, then value = the probability bc we took the amt of times the time period occurred / our total amount of time period datas

    return time_period_probs, weather_probs, congestion_level_probs

# calculate probabilities
time_period_probs, weather_probs, congestion_level_probs = calculate_probabilities(data)

# Output the probabilities with 2 decimal places (probabilities here are independent. still nd convert to joint probabilities, then conditional)
print("Probability of time periods:")
for key, value in time_period_probs.items():
    print(f"{key}: {value:.2f}")

print("\nProbability of weather types:")
for key, value in weather_probs.items():
    print(f"{key}: {value:.2f}")

print("\nProbability of congestion levels:")
for key, value in congestion_level_probs.items():
    print(f"{key}: {value:.2f}")


