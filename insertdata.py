
def InsertData():
    import numpy as np
    import pandas as pd

    # Read ET_a data from Excel file
    et_data = pd.read_excel('2003-2018.xlsx', sheet_name='Sheet5', usecols='H', skiprows=1, nrows=15)
    ET_a = et_data.values.flatten()
    
    kc = np.array([0.9, 0.8, 0.95, 0.85])
    ET_max = ET_a.reshape(-1, 1) * kc.reshape(1, -1)

    ET_max_wheat = ET_max[:,0]
    ET_max_maize = ET_max[:,1]
    ET_max_potato = ET_max[:,2]
    ET_max_barley = ET_max[:,3]
    
    ch_wheat = 0.35
    ch_barley = 0.4
    ch_maize = 0.45
    ch_potato = 0.4
    ct_wheat = 0.1
    ct_barley = 0.1
    ct_maize = 0.6
    ct_potato = 0.6

    k_wheat = 1.17
    k_barley = 0.65
    k_maize = 1.9
    k_potato = 1.9

    G_wheat = 240
    G_barley = 130
    G_maize = 135
    G_potato = 120

    Rse = 308.83
    yo = 202.16
    yc = 392.25
    Rs = 648.03
    ea = 42.4
    ed = 21.2

    F = (Rse - 0.5 * Rs) / (0.8 * Rse)
    Yo = F * yo + (1 - F) * yc

    ymax_wheat = k_wheat * ch_wheat * ct_wheat * G_wheat * Yo * ET_max_wheat / (ea - ed)
    ymax_barley = k_barley * ch_barley * ct_barley * G_barley * Yo * ET_max_barley / (ea - ed)
    ymax_maize = k_maize * ch_maize * ct_maize * G_maize * Yo * ET_max_maize / (ea - ed)
    ymax_potato = k_potato * ch_potato * ct_potato * G_potato * Yo * ET_max_potato / (ea - ed)

    return ymax_barley,ymax_maize,ymax_potato,ymax_wheat
