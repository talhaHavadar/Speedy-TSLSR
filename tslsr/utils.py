import math

def get_bigger_rect(r1, r2):
    """
        Returns bigger rectangle.
        If given two rectangles have the same size then returns first one
    """
    r1_x, r1_y, r1_x2, r1_y2, r1_w, r1_h = __get_rectangle_with_bounds(r1)
    r2_x, r2_y, r2_x2, r2_y2, r2_w, r2_h = __get_rectangle_with_bounds(r2)
    a1 = r1_w * r2_h
    a2 = r2_w * r2_h
    if a1 >= a2:
        return r1
    else:
        return r2

def get_distance_between_points(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    return math.sqrt(((x2-x1) ** 2) + ((y2-y1) ** 2))

def is_similar_rectangle(r1, r2, max_dist):
    max_area_diff = (max_dist + 1) ** 2
    r1_x, r1_y, r1_x2, r1_y2, r1_w, r1_h = __get_rectangle_with_bounds(r1)
    r2_x, r2_y, r2_x2, r2_y2, r2_w, r2_h = __get_rectangle_with_bounds(r2)
    distance = get_distance_between_points((r1_x, r1_y), (r2_x, r2_y))
    return distance <= max_dist and ((r1_w * r1_h) - (r2_w * r2_h)) <= max_area_diff

def eliminate_child_rects(rects):
    rectDict = dict()
    newRects = []
    has_child = False
    rects = list(set(rects))
    for i in range(len(rects)):
        r1 = rects[i]
        for j in range(len(rects)):
            r2 = rects[j]
            if is_same_rectangle(r1, r2):
                continue
            if is_contains_rectangle(rects[i], rects[j]):
                if i not in rectDict:
                    rectDict[i] = [rects[j]]
                else:
                    rectDict[i].append(rects[j])
            elif is_similar_rectangle(r1, r2, 5):
                eliminatedR = None
                if get_bigger_rect(r1, r2) == r1:
                    index = i
                    eliminatedR = r2
                else:
                    index = j
                    eliminatedR = r1
                if index not in rectDict:
                    rectDict[index] = [eliminatedR]
                else:
                    rectDict[index].append(eliminatedR)
    print(rects)
    print(rectDict)
    for (k, v) in rectDict.items():
        for r in v:
            if r in rects:
                rects.remove(r)
    for r in rects:
        newRects.append(r)
    return newRects

def is_same_rectangle(r1, r2):
    r1_x, r1_y, r1_x2, r1_y2, r1_w, r1_h = __get_rectangle_with_bounds(r1)
    r2_x, r2_y, r2_x2, r2_y2, r2_w, r2_h = __get_rectangle_with_bounds(r2)
    if r1_x == r2_x and r1_y == r2_y and r1_x2 == r2_x2 and r1_y2 == r2_y2:
        return True
    return False

def is_contains_rectangle(r1, r2):
    """
        Looks the position of r2
        if r2 is inside of the r1 returns True else return False
    """
    r1_x, r1_y, r1_x2, r1_y2, r1_w, r1_h = __get_rectangle_with_bounds(r1)
    r2_x, r2_y, r2_x2, r2_y2, r2_w, r2_h = __get_rectangle_with_bounds(r2)
    if r1_x == r2_x and r1_y == r2_y and r1_x2 == r2_x2 and r1_y2 == r2_y2:
        return False
    return r2_x >= r1_x and r2_y >= r1_y and r2_w * r2_h <= r1_w * r1_h

def __get_rectangle_with_bounds(rect):
    x, y, w, h = rect
    x2 = x + w
    y2 = y + h
    return (x, y, x2, y2, w, h)
