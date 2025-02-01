import pandas as pd

class BayesianNetwork:
    def __init__(self):
        self.nodes = {}  # to store nodes and their dependencies
        self.probability_table = None  # to store precomputed probabilities

    def add_node(self, node):
        """Adds a node to the network without any parents."""
        if node not in self.nodes:
            self.nodes[node] = []

    def add_edge(self, parent, child):
        """Defines dependency: child depends on parent."""
        if child in self.nodes:
            self.nodes[child].append(parent)
        else:
            self.nodes[child] = [parent]

    def load_probability_data(self, probability_df):
        """Loads precomputed probability values into the network."""
        self.probability_table = probability_df

    def infer_most_likely_congestion(self, time_period, weather):
        """Returns the most likely congestion level given time & weather."""
        if self.probability_table is None:
            raise ValueError("Probability data not loaded!")

        filtered = self.probability_table[
            (self.probability_table['time_period'] == time_period) &
            (self.probability_table['weather'] == weather)
        ]

        if filtered.empty:
            return "No data available for the given inputs."

        # will find the congestion level with highest probability
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

        return f"Probability of {congestion_level} congestion: {filtered.iloc[0]['posterior_probability']:.2%}"


bn = BayesianNetwork()

# define nodes aka variables
bn.add_node("Time Period")
bn.add_node("Weather")
bn.add_node("Congestion Level")

# define edges aka dependencies
bn.add_edge("Time Period", "Congestion Level")
bn.add_edge("Weather", "Congestion Level")

# data obtained from calculate_probabilities.py output file
data = [
    {"time_period": "Afternoon", "weather": "Clear", "congestion_level": "High", "posterior_probability": 0.103448},
    {"time_period": "Afternoon", "weather": "Clear", "congestion_level": "Low", "posterior_probability": 0.823755},
    {"time_period": "Afternoon", "weather": "Clear", "congestion_level": "Medium", "posterior_probability": 0.072797},
    {"time_period": "Afternoon", "weather": "Clouds", "congestion_level": "High", "posterior_probability": 0.062356},
    {"time_period": "Afternoon", "weather": "Clouds", "congestion_level": "Low", "posterior_probability": 0.893764},
    {"time_period": "Afternoon", "weather": "Clouds", "congestion_level": "Medium", "posterior_probability": 0.043880},
    {"time_period": "Afternoon", "weather": "Drizzle", "congestion_level": "High", "posterior_probability": 0.303371},
    {"time_period": "Afternoon", "weather": "Drizzle", "congestion_level": "Low", "posterior_probability": 0.483146},
    {"time_period": "Afternoon", "weather": "Drizzle", "congestion_level": "Medium", "posterior_probability": 0.213483},
    {"time_period": "Afternoon", "weather": "Rain", "congestion_level": "High", "posterior_probability": 0.666667},
    {"time_period": "Afternoon", "weather": "Rain", "congestion_level": "Low", "posterior_probability": 0.176955},
    {"time_period": "Afternoon", "weather": "Rain", "congestion_level": "Medium", "posterior_probability": 0.156379},
    {"time_period": "Afternoon", "weather": "Thunderstorm", "congestion_level": "High", "posterior_probability": 0.250000},
    {"time_period": "Afternoon", "weather": "Thunderstorm", "congestion_level": "Low", "posterior_probability": 0.398148},
    {"time_period": "Afternoon", "weather": "Thunderstorm", "congestion_level": "Medium", "posterior_probability": 0.351852},
    {"time_period": "Evening", "weather": "Clear", "congestion_level": "High", "posterior_probability": 0.052529},
    {"time_period": "Evening", "weather": "Clear", "congestion_level": "Low", "posterior_probability": 0.836576},
    {"time_period": "Evening", "weather": "Clear", "congestion_level": "Medium", "posterior_probability": 0.110895},
    {"time_period": "Evening", "weather": "Clouds", "congestion_level": "High", "posterior_probability": 0.303371},
    {"time_period": "Evening", "weather": "Clouds", "congestion_level": "Low", "posterior_probability": 0.483146},
    {"time_period": "Evening", "weather": "Clouds", "congestion_level": "Medium", "posterior_probability": 0.213483},
    {"time_period": "Evening", "weather": "Drizzle", "congestion_level": "High", "posterior_probability": 0.303371},
    {"time_period": "Evening", "weather": "Drizzle", "congestion_level": "Low", "posterior_probability": 0.483146},
    {"time_period": "Evening", "weather": "Drizzle", "congestion_level": "Medium", "posterior_probability": 0.213483},
    {"time_period": "Evening", "weather": "Rain", "congestion_level": "High", "posterior_probability": 0.635294},
    {"time_period": "Evening", "weather": "Rain", "congestion_level": "Low", "posterior_probability": 0.252941},
    {"time_period": "Evening", "weather": "Rain", "congestion_level": "Medium", "posterior_probability": 0.111765},
    {"time_period": "Evening", "weather": "Thunderstorm", "congestion_level": "High", "posterior_probability": 0.303371},
    {"time_period": "Evening", "weather": "Thunderstorm", "congestion_level": "Low", "posterior_probability": 0.483146},
    {"time_period": "Evening", "weather": "Thunderstorm", "congestion_level": "Medium", "posterior_probability": 0.213483},
    {"time_period": "Morning", "weather": "Clear", "congestion_level": "High", "posterior_probability": 0.220408},
    {"time_period": "Morning", "weather": "Clear", "congestion_level": "Low", "posterior_probability": 0.702041},
    {"time_period": "Morning", "weather": "Clear", "congestion_level": "Medium", "posterior_probability": 0.077551},
    {"time_period": "Morning", "weather": "Clouds", "congestion_level": "High", "posterior_probability": 0.154286},
    {"time_period": "Morning", "weather": "Clouds", "congestion_level": "Low", "posterior_probability": 0.737143},
    {"time_period": "Morning", "weather": "Clouds", "congestion_level": "Medium", "posterior_probability": 0.108571},
    {"time_period": "Morning", "weather": "Drizzle", "congestion_level": "High", "posterior_probability": 0.154286},
    {"time_period": "Morning", "weather": "Drizzle", "congestion_level": "Low", "posterior_probability": 0.737143},
    {"time_period": "Morning", "weather": "Drizzle", "congestion_level": "Medium", "posterior_probability": 0.108571},
    {"time_period": "Morning", "weather": "Rain", "congestion_level": "High", "posterior_probability": 0.566434},
    {"time_period": "Morning", "weather": "Rain", "congestion_level": "Low", "posterior_probability": 0.300699},
    {"time_period": "Morning", "weather": "Rain", "congestion_level": "Medium", "posterior_probability": 0.132867},
    {"time_period": "Morning", "weather": "Thunderstorm", "congestion_level": "High", "posterior_probability": 0.465517},
    {"time_period": "Morning", "weather": "Thunderstorm", "congestion_level": "Low", "posterior_probability": 0.370690},
    {"time_period": "Morning", "weather": "Thunderstorm", "congestion_level": "Medium", "posterior_probability": 0.163793}
]

probability_df = pd.DataFrame(data)

# load precomputed probability table
bn.load_probability_data(probability_df)

# inference + likelihood queries
print(bn.infer_most_likely_congestion("Morning", "Clear"))  # Find most likely congestion level
print(bn.get_congestion_probability("Evening", "Rain", "High"))  # Find probability of specific congestion level
