import pandas as pd

# collected data from the apis..
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
df = pd.DataFrame(data)

# to normalize the posterior probability obtained later on 
def normalize_probabilities(df):
    return df.groupby(['time_period', 'weather'])['posterior_probability'].transform(lambda x: x / x.sum()) # for normalization to sum up = 1, use x / x.sum

# group data by time_period, weather, and congestion_level, and count occurrences
grouped = df.groupby(['time_period', 'weather', 'congestion_level']).size().reset_index(name='count') # count column is added here

# to calculate the prior probability of each congestion_level aka P(Congestion Level)
congestion_level_counts = df['congestion_level'].value_counts() # number of times eg High/Medium/Low appears in dataset
total_count = len(df) # total amount of data collected
prior_prob = congestion_level_counts / total_count
# print("testing", prior_prob[0]) -- output is for P(low) since is '[0]'

# then, calculate the likelihood aka P(Time Period, Weather | Congestion Level)
likelihoods = grouped.groupby(['congestion_level', 'time_period', 'weather'])['count'].sum().reset_index()
total_congestion_level = grouped.groupby('congestion_level')['count'].transform('sum')
likelihoods['probability'] = likelihoods['count'] / total_congestion_level # adding a new column called 'probability'

# now, calculate the evidence P(Time Period, Weather)
evidence_counts = grouped.groupby(['time_period', 'weather'])['count'].sum().reset_index()
evidence_counts['probability'] = evidence_counts['count'] / total_count

# find the the conditional probability using Bayes' Theorem
# P(Congestion Level | Time Period, Weather) = [ P(Time Period, Weather | Congestion Level) * P(Congestion Level) ]/ P(Time Period, Weather)

bayesian_results = []

# eg in grouped, will contain diff rows (since in df format). each rows wld be like this 'Afternoon  Clear  High  1' ==> iterrow() wld loop through each row in grouped
for index, row in grouped.iterrows():
    congestion_level = row['congestion_level']
    time_period = row['time_period']
    weather = row['weather']
    
    # Get likelihood P(Time Period, Weather | Congestion Level)
    likelihood = likelihoods[(likelihoods['congestion_level'] == congestion_level) & 
                             (likelihoods['time_period'] == time_period) & 
                             (likelihoods['weather'] == weather)]['probability'].iloc[0] 
    
    # Get the prior probability P(Congestion Level)
    prior = prior_prob[congestion_level]
    
    # Get the evidence P(Time Period, Weather)
    evidence = evidence_counts[(evidence_counts['time_period'] == time_period) & 
                               (evidence_counts['weather'] == weather)]['probability'].iloc[0]
    
    # Apply Bayes' Theorem
    posterior_probability = (likelihood * prior) / evidence
    bayesian_results.append({'time_period': time_period, 'weather': weather, 
                             'congestion_level': congestion_level, 'posterior_probability': posterior_probability})

# Create a DataFrame with the results
bayesian_df = pd.DataFrame(bayesian_results)

# Normalize the posterior probabilities so they sum to 1
bayesian_df['posterior_probability'] = normalize_probabilities(bayesian_df)

# Display the results
print(bayesian_df)



# NOTES (in Bayes' Theorem):
# P(A | B) = [ P(B ! A)* P(A)] / P(B)
# P(A ! B) = Posterior Probability 
# P(B | A) = Likelihood
# P(A) = Prior Probability
# P(B) = Evidence 

# Pandas dataframe is basically data in like a table format aka w rows and columns