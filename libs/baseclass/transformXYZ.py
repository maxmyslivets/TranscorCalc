"""Трансформирование координат координат из одной
системы отсчета координат в другую систему отсчета координат"""


from numpy import array
from libs.baseclass.transdeg import dms_to_rad


def transformXYZ(X, Y, Z, dX, dY, dZ, wX, wY, wZ, m):

    print('\nFunction in work...\n')

    # переводим секунды в радианы
    wX = dms_to_rad([0, 0, wX])
    wY = dms_to_rad([0, 0, wY])
    wZ = dms_to_rad([0, 0, wZ])

    # переводим масштаб с единицы в милионную часть
    m = -m*(10**-6)

    k = array([[X], [Y], [Z]])
    print('\nИсходные координаты:\n', k)

    dk = array([[dX], [dY], [dZ]])
    print('\nСмещение координат:\n', dk)

    w = array(
        [[1, wZ, -wY],
        [-wZ, 1, wX],
        [wY, -wX, 1]]
        )
    print('\nПовороты:\n', w)
    
    k2 = ((1+m)*w).dot(k)+dk

    return k2