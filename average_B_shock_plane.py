import numpy as np
import pyPLUTO as pp


def average_B_shock_plane(data_file_name, shock_direction, D):
    average_index = 0.
    average_B = 0
    x_count = 0
    y_count = 0
    z_count = 0
    total_count = 0

    B = np.sqrt((D.bx1*D.bx1 + D.bx2*D.bx2 + D.bx3*D.bx3)*4.*3.14)

    input_file = open(data_file_name, 'r')

    for line in input_file:
        data = line.split()
        data = [float(data[i]) for i in range(len(data))]

        if shock_direction == 'x': y_count = 0
        if shock_direction == 'y' or shock_direction == 'z': x_count = 0

        for i in range(0, len(data)):
            index = data[i] - 1.
            if shock_direction == 'x':
                x = int(index)
                y = y_count
                z = z_count
            elif shock_direction == 'y':
                x = x_count
                y = int(index)
                z = z_count
            else:
                x = x_count
                y = y_count
                z = int(index)
            average_index = average_index + index    
            average_B = average_B + B[x, y, z]
            total_count += 1

            if shock_direction == 'x': y_count += 1
            if shock_direction == 'y' or shock_direction == 'z': x_count += 1

        if shock_direction == 'x' or shock_direction == 'y': z_count += 1
        if shock_direction == 'z': y_count += 1

    print('Average index of shock:', average_index/total_count)    
    print('Average B along shock plane:', average_B/total_count)    

    input_file.close()


if __name__ == '__main__':

    wdir = '/home/mvorster/PLUTO/Shock_turbulence/Results/Run_15_b'
    file_time = 7
    shock_direction = 'x'

    if not wdir[-1] == '/':
        wdir = wdir + '/'

    D = pp.pload(file_time, w_dir=wdir + 'output/')
    data_file_name = wdir + 'shock_plane_' + str(file_time) + '.txt'

    average_B_shock_plane(data_file_name, shock_direction, D)
                 
