import numpy as np
import math
def translate(x=0.0,y=0.0,z=0.0,data_type="float32"):
    'Return a translate matrix, translate distance is (x,y,z)'
    matrix =  np.mat([
        [1.0, 0.0, 0.0, x],
        [0.0, 1.0, 0.0, y],
        [0.0, 0.0, 1.0, z],
        [0.0, 0.0, 0.0, 1.0]
    ],dtype=data_type).transpose()
    return matrix
def scale(scale_x=1.0,scale_y=1.0,scale_z=1.0,data_type="float32"):
    'Return a scale matrix, each coordinate component will scale as (scale_x,scale_y,scale_z)'
    matrix =  np.mat([
        [scale_x, 0.0, 0.0, 0.0],
        [0.0, scale_y, 0.0, 0.0],
        [0.0, 0.0, scale_z, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ],dtype=data_type).transpose()
    return matrix
def rotate(rotate_x=0.0,rotate_y=0.0,rotate_z=0.0,data_type="float32"):
    'Return a rotate matrix'
    mat_z = np.mat([
        [math.cos(rotate_z), -math.sin(rotate_z), 0.0, 0.0],
        [math.sin(rotate_z),  math.cos(rotate_z), 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ],dtype=data_type).transpose()
    mat_x = np.mat([
        [1.0, 0.0, 0.0, 0.0],
        [0.0,  math.cos(rotate_x),  -math.sin(rotate_x), 0.0],
        [0.0,  math.sin(rotate_x),  math.cos(rotate_x), 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ],dtype=data_type).transpose()
    mat_y = np.mat([
        [math.cos(rotate_y), 0.0, -math.sin(rotate_y), 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [math.sin(rotate_y), 0.0,  math.cos(rotate_y), 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ],dtype=data_type).transpose()
    matrix = mat_z * mat_y * mat_x
    return matrix
