"""
Matris işlemleri ve izometrik projeksiyon dönüşümleri
"""

import math


def matrix_multiply(matrix_a, matrix_b):
    """İki matrisi çarpar"""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result


def get_isometric_matrix():


    # 1) X ekseni -35.26 derece (üstten hafif aşağı bakış)
    angle_x = math.radians(-35.26)
    cos_x = math.cos(angle_x)
    sin_x = math.sin(angle_x)

    rotate_x = [
        [1, 0,      0,      0],
        [0, cos_x, -sin_x,  0],
        [0, sin_x,  cos_x,  0],
        [0, 0,      0,      1]
    ]

    # 2) Y ekseni +45 derece (sol-üst izometrik açı)
    angle_y = math.radians(45)
    cos_y = math.cos(angle_y)
    sin_y = math.sin(angle_y)

    rotate_y = [
        [cos_y, 0, sin_y, 0],
        [0,     1, 0,     0],
        [-sin_y,0, cos_y, 0],
        [0,     0, 0,     1]
    ]

    # DOĞRU SIRA
    # ÖNCE X → SONRA Y
    T_iso = matrix_multiply(rotate_y, rotate_x)
    return T_iso


def translate_point(point, tx, ty, tz):
    """Bir noktayı öteler"""
    translation_matrix = [
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ]

    point_matrix = [[point[0]], [point[1]], [point[2]], [1]]
    result = matrix_multiply(translation_matrix, point_matrix)

    return [result[0][0], result[1][0], result[2][0]]


def apply_isometric_projection(point):
    """İzometrik projeksiyon uygular"""
    homogeneous_point = [[point[0]], [point[1]], [point[2]], [1]]
    T_iso = get_isometric_matrix()
    result = matrix_multiply(T_iso, homogeneous_point)

    return [result[0][0], result[1][0], result[2][0]]
