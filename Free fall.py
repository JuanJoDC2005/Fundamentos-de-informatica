# Constants
initial_height = 100.0  # Initial height in meters
gravity = 9.81          # Acceleration due to gravity in m/s^2


def position_in_free_fall(time):
    """
    Calculate the position of an object in free fall at a given time.

    The formula used is:
    position = initial_height - (0.5 * gravity * time^2)

    Where:
    - initial_height is the position where the objetct is dropped of.
    - gravity is the acceleration that interacts with the object. (9.81 m/s^2)
    - time is the time in seconds since the object was dropped
    """
    # Calculate the distance fallen due to gravity
    distance_fallen = 0.5 * gravity * (time ** 2)

    # Calculate the current position
    current_position = initial_height - distance_fallen

    return current_position


# Time intervals to check the position (in seconds)
time_intervals = [0, 1, 2, 3, 4, 5]

# Calculate and display the position at each time interval
for time in time_intervals:
    pos = position_in_free_fall(time)
    print(f"At time {time} seconds, the position is {pos:.2f} meters.")
