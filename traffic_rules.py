# Navigation Rules Implementation for ITS
def check_speed_limit(speed, road_type):
    """Check if the vehicle exceeds the speed limit for the given road type."""
    speed_limits = {"expressway": 90, "residential": 50, "school_zone": 40}
    return speed > speed_limits.get(road_type, 50)

def check_signal_compliance(signal, is_moving):
    """Check if the vehicle is violating traffic signals."""
    if signal == "red" and is_moving:
        return "Red light violation"
    if signal == "amber" and is_moving:
        return "Amber light caution violation"
    return None

def check_right_of_way(location, vehicle_action):
    """Check if the vehicle violates right-of-way rules."""
    if location == "pedestrian_crossing" and vehicle_action == "not_yielding":
        return "Violation: Failed to yield at pedestrian crossing"
    if location == "roundabout" and vehicle_action == "not_giving_way":
        return "Violation: Failed to give way at roundabout"
    return None

def check_intersection_logic(is_intersection_blocked, is_entering_intersection):
    """Ensure vehicles don't block intersections."""
    if is_intersection_blocked and is_entering_intersection:
        return "Violation: Blocking intersection"
    return None

def check_traffic_congestion(current_route, congestion_level):
    """Suggest rerouting if congestion is too high."""
    if congestion_level == "high":
        return f"High congestion detected on {current_route}. Consider rerouting."
    return None

navigation_data = [
    {
        "vehicle_id": "A1",
        "speed": 100,
        "road_type": "expressway",
        "signal": "red",
        "is_moving": True,  # Violating red light rule
        "location": "pedestrian_crossing",
        "vehicle_action": "moving_forward",
        "is_intersection_blocked": False,
        "is_entering_intersection": False,
        "current_route": "Route 1",
        "congestion_level": "high",  # Congested route
    },
    {
        "vehicle_id": "B2",
        "speed": 60,  # Exceeding school zone speed limit
        "road_type": "school_zone",
        "signal": "green",
        "is_moving": True,
        "location": "normal",
        "vehicle_action": "moving_forward",
        "is_intersection_blocked": False,
        "is_entering_intersection": False,
        "current_route": "Route 2",
        "congestion_level": "medium",
    },
    {
        "vehicle_id": "C3",
        "speed": 120,  # Exceeding expressway speed limit
        "road_type": "expressway",
        "signal": "green",
        "is_moving": True,
        "location": "normal",
        "vehicle_action": "moving_forward",
        "is_intersection_blocked": False,
        "is_entering_intersection": False,
        "current_route": "Route 1",
        "congestion_level": "high",  # Congested route
    },
    {
        "vehicle_id": "D4",
        "speed": 50,
        "road_type": "residential",
        "signal": "green",
        "is_moving": True,
        "location": "intersection",
        "vehicle_action": "moving_forward",
        "is_intersection_blocked": True,  # Blocking intersection
        "is_entering_intersection": True,
        "current_route": "Route 3",
        "congestion_level": "low",
    },
    {
        "vehicle_id": "E5",
        "speed": 35,
        "road_type": "school_zone",
        "signal": "amber",
        "is_moving": True,  # Moving on amber light instead of stopping
        "location": "normal",
        "vehicle_action": "moving_forward",
        "is_intersection_blocked": False,
        "is_entering_intersection": False,
        "current_route": "Route 2",
        "congestion_level": "medium",
    },
    {
        "vehicle_id": "F6",
        "speed": 85,
        "road_type": "expressway",
        "signal": "green",
        "is_moving": True,
        "location": "normal",
        "vehicle_action": "moving_forward",
        "is_intersection_blocked": False,
        "is_entering_intersection": False,
        "current_route": "Route 1",
        "congestion_level": "high",  # Congested route
    },
    {
        "vehicle_id": "G7",
        "speed": 45,
        "road_type": "residential",
        "signal": "green",
        "is_moving": True,
        "location": "pedestrian_crossing",
        "vehicle_action": "moving_forward",  # Not yielding to pedestrians
        "is_intersection_blocked": False,
        "is_entering_intersection": False,
        "current_route": "Route 3",
        "congestion_level": "low",
    },
    {
        "vehicle_id": "H8",
        "speed": 25,
        "road_type": "school_zone",
        "signal": "green",
        "is_moving": True,
        "location": "normal",
        "vehicle_action": "moving_forward",
        "is_intersection_blocked": False,
        "is_entering_intersection": False,
        "current_route": "Route 2",
        "congestion_level": "medium",
    },
]

# Check Navigation Violations
for vehicle in navigation_data:
    print(f"Checking Vehicle {vehicle['vehicle_id']}:")

    # Speed Limit
    if check_speed_limit(vehicle["speed"], vehicle["road_type"]):
        print(f"- Speeding violation on {vehicle['road_type']}.")

    # Signal Compliance
    signal_violation = check_signal_compliance(vehicle["signal"], vehicle["is_moving"])
    if signal_violation:
        print(f"- {signal_violation}.")

    # Right of Way
    right_of_way_violation = check_right_of_way(vehicle["location"], vehicle["vehicle_action"])
    if right_of_way_violation:
        print(f"- {right_of_way_violation}.")

    # Intersection Logic
    intersection_violation = check_intersection_logic(
        vehicle["is_intersection_blocked"], vehicle["is_entering_intersection"]
    )
    if intersection_violation:
        print(f"- {intersection_violation}.")

    # Traffic Congestion
    congestion_warning = check_traffic_congestion(vehicle["current_route"], vehicle["congestion_level"])
    if congestion_warning:
        print(f"- {congestion_warning}.")

    print("\n")
