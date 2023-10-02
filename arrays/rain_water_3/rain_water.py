'''
calcular_agua_en_cada_caso=min(maxLeft,maxRight)-currentHigh
'''


def get_trapped_rain_water(heights: [int]) -> int:
    total_water = 0
    for p1 in range(len(heights)):
        left_p, right_p = p1, p1
        max_left, max_right = 0, 0

        while left_p >= 0:
            max_left = max(max_left, heights[left_p])
            left_p -= 1
        while right_p < len(heights):
            max_right = max(max_right, heights[right_p])
            right_p += 1

        current_water = min(max_left, max_right) - heights[p1]
        if current_water >= 0:
            total_water += current_water
    return total_water


'''
Logica del algoritmo

1.Identificar el puntero con el valor mas pequeño
2.Es el valor del puntero mayor o igual al maximo en este lado?
    si-> actualizar el maximo en ese lado
    no-> obtner el agua almacenada y sumarla al total
3. Mover el puntero hacia el centro
4. repetir para el otro puntero
'''


def get_trapped_rain_water_opt(heights: [int]) -> int:
    total_water, left, left_max, right_max = 0, 0, 0, 0,
    right = len(heights) - 1

    while left < right:
        if heights[left] <= heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                total_water += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                total_water += right_max - heights[right]
            right -= 1
    return total_water
