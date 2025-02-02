import pandas as pd
from calculate_probabilities import calculate_probabilities # from calculate_probabiltiies.py, import the calculate_probabilities functon

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
        "congestion_level": "Medium"
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
    },
    {
        "time_period": "Morning",
        "weather": "Clouds",
        "congestion_level": "Low"
    },
    {
        "time_period": "Morning",
        "weather": "Thunderstorm",
        "congestion_level": "High"
    },
    {
        "time_period": "Morning",
        "weather": "Thunderstorm",
        "congestion_level": "High"
    },
    {
        "time_period": "Morning",
        "weather": "Rain",
        "congestion_level": "High"
    },
    {
        "time_period": "Morning",
        "weather": "Rain",
        "congestion_level": "High"
    },
    {
        "time_period": "Morning",
        "weather": "Rain",
        "congestion_level": "High"
    },
    {
        "time_period": "Morning",
        "weather": "Rain",
        "congestion_level": "Medium"
    },
    {
        "time_period": "Morning",
        "weather": "Drizzle",
        "congestion_level": "Low"
    },
    {
        "time_period": "Morning",
        "weather": "Drizzle",
        "congestion_level": "Low"
    },
    {
        "time_period": "Morning",
        "weather": "Drizzle",
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
        "weather": "Clouds",
        "congestion_level": "Low"
    },
    {
        "time_period": "Afternoon",
        "weather": "Drizzle",
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
        "time_period": "Evening",
        "weather": "Clear",
        "congestion_level": "Medium"
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
        "weather": "Clouds",
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
    },
    {
        "time_period": "Morning",
        "weather": "Thunderstorm",
        "congestion_level": "Medium"
    },
    {
        "time_period": "Morning",
        "weather": "Thunderstorm",
        "congestion_level": "Low"
    },
    {
        "time_period": "Morning",
        "weather": "Clear",
        "congestion_level": "Medium"
    },
    {
        "time_period": "Morning",
        "weather": "Drizzle",
        "congestion_level": "Medium"
    },
    {
        "time_period": "Morning",
        "weather": "Drizzle",
        "congestion_level": "High"
    },
    {
        "time_period": "Morning",
        "weather": "Rain",
        "congestion_level": "Low"
    },
    {
        "time_period": "Evening",
        "weather": "Clouds",
        "congestion_level": "Medium"
    },
    {
        "time_period": "Evening",
        "weather": "Clouds",
        "congestion_level": "High"
    },
    {
        "time_period": "Evening",
        "weather": "Thunderstorm",
        "congestion_level": "Low"
    },
    {
        "time_period": "Evening",
        "weather": "Thunderstorm",
        "congestion_level": "Medium"
    },
    {
        "time_period": "Evening",
        "weather": "Rain",
        "congestion_level": "High"
    },
    {
        "time_period": "Evening",
        "weather": "Clear",
        "congestion_level": "High"
    },
    {
        "time_period": "Evening",
        "weather": "Drizzle",
        "congestion_level": "Low"
    },
    {
        "time_period": "Evening",
        "weather": "Drizzle",
        "congestion_level": "Medium"
    },
    {
        "time_period": "Evening",
        "weather": "Drizzle",
        "congestion_level": "High"
    },
    {
        "time_period": "Evening",
        "weather": "Rain",
        "congestion_level": "Low"
    },
    {
        "time_period": "Afternoon",
        "weather": "Clouds",
        "congestion_level": "High"
    },
    {
        "time_period": "Afternoon",
        "weather": "Thunderstorm",
        "congestion_level": "Medium"
    },
    {
        "time_period": "Afternoon",
        "weather": "Thunderstorm",
        "congestion_level": "Low"
    },
    {
        "time_period": "Afternoon",
        "weather": "Thunderstorm",
        "congestion_level": "High"
    },
    {
        "time_period": "Afternoon",
        "weather": "Clear",
        "congestion_level": "Medium"
    }, 
    {
        "time_period": "Afternoon",
        "weather": "Clear",
        "congestion_level": "High"
    },
    {
        "time_period": "Afternoon",
        "weather": "Drizzle",
        "congestion_level": "Medium"
    },
    {
        "time_period": "Afternoon",
        "weather": "Thunderstorm",
        "congestion_level": "Medium"
    },
    {
        "time_period": "Afternoon",
        "weather": "Drizzle",
        "congestion_level": "High"
    },
    {
        "time_period": "Afternoon",
        "weather": "Rain",
        "congestion_level": "Low"
    },
    {
        "time_period": "Evening",
        "weather": "Thunderstorm",
        "congestion_level": "High"
    }
]

