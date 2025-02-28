import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force(points):
    def_dist = float("inf")
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dis=distance(points[i], points[j])
            def_dist = min(def_dist,dis)
    return def_dist

def closest_pair(points):
    if len(points) <= 3:
        return brute_force(points)
    
    mid = len(points) // 2  
    xofmid= points[mid][0]

    # Recursively call closest_pair on the sorted left and right halves
    left_half = points[:mid]  
    right_half = points[mid:]  
    d1 = closest_pair(left_half)
    d2 = closest_pair(right_half)
    d = min(d1, d2)

    # Create a strip containing points close to the middle line
    strip = [p for p in points if abs(p[0] - xofmid) < d]
    strip.sort(key=lambda p: p[1])  # Sort by y-coordinate

    # Check pairs in the strip
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):  # Check at most 6 ahead
            d = min(d, distance(strip[i], strip[j]))

    return d

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]

# Sort points by x-coordinate before passing to closest_pair
sorted_points = sorted(points, key=lambda p: p[0])  
print(closest_pair(sorted_points))
