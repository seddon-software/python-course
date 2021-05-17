import matplotlib.pyplot as plt

# plot multiple subplots within one figure

def plotSomeExtraData(axes):
    for i in range(0,8):
        axes[i].plot([50, 75, 100])

def plotSomeData(axes):
    for i in range(0,8):
        axes[i].plot([4, 9, 16, 25, i**2])

def setCustomAxis(fig):
    left = 0.15
    bottom = 0.1
    width = 0.3
    height = 0.1
    ax7 = fig.add_axes([left, bottom, width, height])
    return ax7

def setDefaultAxes(fig):
    rows = 4
    columns = 2
    ax1 = fig.add_subplot(rows, columns, 1) # first plot
    ax2 = fig.add_subplot(rows, columns, 2) # second plot
    ax3 = fig.add_subplot(rows, columns, 3) # third plot
    ax4 = fig.add_subplot(rows, columns, 4) # etc
    ax5 = fig.add_subplot(rows, columns, 5)
    ax6 = fig.add_subplot(rows, columns, 6)
    ax8 = fig.add_subplot(rows, columns, 8)
    return ax1, ax2, ax3, ax4, ax5, ax6, ax8

def main():
    fig = plt.figure()
    ax1, ax2, ax3, ax4, ax5, ax6, ax8 = setDefaultAxes(fig)
    ax7 = setCustomAxis(fig)
    axes = [ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8]
    plotSomeData(axes)
    plotSomeExtraData(axes)
    plt.tight_layout()
    plt.show()

main()
