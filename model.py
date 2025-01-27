from pomegranate import *

time_of_day = Node(DiscreteDistribution({
    "morning": 0.292135,
    "afternoon": 0.382022,
    "evening" :0.325843
}))

weather = Node(DiscreteDistribution({
    "clear": 0.314607,
    "clouds": 0.213483,
    "drizzle": 0.123596,
    "rain": 0.224719,
    "thunderstorm": 0.123596
}))

