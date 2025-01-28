import numpy as np
from scipy.stats import norm

# Probabilities for Time_Period
time_period_probs = {
    'Morning': 0.292135,
    'Afternoon': 0.382022,
    'Evening': 0.325843
}

# Probabilities for Weather
weather_probs = {
    'Clear': 0.314607,
    'Clouds': 0.213483,
    'Drizzle': 0.123596,
    'Rain': 0.224719,
    'Thunderstorm': 0.123596
}

# Conditional probabilities for Congestion_Level based on Time_Period and Weather
# in the format of: High congestion, Medium congestion, Low congestion
congestion_level_probs = {
    'Morning': {
        'Clear': [0.285714, 0.142857, 0.571429],
        'Clouds': [0.142857, 0.142857, 0.714286],
        'Drizzle': [0.142857, 0.333333, 0.333333],
        'Rain': [0.090909, 0.090909, 0.818182],
        'Thunderstorm': [0.333333, 0.333333, 0.333333],
    },
    'Afternoon': {
        'Clear': [0.666667, 0.222222, 0.111111],
        'Clouds': [0.250000, 0.500000, 0.250000],
        'Drizzle': [0.071429, 0.214286, 0.714286],
        'Rain': [0.333333, 0.333333, 0.333333],
        'Thunderstorm': [0.333333, 0.333333, 0.333333],
    },
    'Evening': {
        'Clear': [0.333333, 0.166667, 0.500000],
        'Clouds': [0.333333, 0.333333, 0.333333],
        'Drizzle': [0.666667, 0.333333, 0.000000],
        'Rain': [0.333333, 0.333333, 0.333333],
        'Thunderstorm': [0.200000, 0.200000, 0.600000],
    }
}

# Function to calculate the probability of Congestion_Level given Time_Period and Weather
def get_congestion_level_probability(time_period, weather):
    congestion_probs = congestion_level_probs[time_period][weather]
    return congestion_probs

# Function to calculate the likelihood of the evidence given a certain congestion level
def get_likelihood(time_period, weather, target_congestion_level):
    # Get the probabilities for the target congestion level (High, Medium, Low)
    congestion_probs = congestion_level_probs[time_period][weather]
    
    # Get the index of the target congestion level (High, Medium, Low)
    congestion_levels = ['High', 'Medium', 'Low']
    target_index = congestion_levels.index(target_congestion_level)
    
    # Return the likelihood of the evidence given the target congestion level
    return congestion_probs[target_index]

# Example query: What is the probability of congestion being 'High' given 'Morning' and 'Rain'?
time_period = 'Morning'
weather = 'Rain'
likelihood_congestion_level = 'High'

congestion_probs = get_congestion_level_probability(time_period, weather)
congestion_level = ['High', 'Medium', 'Low']

likelihood = get_likelihood(time_period, weather, likelihood_congestion_level)
print(f"Likelihood of time being {time_period} and weather being {weather} given 'High' congestion: {likelihood:.4f}")

# Normalize the probabilities
congestion_probs = np.array(congestion_probs) / np.sum(congestion_probs)

# Display the result
for i, level in enumerate(congestion_level):
    print(f"Probability of {level} congestion: {congestion_probs[i]:.4f}")
