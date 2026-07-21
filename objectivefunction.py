def objectivefunction (Ks_wheat, phi_wheat, beta_wheat, s_h_wheat, s_w_wheat,s_star_wheat, s_fc_wheat, Ks_maize, phi_maize, beta_maize, s_h_maize, s_w_maize, s_star_maize,\
                       s_fc_maize, Ks_potato, phi_potato, beta_potato, s_h_potato, s_w_potato,s_star_potato, s_fc_potato, Ks_barley, phi_barley, beta_barley, s_h_barley, \
                       s_w_barley,s_star_barley, s_fc_barley,yield_wheat, I_wheat,yield_maize, I_maize ,yield_potato, I_potato ,yield_barley, I_barley,\
                       landa,x1,x2,x3,x4,x5,z1,z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12, z13, z14, z15, z16, z17, z18, z19, z20, z21, z22, z23, z24, z25,I, I_sum, \
    I_behbahan1, A_behbahan, I_Jayezan1, A_Jayezan, A_ramhormoz, I_ramhormoz1, A_ramshir, I_ramshir1, A_shadegan, \
    I_shadegan1, I_behbahan2, I_Jayezan2, I_ramhormoz2, I_ramshir2, I_shadegan2, I_behbahan3, I_Jayezan3, I_ramhormoz3, \
    I_ramshir3, I_shadegan3, I_behbahan4, I_Jayezan4, I_ramhormoz4, I_ramshir4, I_shadegan4, I_behbahan5, I_Jayezan5, \
    I_ramhormoz5, I_ramshir5, I_shadegan5, I_behbahan6, I_Jayezan6, I_ramhormoz6, I_ramshir6, I_shadegan6, I_behbahan7, \
    I_Jayezan7, I_ramhormoz7, I_ramshir7, I_shadegan7, I_behbahan8, I_Jayezan8, I_ramhormoz8, I_ramshir8, I_shadegan8, \
    I_behbahan9, I_Jayezan9, I_ramhormoz9, I_ramshir9, I_shadegan9, I_behbahan10, I_Jayezan10, I_ramhormoz10, I_ramshir10, \
    I_shadegan10, I_behbahan11, I_Jayezan11, I_ramhormoz11, I_ramshir11, I_shadegan11, I_behbahan12, I_Jayezan12, \
    I_ramhormoz12, I_ramshir12, I_shadegan12, I_behbahan13, I_Jayezan13, I_ramhormoz13, I_ramshir13, I_shadegan13, \
    I_behbahan14, I_Jayezan14, I_ramhormoz14, I_ramshir14, I_shegan14, I_behbahan15, I_Jayezan15, I_ramhormoz15, \
    I_ramshir15, I_shadegan15, I_behbahan16, I_Jayezan16, I_ramhormoz16, I_ramshir16, I_shadegan16, I_behbahan17, \
    I_Jayezan17, I_ramhormoz17, I_ramshir17, I_shadegan17, I_behbahan18, I_Jayezan18, I_ramhormoz18, I_ramshir18, \
    I_shadegan18, I_behbahan19, I_Jayezan19, I_ramhormoz19, I_ramshir19, I_shadegan19, I_behbahan20, I_Jayezan20, \
    I_ramhormoz20, I_ramshir20, I_shadegan20, I_behbahan21, I_Jayezan21, I_ramhormoz21, I_ramshir21, I_shadegan21, \
    I_behbahan22, I_Jayezan22, I_ramhormoz22, I_ramshir22, I_shadegan22, I_behbahan23, I_Jayezan23, I_ramhormoz23, \
    I_ramshir23, I_shadegan23, I_behbahan24, I_Jayezan24, I_ramhormoz24, I_ramshir24, I_shadegan24, I_behbahan25, \
    I_Jayezan25, I_ramhormoz25, I_ramshir25, I_shadegan25):

    import numpy as np
    import matplotlib.pyplot as plt
    # scenario 1

    # agent number 1: behbahan agriculture
    o1_scenario1 = np.sum(x1 * z1) * A_behbahan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario1 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I)
    if np.sum(x1 * I) > I_behbahan1:
        o1_scenario1 =o1_scenario1 - ( I_sum-I_behbahan1)*10**25 # Set cost to negative infinity if constraint is violated
    #[(i-1)*4:i*4]
    # agent number 2: Jayezan agriculture 
    o2_scenario1 = np.sum(x2 * z1) * A_Jayezan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario1 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x2 * I) > I_Jayezan1:
        o2_scenario1 =  o2_scenario1-( I_sum-I_Jayezan1)*10**25# Set cost to negative infinity if constraint is violated
    # agent number 3: ramhormoz agriculture
    o3_scenario1 = np.sum(x3 * z1) * A_ramhormoz
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario1 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x3 * I) > I_ramhormoz1:
        o3_scenario1 = o3_scenario1-( I_sum-I_ramhormoz1)*10**25 # Set cost to negative infinity if constraint is violated
    # agent number 4: ramshir agriculture
    o4_scenario1 = np.sum(x4 * z1) * A_ramshir
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario1 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x4 * I) > I_ramshir1:
        o4_scenario1 = o4_scenario1-(I_sum-I_ramshir1)*10**25 # Set cost to negative infinity if constraint is violated
    # agent number 5: shadegan agriculture
    o5_scenario1 = np.sum(x5 * z1) * A_shadegan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario1 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x5 * I) > I_shadegan1:
        o5_scenario1 = o5_scenario1-( I_sum-I_shadegan1)*10**25 # Set cost to negative infinity if constraint is violated

    # scenario 2

    # agent number 1: behbahan agriculture
    o1_scenario2 = np.sum(x1 * z2) * A_behbahan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario2 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x1 * I) > I_behbahan2:
        o1_scenario2 = o1_scenario2-( I_sum-I_behbahan2)*10**25 # Set cost to negative infinity if constraint is violated
    # agent number 2: Jayezan agriculture
    o2_scenario2 = np.sum(x2 * z2) * A_Jayezan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario2 += 1000 *(np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x2 * I) > I_Jayezan2:
        o2_scenario2 = o2_scenario2-(I_sum-I_Jayezan2) *10**25# Set cost to negative infinity if constraint is violated
    # agent number 3: ramhormoz agriculture
    o3_scenario2 = np.sum(x3 * z2) * A_ramhormoz
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario2 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x3 * I) > I_ramhormoz2:
        o3_scenario2 = o3_scenario2-( I_sum-I_ramhormoz2)*10**25 # Set cost to negative infinity if constraint is violated
    # agent number 4: ramshir agriculture
    o4_scenario2 = np.sum(x4 * z2) * A_ramshir
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario2 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x4 * I) > I_ramshir2:
        o4_scenario2 = o4_scenario2-( I_sum-I_ramshir2) *10**13# Set cost to negative infinity if constraint is violated
    # agent number 5: shadegan agriculture
    o5_scenario2 = np.sum(x5 * z2) * A_shadegan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario2 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x5 * I) > I_shadegan2:
        o5_scenario2 = o5_scenario2-( I_sum-I_shadegan2)*10**25 # Set cost to negative infinity if constraint is violated

    # Scenario 3

    # agent number 1: behbahan agriculture
    o1_scenario3 = np.sum(x1 * z3) * A_behbahan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario3 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x1 * I) > I_behbahan3:
        o1_scenario3 = o1_scenario3-( I_sum-I_behbahan3)*10**13
    # agent number 2: Jayezan agriculture
    o2_scenario3 = np.sum(x2 * z3) * A_Jayezan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario3 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x2 * I) > I_Jayezan3:
        o2_scenario3 = o2_scenario3 -( I_sum-I_Jayezan3)*10**13
    # agent number 3: ramhormoz agriculture
    o3_scenario3 = np.sum(x3 * z3) * A_ramhormoz
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario3 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x3 * I) > I_ramhormoz3:
        o3_scenario3 = o3_scenario3-( I_sum-I_ramhormoz3)*10**13
    # agent number 4: ramshir agriculture
    o4_scenario3 = np.sum(x4 * z3) * A_ramshir
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario3 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x4 * I) > I_ramshir3:
        o4_scenario3 = o4_scenario3-( I_sum-I_ramshir3)*10**13
    # agent number 5: shadegan agriculture
    o5_scenario3 = np.sum(x5 * z3) * A_shadegan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario3 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x5 * I) > I_shadegan3:
        o5_scenario3 = o5_scenario3-(I_sum-I_shadegan3)*10**13


    # Scenario 4
    # agent number 1: behbahan agriculture
    o1_scenario4 = np.sum(x1 * z4) * A_behbahan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario4 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x1 * I) > I_behbahan4:
        o1_scenario4 =  o1_scenario4-( I_sum-I_behbahan4)*10**13
    # agent number 2: Jayezan agriculture
    o2_scenario4 = np.sum(x2 * z4) * A_Jayezan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario4 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x2 * I) > I_Jayezan4:
        o2_scenario4 = o2_scenario4 -( I_sum-I_Jayezan4)*10**13
    # agent number 3: ramhormoz agriculture
    o3_scenario4 = np.sum(x3 * z4) * A_ramhormoz
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario4 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x3 * I) > I_ramhormoz4:
        o3_scenario4 = o3_scenario4-( I_sum-I_ramhormoz4)*10**13
    # agent number 4: ramshir agriculture
    o4_scenario4 = np.sum(x4 * z4) * A_ramshir
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario4 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x4 * I) > I_ramshir4:
        o4_scenario4 = o4_scenario4-( I_sum-I_ramshir4)*10**13
    # agent number 5: shadegan agriculture
    o5_scenario4 = np.sum(x5 * z4) * A_shadegan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario4 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x5 * I) > I_shadegan4:
        o5_scenario4 = o5_scenario4-( I_sum-I_shadegan4)*10**13

        # agent number 1: behbahan agriculture

    o1_scenario5 = np.sum(x1 * z5) * A_behbahan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario5 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x * I) <= I_bar_behbahan
    if np.sum(x1 * I) > I_behbahan5:
        o1_scenario5 = o1_scenario5-( I_sum-I_behbahan5)*10**25 # Set cost to negative infinity if constraint is violated
    # agent number 2: Jayezan agriculture
    o2_scenario5 = np.sum(x2 * z5) * A_Jayezan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario5 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x * I) <= I_bar_behbahan
    if np.sum(x2 * I) > I_Jayezan5:
        o2_scenario5 = o2_scenario5-(I_sum-I_Jayezan5) *10**25# Set cost to negative infinity if constraint is violated
    # agent number 3: ramhormoz agriculture
    o3_scenario5 = np.sum(x3 * z5) * A_ramhormoz
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario5 += 1000 * (np.sum(group) - 1) ** 2

    # Additional Constraint: sum(x * I) <= I_bar_behbahan
    if np.sum(x3 * I) > I_ramhormoz5:
        o3_scenario5 = o3_scenario5-(I_sum-I_ramhormoz5)*10**25# Set cost to negative infinity if constraint is violated

    # agent number 4: ramshir agriculture

    o4_scenario5 = np.sum(x4 * z5) * A_ramshir
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario5 += 1000 * (np.sum(group) - 1) ** 2

    # Additional Constraint: sum(x * I) <= I_bar_behbahan
    if np.sum(x4 * I) > I_ramshir5:
        o4_scenario5 = o4_scenario5-(I_sum-I_ramshir5)*10**25# Set cost to negative infinity if constraint is violated

    # agent number 5: shadegan agriculture

    o5_scenario5 = np.sum(x5 * z5) * A_shadegan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario5 += 1000 * (np.sum(group) - 1) ** 2

    # Additional Constraint: sum(x * I) <= I_bar_behbahan
    if np.sum(x5 * I) > I_shadegan5:
        o5_scenario5 = o5_scenario5-(I_sum-I_shadegan5)*10**25 # Set cost to negative infinity if constraint is violated


    # scenario  6
    # agent number 1: behbahan agriculture

    o1_scenario6 = np.sum(x1 * z6) * A_behbahan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario6 += 1000 * (np.sum(group) - 1) ** 2

    # Additional Constraint: sum(x * I) <= I_behbahan6
    if np.sum(x1 * I) > I_behbahan6:
        o1_scenario6 = o1_scenario6-(I_sum-I_behbahan6)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 2: Jayezan agriculture

    o2_scenario6 = np.sum(x2 * z6) * A_Jayezan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario6 += 1000 * (np.sum(group) - 1) ** 2

    # Additional Constraint: sum(x * I) <= I_Jayezan6
    if np.sum(x2 * I) > I_Jayezan6:
        o2_scenario6 = o2_scenario6-(I_sum-I_Jayezan6) *10**13# Set cost to negative infinity if constraint is violated

    # agent number 3: ramhormoz agriculture

    o3_scenario6 = np.sum(x3 * z6) * A_ramhormoz
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario6 += 1000 * (np.sum(group) - 1) ** 2

    # Additional Constraint: sum(x * I) <= I_ramhormoz6
    if np.sum(x3 * I) > I_ramhormoz6:
        o3_scenario6 = o3_scenario6 -(I_sum-I_ramhormoz6)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 4: ramshir agriculture

    o4_scenario6 = np.sum(x4 * z6) * A_ramshir
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario6 += 1000 * (np.sum(group) - 1) ** 2

    # Additional Constraint: sum(x * I) <= I_ramshir6
    if np.sum(x4 * I) > I_ramshir6:
        o4_scenario6 = o4_scenario6-(I_sum-I_ramshir6)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 5: shadegan agriculture

    o5_scenario6 = np.sum(x5 * z6) * A_shadegan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario6 += 1000 * (np.sum(group) - 1) ** 2

    # Additional Constraint: sum(x * I) <= I_shadegan6
    if np.sum(x5 * I) > I_shadegan6:
        o5_scenario6 = o5_scenario6-(I_sum-I_shadegan6) *10**25# Set cost to negative infinity if constraint is violated


    # Scenario 7

    # Agent 1: Behbahan agriculture
    o1_scenario7 = np.sum(x1 * z7) * A_behbahan
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario7 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x1* I) > I_behbahan7:
        o1_scenario7 = o1_scenario7 -(I_sum-I_behbahan7)*10**13

    # Agent 2: Jayezan agriculture 
    o2_scenario7 = np.sum(x2* z7) * A_Jayezan
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario7 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x2* I) > I_Jayezan7:
        o2_scenario7 = o2_scenario7-(I_sum-I_Jayezan7)*10**13

    # Agent 3: Ramhormoz agriculture
    o3_scenario7 = np.sum(x3* z7) * A_ramhormoz
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario7 += 1000 * (np.sum(group) - 1) ** 2  
    if np.sum(x3* I) > I_ramhormoz7:
        o3_scenario7 = o3_scenario7-(I_sum-I_ramhormoz7)*10**13

    # Agent 4: Ramshir agriculture
    o4_scenario7 = np.sum(x4* z7) * A_ramshir
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario7 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x4* I) > I_ramshir7:
        o4_scenario7 = o4_scenario7-(I_sum-I_ramshir7)*10**13

    # Agent 5: Shadegan agriculture
    o5_scenario7 = np.sum(x5* z7) * A_shadegan  
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario7 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x5* I) > I_shadegan7:
        o5_scenario7 = o5_scenario7-(I_sum-I_shadegan7)*10**13

    # Scenario 8

    # Agent 1: Behbahan agriculture
    o1_scenario8 = np.sum(x1 * z8) * A_behbahan
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario8 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x1 * I) > I_behbahan8:
        o1_scenario8 = o1_scenario8-(I_sum-I_behbahan8)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 2: Jayezan agriculture
    o2_scenario8 = np.sum(x2 * z8) * A_Jayezan
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario8 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x2 * I) > I_Jayezan8:
        o2_scenario8 = o2_scenario8-(I_sum-I_Jayezan8)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 3: Ramhormoz agriculture
    o3_scenario8 = np.sum(x3 * z8) * A_ramhormoz
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario8 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x3 * I) > I_ramhormoz8:
        o3_scenario8 = -o3_scenario8-(I_sum-I_ramhormoz8)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 4: Ramshir agriculture
    o4_scenario8 = np.sum(x4 * z8) * A_ramshir
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario8 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x4 * I) > I_ramshir8:
        o4_scenario8 = o4_scenario8-(I_sum-I_ramshir8)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 5: Shadegan agriculture
    o5_scenario8 = np.sum(x5 * z8) * A_shadegan
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario8 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x5 * I) > I_shadegan8:
        o5_scenario8 = o5_scenario8-(I_sum-I_shadegan8)*10**25# Set cost to negative infinity if constraint is violated

    # Scenario 9

    # Agent 1: Behbahan agriculture
    o1_scenario9 = np.sum(x1 * z9) * A_behbahan
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario9 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x1 * I) > I_behbahan9:
        o1_scenario9 = o1_scenario9-(I_sum-I_behbahan9)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 2: Jayezan agriculture
    o2_scenario9 = np.sum(x2 * z9) * A_Jayezan
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario9 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x2 * I) > I_Jayezan9:
        o2_scenario9 = o2_scenario9-(I_sum-I_Jayezan9)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 3: Ramhormoz agriculture
    o3_scenario9 = np.sum(x3 * z9) * A_ramhormoz
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario9 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x3 * I) > I_ramhormoz9:
        o3_scenario9 = o3_scenario9-(I_sum-I_ramhormoz9)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 4: Ramshir agriculture
    o4_scenario9 = np.sum(x4 * z9) * A_ramshir
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario9 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x4 * I) > I_ramshir9:
        o4_scenario9 = o4_scenario9-(I_sum-I_ramshir9)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 5: Shadegan agriculture
    o5_scenario9 = np.sum(x5 * z9) * A_shadegan
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario9 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x5 * I) > I_shadegan9:
        o5_scenario9 = o5_scenario9 -(I_sum-I_shadegan9)*10**25# Set cost to negative infinity if constraint is violated


    # Scenario 10

    # Agent 1: Behbahan agriculture
    o1_scenario10 = np.sum(x1 * z10) * A_behbahan
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario10 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x1 * I) > I_behbahan10:
        o1_scenario10 = o1_scenario10-(I_sum-I_behbahan10)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 2: Jayezan agriculture
    o2_scenario10 = np.sum(x2 * z10) * A_Jayezan
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario10 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x2 * I) > I_Jayezan10:
        o2_scenario10 = o2_scenario10-(I_sum-I_Jayezan10)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 3: Ramhormoz agriculture
    o3_scenario10 = np.sum(x3 * z10) * A_ramhormoz
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario10 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x3 * I) > I_ramhormoz10:
        o3_scenario10 = o3_scenario10-(I_sum- I_ramhormoz10)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 4: Ramshir agriculture
    o4_scenario10 = np.sum(x4 * z10) * A_ramshir
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario10 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x4 * I) > I_ramshir10:
        o4_scenario10 = o4_scenario10-(I_sum-I_ramshir10)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 5: Shadegan agriculture
    o5_scenario10 = np.sum(x5 * z10) * A_shadegan
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario10 += 1000 * (np.sum(group) - 1) ** 2
    if np.sum(x5 * I) > I_shadegan10:
        o5_scenario10 = o5_scenario10-(I_sum-I_shadegan10)*10**25 # Set cost to negative infinity if constraint is violated

    # scenario 11

    # agent number 1: behbahan agriculture
    o1_scenario11 = np.sum(x1 * z11) * A_behbahan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario11 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x1 * I) > I_behbahan11:
        o1_scenario11 = o1_scenario11-(I_sum-I_behbahan11)*10**25# Set cost to negative infinity if constraint is violated

    # agent number 2: Jayezan agriculture
    o2_scenario11 = np.sum(x2 * z11) * A_Jayezan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario11 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x2 * I) > I_Jayezan11:
        o2_scenario11 = o2_scenario11-(I_sum-I_Jayezan11)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 3: ramhormoz agriculture
    o3_scenario11 = np.sum(x3 * z11) * A_ramhormoz
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario11 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x3 * I) > I_ramhormoz11:
        o3_scenario11 = o3_scenario11-(I_sum-I_ramhormoz11)*10**25# Set cost to negative infinity if constraint is violated

    # agent number 4: ramshir agriculture
    o4_scenario11 = np.sum(x4 * z11) * A_ramshir
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario11 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x4 * I) > I_ramshir11:
        o4_scenario11 = o4_scenario11-(I_sum-I_ramshir11)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 5: shadegan agriculture
    o5_scenario11 = np.sum(x5 * z11) * A_shadegan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario11 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x5 * I) > I_shadegan11:
        o5_scenario11 = o5_scenario11-(I_sum- I_shadegan11)*10**25 # Set cost to negative infinity if constraint is violated


    # scenario 12

    # agent number 1: behbahan agriculture
    o1_scenario12 = np.sum(x1 * z12) * A_behbahan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario12 = o1_scenario12 + 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x*I) <= I_bar_behbahan
    if np.sum(x1 * I) > I_behbahan12:
        o1_scenario12 = o1_scenario12 -(I_sum-I_behbahan12)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 2: Jayezan agriculture
    o2_scenario12 = np.sum(x2 * z12) * A_Jayezan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario12 = o2_scenario12 + 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x*I) <= I_bar_behbahan
    if np.sum(x2 * I) > I_Jayezan12:
        o2_scenario12 = o2_scenario12-(I_sum-I_Jayezan12)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 3: ramhormoz agriculture
    o3_scenario12 = np.sum(x3 * z12) * A_ramhormoz
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario12 = o3_scenario12 + 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x*I) <= I_bar_behbahan
    if np.sum(x3 * I) > I_ramhormoz12:
        o3_scenario12 = o3_scenario12-(I_sum-I_ramhormoz12)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 4: ramshir agriculture
    o4_scenario12 = np.sum(x4 * z12) * A_ramshir
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario12 = o4_scenario12 + 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x*I) <= I_bar_behbahan
    if np.sum(x4 * I) > I_ramshir12:
        o4_scenario12 = o4_scenario12-(I_sum-I_ramshir12)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 5: shadegan agriculture
    o5_scenario12 = np.sum(x5 * z12) * A_shadegan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario12 = o5_scenario12 + 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x*I) <= I_bar_behbahan
    if np.sum(x5 * I) > I_shadegan12:
        o5_scenario12 = o5_scenario12-(I_sum-I_shadegan12)*10**25 # Set cost to negative infinity if constraint is violated

    # scenario 13

    # agent number 1: behbahan agriculture
    o1_scenario13 = np.sum(x1 * z13) * A_behbahan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario13 = o1_scenario13 + 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x*I) <= I_bar_behbahan
    if np.sum(x1 * I) > I_behbahan13:
        o1_scenario13 = o1_scenario13-(I_sum-I_behbahan13)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 2: Jayezan agriculture
    o2_scenario13 = np.sum(x2 * z13) * A_Jayezan
    # Constraint: Restrict the sum of eachgroup of 4 variables to be equal to 1
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario13 = o2_scenario13 + 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x*I) <= I_bar_behbahan
    if np.sum(x2 * I) > I_Jayezan13:
        o2_scenario13 = o2_scenario13-(I_sum-I_Jayezan13)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 3: ramhormoz agriculture
    o3_scenario13 = np.sum(x3 * z13) * A_ramhormoz
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario13 = o3_scenario13 + 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x*I) <= I_bar_behbahan
    if np.sum(x3 * I) > I_ramhormoz13:
        o3_scenario13 = o3_scenario13 -(I_sum- I_ramhormoz13)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 4: ramshir agriculture
    o4_scenario13 = np.sum(x4 * z13) * A_ramshir
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario13 = o4_scenario13 + 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x*I) <= I_bar_behbahan
    if np.sum(x4 * I) > I_ramshir13:
        o4_scenario13 = o4_scenario13-(I_sum-I_ramshir13)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 5: shadegan agriculture
    o5_scenario13 = np.sum(x5 * z13) * A_shadegan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario13 = o5_scenario13 + 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x*I) <= I_bar_behbahan
    if np.sum(x5 * I) > I_shadegan13:
        o5_scenario13 = o5_scenario13-(I_sum-I_shadegan13)*10**25 # Set cost to negative infinity if constraint is violated

    #scenario 14

    # agent number 1: behbahan agriculture
    o1_scenario14 = np.sum(x1 * z14) * A_behbahan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario14 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x1 * I) > I_behbahan14:
        o1_scenario14 = o1_scenario14-(I_sum-I_behbahan14)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 2: Jayezan agriculture
    o2_scenario14 = np.sum(x2 * z14) * A_Jayezan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario14 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x2 * I) > I_Jayezan14:
        o2_scenario14 = o2_scenario14-(I_sum-I_Jayezan14)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 3: ramhormoz agriculture
    o3_scenario14 = np.sum(x3 * z14) * A_ramhormoz
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario14 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x3 * I) > I_ramhormoz14:
        o3_scenario14 = o3_scenario14-(I_sum-I_ramhormoz14)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 4: ramshir agriculture
    o4_scenario14 = np.sum(x4 * z14) * A_ramshir
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario14 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x4 * I) > I_ramshir14:
        o4_scenario14 = o4_scenario14-(I_sum-I_ramshir14)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 5: shadegan agriculture
    o5_scenario14 = np.sum(x5 * z14) * A_shadegan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario14 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x5 * I) > I_shegan14:
        o5_scenario14 = o5_scenario14-(I_sum-I_shegan14)*10**25 # Set cost to negative infinity if constraint is violated

    # scenario 15:

    # agent number 1: behbahan agriculture
    o1_scenario15 = np.sum(x1 * z15) * A_behbahan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario15 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x1 * I) > I_behbahan15:
        o1_scenario15 = o1_scenario15-(I_sum-I_behbahan15)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 2: Jayezan agriculture
    o2_scenario15 = np.sum(x2 * z15) * A_Jayezan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario15 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x2 * I) > I_Jayezan15:
        o2_scenario15 = o2_scenario15-(I_sum-I_Jayezan15)*10**25# Set cost to negative infinity if constraint is violated

    # agent number 3: ramhormoz agriculture
    o3_scenario15 = np.sum(x3 * z15) * A_ramhormoz
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario15 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x3 * I) > I_ramhormoz15:
        o3_scenario15 = o3_scenario15-(I_sum-I_ramhormoz15)*10**25# Set cost to negative infinity if constraint is violated

    # agent number 4: ramshir agriculture
    o4_scenario15 = np.sum(x4 * z15) * A_ramshir
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario15 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x4 * I) > I_ramshir15:
        o4_scenario15 = o4_scenario15-(I_sum-I_ramshir15) *10**13# Set cost to negative infinity if constraint is violated

    # agent number 5: shadegan agriculture
    o5_scenario15 = np.sum(x5 * z15) * A_shadegan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario15 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x5 * I) > I_shadegan15:
        o5_scenario15 = o5_scenario15-(I_sum-I_shadegan15)*10**25 # Set cost to negative infinity if constraint is violated

    # scenario 16

    # agent number 1: behbahan agriculture
    o1_scenario16 = np.sum(x1 * z16) * A_behbahan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario16 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x1 * I) > I_behbahan16:
        o1_scenario16 = o1_scenario16 -(I_sum-I_behbahan16)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 2: Jayezan agriculture
    o2_scenario16 = np.sum(x2 * z16) * A_Jayezan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario16 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x2 * I) > I_Jayezan16:
        o2_scenario16 = o2_scenario16-(I_sum-I_Jayezan16)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 3: ramhormoz agriculture
    o3_scenario16 = np.sum(x3 * z16) * A_ramhormoz
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario16 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x3 * I) > I_ramhormoz16:
        o3_scenario16 = o3_scenario16-(I_sum-I_ramhormoz16)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 4: ramshir agriculture
    o4_scenario16 = np.sum(x4 * z16) * A_ramshir
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario16 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x4 * I) > I_ramshir16:
        o4_scenario16 = o4_scenario16-(I_sum-I_ramshir16) *10**13# Set cost to negative infinity if constraint is violated

    # agent number 5: shadegan agriculture
    o5_scenario16 = np.sum(x5 * z16) * A_shadegan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario16 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x5 * I) > I_shadegan16:
        o5_scenario16 = o5_scenario16-(I_sum-I_shadegan16)*10**25 # Set cost to negative infinity if constraint is violated

    # scenario 17

    # agent number 1: behbahan agriculture
    o1_scenario17 = np.sum(x1 * z17) * A_behbahan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario17 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x1 * I) > I_behbahan17:
        o1_scenario17 = o1_scenario17-(I_sum-I_behbahan17)*10**25 # Set cost tonegative infinity if constraint is violated

    # agent number 2: Jayezan agriculture
    o2_scenario17 = np.sum(x2 * z17) * A_Jayezan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario17 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x2 * I) > I_Jayezan17:
        o2_scenario17 = o2_scenario17-(I_sum-I_Jayezan17)*10**25# Set cost to negative infinity if constraint is violated

    # agent number 3: ramhormoz agriculture
    o3_scenario17 = np.sum(x3 * z17) * A_ramhormoz
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario17 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x3 * I) > I_ramhormoz17:
        o3_scenario17 = o3_scenario17-(I_sum-I_ramhormoz17)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 4: ramshir agriculture
    o4_scenario17 = np.sum(x4 * z17) * A_ramshir
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario17 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x4 * I) > I_ramshir17:
        o4_scenario17 = o4_scenario17-(I_sum-I_ramshir17)*10**25 # Set cost to negative infinity if constraint is violated

    # agent number 5: shadegan agriculture
    o5_scenario17 = np.sum(x5 * z17) * A_shadegan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario17 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x5 * I) > I_shadegan17:
        o5_scenario17 = o5_scenario17-(I_sum-I_shadegan17)*10**25# Set cost to negative infinity if constraint is violated

    # Scenario 18

    # agent number 1: behbahan agriculture
    o1_scenario18 = np.sum(x1 * z18) * A_behbahan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario18 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x1 * I) > I_behbahan18:
        o1_scenario18 = o1_scenario18-(I_sum-I_behbahan18)*10**13

    # agent number 2: Jayezan agriculture
    o2_scenario18 = np.sum(x2 * z18) * A_Jayezan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario18 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x2 * I) > I_Jayezan18:
        o2_scenario18 = o2_scenario18-(I_sum-I_Jayezan18)*10**13

    # agent number 3: ramhormoz agriculture
    o3_scenario18 = np.sum(x3 * z18) * A_ramhormoz
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario18 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x3 * I) > I_ramhormoz18:
        o3_scenario18 = o3_scenario18-(I_sum-I_ramhormoz18)*10**13

    # agent number 4: ramshir agriculture
    o4_scenario18 = np.sum(x4 * z18) * A_ramshir
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario18 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x4 * I) > I_ramshir18:
        o4_scenario18 =  o4_scenario18-(I_sum-I_ramshir18)*10**13

    # agent number 5: shadegan agriculture
    o5_scenario18 = np.sum(x5 * z18) * A_shadegan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario18 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x5 * I) > I_shadegan18:
        o5_scenario18 = o5_scenario18-(I_sum-I_shadegan18)*10**13

    # Scenario 19

    # agent number 1: behbahan agriculture
    o1_scenario19 = np.sum(x1 * z19) * A_behbahan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario19 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x1 * I) > I_behbahan19:
        o1_scenario19 = o1_scenario19-(I_sum-I_behbahan19)*10**13

    # agent number 2: Jayezan agriculture
    o2_scenario19 = np.sum(x2 * z19) * A_Jayezan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario19 += 1000 *(np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_Jayezan
    if np.sum(x2 * I) > I_Jayezan19:
        o2_scenario19 = o2_scenario19 -(I_sum-I_Jayezan19)*10**13

    # agent number 3: ramhormoz agriculture
    o3_scenario19 = np.sum(x3 * z19) * A_ramhormoz
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario19 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_ramhormoz
    if np.sum(x3 * I) > I_ramhormoz19:
        o3_scenario19 = o3_scenario19-(I_sum-I_ramhormoz19)*10**13

    # agent number 4: ramshir agriculture
    o4_scenario19 = np.sum(x4 * z19) * A_ramshir
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario19 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_ramshir
    if np.sum(x4 * I) > I_ramshir19:
        o4_scenario19 = o4_scenario19 -(I_sum-I_ramshir19)*10**13

    # agent number 5: shadegan agriculture
    o5_scenario19 = np.sum(x5 * z19) * A_shadegan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario19 += 1000 * (np.sum(group) - 1) ** 2
    # Additional Constraint: sum(x.*I) <= I_bar_shadegan
    if np.sum(x5 * I) > I_shadegan19:
        o5_scenario19 =  o5_scenario19-(I_sum-I_shadegan19)*10**13

    # Scenario 20

    # Agent 1: Behbahan agriculture
    o1_scenario20 = np.sum(x1 * z20) * A_behbahan
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario20 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x1 * I) > I_behbahan20:
        o1_scenario20 =  o1_scenario20 -(I_sum-I_behbahan20)*10**25# Set cost to negative infinity if constraint is violated

    # Agent 2: Jayezan agriculture
    o2_scenario20 = np.sum(x2 * z20) * A_Jayezan
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario20 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x2 * I) > I_Jayezan20:
        o2_scenario20 = o2_scenario20-(I_sum-I_Jayezan20)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 3: Ramhormoz agriculture
    o3_scenario20 = np.sum(x3 * z20) * A_ramhormoz
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario20 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x3 * I) > I_ramhormoz20:
        o3_scenario20 = o3_scenario20-(I_sum-I_ramhormoz20)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 4: Ramshir agriculture
    o4_scenario20 = np.sum(x4 * z20) * A_ramshir
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario20 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x4 * I) > I_ramshir20:
        o4_scenario20 = o4_scenario20-(I_sum-I_ramshir20)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 5: Shadegan agriculture
    o5_scenario20 = np.sum(x5 * z20) * A_shadegan
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario20 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x5 * I) > I_shadegan20:
        o5_scenario20 = o5_scenario20-(I_sum-I_shadegan20)*10**25# Set cost to negative infinity if constraint is violated


    # Scenario 21

    # Agent 1: Behbahan agriculture
    o1_scenario21 = np.sum(x1 * z21) * A_behbahan
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario21 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x1 * I) > I_behbahan21:
        o1_scenario21 = o1_scenario21 -(I_sum-I_behbahan21)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 2: Jayezan agriculture
    o2_scenario21 = np.sum(x2 * z21) * A_Jayezan
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario21 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x2 * I) > I_Jayezan21:
        o2_scenario21 = o2_scenario21-(I_sum-I_Jayezan21)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 3: Ramhormoz agriculture
    o3_scenario21 = np.sum(x3 * z21) * A_ramhormoz
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario21 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x3 * I) > I_ramhormoz21:
        o3_scenario21 = o3_scenario21-(I_sum-I_ramhormoz21)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 4: Ramshir agriculture
    o4_scenario21 = np.sum(x4 * z21) * A_ramshir
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario21 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x4 * I) > I_ramshir21:
        o4_scenario21 = o4_scenario21-(I_sum-I_ramshir21) *10**25# Set cost to negative infinity if constraint is violated

    # Agent 5: Shadegan agriculture
    o5_scenario21 = np.sum(x5 * z21) * A_shadegan
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario21 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x5 * I) > I_shadegan21:
        o5_scenario21 = o5_scenario21-(I_sum- I_shadegan21)*10**25 # Set cost to negative infinity if constraint is violated

    # scenario 22

    # agent number 1: behbahan agriculture
    o1_scenario22 = np.sum(x1 * z22) * A_behbahan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario22 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x1 * I) > I_behbahan22:
        o1_scenario22 = o1_scenario22-(I_sum-I_behbahan22)*10**25 # Set cost to negative infinity if constraint is violated
    # agent number 2: Jayezan agriculture
    o2_scenario22 = np.sum(x2 * z22) * A_Jayezan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario22 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x2 * I) > I_Jayezan22:
       o2_scenario22  =  o2_scenario22 -(I_sum-I_Jayezan22)*10**25 # Set cost to negative infinity if constraint is violated
    # agent number 3: ramhormoz agriculture
    o3_scenario22 = np.sum(x3 * z22) * A_ramhormoz
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario22 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x3 * I) > I_ramhormoz22:
        o3_scenario22 = o3_scenario22-(I_sum-I_ramhormoz22) *10**25# Set cost to negative infinity if constraint is violated
    # agent number 4: ramshir agriculture
    o4_scenario22 = np.sum(x4 * z22) * A_ramshir
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario22 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x4 * I) > I_ramshir22:
        o4_scenario22 = o4_scenario22-(I_sum-I_ramshir22) *10**13# Set cost to negative infinity if constraint is violated
    # agent number 5: shadegan agriculture
    o5_scenario22 = np.sum(x5 * z22) * A_shadegan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario22 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x5 * I) > I_shadegan22:
        o5_scenario22 = o5_scenario22-(I_sum-I_shadegan22)*10**25# Set cost to negative infinity if constraint is violated

    # scenario 23

    # agent number 1: behbahan agriculture
    o1_scenario23 = np.sum(x1 * z23) * A_behbahan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario23 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x1 * I) > I_behbahan23:
        o1_scenario23 = -(I_sum-I_behbahan23)*10**13# Set cost to negative infinity if constraint is violated
    # agent number 2: Jayezan agriculture
    o2_scenario23 = np.sum(x2 * z23) * A_Jayezan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to1
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario23 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x2 * I) > I_Jayezan23:
        o2_scenario23 = o2_scenario23-(I_sum-I_Jayezan23) *10**25# Set cost to negative infinity if constraint is violated
    # agent number 3: ramhormoz agriculture
    o3_scenario23 = np.sum(x3 * z23) * A_ramhormoz
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario23 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x3 * I) > I_ramhormoz23:
        o3_scenario23 = o3_scenario23-(I_sum-I_ramhormoz23)*10**25 # Set cost to negative infinity if constraint is violated
    # agent number 4: ramshir agriculture
    o4_scenario23 = np.sum(x4 * z23) * A_ramshir
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario23 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x4 * I) > I_ramshir23:
        o4_scenario23 = o4_scenario23-(I_sum-I_ramshir23)*10**25 # Set cost to negative infinity if constraint is violated
    # agent number 5: shadegan agriculture
    o5_scenario23 = np.sum(x5 * z23) * A_shadegan
    # Constraint: Restrict the sum of each group of 4 variables to be equal to 1
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario23 += 1000 * (np.sum(group) - 1)**2
    # Additional Constraint: sum(x.*I) <= I_bar_behbahan
    if np.sum(x5 * I) > I_shadegan23:
        o5_scenario23 = o5_scenario23-(I_sum-I_shadegan23)*10**25# Set cost to negative infinity if constraint is violated

    # Scenario 24

    # Agent 1: Behbahan agriculture
    o1_scenario24 = np.sum(x1 * z24) * A_behbahan
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario24 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x1 * I) > I_behbahan24:
        o1_scenario24 = o1_scenario24-(I_sum-I_behbahan24)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 2: Jayezan agriculture
    o2_scenario24 = np.sum(x2 * z24) * A_Jayezan
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario24 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x2 * I) > I_Jayezan24:
        o2_scenario24 = o2_scenario24-(I_sum-I_Jayezan24)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 3: Ramhormoz agriculture
    o3_scenario24 = np.sum(x3 * z24) * A_ramhormoz
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario24 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x3 * I) > I_ramhormoz24:
        o3_scenario24 = o3_scenario24-(I_sum-I_ramhormoz24)*10**25# Set cost to negative infinity if constraint is violated

    # Agent 4: Ramshir agriculture
    o4_scenario24 = np.sum(x4 * z24) * A_ramshir
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario24 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x4 * I) > I_ramshir24:
        o4_scenario24 = o4_scenario24-(I_sum-I_ramshir24)*10**25# Set cost to negative infinity if constraint is violated

    # Agent 5: Shadegan agriculture
    o5_scenario24 = np.sum(x5 * z24) * A_shadegan
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario24 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x5 * I) > I_shadegan24:
        o5_scenario24 = o5_scenario24-(I_sum-I_shadegan24)*10**25 # Set cost to negative infinity if constraint is violated

    # Scenario 25

    # Agent 1: Behbahan agriculture
    o1_scenario25 = np.sum(x1 * z25) * A_behbahan
    for i in range(15):
        group = x1[0, i*4 : i*4 + 4]
        o1_scenario25 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x1 * I) > I_behbahan25:
        o1_scenario25 = o1_scenario25-(I_sum-I_behbahan25)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 2: Jayezan agriculture
    o2_scenario25 = np.sum(x2 * z25) * A_Jayezan
    for i in range(15):
        group = x2[0, i*4 : i*4 + 4]
        o2_scenario25 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x2 * I) > I_Jayezan25:
        o2_scenario25 = o2_scenario25-(I_sum-I_Jayezan25)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 3: Ramhormoz agriculture
    o3_scenario25 = np.sum(x3 * z25) * A_ramhormoz
    for i in range(15):
        group = x3[0, i*4 : i*4 + 4]
        o3_scenario25 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x3 * I) > I_ramhormoz25:
        o3_scenario25 =  o3_scenario25-(I_sum-I_ramhormoz25)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 4: Ramshir agriculture
    o4_scenario25 = np.sum(x4 * z25) * A_ramshir
    for i in range(15):
        group = x4[0, i*4 : i*4 + 4]
        o4_scenario25 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x4 * I) > I_ramshir25:
        o4_scenario25 = o4_scenario25-(I_sum-I_ramshir25)*10**25 # Set cost to negative infinity if constraint is violated

    # Agent 5: Shadegan agriculture
    o5_scenario25 = np.sum(x5 * z25) * A_shadegan
    for i in range(15):
        group = x5[0, i*4 : i*4 + 4]
        o5_scenario25 += 1000 * (np.sum(group) - 1)**2
    if np.sum(x5 * I) > I_shadegan25:
        o5_scenario25 =  o5_scenario25-(I_sum-I_shadegan25)*10**25 # Set cost to negative infinity if constraint is violated


    o_scenario1 = o1_scenario1 + o2_scenario1 + o3_scenario1 + o4_scenario1 + o5_scenario1
    o_scenario2 = o1_scenario2 + o2_scenario2 + o3_scenario2 + o4_scenario2 + o5_scenario2
    o_scenario3 = o1_scenario3 + o2_scenario3 + o3_scenario3 + o4_scenario3 + o5_scenario3
    o_scenario4 = o1_scenario4 + o2_scenario4 + o3_scenario4 + o4_scenario4 + o5_scenario4
    o_scenario5 = o1_scenario5 + o2_scenario5 + o3_scenario5 + o4_scenario5 + o5_scenario5
    o_scenario6 = o1_scenario6 + o2_scenario6 + o3_scenario6 + o4_scenario6 + o5_scenario6
    o_scenario7 = o1_scenario7 + o2_scenario7 + o3_scenario7 + o4_scenario7 + o5_scenario7
    o_scenario8 = o1_scenario8 + o2_scenario8 + o3_scenario8 + o4_scenario8 + o5_scenario8
    o_scenario9 = o1_scenario9 + o2_scenario9 + o3_scenario9 + o4_scenario9 + o5_scenario9
    o_scenario10 = o1_scenario10 + o2_scenario10 + o3_scenario10 + o4_scenario10 + o5_scenario10
    o_scenario11 = o1_scenario11 + o2_scenario11 + o3_scenario11 + o4_scenario11 + o5_scenario11
    o_scenario12 = o1_scenario12 + o2_scenario12 + o3_scenario12 + o4_scenario12 + o5_scenario12
    o_scenario13 = o1_scenario13 + o2_scenario13 + o3_scenario13 + o4_scenario13 + o5_scenario13
    o_scenario14 = o1_scenario14 + o2_scenario14 + o3_scenario14 + o4_scenario14 + o5_scenario14
    o_scenario15 = o1_scenario15 + o2_scenario15 + o3_scenario15 + o4_scenario15 + o5_scenario15
    o_scenario16 = o1_scenario16 + o2_scenario16 + o3_scenario16 + o4_scenario16 + o5_scenario16
    o_scenario17 = o1_scenario17 + o2_scenario17 + o3_scenario17 + o4_scenario17 + o5_scenario17
    o_scenario18 = o1_scenario18 + o2_scenario18 + o3_scenario18 + o4_scenario18 + o5_scenario18
    o_scenario19 = o1_scenario19 + o2_scenario19 + o3_scenario19 + o4_scenario19 + o5_scenario19
    o_scenario20 = o1_scenario20 + o2_scenario20 + o3_scenario20 + o4_scenario20 + o5_scenario20
    o_scenario21 = o1_scenario21 + o2_scenario21 + o3_scenario21 + o4_scenario21 + o5_scenario21
    o_scenario22 = o1_scenario22 + o2_scenario22 + o3_scenario22 + o4_scenario22 + o5_scenario22
    o_scenario23 = o1_scenario23 + o2_scenario23 + o3_scenario23 + o4_scenario23 + o5_scenario23
    o_scenario24 = o1_scenario24 + o2_scenario24 + o3_scenario24 + o4_scenario24 + o5_scenario24
    o_scenario25 = o1_scenario25 + o2_scenario25 + o3_scenario25 + o4_scenario25 + o5_scenario25

    mean = (o_scenario1 + o_scenario2 + o_scenario3 + o_scenario4 + o_scenario5 +
            o_scenario6 + o_scenario7 + o_scenario8 + o_scenario9 + o_scenario10 +
            o_scenario11 + o_scenario12 + o_scenario13 + o_scenario14 + o_scenario15 +
            o_scenario16 + o_scenario17 + o_scenario18 + o_scenario19 + o_scenario20 +
            o_scenario21 + o_scenario22 + o_scenario23 + o_scenario24 + o_scenario25) / 25

    variance = (((o_scenario1 - mean)**2) + ((o_scenario2 - mean)**2) + ((o_scenario3 - mean)**2) +
                ((o_scenario4 - mean)**2) + ((o_scenario5 - mean)**2) + ((o_scenario6 - mean)**2) +
                ((o_scenario7 - mean)**2) + ((o_scenario8 - mean)**2) + ((o_scenario9 - mean)**2) +
                ((o_scenario10 - mean)**2) + ((o_scenario11 - mean)**2) + ((o_scenario12 - mean)**2) +
                ((o_scenario13 - mean)**2) +((o_scenario14 - mean)**2) + ((o_scenario15 - mean)**2) + 
                ((o_scenario16 - mean)**2) +((o_scenario17 - mean)**2) + ((o_scenario18 - mean)**2) +
                ((o_scenario19 - mean)**2) +((o_scenario20 - mean)**2) + ((o_scenario21 - mean)**2) +
                ((o_scenario22 - mean)**2) +((o_scenario23 - mean)**2) + ((o_scenario24 - mean)**2) +
                ((o_scenario25 - mean)**2)) / 25

    o = mean - (landa * np.sqrt(variance))
    
    return o 