class BayesianNetwork:
    def __init__(self):
        self.nodes = {}  # dictionary to store key as nodes and the values as the list of their parents nodes(if any)
        self.probability_table = None  # to store precomputed probabilities (from calculate_probabilities.py)

    def add_node(self, node):
        if node not in self.nodes: # if we havent added particular node before, we will add it in the 'nodes' dictionary where this particular node = key, and there are no values for it yet (no parent nodes)
            self.nodes[node] = [] 

    def add_edge(self, parent, child): # for dependencies 
        if child in self.nodes: # if exist, will simply append. if dont exist, will manually add both key and value
            self.nodes[child].append(parent) # eg child = congestion, so key = congestion, value = [time period, weather]
        else: 
            self.nodes[child] = [parent] # if child eg congestion doesnt exist in nodes dictionary yet ==> will manually set the child as key, and the parent as value in the nodes dicitonary

    def load_probability_data(self, probability_df):
        self.probability_table = probability_df

    def infer_most_likely_congestion(self, time_period, weather):
        if self.probability_table is None:
            raise ValueError("Probability data not loaded!")

        filtered = self.probability_table[
            (self.probability_table['time_period'] == time_period) &
            (self.probability_table['weather'] == weather)
        ]

        if filtered.empty:
            return "No data available for the given inputs."

        # will find the congestion level with highest probability to occur since '.loc' basically wld retrieve the specific row of data where the posterior_probability has max value using the index given by idxmax()
        # '.idxmax()' ==> basiclaly represents index of the maximum value
        # eg highest max value is at index 1, so code will be 'most_likely = filtered.loc[1]' ==> '.loc' will return the data at row at index 1
        most_likely = filtered.loc[filtered['posterior_probability'].idxmax()]
        return f"Most likely congestion level: {most_likely['congestion_level']} (Probability: {most_likely['posterior_probability']:.2%})"

    def get_congestion_probability(self, time_period, weather, congestion_level):
        if self.probability_table is None:
            raise ValueError("Probability data not loaded!")

        filtered = self.probability_table[
            (self.probability_table['time_period'] == time_period) &
            (self.probability_table['weather'] == weather) &
            (self.probability_table['congestion_level'] == congestion_level)
        ]

        if filtered.empty:
            return f"No data available for {time_period}, {weather}, {congestion_level}."

        return f"Probability of {congestion_level} congestion when {time_period} and {weather}: {filtered.iloc[0]['posterior_probability']:.2%}"

# make an instance of BayesianNetwork class
bn = BayesianNetwork()

bn.add_node("Time Period")
bn.add_node("Weather")
bn.add_node("Congestion Level")

bn.add_edge("Time Period", "Congestion Level")
bn.add_edge("Weather", "Congestion Level")

# now, get the posterior probability data from calculate_probabilities function in calculate_probabilites.py file (as seen from the calculate_probabiltiies.py, this will return in Dataframe format)
probability_df = calculate_probabilities(data) # now, probability_df = dataframe of all posterior probabilities for all unique combinations

# load precomputed probability table
bn.load_probability_data(probability_df)

# inference + likelihood queries
print(bn.infer_most_likely_congestion("Evening", "Rain"))  # Find most likely congestion level
print(bn.get_congestion_probability("Morning", "Clear", "Low"))  # Find probability of specific congestion level



# NOTES:
# '.loc' ==> access rows by label/index
# ':.2%' ==> basically multiply by & and also round up to 2dp