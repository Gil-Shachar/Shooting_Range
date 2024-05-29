import matplotlib.pyplot as plt
import numpy as np

# Data for the hits and the target
x_hits = []
y_hits = []
target = []

number_of_hits = int(input("What's the number of hits? "))

for i in range(number_of_hits):
    print(f"{i+1} hit: ")
    x_coordinate = float(input("X coordinate: "))
    y_coordinate = float(input("Y coordinate: "))
    x_hits.append(x_coordinate)
    y_hits.append(y_coordinate)

x_target = float(input("X coordinate of target? "))
y_target = float(input("Y coordinate of target? "))
target.append(x_target)
target.append(y_target)


def find_closest_hit(x_hits, y_hits, target):
    distances = np.sqrt((np.array(x_hits) - target[0])**2 + (np.array(y_hits) - target[1])**2)
    print(distances)
    min_distance_index = np.argmin(distances)
    return min_distance_index, distances[min_distance_index]


# Find the closest hit
closest_hit_index, closest_hit_distance = find_closest_hit(x_hits, y_hits, target)
print(f"The closest hit is at ({x_hits[closest_hit_index]}, {y_hits[closest_hit_index]}) with a distance of {closest_hit_distance:.2f}.")

# Create the plot
plt.figure(figsize=(8, 8))

# Plot the hits
plt.scatter(x_hits, y_hits, color='blue', label='Hits')

# Plot the target
plt.scatter(target[0], target[1], color='red', marker='*', s=200, label='Target')

# Add a circle for the target radius
target_radius = plt.Circle((target[0], target[1]), 1, color='red', fill=False, linestyle='--', linewidth=1.5)
plt.gca().add_patch(target_radius)

# Set the limits of the plot to ensure all points and the circle are visible
plt.xlim(min(x_hits + [target[0]]) - 2, max(x_hits + [target[0]]) + 2)
plt.ylim(min(y_hits + [target[1]]) - 2, max(y_hits + [target[1]]) + 2)

# Adding titles and labels
plt.title('Shooting Range Hits')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')

# Adding a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.axis('equal')  # Ensure the aspect ratio is equal to see the circle properly
plt.show()
