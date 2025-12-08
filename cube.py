"""
Köşesi kesilmiş birim küp geometrisi
"""

def get_cut_cube_vertices():
    """Köşesi kesilmiş küpün köşe noktaları"""
    return [
        [0.5, 0.0, 0.0],  # 0 - kesilmiş köşe (x)
        [0.0, 0.5, 0.0],  # 1 - kesilmiş köşe (y) 
        [0.0, 0.0, 0.5],  # 2 - kesilmiş köşe (z)

        [1.0, 0.0, 0.0],  # 3
        [1.0, 1.0, 0.0],  # 4
        [0.0, 1.0, 0.0],  # 5 

        [1.0, 0.0, 1.0],  # 6
        [1.0, 1.0, 1.0],  # 7
        [0.0, 1.0, 1.0],  # 8
        [0.0, 0.0, 1.0],  # 9
    ]


def get_cut_cube_edges():
    """Küpün kenarları"""
    return [
        # Kesilmiş üçgen yüz
        [0, 1], [1, 2], [2, 0],

        # Kesik noktadan diğer köşelere
        [0, 3], [0, 6],
        [1, 5], [1, 8],
        [2, 9],

        # Alt yüz (z=0)
        [3, 4], [4, 5], [5, 1], [1, 0], [0, 3],

        # Üst yüz (z=1)
        [6, 7], [7, 8], [8, 1], [9, 2], [2, 0], [0, 6], [9, 6],

        # Dikey kenarlar
        [3, 6], [4, 7], [5, 8], [9, 2]
    ]
