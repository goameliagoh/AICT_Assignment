import pandas as pd # pandas makes code cleaner, and output easier to be organized

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

df = pd.DataFrame(data) # convert collected data to dataframe format

# group by time_period, weather, and congestion_level, and count occurrences
# --- df.groupby: group data according to the unique combinations ==> eg Afternoon Clear Low is 1 group, Afternoon Clear High is 1 group
# --- .size(): count number of rows in each group (basically seeing how many rows of Afternoon Clear Low appears. Eg Afternoon Clear Low appears 5 times)
# --- name='count': is just to store the amount of times the row appears for each unique group (aka 5^)
# --- .reset_index() is to flatten the  indexing (see below)
grouped = df.groupby(['time_period', 'weather', 'congestion_level']).size().reset_index(name='count')



# ---------- for indepdent probabilities ---------------------
total_entries = len(df)

# Calculate P(time_period)
p_time_period = df["time_period"].value_counts() / total_entries
print("\nIndependent probabilities for time_period:")
print(p_time_period.to_string()) # if not, output when u just print(p_time_period) wld include "Name: count, dtype: float64"

# Calculate P(weather)
p_weather = df["weather"].value_counts() / total_entries
print("\nIndependent probabilities for weather:")
print(p_weather.to_string())

# Calculate P(congestion_level)
p_congestion_level = df["congestion_level"].value_counts() / total_entries
print("\nIndependent probabilities for congestion_level:")
print(p_congestion_level.to_string())
#  --------------------------------------------------------------



#  ------------------- for conditional probability ----------------------------
# group by time_period and weather to calculate conditional probabilities
# --- "grouped['P(congestion_level|time_period,weather)']" is the code to ADD a new column to our "grouped" dataframe and rn, this whole line of code is giving this new column VALUES
# --- transforms: a Pandas method to allow you to apply function like lambda to a group of data. it will apply the transformation to each unique group and return a new df of the same shape, js diff values. in this case, 'count' represents the groups where the transformation is applied to
# --- DONT HAVE congestion_level in the grouped.groupby(['time_period', 'weather']) bc congestion_level is what we r tryna find --> so we only grp data by time period and weather 
# --- overall, this is firstly grouping your data into unique group combinations regarding the time and weather --> then. we will focus on the 'count' column --> and therefore the 'count' column is where we apply our transformations on. 
# --- lamnda = just a simpler way to do quick operations in Python
# --- the lamba x : x / x.sum is applied for each unique group (aka each unique combo of time and weather ), not the whole set of data..
grouped['P(congestion_level|time_period,weather)'] = grouped.groupby(['time_period', 'weather'])['count'].transform(lambda x: x / x.sum())
#  --------------------------------------------------------------------------------



# # Round the conditional probabilities to 2 decimal places (js rmv this line of code if dw in 2dp) <== dw round so cn be more accurate?
# grouped['P(congestion_level|time_period,weather)'] = grouped['P(congestion_level|time_period,weather)'].round(2)

# Display the result
print()
print(grouped)

# -- TESTING OUTPUT
# print(grouped['P(congestion_level|time_period,weather)']) -- output is just the conditional probabilities calculated for P(congestion | time, weather)




#  ---------------------- NOTES --------------------------------------
# some of the conditional probability output eg:
# P(Low | Drizzle, Evening) = 0.33
# P(Medium | Drizzle, Evening) = 0.33
# P(High | Drizzle, Evening) = 0.33
# aka the total ( 0.33 + 0.33 + 0.33 ) dont add up to be = 1 bc the values are not exactly 0.33, it is 0.333333333333333333333 aka a lot a lot of decimals. so total not exactly = 1



# how to add columns in Pandas?
# 1. to add new columns in pandas ==> df['new_column'] = some_calculation_or_values
# 2. can use ==> reset_index(name='new_column') <== but only for situations where you work with grouped data eg you use .groupby() and .size()


# before reset_index:
# time_period  weather
# Afternoon    Clear      1
#              Rainy      1
# Morning      Cloudy     1
#              Sunny      1
# dtype: int64


# after reset_index:
#    time_period weather  count
# 0   Afternoon   Clear      1
# 1   Afternoon   Rainy      1
# 2    Morning   Cloudy     1
# 3    Morning   Sunny      1
