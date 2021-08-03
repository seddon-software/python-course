import matplotlib.pyplot as plt
import numpy as np

def configureSubplot(ax1, title, x, y):
    ax1.set_title(title)
    ax1.set_xlabel(x)
    ax1.set_ylabel(y)

def main():
    # define subplots     
    ax1 = plt.subplot2grid((4,5),(0,0), colspan=3, rowspan=3)
    ax2 = plt.subplot2grid((4,5),(3,0), colspan=2)
    ax3 = plt.subplot2grid((4,5),(3,2), colspan=2)
    ax4 = plt.subplot2grid((4,5),(0,3), rowspan=2, colspan=2)

    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=1.0, hspace=1.0)

    t = np.arange(0.0, 5.0, 0.01)
    ax1.plot(t, t*t)
    ax2.plot(t, t*t + t)
    ax3.plot(t, t*t + 1)
    ax4.plot(t, t*t*t)
    configureSubplot(ax1, 'y = t^2'    , 't', 'y')
    configureSubplot(ax2, 'y = t^2 + t', 't', 'y')
    configureSubplot(ax3, 'y = t^2 + 1', 't', 'y')
    configureSubplot(ax4, 'y = t^3'    , 't', 'y')
    plt.show()

main()