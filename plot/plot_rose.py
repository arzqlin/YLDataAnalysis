import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import matplotlib
import numpy as np
from math import pi
from mpl_toolkits.axes_grid1 import make_axes_locatable
import inspect

def plot_rose(df, chemical):
    #prepping the axis of the graph
    theta = np.linspace(0,2*np.pi,37)
    r = np.linspace(0,7.6,20)

    Theta, R = np.meshgrid(theta, r)

    #sorting data from df
    C = np.zeros((19, 36))
    C.fill(np.nan)

    value_count = np.zeros((19,36))
    

    for key, value in df[chemical].iteritems():
        ws = df.at[key, 'm/s']
        wd = df.at[key, 'Degree']
        ws_bracket = int(ws/0.4)
        wd_bracket = int(wd/10)

        if np.isnan(C[ws_bracket][wd_bracket]) == True:
            value_count[ws_bracket][wd_bracket] += 1
            C[ws_bracket][wd_bracket] = value         
        else:
            value_count[ws_bracket][wd_bracket] += 1
            C[ws_bracket][wd_bracket] = (C[ws_bracket][wd_bracket] + value)/ value_count[ws_bracket][wd_bracket]
    
    max_value = max(max(x) for x in C)

    # set figure_title string
    fig_title = '{} Conc. (ppbv) vs Wind Condition at YL - 1/2011 to 12/2011'.format(chemical.capitalize())


    fig, ax = plt.subplots(subplot_kw={"projection":"polar"}, nrows = 1, ncols = 1,figsize=(11.69,8.27), dpi = 100)

    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    norm = matplotlib.colors.Normalize(vmin = 0, vmax = np.max(C), clip = False)

    im = ax.pcolormesh(Theta, R, C, cmap='Blues', norm = norm)

    t = plt.title(fig_title, fontdict = {'fontsize' : 16, 'fontweight' : 'bold'}, pad = 20)

    fig.colorbar(im)


    plt.tight_layout(pad=5)



def plot_rose_bullets(df, chemical):

    # clear out None values 
    df[chemical].fillna(-99999.0, inplace=True)
    df = df[df[chemical] >= 0] 


    df['speed_x'] = df['m/s'] * np.sin(df['Degree'] * pi / 180.0)
    df['speed_y'] = df['m/s'] * np.cos(df['Degree'] * pi / 180.0)

    fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize=(14, 10), dpi=100)

    ax.set_aspect('equal')

    ax = df.plot(kind = 'scatter', x='speed_x', y='speed_y', c = df[chemical], alpha=0.8, ax = ax, grid = True,colormap='viridis_r', s = 5)
    

    ax.set_title('Pollution Rose of {} - 2011'.format(chemical.capitalize()),fontsize = 20)
    ax.set_xlabel('Speed X (m/s)',fontsize = 16)
    ax.set_ylabel('Speed Y (m/s)',fontsize = 16)
    ax.set_axisbelow(True)

    # make the axes equal so (0,0) would be at the center
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    lim = max([x0, x1, y0, y1], key=abs)
    ax.set_xlim(lim * -1, lim)
    ax.set_ylim(lim * -1, lim)


    f = plt.gcf()
    cax = f.get_axes()[1]
    cax.set_ylabel('Concentration (ppbv)', fontsize = 16, labelpad = 16 )
 
    plt.tight_layout()
def plot_rose_ARCHIVE(df, chemical):
    df['speed_x'] = df['m/s'] * np.sin(df['Degree'] * pi / 180.0)
    df['speed_y'] = df['m/s'] * np.cos(df['Degree'] * pi / 180.0)

    fig, ax = plt.subplots(figsize=(10, 10), dpi=100)

    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()

    ax.set_aspect('equal')

    ax = df.plot(kind = 'scatter', x='speed_x', y='speed_y', c = df[chemical], alpha=0.8, ax = ax, grid = True,colormap='viridis_r', s = 10)
    

    ax.set_title('Pollution rose of {}'.format(chemical),fontsize = 20)
    ax.set_xlabel('Speed_x',fontsize = 16)
    ax.set_ylabel('Speed_y',fontsize = 16)

    divider = make_axes_locatable(ax)
    cax1 = divider.append_axes("right", size="5%", pad=0.05)



    plt.tight_layout(h_pad=1)

if __name__ == '__main__':
    pass