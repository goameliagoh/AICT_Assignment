import numpy as np
from scipy.stats import norm

# dictionary to store independent probabilities for Time 
time_period_probs = {
    'Morning': 0.292135,
    'Afternoon': 0.382022,
    'Evening': 0.325843
}

# dictionary to store independent probabilities for Weather
weather_probs = {
    'Clear': 0.314607,
    'Clouds': 0.213483,
    'Drizzle': 0.123596,
    'Rain': 0.224719,
    'Thunderstorm': 0.123596
}

# conditional probabilities for Congestion, given the Time and Weather
# in the format of: High congestion, Medium congestion, Low congestion (cn be any format as long as consistent)
congestion_level_probs = {
    'Morning': {
        'Clear': [0.285714, 0.142857, 0.571429],
        'Clouds': [0.200000, 0.200000, 0.600000],
        'Drizzle': [0.200000, 0.200000, 0.600000],
        'Rain': [0.600000, 0.200000, 0.200000],
        'Thunderstorm': [0.500000, 0.250000, 0.250000],
    },
    'Afternoon': {
        'Clear': [0.142857, 0.142857, 0.714286],
        'Clouds': [0.090909, 0.090909, 0.818182],
        'Drizzle': [0.333333, 0.333333, 0.333333],
        'Rain': [0.666667, 0.222222, 0.111111],
        'Thunderstorm': [0.250000, 0.500000, 0.250000],
    },
    'Evening': {
        'Clear': [0.071429, 0.214286, 0.714286],
        'Clouds': [0.333333, 0.333333, 0.333333],
        'Drizzle': [0.333333, 0.333333, 0.333333],
        'Rain': [0.666667, 0.166667, 0.166667],
        'Thunderstorm': [0.333333, 0.333333, 0.333333],
    }
}

# to calculate the probability of Congestion_Level given Time_Period and Weather (Inference)
def get_inference(time_period, weather):
    congestion_probs = congestion_level_probs[time_period][weather]
    return congestion_probs

# to calculate the likelihood of a certain given congestion level occuring when it is (given time), (given weather)
def get_likelihood(time_period, weather, target_congestion_level):
    # get the probabilities for given target congestion level (High, Medium, Low)
    congestion_probs = congestion_level_probs[time_period][weather]
    
    congestion_levels = ['High', 'Medium', 'Low'] # <== aka the same format as i used above aka High to Low congestion
    target_index = congestion_levels.index(target_congestion_level) # <-- to get the index of where the target congestion is at (look @ notes below for example)
    
    return congestion_probs[target_index]



# Example query: What is the probability of congestion being 'High' given 'Morning' and 'Rain'?
time_period = 'Afternoon'
weather = 'Rain'
likelihood_congestion_level = 'High'

# Inference:
congestion_probs = get_inference(time_period, weather)
# Display the result
congestion_level = ['High', 'Medium', 'Low'] # so can enumerate
print("Inference:")
print()
for i, level in enumerate(congestion_level):
    print(f"Probability of {level} congestion when time is {time_period} and weather is {weather}: {congestion_probs[i]:.4f}")

print()

# Likelihood:
likelihood = get_likelihood(time_period, weather, likelihood_congestion_level)
print()
print("Likelihood:")
print(f"\nLikelihood of time being {time_period} and weather being {weather} given 'High' congestion: {likelihood:.4f}")

print()






# ----------NOTES --------------
# .index() function ==> eg colors = ['Red', 'Yellow', 'Blue', 'Green'], target_color = 'Green', index_of_target_color = colors.index(target_color), print(index_of_target_color), output = 3
# .enumerate() function ==> same eg as ^^, for index, color in enumerate(colors) print (f{index}, {color}), output = 0 Red, 1 Yellow, 2 Blue, 3 Green