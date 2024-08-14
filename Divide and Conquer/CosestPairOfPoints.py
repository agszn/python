import math

def closest_pair_of_points(points):
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def closest_pair_rec(Px, Py):
        if len(Px) <= 3:
            min_dist = float('inf')
            for i in range(len(Px)):
                for j in range(i + 1, len(Px)):
                    if distance(Px[i], Px[j]) < min_dist:
                        min_dist = distance(Px[i], Px[j])
                        min_pair = (Px[i], Px[j])
            return min_pair, min_dist

        mid = len(Px) // 2
        Qx = Px[:mid]
        Rx = Px[mid:]

        midpoint = Px[mid][0]
        Qy = list(filter(lambda x: x[0] <= midpoint, Py))
        Ry = list(filter(lambda x: x[0] > midpoint, Py))

        (p1, q1), dist1 = closest_pair_rec(Qx, Qy)
        (p2, q2), dist2 = closest_pair_rec(Rx, Ry)

        if dist1 <= dist2:
            d = dist1
            min_pair = (p1, q1)
        else:
            d = dist2
            min_pair = (p2, q2)

        strip = [p for p in Py if abs(p[0] - midpoint) < d]

        min_dist = d
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                p, q = strip[i], strip[j]
                dst = distance(p, q)
                if dst < min_dist:
                    min_dist = dst
                    min_pair = (p, q)

        return min_pair, min_dist

    Px = sorted(points, key=lambda x: x[0])
    Py = sorted(points, key=lambda x: x[1])

    return closest_pair_rec(Px, Py)
