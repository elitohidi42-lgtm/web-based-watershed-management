def PSO(Ks_wheat, phi_wheat, beta_wheat, s_h_wheat, s_w_wheat,s_star_wheat, s_fc_wheat, Ks_maize, phi_maize, beta_maize, s_h_maize, s_w_maize, s_star_maize,\
    s_fc_maize, Ks_potato, phi_potato, beta_potato, s_h_potato, s_w_potato,s_star_potato, s_fc_potato, Ks_barley, phi_barley, beta_barley, s_h_barley, s_w_barley\
    ,s_star_barley, s_fc_barley,yield_wheat, I_wheat,yield_maize, I_maize ,yield_potato, I_potato ,yield_barley, I_barley,objectivefunction,landa,VarMin,VarMax,I,I_sum,I_behbahan1, I_Jayezan1, I_ramhormoz1,I_ramshir1,\
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
    import readdata
    from objectivefunction import objectivefunction
    
    z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12, z13, z14, z15, z16, z17, z18, z19, z20, z21, z22, z23, z24, z25,I,I_sum, \
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
    I_Jayezan25, I_ramhormoz25, I_ramshir25, I_shadegan25= readdata.functionread(Ks_wheat, phi_wheat, beta_wheat, s_h_wheat, s_w_wheat,s_star_wheat, s_fc_wheat, Ks_maize, phi_maize, beta_maize, s_h_maize, s_w_maize, s_star_maize,\
    s_fc_maize, Ks_potato, phi_potato, beta_potato, s_h_potato, s_w_potato,s_star_potato, s_fc_potato, Ks_barley, phi_barley, beta_barley, s_h_barley, s_w_barley,s_star_barley, s_fc_barley,yield_wheat, I_wheat,yield_maize, I_maize ,yield_potato, I_potato ,yield_barley, I_barley)
    

    CostFunction = lambda x: objectivefunction(Ks_wheat, phi_wheat, beta_wheat, s_h_wheat, s_w_wheat,s_star_wheat, s_fc_wheat, Ks_maize, phi_maize, beta_maize, s_h_maize, s_w_maize, s_star_maize,\
        s_fc_maize, Ks_potato, phi_potato, beta_potato, s_h_potato, s_w_potato,s_star_potato, s_fc_potato, Ks_barley, phi_barley, beta_barley, s_h_barley, s_w_barley,s_star_barley, s_fc_barley,yield_wheat, I_wheat,yield_maize, I_maize ,yield_potato, I_potato ,yield_barley, I_barley,landa,
        x[:, 0:60],      x[:, 60:120],    x[:, 120:180],   x[:, 180:240],   x[:, 240:300],z1,z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12, z13, z14, z15, z16, z17, z18, z19, z20, z21, z22, z23, z24, z25,I,I_sum, \
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
    I_Jayezan25, I_ramhormoz25, I_ramshir25, I_shadegan25)

    nVar = 300            # Number of Decision Variables
    VarSize = [1, nVar]    # Size of Decision Variables Matrix
    #VarMin = 0.05          # Lower Bound of Variables
    #VarMax = 0.8           # Upper Bound of Variables
    # PSO Parameters
    MaxIt = 60       # Maximum Number of Iterations
    nPop =  18      # Population Size (Swarm Size)
    # PSO Parameters
    w2 = 1.2
    w1 = 0.9            # Inertia Weight
    c1f = 1.2           # Personal Learning Coefficient
    c1i = 2.2
    c2f = 1.5           # Global Learning Coefficient 
    c2i = 0.7
    # Velocity Limits
    VelMax = 0.1 * ((VarMax/100) - (VarMin/100))
    VelMin = -VelMax

    # Initialization
    class Particle:
        def __init__(self):
            self.Position = np.zeros(VarSize)  # Initialize Position as a one-dimensional array
            self.Cost = -np.inf
            self.Velocity = np.zeros(VarSize)  # Initialize Velocity as a one-dimensional array
            self.Best = BestParticle()

    class BestParticle:
        def __init__(self):
            self.Position = np.zeros(VarSize)  # Initialize Position as a one-dimensional array
            self.Cost = -np.inf
    particle = [Particle() for _ in range(nPop)]
    GlobalBest = BestParticle()
    GlobalBest.Position = np.zeros(VarSize)  # Initialize Position as a one-dimensional array
    GlobalBest.Cost = -np.inf

    for i in range(nPop):
        # Initialize Position
        particle[i].Position = np.zeros(VarSize)
        for j in range(nVar // 4):
            group = np.random.uniform(VarMin / 100, VarMax / 100, 4)
            group_sum = np.sum(group)
            group = group / group_sum  # Normalize the group values
            particle[i].Position[0, j * 4: j * 4 + 4] = group
            
            # Initialize Velocity
        particle[i].Velocity = np.ones(VarSize)

        # Evaluation
        particle[i].Cost = CostFunction(particle[i].Position)

        # Update Personal Best
        particle[i].Best.Position = particle[i].Position
        particle[i].Best.Cost = particle[i].Cost

        # Update Global Best
        if particle[i].Cost > GlobalBest.Cost:
            GlobalBest.Cost = particle[i].Cost
            GlobalBest.Position = particle[i].Position

    BestCost = np.zeros(MaxIt)
    c1 = np.zeros(MaxIt)
    c2 = np.zeros(MaxIt)
    w = np.zeros(MaxIt)

    mean_values = []
    variance_values = []
    x_best_values = [] 
    # PSO Main Loop
    for it in range(MaxIt):
        for i in range(nPop):

            c1[it] = ((c1f-c1i)*(it/MaxIt))+ c1i
            c2[it] = ((c2f-c2i)*(it/MaxIt))+ c2i
            w[it] = ((w1-w2)*((MaxIt-it)/MaxIt))+ w2

            # Update Velocity
            particle[i].Velocity = w[it] * particle[i].Velocity \
                + c1[it] * np.random.rand(*VarSize) * (particle[i].Best.Position - particle[i].Position) \
                + c2[it] * np.random.rand(*VarSize) * (GlobalBest.Position - particle[i].Position)

            # Apply Velocity Limits
            particle[i].Velocity = np.maximum(particle[i].Velocity, VelMin)
            particle[i].Velocity = np.minimum(particle[i].Velocity, VelMax)

            # Update Position
            particle[i].Position = particle[i].Position + particle[i].Velocity

            # Velocity Mirror Effect
            IsOutside = (particle[i].Position < (VarMin/100)) | (particle[i].Position > (VarMax/100))
            particle[i].Velocity[IsOutside] = -particle[i].Velocity[IsOutside]

            # Apply Position Limits
            particle[i].Position = np.maximum(particle[i].Position, (VarMin/100))
            particle[i].Position = np.minimum(particle[i].Position, (VarMax/100))

            # Apply Constraint
            for j in range(nVar // 4):
                group = particle[i].Position[0, j * 4: j * 4 + 4]
                group_sum = np.sum(group)
                if group_sum != 1:
                    group = group / group_sum  # Normalize the group values
                    particle[i].Position[0, j * 4: j * 4 + 4] = group


            # Handle Constraint Violation
            # If the constraint is violated, set the cost to negative infinity
            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan1:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan1)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan1:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan1)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz1:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz1)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir1:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir1)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan1:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan1)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) > I_behbahan2:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan2)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) > I_Jayezan2:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan2)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz2:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz2)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) > I_ramshir2:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir2)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) > I_shadegan2:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan2)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) > I_behbahan3:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan3)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) > I_Jayezan3:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan3)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz3:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz3)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) > I_ramshir3:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir3)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) > I_shadegan3:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan3)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) > I_behbahan4:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan4)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) > I_Jayezan4:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan4)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz4:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz4)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) > I_ramshir4:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir4)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) > I_shadegan4:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan4)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan5:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan5)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan5:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan5)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz5:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz5)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir5:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir5)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan5:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan5)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan6:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan6)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan6:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan6)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz6:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz6)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir6:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir6)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan6:
                particle[i].Cost = particle[i].Cost-(I_sum- I_shadegan6)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan7:
                particle[i].Cost = particle[i].Cost-(I_sum- I_behbahan7)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan7:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan7)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz7:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz7)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir7:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir7)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan7:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan7)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan8:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan8)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan8:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan8)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz8:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz8)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir8:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir8)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan8:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan8)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan9:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan9)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan9:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan9)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz9:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz9)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir9:
                particle[i].Cost = particle[i].Cost-(I_sum- I_ramshir9)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan9:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan9)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan10:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan10)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan10:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan10)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz10:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz10)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir10:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir10)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan10:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan10)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan11:
                particle[i].Cost = particle[i].Cost-(I_sum- I_behbahan11)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan11:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan11)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz11:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz11)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir11:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir11)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan11:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan11)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan12:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan12)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan12:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan12)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz12:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz12)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir12:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir12)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan12:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan12)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan13:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan13)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan13:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan13)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz13:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz13)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir13:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir13)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan13:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan13)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan14:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan14)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan14:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan14)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz14:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz14)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir14:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir14)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shegan14:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shegan14)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan15:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan15)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan15:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan15)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz15:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz15)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir15:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir15)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan15:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan15)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan16:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan16)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan16:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan16)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz16:
                particle[i].Cost = particle[i].Cost-(I_sum- I_ramhormoz16)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir16:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir16)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan16:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan16)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan17:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan17)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan17:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan17)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz17:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz17)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir17:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir17)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan17:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan17)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan18:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan18)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan18:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan18)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz18:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz18)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir18:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir18)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan18:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan18)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan19:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan19)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan19:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan19)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz19:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz19)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir19:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir19)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan19:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan19)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan20:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan20)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan20:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan20)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz20:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz20)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir20:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir20)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan20:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan20)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan21:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan21)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan21:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan21)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz21:
                particle[i].Cost = particle[i].Cost-(I_sum- I_ramhormoz21)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir21:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir21)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan21:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan21)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan22:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan22)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan22:
                particle[i].Cost = particle[i].Cost-(I_sum- I_Jayezan22)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz22:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz22)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir22:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir22)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan22:
                particle[i].Cost = particle[i].Cost-(I_sum-I_shadegan22)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan23:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan23)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan23:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan23)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz23:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz23)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir23:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir23)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan23:
                particle[i].Cost = particle[i].Cost -(I_sum-I_shadegan23)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan24:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan24)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan24:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan24)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz24:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz24)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir24:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir24)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan24:
                particle[i].Cost = particle[i].Cost -(I_sum-I_shadegan24)*10**16

            if np.sum(particle[i].Position[:, 0:60] * I) >     I_behbahan25:
                particle[i].Cost = particle[i].Cost-(I_sum-I_behbahan25)*10**16
            if np.sum(particle[i].Position[:, 60:120] * I) >    I_Jayezan25:
                particle[i].Cost = particle[i].Cost-(I_sum-I_Jayezan2)*10**16
            if np.sum(particle[i].Position[:, 120:180] * I) > I_ramhormoz25:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramhormoz25)*10**16
            if np.sum(particle[i].Position[:, 180:240] * I) >   I_ramshir25:
                particle[i].Cost = particle[i].Cost-(I_sum-I_ramshir25)*10**16
            if np.sum(particle[i].Position[:, 240:300] * I) >  I_shadegan25:
                particle[i].Cost = particle[i].Cost -(I_sum-I_shadegan25)*10**16

            # Evaluation
            particle[i].Cost = CostFunction(particle[i].Position)

            # Update Personal Best
            if particle[i].Cost > particle[i].Best.Cost:
                particle[i].Best.Position = particle[i].Position
                particle[i].Best.Cost = particle[i].Cost

                # Update Global Best
                if particle[i].Cost > GlobalBest.Cost:
                    GlobalBest.Cost = particle[i].Cost
                    GlobalBest.Position = particle[i].Position

        BestCost[it] = GlobalBest.Cost
        best_solution = GlobalBest.Position

        mean_value = np.mean([particle[i].Cost for i in range(nPop)])
        mean_values.append(mean_value)
        # Compute variance value at each iteration and store it
        variance_value = np.mean([((particle[i].Cost - mean_value)**2) for i in range(nPop)])
        variance_values.append(variance_value)
        best_particle_index = np.argmax([particle[i].Cost for i in range(nPop)])
        x_best_values.append(particle[best_particle_index].Position)

    # # Plot changes in the "mean" parameter
    # plt.figure(figsize=(10, 6))
    # plt.plot(mean_values, label='Mean')
    # plt.xlabel("Iteration")
    # plt.ylabel("Mean Value")
    # plt.title("Changes in Mean during PSO")
    # plt.legend()
    # plt.grid(True)
    # plt.tight_layout()
    # plt.show()

    # # Plot changes in the "variance" parameter
    # plt.figure(figsize=(10, 6))
    # plt.plot(variance_values, label='Variance', color='orange')
    # plt.xlabel("Iteration")
    # plt.ylabel("Variance Value")
    # plt.title("Changes in Variance during PSO")
    # plt.legend()
    # plt.grid(True)
    # plt.tight_layout()
    # plt.show()


    return BestCost,best_solution
