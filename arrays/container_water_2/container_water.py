'''
formula para calcular el area maxima entre dos numeros del arreglo
area=min(a,b) * (bi-ai)
'''


def get_max_water_container(heights: [int]) -> int:
    max_area = 0
    if len(heights) < 2:
        return max_area

    for p1 in range(len(heights)):
        for p2 in range(p1 + 1, len(heights)):
            height = min(heights[p1], heights[p2])
            width = p2 - p1
            area = height * width
            max_area = max(max_area, area)

    return max_area


def get_max_water_container_opt(heights: [int]) -> int:
    max_area = 0
    if len(heights) < 2:
        return max_area

    a = 0
    b = len(heights) - 1

    while a < b:
        height = min(heights[a], heights[b])
        width = b - a
        area = height * width
        max_area = max(max_area, area)
        if heights[a] <= heights[b]:
            a += 1
        else:
            b -= 1
    return max_area
