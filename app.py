from flask import Flask , render_template, url_for , request
import numpy as np
import matplotlib.pyplot as plt
import io
from io import BytesIO
import base64
from matplotlib.font_manager import FontProperties

from insertdata import InsertData
from wheattraditional  import wheattraditional
from maizetraditional  import maizetraditional
from potatotraditional import potatotraditional
from barleytraditional import barleytraditional
from wheatmicro  import wheatmicro
from maizemicro  import maizemicro
from potatomicro import potatomicro
from barleymicro import barleymicro
from readdata import functionread
from wheatdefmicro  import wheatdefmicro
from maizedefmicro  import maizedefmicro
from potatodefmicro import potatodefmicro
from barleydefmicro import barleydefmicro
from wheatnoirr  import wheatnoirr
from maizenoirr import maizenoirr
from potatonoirr import potatonoirr
from barleynoirr import barleynoirr

from readdata import functionread
from objectivefunction import objectivefunction
from PSO import PSO

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html" , methods=['GET'])

@app.route("/submit")
def showResult() :

    minimumpercent=request.args.get("minimumpercent" )
    maximumpercent=request.args.get("maximumpercent" )
    landa = request.args.get("landa" )
    soiltype_wheat=request.args.get("soiltype_wheat")
    soiltype_barley=request.args.get("soiltype_barley")
    soiltype_maize=request.args.get("soiltype_maize")
    soiltype_potato=request.args.get("soiltype_potato")
    irrigation=request.args.get("irrigation")

    landa=float(landa)
    minimumpercent=float(minimumpercent)
    maximumpercent=float(maximumpercent)

    ymax_barley,ymax_maize,ymax_potato,ymax_wheat=InsertData()


    soil_params = {
        "loam": {"Ks": 200, "phi": 0.45, "beta": 14.8, "s_h": 0.19, "s_w": 0.24, "s_star": 0.57, "s_fc": 0.65},
        "Sandy loam": {"Ks": 80, "phi": 0.43, "beta": 13.8, "s_h": 0.14, "s_w": 0.18, "s_star": 0.46, "s_fc": 0.56},
        "Loamy sand": {"Ks": 200, "phi": 0.35, "beta": 12.1, "s_h": 0.08, "s_w": 0.11, "s_star": 0.33, "s_fc": 0.35},
        "Sand": {"Ks": 100, "phi": 0.42, "beta": 12.7, "s_h": 0.08, "s_w": 0.11, "s_star": 0.31, "s_fc": 0.52},
    }

    # Get soil parameters for each crop type
    params_wheat = soil_params[soiltype_wheat]
    params_maize = soil_params[soiltype_maize]
    params_barley = soil_params[soiltype_barley]
    params_potato = soil_params[soiltype_potato]

    # Extract parameters for each crop type
    Ks_wheat, phi_wheat, beta_wheat, s_h_wheat, s_w_wheat, s_star_wheat, s_fc_wheat = params_wheat["Ks"], params_wheat[
        "phi"], params_wheat["beta"], params_wheat["s_h"], params_wheat["s_w"], params_wheat["s_star"], params_wheat["s_fc"]

    Ks_maize, phi_maize, beta_maize, s_h_maize, s_w_maize, s_star_maize, s_fc_maize = params_maize["Ks"], params_maize[
        "phi"], params_maize["beta"], params_maize["s_h"], params_maize["s_w"], params_maize["s_star"], params_maize["s_fc"]

    Ks_barley, phi_barley, beta_barley, s_h_barley, s_w_barley, s_star_barley, s_fc_barley = params_barley["Ks"], params_barley[
        "phi"], params_barley["beta"], params_barley["s_h"], params_barley["s_w"], params_barley["s_star"], params_barley["s_fc"]

    Ks_potato, phi_potato, beta_potato, s_h_potato, s_w_potato, s_star_potato, s_fc_potato = params_potato["Ks"], params_potato[
        "phi"], params_potato["beta"], params_potato["s_h"], params_potato["s_w"], params_potato["s_star"], params_potato["s_fc"]
    
    if irrigation == "traditional irrigation":
        yield_wheat, I_wheat = wheattraditional(ymax_wheat, Ks_wheat, phi_wheat, beta_wheat, s_h_wheat, s_w_wheat,s_star_wheat, s_fc_wheat)
        yield_maize, I_maize = maizetraditional(ymax_maize, Ks_maize, phi_maize, beta_maize, s_h_maize, s_w_maize, s_star_maize, s_fc_maize)
        yield_potato, I_potato = potatotraditional(ymax_potato, Ks_potato, phi_potato, beta_potato, s_h_potato, s_w_potato,s_star_potato, s_fc_potato)
        yield_barley, I_barley = barleytraditional(ymax_barley, Ks_barley, phi_barley, beta_barley, s_h_barley, s_w_barley,s_star_barley, s_fc_barley)

    elif  irrigation == "traditional Deficit irrigation":
        yield_wheat, I_wheat = wheatnoirr(ymax_wheat, Ks_wheat, phi_wheat, beta_wheat, s_h_wheat, s_w_wheat,s_star_wheat, s_fc_wheat)
        yield_maize, I_maize = maizenoirr(ymax_maize, Ks_maize, phi_maize, beta_maize, s_h_maize, s_w_maize, s_star_maize, s_fc_maize)
        yield_potato, I_potato = potatonoirr(ymax_potato, Ks_potato, phi_potato, beta_potato, s_h_potato, s_w_potato,s_star_potato, s_fc_potato)
        yield_barley, I_barley = barleynoirr(ymax_barley, Ks_barley, phi_barley, beta_barley, s_h_barley, s_w_barley,s_star_barley, s_fc_barley)
 
    elif irrigation == "micro irrigation":
        yield_wheat, I_wheat = wheatmicro(ymax_wheat, Ks_wheat, phi_wheat, beta_wheat, s_h_wheat, s_w_wheat,s_star_wheat, s_fc_wheat)
        yield_maize, I_maize = maizemicro(ymax_maize, Ks_maize, phi_maize, beta_maize, s_h_maize, s_w_maize, s_star_maize, s_fc_maize)
        yield_potato, I_potato = potatomicro(ymax_potato, Ks_potato, phi_potato, beta_potato, s_h_potato, s_w_potato,s_star_potato, s_fc_potato)
        yield_barley, I_barley = barleymicro(ymax_barley, Ks_barley, phi_barley, beta_barley, s_h_barley, s_w_barley,s_star_barley, s_fc_barley)

    elif irrigation == "micro Deficit irrigation":
        yield_wheat, I_wheat = wheatdefmicro(ymax_wheat, Ks_wheat, phi_wheat, beta_wheat, s_h_wheat, s_w_wheat,s_star_wheat, s_fc_wheat)
        yield_maize, I_maize = maizedefmicro(ymax_maize, Ks_maize, phi_maize, beta_maize, s_h_maize, s_w_maize, s_star_maize, s_fc_maize)
        yield_potato, I_potato = potatodefmicro(ymax_potato, Ks_potato, phi_potato, beta_potato, s_h_potato, s_w_potato,s_star_potato, s_fc_potato)
        yield_barley, I_barley = barleydefmicro(ymax_barley, Ks_barley, phi_barley, beta_barley, s_h_barley, s_w_barley,s_star_barley, s_fc_barley)
    
    # years = np.arange(2003, 2018)  # Assuming there are 15 years of data
    # num_crops = 4
    # reshaped_yield_wheat = yield_wheat.reshape(1, -1)
    # reshaped_yield_maize = yield_maize.reshape(1, -1)
    # reshaped_yield_potato = yield_potato.reshape(1, -1)      
    # reshaped_yield_barley = yield_barley.reshape(1, -1)

    # years = np.arange(2003, 2018)  # Assuming there are 15 years of data
    # num_crops = 4

    # # Combine all crop yield data into a single array
    # crop_yield_data = np.vstack((reshaped_yield_wheat[0], reshaped_yield_maize[0], reshaped_yield_potato[0], reshaped_yield_barley[0]))

    # plt.figure(figsize=(10, 6))
    # bar_width = 0.2  # Width of each bar
    # bar_offsets = np.arange(num_crops) * bar_width  # Offset for each group of bars
    # crop_labels = ['Wheat', 'Maize', 'Potato', 'Barley']

    # for i in range(num_crops):
    #     plt.bar(years + bar_offsets[i], crop_yield_data[i], width=bar_width, label=crop_labels[i])

    # # Formatting the plot
    # plt.xlabel('Year', fontname='Times New Roman', fontsize=20, fontweight='bold')
    # plt.ylabel('Yield (ton/ha)', fontname='Times New Roman', fontsize=20, fontweight='bold')
    # plt.title('Crops Yield - Micro Irrigation', fontname='Times New Roman', fontsize=22, fontweight='bold')
    # plt.xticks(years + (bar_width * (num_crops - 1) / 2), years, fontname='Times New Roman', fontsize=20)
    # plt.legend(fontsize=18)

    # # Remove vertical grid lines
    # plt.grid(axis='y', linestyle='-', alpha=0.7, linewidth=0.5)  # Set linestyle='-' and alpha=0.7 to keep horizontal grid lines

    # # Customize horizontal grid lines
    # plt.grid(axis='x', linestyle='', alpha=0.0)  # Remove vertical grid lines

    # # Make the numbers on both axes bold
    # plt.xticks(fontname='Times New Roman', fontsize=19, fontweight='bold')
    # plt.yticks(fontname='Times New Roman', fontsize=19, fontweight='bold')

    # # Show the plot
    # plt.tight_layout()
    # plt.show()


    # Sample data for demonstration
    A_behbahan = 45095.016
    A_Jayezan = 10441.9
    A_ramhormoz = 41651.1
    A_ramshir = 27407.706
    A_shadegan = 41224.4
    A_ave = (A_behbahan + A_Jayezan + A_ramhormoz + A_ramshir + A_shadegan) / 5

    # # Assuming you have defined I_wheat, I_maize, I_potato, and I_barley elsewhere
    # reshaped_whaet = I_wheat.reshape(1, -1) * A_ave * 0.001
    # reshaped_maize = I_maize.reshape(1, -1) * A_ave * 0.001
    # reshaped_potato = I_potato.reshape(1, -1) * A_ave * 0.001
    # reshaped_barley = I_barley.reshape(1, -1) * A_ave * 0.001

    # years = np.arange(2003, 2018)  # Assuming there are 15 years of data
    # num_crops = 4

    # # Combine all crop data into a single array
    # crop_data = np.vstack((reshaped_whaet[0], reshaped_maize[0], reshaped_potato[0], reshaped_barley[0]))

    # plt.figure(figsize=(10, 6))
    # bar_width = 0.2  # Width of each bar
    # bar_offsets = np.arange(num_crops) * bar_width  # Offset for each group of bars
    # crop_labels = ['Wheat', 'Maize', 'Potato', 'Barley']

    # for i in range(num_crops):
    #     plt.bar(years + bar_offsets[i], crop_data[i], width=bar_width, label=crop_labels[i])

    # # Customize the font and size of labels for x and y axes
    # plt.xlabel('Years', fontsize=20, fontweight='bold', fontname='Times New Roman')
    # plt.ylabel('Water Use (m3)', fontsize=20, fontweight='bold', fontname='Times New Roman')

    # # Customize the font and size of the title
    # plt.title('Crops Water Use - Traditional Deficit Irrigation', fontsize=20, fontweight='bold', fontname='Times New Roman')

    # # Customize the font and size of numbers on x and y axes
    # plt.xticks(years + (bar_width * (num_crops - 1) / 2), years, fontsize=20, fontweight='bold', fontname='Times New Roman')
    # plt.yticks(fontsize=18, fontweight='bold', fontname='Times New Roman')

    # # Customize the legend font size
    # legend = plt.legend(fontsize=16)

    # plt.grid(True, axis='y')  # Only horizontal grids
    # plt.tight_layout()

    # # Show the plot
    # plt.show()



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
    I_Jayezan25, I_ramhormoz25, I_ramshir25, I_shadegan25 = functionread(Ks_wheat, phi_wheat, beta_wheat, s_h_wheat, s_w_wheat,s_star_wheat, s_fc_wheat, Ks_maize, phi_maize, beta_maize, s_h_maize, s_w_maize, s_star_maize,\
    s_fc_maize, Ks_potato, phi_potato, beta_potato, s_h_potato, s_w_potato,s_star_potato, s_fc_potato, Ks_barley, phi_barley, beta_barley, s_h_barley, s_w_barley,s_star_barley, s_fc_barley,yield_wheat, I_wheat,yield_maize, I_maize ,yield_potato, I_potato ,yield_barley, I_barley)

    x = np.zeros((1, 7500))
    o= objectivefunction (Ks_wheat, phi_wheat, beta_wheat, s_h_wheat, s_w_wheat,s_star_wheat, s_fc_wheat, Ks_maize, phi_maize, beta_maize, s_h_maize, s_w_maize, s_star_maize,\
    s_fc_maize, Ks_potato, phi_potato, beta_potato, s_h_potato, s_w_potato,s_star_potato, s_fc_potato, Ks_barley, phi_barley, beta_barley, s_h_barley, s_w_barley,s_star_barley,\
    s_fc_barley,yield_wheat, I_wheat,yield_maize, I_maize ,yield_potato, I_potato ,yield_barley, I_barley,landa,
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


    BestCost,best_solution =PSO( Ks_wheat, phi_wheat, beta_wheat, s_h_wheat, s_w_wheat,s_star_wheat, s_fc_wheat, Ks_maize, phi_maize, beta_maize, s_h_maize, s_w_maize, s_star_maize,\
    s_fc_maize, Ks_potato, phi_potato, beta_potato, s_h_potato, s_w_potato,s_star_potato, s_fc_potato, Ks_barley, phi_barley, beta_barley, s_h_barley, s_w_barley,s_star_barley\
    , s_fc_barley,yield_wheat, I_wheat,yield_maize, I_maize ,yield_potato, I_potato ,yield_barley, I_barley,objectivefunction,landa,minimumpercent,maximumpercent,I,I_sum,I_behbahan1, I_Jayezan1, I_ramhormoz1,I_ramshir1,\
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

    last_best_cost = BestCost[-1]
    formatted_last_best_cost = f"{last_best_cost:.3e}"
    
    def generate_plot(BestCost):
        plt.plot(BestCost)
        plt.xlabel('Iteration')
        plt.ylabel('Best profit')
        plt.title('Changes in Best Profit')

        # Save the plot to a bytes buffer
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()

        # Encode the plot image to base64 for rendering in HTML
        plot_img = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return plot_img

    plot_img = generate_plot(BestCost)

    agent1 =np.array( A_behbahan*best_solution[:, :60] ) # Assuming x1 is for the first agent
    agent2 = np.array(A_Jayezan*best_solution[:, 60:120])  # Assuming x2 is for the second agent
    agent3 = np.array(A_ramhormoz*best_solution[:, 120:180] ) # Assuming x3 is for the third agent
    agent4 = np.array(A_ramshir*best_solution[:, 180:240] ) # Assuming x4 is for the fourth agent
    agent5= np.array(A_shadegan*best_solution[:, 240:300])  # Assuming x5 is for the fifth agent

    years_to_display = [2003, 2006, 2009,2012, 2015, 2018]
    agent1 = np.array(agent1).reshape(15, 4)
    wheat1 = agent1[:, 0]
    barley1 = agent1[:, 1]
    maize1 = agent1[:, 2]
    potato1 = agent1[:, 3]
    years = np.arange(2003, 2018)
    # plt.figure(figsize=(5, 3))
    # plt.bar(years, wheat1, label='Wheat',color='gold' )
    # plt.bar(years, barley1, bottom=wheat1, label='Barley',color='darkorange')
    # plt.bar(years, maize1, bottom=wheat1 + barley1, label='Maize',color='limegreen')
    # plt.bar(years, potato1, bottom=wheat1 + barley1 + maize1, label='Potato',color='cornflowerblue')

    # plt.xlabel('Year')
    # plt.ylabel('Crop pattern (ha)')
    # plt.title('Agent 1 (Behbahan) Crop pattern Over 15 Years')
    # plt.xticks(years)
    # plt.legend()

    # plt.tight_layout()

    #plt.show()




    agent2 = agent2.reshape(15, 4)

    wheat2 = agent2[:, 0]
    barley2 = agent2[:, 1]
    maize2 = agent2[:, 2]
    potato2 = agent2[:, 3]
    years = np.arange(2003, 2018)
    # plt.figure(figsize=(10, 6))
    # # Stacked bar plot for Agent 2
    # plt.bar(years, wheat2, label='Wheat',color='gold')
    # plt.bar(years, barley2, bottom=wheat2, label='Barley',color='darkorange')
    # plt.bar(years, maize2, bottom=wheat2 + barley2, label='Maize',color='limegreen')
    # plt.bar(years, potato2, bottom=wheat2 + barley2 + maize2, label='Potato',color='cornflowerblue')

    # plt.xlabel('Year')
    # plt.ylabel('Crop pattern (ha)')
    # plt.title('Agent 2 (Jayezan) Crop pattern Over 15 Years')
    # plt.xticks(years)
    # plt.legend()
    # plt.tight_layout()

    # plt.show()



    agent3 = agent3.reshape(15, 4)
    wheat3 = agent3[:, 0]
    barley3 = agent3[:, 1]
    maize3 = agent3[:, 2]
    potato3 = agent3[:, 3]
    years = np.arange(2003, 2018)
    # plt.bar(years, wheat3, label='Wheat', color='gold')
    # plt.bar(years, barley3, bottom=wheat3, label='Barley',color='darkorange')
    # plt.bar(years, maize3, bottom=wheat3 + barley3, label='Maize',color='limegreen')
    # plt.bar(years, potato3, bottom=wheat3 + barley3 + maize3, label='Potato', color='cornflowerblue')
    # plt.xlabel('Year')
    # plt.ylabel('Crop pattern (ha)')
    # plt.title('Agent 3 (Ramhormoz) Crop pattern Over 15 Years')
    # plt.xticks(years)
    # plt.legend()
    # plt.tight_layout()

    # plt.show()


    agent4 = agent4.reshape(15, 4)

    wheat4 = agent4[:, 0]
    barley4 = agent4[:, 1]
    maize4 = agent4[:, 2]
    potato4 = agent4[:, 3]
    years = np.arange(2003, 2018)
    # plt.figure(figsize=(10, 6))
    # plt.bar(years, wheat4, label='Wheat', color='gold' )
    # plt.bar(years, barley4, bottom=wheat4, label='Barley',color='darkorange')
    # plt.bar(years, maize4, bottom=wheat4 + barley4, label='Maize',color='limegreen')
    # plt.bar(years, potato4, bottom=wheat4 + barley4 + maize4, label='Potato',color='cornflowerblue')

    # plt.xlabel('Year')
    # plt.ylabel('Crop pattern (ha)')
    # plt.title('Agent 4 (Ramshir) Crop pattern Over 15 Years')
    # plt.xticks(years)
    # plt.legend()
    # plt.tight_layout()

    # plt.show()


    agent5 = agent5.reshape(15, 4)

    wheat5 = agent5[:, 0]
    barley5 = agent5[:, 1]
    maize5 = agent5[:, 2]
    potato5 = agent5[:, 3]
    years = np.arange(2003, 2018)
    # plt.figure(figsize=(10, 6))
    # plt.bar(years, wheat5, label='Wheat',color='gold')
    # plt.bar(years, barley5, bottom=wheat5, label='Barley',color='darkorange')
    # plt.bar(years, maize5, bottom=wheat5 + barley5, label='Maize',color='limegreen')
    # plt.bar(years, potato5, bottom=wheat5 + barley5 + maize5, label='Potato',color='cornflowerblue')
    # plt.xlabel('Year')
    # plt.ylabel('Crop pattern (ha)')
    # plt.title('Agent 5 (Shadegan) Crop pattern Over 15 Years')
    # plt.xticks(years)
    # plt.legend()
    # plt.tight_layout()
    # plt.show()

    wheat_sum=(wheat1+wheat2+wheat3+wheat4+wheat5)
    barley_sum=(barley1+barley2+barley3+barley4+barley5)
    maize_sum=(maize1+maize2+maize3+maize4+maize5)
    potato_sum=(potato1+potato2+potato3+potato4+potato5)
    # print(wheat_sum)
    # years = np.arange(2003, 2018)
    # plt.figure(figsize=(10, 6))
    # plt.bar(years, wheat_sum, label='Wheat', color='gold')
    # plt.bar(years, barley_sum, bottom=wheat_sum, label='Barley',color='darkorange')
    # plt.bar(years, maize_sum, bottom=wheat_sum + barley_sum, label='Maize', color='limegreen')
    # plt.bar(years, potato_sum, bottom=wheat_sum + barley_sum + maize_sum, label='Potato', color='cornflowerblue')

    # plt.xlabel('Year')
    # plt.ylabel('Crop pattern (ha)')
    # plt.title('Total produced crop')
    # plt.xticks(years)
    # plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    # plt.tight_layout()

    # plt.show()

    # # Create a single figure with multiple subplots

    # Define the font properties
    # font_properties = FontProperties(family='Times New Roman', size=14, weight='bold')

    # fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20, 10))
    # years = np.arange(2003, 2018)
    # years_to_display = [2003, 2006, 2009,2012, 2015, 2018]
    # #years = np.arange(min(years), max(years) + 1, step=)
    # # Agent 1 subplot
    # axes[0, 0].bar(years, wheat1, label='Wheat', color='khaki')
    # axes[0, 0].bar(years, barley1, bottom=wheat1, label='Barley', color='lightcoral')
    # axes[0, 0].bar(years, maize1, bottom=wheat1 + barley1, label='Maize', color='lightgreen')
    # axes[0, 0].bar(years, potato1, bottom=wheat1 + barley1 + maize1, label='Potato', color='cornflowerblue')
    # axes[0, 0].set_title('Agent 1 (Behbahan)', fontproperties=font_properties)
    # axes[0, 0].set_xlabel('Year', fontproperties=font_properties)
    # axes[0, 0].set_ylabel('Area (ha)', fontproperties=font_properties)
    # axes[0, 0].tick_params(axis='both', labelsize=12)
    # axes[0, 0].get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    # # Agent 2 subplot
    # axes[0, 1].bar(years, wheat2, label='Wheat', color='khaki')
    # axes[0, 1].bar(years, barley2, bottom=wheat2, label='Barley', color='lightcoral')
    # axes[0, 1].bar(years, maize2, bottom=wheat2 + barley2, label='Maize', color='lightgreen')
    # axes[0, 1].bar(years, potato2, bottom=wheat2 + barley2 + maize2, label='Potato', color='cornflowerblue')
    # axes[0, 1].set_title('Agent 2 (Jayezan)', fontproperties=font_properties)
    # axes[0, 1].set_xlabel('Year', fontproperties=font_properties)
    # axes[0, 1].set_ylabel('Area (ha)', fontproperties=font_properties)
    # axes[0, 1].tick_params(axis='both', labelsize=12)
    # axes[0, 1].get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    # # Agent 3 subplot
    # axes[0, 2].bar(years, wheat3, label='Wheat', color='khaki')
    # axes[0, 2].bar(years, barley3, bottom=wheat3, label='Barley', color='lightcoral')
    # axes[0, 2].bar(years, maize3, bottom=wheat3 + barley3, label='Maize', color='lightgreen')
    # axes[0, 2].bar(years, potato3, bottom=wheat3 + barley3 + maize3, label='Potato', color='cornflowerblue')
    # axes[0, 2].set_title('Agent 3 (Ramhormoz)', fontproperties=font_properties)
    # axes[0, 2].set_xlabel('Year', fontproperties=font_properties)
    # axes[0, 2].set_ylabel('Area (ha)', fontproperties=font_properties)
    # axes[0, 2].tick_params(axis='both', labelsize=12)
    # axes[0, 2].get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    # # Agent 4 subplot
    # axes[1, 0].bar(years, wheat4, label='Wheat', color='khaki')
    # axes[1, 0].bar(years, barley4, bottom=wheat4, label='Barley', color='lightcoral')
    # axes[1, 0].bar(years, maize4, bottom=wheat4 + barley4, label='Maize', color='lightgreen')
    # axes[1, 0].bar(years, potato4, bottom=wheat4 + barley4 + maize4, label='Potato', color='cornflowerblue')
    # axes[1, 0].set_title('Agent 4 (Ramshir)', fontproperties=font_properties)
    # axes[1, 0].set_xlabel('Year', fontproperties=font_properties)
    # axes[1, 0].set_ylabel('Area (ha)', fontproperties=font_properties)
    # axes[1, 0].tick_params(axis='both', labelsize=12)
    # axes[1, 0].get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    # # Agent 5 subplot
    # axes[1, 1].bar(years, wheat5, label='Wheat', color='khaki')
    # axes[1, 1].bar(years, barley5, bottom=wheat5, label='Barley', color='lightcoral')
    # axes[1, 1].bar(years, maize5, bottom=wheat5 + barley5, label='Maize', color='lightgreen')
    # axes[1, 1].bar(years, potato5, bottom=wheat5 + barley5 + maize5, label='Potato', color='cornflowerblue')
    # axes[1, 1].set_title('Agent 5 (Shadegan)', fontproperties=font_properties)
    # axes[1, 1].set_xlabel('Year', fontproperties=font_properties)
    # axes[1, 1].set_ylabel('Area (ha)', fontproperties=font_properties)
    # axes[1, 1].tick_params(axis='both', labelsize=12)
    # axes[1, 1].get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    # # Total produced crop subplot
    # axes[1, 2].bar(years, wheat_sum, label='Wheat', color='khaki')
    # axes[1, 2].bar(years, barley_sum, bottom=wheat_sum, label='Barley', color='lightcoral')
    # axes[1, 2].bar(years, maize_sum, bottom=wheat_sum + barley_sum, label='Maize', color='lightgreen')
    # axes[1, 2].bar(years, potato_sum, bottom=wheat_sum + barley_sum + maize_sum, label='Potato', color='cornflowerblue')
    # axes[1, 2].set_title('Total produced crop', fontproperties=font_properties)
    # axes[1, 2].set_xlabel('Year', fontproperties=font_properties)
    # axes[1, 2].set_ylabel('Area (ha)', fontproperties=font_properties)
    # axes[1, 2].tick_params(axis='both', labelsize=12)
    # axes[1, 2].get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))


    # legend = axes[1, 1].legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4, prop=font_properties)
    # plt.suptitle('Crop Patern for Risk Taker attitude - Micro Irrigation', fontsize=16, fontweight='bold', fontproperties=font_properties)
    # for ax in axes.flat:
    #     ax.set_xticks(years_to_display)


    # # Adjust layout and show the plots
    # plt.tight_layout()
    # plt.show()


    print(I_sum)
    #print(BestCost)

    return render_template("show.html" , methods=['GET'], landa=landa ,minimumpercent=minimumpercent , 
                           maximumpercent=maximumpercent , soiltype_wheat=soiltype_wheat ,soiltype_barley=soiltype_barley,soiltype_maize=soiltype_maize,soiltype_potato=soiltype_potato , irrigation=irrigation ,BestCost =formatted_last_best_cost ,best_solution=best_solution, plot_img=plot_img )