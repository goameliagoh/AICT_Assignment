from logic import *

# Define symbols for each condition
speed_limit_exceeded = Symbol("speed_limit_exceeded")
road_type_expressway = Symbol("road_type_expressway")
road_type_residential = Symbol("road_type_residential")
road_type_school_zone = Symbol("road_type_school_zone")
signal_red = Symbol("signal_red")
signal_amber = Symbol("signal_amber")
is_moving = Symbol("is_moving")
location_pedestrian_crossing = Symbol("location_pedestrian_crossing")
location_roundabout = Symbol("location_roundabout")
vehicle_action_not_yielding = Symbol("vehicle_action_not_yielding")
vehicle_action_not_giving_way = Symbol("vehicle_action_not_giving_way")
is_intersection_blocked = Symbol("is_intersection_blocked")
is_entering_intersection = Symbol("is_entering_intersection")
congestion_level_high = Symbol("congestion_level_high")

# Define knowledge base for traffic rules
knowledge = And(
    # Speed Limit Rules
    Implication(And(road_type_expressway, speed_limit_exceeded), Symbol("speeding_violation_expressway")),
    Implication(And(road_type_residential, speed_limit_exceeded), Symbol("speeding_violation_residential")),
    Implication(And(road_type_school_zone, speed_limit_exceeded), Symbol("speeding_violation_school_zone")),

    # Signal Compliance Rules
    Implication(And(signal_red, is_moving), Symbol("red_light_violation")),
    Implication(And(signal_amber, is_moving), Symbol("amber_light_caution_violation")),

    # Right of Way Rules
    Implication(And(location_pedestrian_crossing, vehicle_action_not_yielding), Symbol("failed_to_yield_at_pedestrian_crossing")),
    Implication(And(location_roundabout, vehicle_action_not_giving_way), Symbol("failed_to_give_way_at_roundabout")),

    # Intersection Logic Rule
    Implication(And(is_intersection_blocked, is_entering_intersection), Symbol("blocking_intersection")),

    # Traffic Congestion Rule
    Implication(congestion_level_high, Symbol("high_congestion_detected"))
)

# Navigation data
navigation_data = [
    {"vehicle_id": "A1", "speed_limit_exceeded": True, "road_type_expressway": True, "road_type_residential": False, "road_type_school_zone": False, "signal_red": False, "signal_amber": False, "is_moving": True, "location_pedestrian_crossing": True, "vehicle_action_not_yielding": True, "is_intersection_blocked": False, "is_entering_intersection": False, "congestion_level_high": True},
    {"vehicle_id": "B2", "speed_limit_exceeded": True, "road_type_expressway": False, "road_type_residential": False, "road_type_school_zone": True, "signal_red": False, "signal_amber": False, "is_moving": True, "location_pedestrian_crossing": False, "vehicle_action_not_yielding": False, "is_intersection_blocked": False, "is_entering_intersection": False, "congestion_level_high": False},
    {"vehicle_id": "C3", "speed_limit_exceeded": True, "road_type_expressway": True, "road_type_residential": False, "road_type_school_zone": False, "signal_red": False, "signal_amber": False, "is_moving": True, "location_pedestrian_crossing": False, "vehicle_action_not_yielding": False, "is_intersection_blocked": False, "is_entering_intersection": False, "congestion_level_high": True},
    {"vehicle_id": "D4", "speed_limit_exceeded": False, "road_type_expressway": False, "road_type_residential": True, "road_type_school_zone": False, "signal_red": False, "signal_amber": False, "is_moving": True, "location_pedestrian_crossing": False, "vehicle_action_not_yielding": False, "is_intersection_blocked": True, "is_entering_intersection": True, "congestion_level_high": False},
    {"vehicle_id": "E5", "speed_limit_exceeded": False, "road_type_expressway": False, "road_type_residential": False, "road_type_school_zone": True, "signal_red": False, "signal_amber": True, "is_moving": True, "location_pedestrian_crossing": False, "vehicle_action_not_yielding": False, "is_intersection_blocked": False, "is_entering_intersection": False, "congestion_level_high": False},
    {"vehicle_id": "F6", "speed_limit_exceeded": False, "road_type_expressway": True, "road_type_residential": False, "road_type_school_zone": False, "signal_red": False, "signal_amber": False, "is_moving": True, "location_pedestrian_crossing": False, "vehicle_action_not_yielding": False, "is_intersection_blocked": False, "is_entering_intersection": False, "congestion_level_high": True},
    {"vehicle_id": "G7", "speed_limit_exceeded": False, "road_type_expressway": False, "road_type_residential": True, "road_type_school_zone": False, "signal_red": True, "signal_amber": False, "is_moving": True, "location_pedestrian_crossing": True, "vehicle_action_not_yielding": True, "is_intersection_blocked": False, "is_entering_intersection": False, "congestion_level_high": False},
    {"vehicle_id": "H8", "speed_limit_exceeded": False, "road_type_expressway": False, "road_type_residential": False, "road_type_school_zone": True, "signal_red": False, "signal_amber": False, "is_moving": True, "location_pedestrian_crossing": False, "vehicle_action_not_yielding": False, "is_intersection_blocked": False, "is_entering_intersection": False, "congestion_level_high": False}
]

# Helper function to create a model from vehicle data
def create_model(vehicle_data):
    model = {
        speed_limit_exceeded: vehicle_data["speed_limit_exceeded"],
        road_type_expressway: vehicle_data["road_type_expressway"],
        road_type_residential: vehicle_data["road_type_residential"],
        road_type_school_zone: vehicle_data["road_type_school_zone"],
        signal_red: vehicle_data["signal_red"],
        signal_amber: vehicle_data["signal_amber"],
        is_moving: vehicle_data["is_moving"],
        location_pedestrian_crossing: vehicle_data["location_pedestrian_crossing"],
        location_roundabout: False,  
        vehicle_action_not_yielding: vehicle_data["vehicle_action_not_yielding"],
        vehicle_action_not_giving_way: False,  
        is_intersection_blocked: vehicle_data["is_intersection_blocked"],
        is_entering_intersection: vehicle_data["is_entering_intersection"],
        congestion_level_high: vehicle_data["congestion_level_high"]
    }
    return model

# Check violations for each vehicle
for vehicle in navigation_data:
    print(f"Violations for Vehicle {vehicle['vehicle_id']}:")
    model = create_model(vehicle)
    for violation in ["speeding_violation_expressway", "speeding_violation_residential", "speeding_violation_school_zone", "red_light_violation", "amber_light_caution_violation", "failed_to_yield_at_pedestrian_crossing", "failed_to_give_way_at_roundabout", "blocking_intersection", "high_congestion_detected"]:
        if model_check(knowledge, Symbol(violation), model):
            print(f"- {violation.replace('_', ' ').capitalize()}")
    print()
