import pandas as pd
import tkinter.ttk as ttk
import tkinter as tk
import numpy as np
import multiprocessing as mp
import time
import easygui
import math, cmath
from scipy.linalg import logm

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.figure import Figure
from tkinter import filedialog

class MyWindow:
    # this routine is called when the MyWindow object is created
    def __init__(self, root, pb, fig, canvas, q):
        # self points to the object's dictionary
        # store various variable for use in other methods
        self.root = root
        self.pb = pb
        self.fig = fig
        self.canvas = canvas
        self.q = q
        self.setup()

    def progressbar_start(self):
        pb.pack()
        self.pb_label.pack()
        pb.start()

    def progressbar_stop(self):
        pb.stop()
        pb.pack_forget()
        self.pb_label.pack_forget()

    def create_results(self, q, results):
        # this runs in another process and uses a q to share info with the calling process
        N = 10
        for n in range(N):
            results.append(n*n)
        q.put(results)


    def setup(self):
        # get variable from object dictionary
        root = self.root
        fig = self.fig
        canvas = self.canvas
        q = self.q
        
        # pack_toolbar=False will make it easier to use a layout manager later on.
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()

        cd_mode =  tk.Button(master=root, text="Mueller Matrix - CD mode", padx=10, 
                                pady=5, fg="white", bg="#263D42", command=self.test)

        cd_mode.pack(side=tk.BOTTOM)

        quitButton = tk.Button(master=root, text="Quit", command=root.quit)
        # pb = ttk.Progressbar(master=root, orient='horizontal', mode='indeterminate', length=500)

        # Packing order is important. Widgets are processed sequentially and if there
        # is no space left, because the window is too small, they are not displayed.
        # The canvas is rather flexible in its size, so we pack it last which makes
        # sure the UI controls are displayed as long as possible.
        quitButton.pack(side=tk.BOTTOM)
        pb.pack(side=tk.BOTTOM)
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.pb_label = tk.Label(text = 'Processing data')
        
        self.pb_label.pack(side=tk.BOTTOM)
        self.createSubProcess()

    def createSubProcess(self):
        # create a sub process that will append some data to results
        results = [1, 2, 3]
        p = mp.Process(target=MyWindow.create_results, args=(self, q, results))
        p.start()
        results = q.get()
        print(results)
        p.join()

    def test(self):
        

        def getFileNames():
            fileNames = filedialog.askopenfilenames(
                initialdir=".", 
                title="Select File",
                filetypes = (("comma separated file","*.csv"), ("all files", "*.*"))
            )
            return fileNames

        self.progressbar_start()
        
        files = getFileNames()

        

        csv_files = []

        for filename in files:
        
            csv_files.append(filename)
        

        def plotGraph():
            # assume only 1 file is returned
            for file in csv_files:
               
                csv_file = pd.read_csv(file, skiprows = 16) 
                csv_file = csv_file[['Wavelength', 'X', 'Y', 'M00', 'M01', 'M02', 'M03', 'M10',
                    'M11', 'M12', 'M13', 'M20', 'M21', 'M22', 'M23', 'M30', 'M31', 'M32', 'M33', 'CD', 'CR', 'LD', 'LR', 'LDp', 'LRp']] 
                msg5 = "Do you want to substract the baseline? if yes, please select your baseline in the next window."
                choices5 = ["Yes", "No"]
                reply5 = easygui.buttonbox(msg5, choices=choices5)
                    
                if str(reply5) == 'Yes':
                    csv_baseline = []
                    print(dir(easygui))
                    baselines = self.gui.baseline()

                    for baselin in baselines:
                        csv_baseline.append(baselin)

                    for base in csv_baseline:
                        with open(base) as q:
                            for line in q:
                                if line.startswith('DATA'):
                                    t=t+1
                                    break
                                else:
                                    t=t+1
                        csv_base = pd.read_csv(base, skiprows = t) 
                        csv_base = csv_base[['Wavelength', 'X', 'Y', 'M00', 'M01', 'M02', 'M03', 'M10',
                            'M11', 'M12', 'M13', 'M20', 'M21', 'M22', 'M23', 'M30', 'M31', 'M32', 'M33', 'CD', 'CR', 'LD', 'LR', 'LDp', 'LRp']] 

                    
                    csv_file['CD'] = csv_file['CD'] - csv_base['CD']
                    csv_file['CR'] = csv_file['CR'] - csv_base['CR']
                    csv_file['LD'] = csv_file['LD'] - csv_base['LD']
                    csv_file['LR'] = csv_file['LR'] - csv_base['LR']
                    csv_file['LDp'] = csv_file['LDp'] - csv_base['LDp']
                    csv_file['LRp'] = csv_file['LRp'] - csv_base['LRp']

                

                csv_file['CD'] *= 32980 * 0.94
                csv_file['CR'] *= 32980 * 0.94
                csv_file['LR'] *= -0.94
                csv_file['LRp'] *= -0.94
                csv_file['LD'] *= -0.94
                csv_file['LDp'] *= -0.94

                t = csv_file['Wavelength'][0]

                k = 0

                for i in range(len(csv_file)):
                    if csv_file['Wavelength'][i] == t:
                        k += 1

                Wavelength_new = []

                Wavelength_new.append(csv_file['Wavelength'][0])

                Wavelength_CD = [[] for i in range(k+2)]
                Wavelength_CR = [[] for i in range(k+2)]
                Wavelength_LR = [[] for i in range(k+2)]
                Wavelength_LD = [[] for i in range(k+2)]
                Wavelength_LRp = [[] for i in range(k+2)]
                Wavelength_LDp = [[] for i in range(k+2)]
                Wavelength_g_factor = [[] for i in range(k+2)]

                Wavelength_Abs = [[] for i in range(k+2)]
                Wavelength_M00 = [[] for i in range(k+2)]
                Wavelength_M01 = [[] for i in range(k+2)]
                Wavelength_M02 = [[] for i in range(k+2)]
                Wavelength_M03 = [[] for i in range(k+2)]
                Wavelength_M10 = [[] for i in range(k+2)]
                Wavelength_M11 = [[] for i in range(k+2)]
                Wavelength_M12 = [[] for i in range(k+2)]
                Wavelength_M13 = [[] for i in range(k+2)]
                Wavelength_M20 = [[] for i in range(k+2)]
                Wavelength_M21 = [[] for i in range(k+2)]
                Wavelength_M22 = [[] for i in range(k+2)]
                Wavelength_M23 = [[] for i in range(k+2)]
                Wavelength_M30 = [[] for i in range(k+2)]
                Wavelength_M31 = [[] for i in range(k+2)]
                Wavelength_M32 = [[] for i in range(k+2)]
                Wavelength_M33 = [[] for i in range(k+2)]

                Wavelength_CD_new = [[] for i in range(k+2)]
                Wavelength_LD_new = [[] for i in range(k+2)]
                Wavelength_CB_new = [[] for i in range(k+2)]
                Wavelength_LB_new = [[] for i in range(k+2)]
                Wavelength_LDp_new = [[] for i in range(k+2)]
                Wavelength_LBp_new = [[] for i in range(k+2)]
                Wavelength_g_factor_new = [[] for i in range(k+2)]

                Wavelength_mCD = [[] for i in range(k+2)]   # with matrix logarithm
                Wavelength_mCB = [[] for i in range(k+2)]
                Wavelength_mLB = [[] for i in range(k+2)]
                Wavelength_mLD = [[] for i in range(k+2)]
                Wavelength_mLBp = [[] for i in range(k+2)]
                Wavelength_mLDp = [[] for i in range(k+2)]
                Wavelength_mg_factor = [[] for i in range(k+2)]

                Wavelength_aCD = [[] for i in range(k+2)]   # with analytical inversion
                Wavelength_aCB = [[] for i in range(k+2)]
                Wavelength_aLB = [[] for i in range(k+2)]
                Wavelength_aLD = [[] for i in range(k+2)]
                Wavelength_aLBp = [[] for i in range(k+2)]
                Wavelength_aLDp = [[] for i in range(k+2)]
                Wavelength_ag_factor = [[] for i in range(k+2)]

                Wavelength_CD[0].append(csv_file['Wavelength'][0])
                Wavelength_CR[0].append(csv_file['Wavelength'][0])
                Wavelength_LR[0].append(csv_file['Wavelength'][0])
                Wavelength_LD[0].append(csv_file['Wavelength'][0])
                Wavelength_LRp[0].append(csv_file['Wavelength'][0])
                Wavelength_LDp[0].append(csv_file['Wavelength'][0])
                Wavelength_g_factor[0].append(csv_file['Wavelength'][0])
                Wavelength_Abs[0].append(csv_file['Wavelength'][0])
                Wavelength_CD_new[0].append(csv_file['Wavelength'][0])
                Wavelength_LD_new[0].append(csv_file['Wavelength'][0])
                Wavelength_LDp_new[0].append(csv_file['Wavelength'][0])
                Wavelength_CB_new[0].append(csv_file['Wavelength'][0])
                Wavelength_LB_new[0].append(csv_file['Wavelength'][0])
                Wavelength_LBp_new[0].append(csv_file['Wavelength'][0])
                Wavelength_g_factor_new[0].append(csv_file['Wavelength'][0])

                Wavelength_mCD[0].append(csv_file['Wavelength'][0])
                Wavelength_mCB[0].append(csv_file['Wavelength'][0])
                Wavelength_mLB[0].append(csv_file['Wavelength'][0])
                Wavelength_mLD[0].append(csv_file['Wavelength'][0])
                Wavelength_mLBp[0].append(csv_file['Wavelength'][0])
                Wavelength_mLDp[0].append(csv_file['Wavelength'][0])
                Wavelength_mg_factor[0].append(csv_file['Wavelength'][0])
                
                Wavelength_aCD[0].append(csv_file['Wavelength'][0])
                Wavelength_aCB[0].append(csv_file['Wavelength'][0])
                Wavelength_aLB[0].append(csv_file['Wavelength'][0])
                Wavelength_aLD[0].append(csv_file['Wavelength'][0])
                Wavelength_aLBp[0].append(csv_file['Wavelength'][0])
                Wavelength_aLDp[0].append(csv_file['Wavelength'][0])
                Wavelength_ag_factor[0].append(csv_file['Wavelength'][0])

                Wavelength_CD[1].append(csv_file['CD'][0])   
                Wavelength_CR[1].append((csv_file['CR'][0]))    
                Wavelength_LR[1].append((csv_file['LR'][0])) 
                Wavelength_LD[1].append(csv_file['LD'][0]) 
                Wavelength_LRp[1].append((csv_file['LRp'][0])) 
                Wavelength_LDp[1].append(csv_file['LDp'][0])  
                Wavelength_g_factor[1].append((csv_file['CD'][0]/32980)/(math.log10(1/csv_file['M00'][0]))) 

                
                if str(reply5) == 'Yes':
                    M = []
                    M.append(csv_file['M00'][0])
                    M.append(csv_file['M01'][0])
                    M.append(csv_file['M02'][0])
                    M.append(csv_file['M03'][0])
                    M.append(csv_file['M10'][0])
                    M.append(csv_file['M11'][0])
                    M.append(csv_file['M12'][0])
                    M.append(csv_file['M13'][0])
                    M.append(csv_file['M20'][0])
                    M.append(csv_file['M21'][0])
                    M.append(csv_file['M22'][0])
                    M.append(csv_file['M23'][0])
                    M.append(csv_file['M30'][0])
                    M.append(csv_file['M31'][0])
                    M.append(csv_file['M32'][0])
                    M.append(csv_file['M33'][0])

                    matrix = np.array(M).reshape(4,4)

                    LM = -1*logm(matrix)

                    B = []
                    B.append(csv_base['M00'][0])    # base = baseline
                    B.append(csv_base['M01'][0])
                    B.append(csv_base['M02'][0])
                    B.append(csv_base['M03'][0])
                    B.append(csv_base['M10'][0])
                    B.append(csv_base['M11'][0])
                    B.append(csv_base['M12'][0])
                    B.append(csv_base['M13'][0])
                    B.append(csv_base['M20'][0])
                    B.append(csv_base['M21'][0])
                    B.append(csv_base['M22'][0])
                    B.append(csv_base['M23'][0])
                    B.append(csv_base['M30'][0])
                    B.append(csv_base['M31'][0])
                    B.append(csv_base['M32'][0])
                    B.append(csv_base['M33'][0])

                    matrix_base = np.array(B).reshape(4,4)

                    LM_base = -1*logm(matrix_base)

                    Wavelength_mCD[1].append(((LM[0, 3] + LM[3, 0])/-2) - ((LM_base[0, 3] + LM_base[3, 0])/-2)) 
                    Wavelength_mCB[1].append(((LM[1, 2] - LM[2, 1])/2) - ((LM_base[1, 2] - LM_base[2, 1])/2))
                    Wavelength_mLD[1].append(((LM[0, 1] + LM[1, 0])/-2) - ((LM_base[0, 1] + LM_base[1, 0])/-2))
                    Wavelength_mLDp[1].append(((LM[0, 2] + LM[2, 0])/-2) - ((LM_base[0, 2] + LM_base[2, 0])/-2))
                    Wavelength_mLB[1].append(((LM[2, 3] - LM[3, 2])/2) - ((LM_base[2, 3] - LM_base[3, 2])/2))
                    Wavelength_mLBp[1].append(((LM[1, 3] - LM[3, 1])/2) - ((LM_base[1, 3] - LM_base[3, 1])/2))
                    Wavelength_mg_factor[1].append(((((LM[0, 3] + LM[3, 0])/-2) - ((LM_base[0, 3] + LM_base[3, 0])/-2))/((LM[0, 0] + LM[1, 1] + LM[2, 2] + LM[3, 3])/4) - (LM_base[0, 0] + LM_base[1, 1] + LM_base[2, 2] + LM_base[3, 3])/4))

                    r00 = math.sqrt((matrix[0, 0] + matrix[0, 1] + matrix[1, 0] + matrix[1, 1])/2)
                    r01 = math.sqrt((matrix[0, 0] - matrix[0, 1] + matrix[1, 0] - matrix[1, 1])/2)
                    r10 = math.sqrt((matrix[0, 0] + matrix[0, 1] - matrix[1, 0] - matrix[1, 1])/2)
                    r11 = math.sqrt((matrix[0, 0] - matrix[0, 1] - matrix[1, 0] + matrix[1, 1])/2)

                    e01 = ((matrix[0, 2] + matrix[1, 2]) - (matrix[0, 3] + matrix[1, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 0])**2 - (matrix[0, 1] + matrix[1, 1])**2)
                    e10 = ((matrix[2, 0] + matrix[2, 1]) + (matrix[3, 0] + matrix[3, 1])*1j) / math.sqrt((matrix[0, 0] + matrix[0, 1])**2 - (matrix[1, 0] + matrix[1, 1])**2)
                    e11 = ((matrix[2, 2] + matrix[3, 3]) + (matrix[3, 2] - matrix[2, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 1])**2 - (matrix[1, 0] + matrix[0, 1])**2)

                    K = ((r00*r11*e11 - r01*r10*e10*e01)**-0.5)
                    Tk = 2*cmath.acos((K*(r00+r11*e11))/2)
                    O = (Tk*K)/(2*cmath.sin(Tk/2))

                    LBLD = O * (r00 - r11*e11)*1j
                    LBpLDp = O * (r01*e01 + r10*e10)*1j
                    CBCD = O * (r01*e01 - r10*e10)

                    r00_base = math.sqrt((matrix_base[0, 0] + matrix_base[0, 1] + matrix_base[1, 0] + matrix_base[1, 1])/2)
                    r01_base = math.sqrt((matrix_base[0, 0] - matrix_base[0, 1] + matrix_base[1, 0] - matrix_base[1, 1])/2)
                    r10_base = math.sqrt((matrix_base[0, 0] + matrix_base[0, 1] - matrix_base[1, 0] - matrix_base[1, 1])/2)
                    r11_base = math.sqrt((matrix_base[0, 0] - matrix_base[0, 1] - matrix_base[1, 0] + matrix_base[1, 1])/2)

                    e01_base = ((matrix_base[0, 2] + matrix_base[1, 2]) - (matrix_base[0, 3] + matrix_base[1, 3])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[1, 0])**2 - (matrix_base[0, 1] + matrix_base[1, 1])**2)
                    e10_base = ((matrix_base[2, 0] + matrix_base[2, 1]) + (matrix_base[3, 0] + matrix_base[3, 1])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[0, 1])**2 - (matrix_base[1, 0] + matrix_base[1, 1])**2)
                    e11_base = ((matrix_base[2, 2] + matrix_base[3, 3]) + (matrix_base[3, 2] - matrix_base[2, 3])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[1, 1])**2 - (matrix_base[1, 0] + matrix_base[0, 1])**2)

                    K_base = ((r00_base*r11_base*e11_base - r01_base*r10_base*e10_base*e01_base)**-0.5)
                    Tk_base = 2*cmath.acos((K_base*(r00_base+r11_base*e11_base))/2)
                    O_base = (Tk_base*K_base)/(2*cmath.sin(Tk_base/2))

                    LBLD_base = O_base * (r00_base - r11_base*e11_base)*1j
                    LBpLDp_base = O_base * (r01_base*e01_base + r10_base*e10_base)*1j
                    CBCD_base = O_base * (r01_base*e01_base - r10_base*e10_base)

                    Wavelength_aLB[1].append(LBLD.real - LBLD_base.real)
                    Wavelength_aLD[1].append(-1*LBLD.imag - -1*LBLD_base.imag)

                    Wavelength_aLBp[1].append(LBpLDp.real - LBpLDp_base.real)
                    Wavelength_aLDp[1].append(-1*LBpLDp.imag - -1*LBpLDp_base.imag)

                    Wavelength_aCB[1].append(CBCD.real - CBCD_base.real)
                    Wavelength_aCD[1].append(-1*CBCD.imag - -1*CBCD_base.imag)

                    Wavelength_ag_factor[1].append((-1*CBCD.imag - -1*CBCD_base.imag)/(math.log10(1/(csv_file['M00'][0]/csv_base['M00'][0]))))

                    Wavelength_Abs[1].append(math.log10(1/(csv_file['M00'][0]/csv_base['M00'][0])))
                    Wavelength_CD_new[1].append(32980*0.94*0.993557*((csv_file['M30'][0]+csv_file['M03'][0])/(2*csv_file['M00'][0])-(csv_base['M30'][0]+csv_base['M03'][0])/(2*csv_base['M00'][0]))) 
                    Wavelength_LD_new[1].append((-1.070135)*((csv_file['M10'][0]+csv_file['M01'][0])/(2*csv_file['M00'][0])-(csv_base['M10'][0]+csv_base['M01'][0])/(2*csv_base['M00'][0])))  
                    Wavelength_LDp_new[1].append((-1.063424)*((csv_file['M20'][0]+csv_file['M02'][0])/(2*csv_file['M00'][0])-(csv_base['M20'][0]+csv_base['M02'][0])/(2*csv_base['M00'][0]))) 
                    Wavelength_CB_new[1].append(0.285787*1000*math.degrees(2*(np.arcsin((csv_file['M12'][0]-csv_file['M21'][0])/(2*csv_file['M00'][0])-np.arcsin((csv_base['M12'][0]-csv_base['M21'][0])/(2*csv_base['M00'][0]))))))  
                    Wavelength_LB_new[1].append((-0.0193343)*math.degrees((np.arcsin((csv_file['M23'][0]-csv_file['M32'][0])/(2*csv_file['M00'][0])-np.arcsin((csv_base['M23'][0]-csv_base['M32'][0])/(2*csv_base['M00'][0]))))))
                    Wavelength_LBp_new[1].append((-0.2056925)*math.degrees((np.arcsin((csv_file['M31'][0]-csv_file['M13'][0])/(2*csv_file['M00'][0])-np.arcsin((csv_base['M31'][0]-csv_base['M13'][0])/(2*csv_base['M00'][0]))))))
                    Wavelength_g_factor_new[1].append((((0.94*0.993557*((csv_file['M30'][0]+csv_file['M03'][0])/(2*csv_file['M00'][0])-(csv_base['M30'][0]+csv_base['M03'][0])/(2*csv_base['M00'][0]))))/(math.log10(1/(csv_file['M00'][0]/csv_base['M00'][0])))))
                else:
                    M = []
                    M.append(csv_file['M00'][0])
                    M.append(csv_file['M01'][0])
                    M.append(csv_file['M02'][0])
                    M.append(csv_file['M03'][0])
                    M.append(csv_file['M10'][0])
                    M.append(csv_file['M11'][0])
                    M.append(csv_file['M12'][0])
                    M.append(csv_file['M13'][0])
                    M.append(csv_file['M20'][0])
                    M.append(csv_file['M21'][0])
                    M.append(csv_file['M22'][0])
                    M.append(csv_file['M23'][0])
                    M.append(csv_file['M30'][0])
                    M.append(csv_file['M31'][0])
                    M.append(csv_file['M32'][0])
                    M.append(csv_file['M33'][0])

                    matrix = np.array(M).reshape(4,4)

                    LM = -1*logm(matrix)

                    Wavelength_mCD[1].append((LM[0, 3] + LM[3, 0])/-2)
                    Wavelength_mCB[1].append((LM[1, 2] - LM[2, 1])/2)
                    Wavelength_mLD[1].append((LM[0, 1] + LM[1, 0])/-2)
                    Wavelength_mLDp[1].append((LM[0, 2] + LM[2, 0])/-2)
                    Wavelength_mLB[1].append((LM[2, 3] - LM[3, 2])/2)
                    Wavelength_mLBp[1].append((LM[1, 3] - LM[3, 1])/2)
                    Wavelength_mg_factor[1].append((((LM[0, 3] + LM[3, 0])/-2)/((LM[0, 0] + LM[1, 1] + LM[2, 2] + LM[3, 3])/4)))

                    r00 = math.sqrt((matrix[0, 0] + matrix[0, 1] + matrix[1, 0] + matrix[1, 1])/2)
                    r01 = math.sqrt((matrix[0, 0] - matrix[0, 1] + matrix[1, 0] - matrix[1, 1])/2)
                    r10 = math.sqrt((matrix[0, 0] + matrix[0, 1] - matrix[1, 0] - matrix[1, 1])/2)
                    r11 = math.sqrt((matrix[0, 0] - matrix[0, 1] - matrix[1, 0] + matrix[1, 1])/2)

                    e01 = ((matrix[0, 2] + matrix[1, 2]) - (matrix[0, 3] + matrix[1, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 0])**2 - (matrix[0, 1] + matrix[1, 1])**2)
                    e10 = ((matrix[2, 0] + matrix[2, 1]) + (matrix[3, 0] + matrix[3, 1])*1j) / math.sqrt((matrix[0, 0] + matrix[0, 1])**2 - (matrix[1, 0] + matrix[1, 1])**2)
                    e11 = ((matrix[2, 2] + matrix[3, 3]) + (matrix[3, 2] - matrix[2, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 1])**2 - (matrix[1, 0] + matrix[0, 1])**2)

                    K = ((r00*r11*e11 - r01*r10*e10*e01)**-0.5)
                    Tk = 2*cmath.acos((K*(r00+r11*e11))/2)
                    O = (Tk*K)/(2*cmath.sin(Tk/2))

                    LBLD = O * (r00 - r11*e11)*1j
                    LBpLDp = O * (r01*e01 + r10*e10)*1j
                    CBCD = O * (r01*e01 - r10*e10)

                    Wavelength_aLB[1].append(LBLD.real)
                    Wavelength_aLD[1].append(-1*LBLD.imag)

                    Wavelength_aLBp[1].append(LBpLDp.real)
                    Wavelength_aLDp[1].append(-1*LBpLDp.imag)

                    Wavelength_aCB[1].append(CBCD.real)
                    Wavelength_aCD[1].append(-1*CBCD.imag)

                    Wavelength_ag_factor[1].append((-1*CBCD.imag)/(math.log10(1/csv_file['M00'][0])))


                    Wavelength_Abs[1].append(math.log10(1/csv_file['M00'][0]))
                    Wavelength_CD_new[1].append(32980*0.94*0.993557*((csv_file['M30'][0]+csv_file['M03'][0])/(2*csv_file['M00'][0]))) 
                    Wavelength_LD_new[1].append((-1.070135)*((csv_file['M10'][0]+csv_file['M01'][0])/(2*csv_file['M00'][0])))  
                    Wavelength_LDp_new[1].append((-1.063424)*((csv_file['M20'][0]+csv_file['M02'][0])/(2*csv_file['M00'][0]))) 
                    Wavelength_CB_new[1].append(0.285787*1000*math.degrees(2*np.arcsin((csv_file['M12'][0]-csv_file['M21'][0])/(2*csv_file['M00'][0]))))  
                    Wavelength_LB_new[1].append((-0.0193343)*math.degrees(np.arcsin((csv_file['M23'][0]-csv_file['M32'][0])/(2*csv_file['M00'][0]))))
                    Wavelength_LBp_new[1].append((-0.2056925)*math.degrees(np.arcsin((csv_file['M31'][0]-csv_file['M13'][0])/(2*csv_file['M00'][0]))))
                    Wavelength_g_factor_new[1].append((((csv_file['M30'][0]+csv_file['M03'][0])/(2*csv_file['M00'][0]))/(math.log10(1/csv_file['M00'][0]))))
                

                Wavelength_M00[0].append(csv_file['Wavelength'][0])
                Wavelength_M00[1].append(csv_file['M00'][0])

                Wavelength_M01[0].append(csv_file['Wavelength'][0])
                Wavelength_M01[1].append(csv_file['M01'][0])

                Wavelength_M02[0].append(csv_file['Wavelength'][0])
                Wavelength_M02[1].append(csv_file['M02'][0])

                Wavelength_M03[0].append(csv_file['Wavelength'][0])
                Wavelength_M03[1].append(csv_file['M03'][0])

                Wavelength_M10[0].append(csv_file['Wavelength'][0])
                Wavelength_M10[1].append(csv_file['M10'][0])

                Wavelength_M11[0].append(csv_file['Wavelength'][0])
                Wavelength_M11[1].append(csv_file['M11'][0])

                Wavelength_M12[0].append(csv_file['Wavelength'][0])
                Wavelength_M12[1].append(csv_file['M12'][0])

                Wavelength_M13[0].append(csv_file['Wavelength'][0])
                Wavelength_M13[1].append(csv_file['M13'][0])

                Wavelength_M20[0].append(csv_file['Wavelength'][0])
                Wavelength_M20[1].append(csv_file['M20'][0])

                Wavelength_M21[0].append(csv_file['Wavelength'][0])
                Wavelength_M21[1].append(csv_file['M21'][0])

                Wavelength_M22[0].append(csv_file['Wavelength'][0])
                Wavelength_M22[1].append(csv_file['M22'][0])

                Wavelength_M23[0].append(csv_file['Wavelength'][0])
                Wavelength_M23[1].append(csv_file['M23'][0])

                Wavelength_M30[0].append(csv_file['Wavelength'][0])
                Wavelength_M30[1].append(csv_file['M30'][0])

                Wavelength_M31[0].append(csv_file['Wavelength'][0])
                Wavelength_M31[1].append(csv_file['M31'][0])

                Wavelength_M32[0].append(csv_file['Wavelength'][0])
                Wavelength_M32[1].append(csv_file['M32'][0])

                Wavelength_M33[0].append(csv_file['Wavelength'][0])
                Wavelength_M33[1].append(csv_file['M33'][0])


                for i in range(1, len(csv_file)):
                    if csv_file['Wavelength'][i] != t:
                        Wavelength_CD[0].append(csv_file['Wavelength'][i])
                        Wavelength_CR[0].append(csv_file['Wavelength'][i])
                        Wavelength_LR[0].append(csv_file['Wavelength'][i])
                        Wavelength_LD[0].append(csv_file['Wavelength'][i])
                        Wavelength_LRp[0].append(csv_file['Wavelength'][i])
                        Wavelength_LDp[0].append(csv_file['Wavelength'][i])
                        Wavelength_g_factor[0].append(csv_file['Wavelength'][i])

                        Wavelength_Abs[0].append(csv_file['Wavelength'][i])
                        Wavelength_M00[0].append(csv_file['Wavelength'][i])
                        Wavelength_M01[0].append(csv_file['Wavelength'][i])
                        Wavelength_M02[0].append(csv_file['Wavelength'][i])
                        Wavelength_M03[0].append(csv_file['Wavelength'][i])
                        Wavelength_M10[0].append(csv_file['Wavelength'][i])
                        Wavelength_M11[0].append(csv_file['Wavelength'][i])
                        Wavelength_M12[0].append(csv_file['Wavelength'][i])
                        Wavelength_M13[0].append(csv_file['Wavelength'][i])
                        Wavelength_M20[0].append(csv_file['Wavelength'][i])
                        Wavelength_M21[0].append(csv_file['Wavelength'][i])
                        Wavelength_M22[0].append(csv_file['Wavelength'][i])
                        Wavelength_M23[0].append(csv_file['Wavelength'][i])
                        Wavelength_M30[0].append(csv_file['Wavelength'][i])
                        Wavelength_M31[0].append(csv_file['Wavelength'][i])
                        Wavelength_M32[0].append(csv_file['Wavelength'][i])
                        Wavelength_M33[0].append(csv_file['Wavelength'][i])

                        Wavelength_CD_new[0].append(csv_file['Wavelength'][i])
                        Wavelength_LD_new[0].append(csv_file['Wavelength'][i])
                        Wavelength_LDp_new[0].append(csv_file['Wavelength'][i])
                        Wavelength_CB_new[0].append(csv_file['Wavelength'][i])
                        Wavelength_LB_new[0].append(csv_file['Wavelength'][i])
                        Wavelength_LBp_new[0].append(csv_file['Wavelength'][i])
                        Wavelength_g_factor_new[0].append(csv_file['Wavelength'][i])

                        Wavelength_mCD[0].append(csv_file['Wavelength'][i])
                        Wavelength_mCB[0].append(csv_file['Wavelength'][i])
                        Wavelength_mLB[0].append(csv_file['Wavelength'][i])
                        Wavelength_mLD[0].append(csv_file['Wavelength'][i])
                        Wavelength_mLBp[0].append(csv_file['Wavelength'][i])
                        Wavelength_mLDp[0].append(csv_file['Wavelength'][i])
                        Wavelength_mg_factor[0].append(csv_file['Wavelength'][i])

                        Wavelength_aCD[0].append(csv_file['Wavelength'][i])
                        Wavelength_aCB[0].append(csv_file['Wavelength'][i])
                        Wavelength_aLB[0].append(csv_file['Wavelength'][i])
                        Wavelength_aLD[0].append(csv_file['Wavelength'][i])
                        Wavelength_aLBp[0].append(csv_file['Wavelength'][i])
                        Wavelength_aLDp[0].append(csv_file['Wavelength'][i])
                        Wavelength_ag_factor[0].append(csv_file['Wavelength'][i])
                        
                    else:
                        break

                j = 0

                for i in range(1, len(csv_file)):
                    if csv_file['Wavelength'][i] != t:
                        Wavelength_CD[j+1].append(csv_file['CD'][i])
                        Wavelength_CR[j+1].append((csv_file['CR'][i]))
                        Wavelength_LR[j+1].append((csv_file['LR'][i]))
                        Wavelength_LD[j+1].append(csv_file['LD'][i])
                        Wavelength_LRp[j+1].append((csv_file['LRp'][i]))
                        Wavelength_LDp[j+1].append(csv_file['LDp'][i])
                        Wavelength_g_factor[j+1].append(csv_file['CD'][i]/32980/(math.log10(1/csv_file['M00'][i])))
                        Wavelength_M00[j+1].append(csv_file['M00'][i])
                        Wavelength_M01[j+1].append(csv_file['M01'][i])
                        Wavelength_M02[j+1].append(csv_file['M02'][i])
                        Wavelength_M03[j+1].append(csv_file['M03'][i])
                        Wavelength_M10[j+1].append(csv_file['M10'][i])
                        Wavelength_M11[j+1].append(csv_file['M11'][i])
                        Wavelength_M12[j+1].append(csv_file['M12'][i])
                        Wavelength_M13[j+1].append(csv_file['M13'][i])
                        Wavelength_M20[j+1].append(csv_file['M20'][i])
                        Wavelength_M21[j+1].append(csv_file['M21'][i])
                        Wavelength_M22[j+1].append(csv_file['M22'][i])
                        Wavelength_M23[j+1].append(csv_file['M23'][i])
                        Wavelength_M30[j+1].append(csv_file['M30'][i])
                        Wavelength_M31[j+1].append(csv_file['M31'][i])
                        Wavelength_M32[j+1].append(csv_file['M32'][i])
                        Wavelength_M33[j+1].append(csv_file['M33'][i])

                        if str(reply5) == 'Yes':

                            M = []
                            M.append(csv_file['M00'][i])
                            M.append(csv_file['M01'][i])
                            M.append(csv_file['M02'][i])
                            M.append(csv_file['M03'][i])
                            M.append(csv_file['M10'][i])
                            M.append(csv_file['M11'][i])
                            M.append(csv_file['M12'][i])
                            M.append(csv_file['M13'][i])
                            M.append(csv_file['M20'][i])
                            M.append(csv_file['M21'][i])
                            M.append(csv_file['M22'][i])
                            M.append(csv_file['M23'][i])
                            M.append(csv_file['M30'][i])
                            M.append(csv_file['M31'][i])
                            M.append(csv_file['M32'][i])
                            M.append(csv_file['M33'][i])

                            matrix = np.array(M).reshape(4,4)

                            LM = -1*logm(matrix)

                            B = []
                            B.append(csv_base['M00'][i])    # base = baseline
                            B.append(csv_base['M01'][i])
                            B.append(csv_base['M02'][i])
                            B.append(csv_base['M03'][i])
                            B.append(csv_base['M10'][i])
                            B.append(csv_base['M11'][i])
                            B.append(csv_base['M12'][i])
                            B.append(csv_base['M13'][i])
                            B.append(csv_base['M20'][i])
                            B.append(csv_base['M21'][i])
                            B.append(csv_base['M22'][i])
                            B.append(csv_base['M23'][i])
                            B.append(csv_base['M30'][i])
                            B.append(csv_base['M31'][i])
                            B.append(csv_base['M32'][i])
                            B.append(csv_base['M33'][i])

                            matrix_base = np.array(B).reshape(4,4)

                            LM_base = -1*logm(matrix_base)

                            Wavelength_mCD[j+1].append(((LM[0, 3] + LM[3, 0])/-2) - ((LM_base[0, 3] + LM_base[3, 0])/-2)) 
                            Wavelength_mCB[j+1].append(((LM[1, 2] - LM[2, 1])/2) - ((LM_base[1, 2] - LM_base[2, 1])/2))
                            Wavelength_mLD[j+1].append(((LM[0, 1] + LM[1, 0])/-2) - ((LM_base[0, 1] + LM_base[1, 0])/-2))
                            Wavelength_mLDp[j+1].append(((LM[0, 2] + LM[2, 0])/-2) - ((LM_base[0, 2] + LM_base[2, 0])/-2))
                            Wavelength_mLB[j+1].append(((LM[2, 3] - LM[3, 2])/2) - ((LM_base[2, 3] - LM_base[3, 2])/2))
                            Wavelength_mLBp[j+1].append(((LM[1, 3] - LM[3, 1])/2) - ((LM_base[1, 3] - LM_base[3, 1])/2))
                            Wavelength_mg_factor[j+1].append(((((LM[0, 3] + LM[3, 0])/-2) - ((LM_base[0, 3] + LM_base[3, 0])/-2))/((LM[0, 0] + LM[1, 1] + LM[2, 2] + LM[3, 3])/4) - (LM_base[0, 0] + LM_base[1, 1] + LM_base[2, 2] + LM_base[3, 3])/4))

                            r00 = math.sqrt((matrix[0, 0] + matrix[0, 1] + matrix[1, 0] + matrix[1, 1])/2)
                            r01 = math.sqrt((matrix[0, 0] - matrix[0, 1] + matrix[1, 0] - matrix[1, 1])/2)
                            r10 = math.sqrt((matrix[0, 0] + matrix[0, 1] - matrix[1, 0] - matrix[1, 1])/2)
                            r11 = math.sqrt((matrix[0, 0] - matrix[0, 1] - matrix[1, 0] + matrix[1, 1])/2)

                            e01 = ((matrix[0, 2] + matrix[1, 2]) - (matrix[0, 3] + matrix[1, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 0])**2 - (matrix[0, 1] + matrix[1, 1])**2)
                            e10 = ((matrix[2, 0] + matrix[2, 1]) + (matrix[3, 0] + matrix[3, 1])*1j) / math.sqrt((matrix[0, 0] + matrix[0, 1])**2 - (matrix[1, 0] + matrix[1, 1])**2)
                            e11 = ((matrix[2, 2] + matrix[3, 3]) + (matrix[3, 2] - matrix[2, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 1])**2 - (matrix[1, 0] + matrix[0, 1])**2)

                            K = ((r00*r11*e11 - r01*r10*e10*e01)**-0.5)
                            Tk = 2*cmath.acos((K*(r00+r11*e11))/2)
                            O = (Tk*K)/(2*cmath.sin(Tk/2))

                            LBLD = O * (r00 - r11*e11)*1j
                            LBpLDp = O * (r01*e01 + r10*e10)*1j
                            CBCD = O * (r01*e01 - r10*e10)

                            r00_base = math.sqrt((matrix_base[0, 0] + matrix_base[0, 1] + matrix_base[1, 0] + matrix_base[1, 1])/2)
                            r01_base = math.sqrt((matrix_base[0, 0] - matrix_base[0, 1] + matrix_base[1, 0] - matrix_base[1, 1])/2)
                            r10_base = math.sqrt((matrix_base[0, 0] + matrix_base[0, 1] - matrix_base[1, 0] - matrix_base[1, 1])/2)
                            r11_base = math.sqrt((matrix_base[0, 0] - matrix_base[0, 1] - matrix_base[1, 0] + matrix_base[1, 1])/2)

                            e01_base = ((matrix_base[0, 2] + matrix_base[1, 2]) - (matrix_base[0, 3] + matrix_base[1, 3])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[1, 0])**2 - (matrix_base[0, 1] + matrix_base[1, 1])**2)
                            e10_base = ((matrix_base[2, 0] + matrix_base[2, 1]) + (matrix_base[3, 0] + matrix_base[3, 1])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[0, 1])**2 - (matrix_base[1, 0] + matrix_base[1, 1])**2)
                            e11_base = ((matrix_base[2, 2] + matrix_base[3, 3]) + (matrix_base[3, 2] - matrix_base[2, 3])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[1, 1])**2 - (matrix_base[1, 0] + matrix_base[0, 1])**2)

                            K_base = ((r00_base*r11_base*e11_base - r01_base*r10_base*e10_base*e01_base)**-0.5)
                            Tk_base = 2*cmath.acos((K_base*(r00_base+r11_base*e11_base))/2)
                            O_base = (Tk_base*K_base)/(2*cmath.sin(Tk_base/2))

                            LBLD_base = O_base * (r00_base - r11_base*e11_base)*1j
                            LBpLDp_base = O_base * (r01_base*e01_base + r10_base*e10_base)*1j
                            CBCD_base = O_base * (r01_base*e01_base - r10_base*e10_base)

                            Wavelength_aLB[j+1].append(LBLD.real - LBLD_base.real)
                            Wavelength_aLD[j+1].append(-1*LBLD.imag - -1*LBLD_base.imag)

                            Wavelength_aLBp[j+1].append(LBpLDp.real - LBpLDp_base.real)
                            Wavelength_aLDp[j+1].append(-1*LBpLDp.imag - -1*LBpLDp_base.imag)

                            Wavelength_aCB[j+1].append(CBCD.real - CBCD_base.real)
                            Wavelength_aCD[j+1].append(-1*CBCD.imag - -1*CBCD_base.imag)

                            Wavelength_ag_factor[j+1].append((-1*CBCD.imag - -1*CBCD_base.imag)/(math.log10(1/(csv_file['M00'][i]/csv_base['M00'][i]))))


                            Wavelength_CD_new[j+1].append(32980*0.94*0.993557*((csv_file['M30'][i]+csv_file['M03'][i])/(2*csv_file['M00'][i])-(csv_base['M30'][i]+csv_base['M03'][i])/(2*csv_base['M00'][i])))
                            Wavelength_LD_new[j+1].append((-1.070135)*((csv_file['M10'][i]+csv_file['M01'][i])/(2*csv_file['M00'][i])-(csv_base['M10'][i]+csv_base['M01'][i])/(2*csv_base['M00'][i])))
                            Wavelength_LDp_new[j+1].append((-1.063424)*((csv_file['M20'][i]+csv_file['M02'][i])/(2*csv_file['M00'][i])-(csv_base['M20'][i]+csv_base['M02'][i])/(2*csv_base['M00'][i])))
                            Wavelength_CB_new[j+1].append(0.285787*1000*math.degrees(2*(np.arcsin((csv_file['M12'][i]-csv_file['M21'][i])/(2*csv_file['M00'][i])-np.arcsin((csv_base['M12'][i]-csv_base['M21'][i])/(2*csv_base['M00'][i]))))))
                            Wavelength_LB_new[j+1].append((-0.0193343)*math.degrees((np.arcsin((csv_file['M23'][i]-csv_file['M32'][i])/(2*csv_file['M00'][i])-np.arcsin((csv_base['M23'][i]-csv_base['M32'][i])/(2*csv_base['M00'][i]))))))
                            Wavelength_LBp_new[j+1].append((-0.2056925)*math.degrees((np.arcsin((csv_file['M31'][i]-csv_file['M13'][i])/(2*csv_file['M00'][i])-np.arcsin((csv_base['M31'][i]-csv_base['M13'][i])/(2*csv_base['M00'][i]))))))
                            Wavelength_g_factor_new[j+1].append((((0.94*0.993557*((csv_file['M30'][i]+csv_file['M03'][i])/(2*csv_file['M00'][i])-(csv_base['M30'][i]+csv_base['M03'][i])/(2*csv_base['M00'][i]))))/(math.log10(1/(csv_file['M00'][i]/csv_base['M00'][i])))))
                            Wavelength_Abs[j+1].append(math.log10(1/(csv_file['M00'][i]/csv_base['M00'][i])))

                        else:

                            M = []
                            M.append(csv_file['M00'][i])
                            M.append(csv_file['M01'][i])
                            M.append(csv_file['M02'][i])
                            M.append(csv_file['M03'][i])
                            M.append(csv_file['M10'][i])
                            M.append(csv_file['M11'][i])
                            M.append(csv_file['M12'][i])
                            M.append(csv_file['M13'][i])
                            M.append(csv_file['M20'][i])
                            M.append(csv_file['M21'][i])
                            M.append(csv_file['M22'][i])
                            M.append(csv_file['M23'][i])
                            M.append(csv_file['M30'][i])
                            M.append(csv_file['M31'][i])
                            M.append(csv_file['M32'][i])
                            M.append(csv_file['M33'][i])

                            matrix = np.array(M).reshape(4,4)

                            LM = -1*logm(matrix)

                            Wavelength_mCD[j+1].append((LM[0, 3] + LM[3, 0])/-2)
                            Wavelength_mCB[j+1].append((LM[1, 2] - LM[2, 1])/2)
                            Wavelength_mLD[j+1].append((LM[0, 1] + LM[1, 0])/-2)
                            Wavelength_mLDp[j+1].append((LM[0, 2] + LM[2, 0])/-2)
                            Wavelength_mLB[j+1].append((LM[2, 3] - LM[3, 2])/2)
                            Wavelength_mLBp[j+1].append((LM[1, 3] - LM[3, 1])/2)
                            Wavelength_mg_factor[j+1].append((((LM[0, 3] + LM[3, 0])/-2)/((LM[0, 0] + LM[1, 1] + LM[2, 2] + LM[3, 3])/4)))

                            r00 = math.sqrt((matrix[0, 0] + matrix[0, 1] + matrix[1, 0] + matrix[1, 1])/2)
                            r01 = math.sqrt((matrix[0, 0] - matrix[0, 1] + matrix[1, 0] - matrix[1, 1])/2)
                            r10 = math.sqrt((matrix[0, 0] + matrix[0, 1] - matrix[1, 0] - matrix[1, 1])/2)
                            r11 = math.sqrt((matrix[0, 0] - matrix[0, 1] - matrix[1, 0] + matrix[1, 1])/2)

                            e01 = ((matrix[0, 2] + matrix[1, 2]) - (matrix[0, 3] + matrix[1, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 0])**2 - (matrix[0, 1] + matrix[1, 1])**2)
                            e10 = ((matrix[2, 0] + matrix[2, 1]) + (matrix[3, 0] + matrix[3, 1])*1j) / math.sqrt((matrix[0, 0] + matrix[0, 1])**2 - (matrix[1, 0] + matrix[1, 1])**2)
                            e11 = ((matrix[2, 2] + matrix[3, 3]) + (matrix[3, 2] - matrix[2, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 1])**2 - (matrix[1, 0] + matrix[0, 1])**2)

                            K = ((r00*r11*e11 - r01*r10*e10*e01)**-0.5)
                            Tk = 2*cmath.acos((K*(r00+r11*e11))/2)
                            O = (Tk*K)/(2*cmath.sin(Tk/2))

                            LBLD = O * (r00 - r11*e11)*1j
                            LBpLDp = O * (r01*e01 + r10*e10)*1j
                            CBCD = O * (r01*e01 - r10*e10)

                            Wavelength_aLB[j+1].append(LBLD.real)
                            Wavelength_aLD[j+1].append(-1*LBLD.imag)

                            Wavelength_aLBp[j+1].append(LBpLDp.real)
                            Wavelength_aLDp[j+1].append(-1*LBpLDp.imag)

                            Wavelength_aCB[j+1].append(CBCD.real)
                            Wavelength_aCD[j+1].append(-1*CBCD.imag)

                            Wavelength_ag_factor[j+1].append((-1*CBCD.imag)/(math.log10(1/csv_file['M00'][i])))


                            Wavelength_Abs[j+1].append(math.log10(1/csv_file['M00'][i]))
                            Wavelength_CD_new[j+1].append(32980*0.94*0.993557*((csv_file['M30'][i]+csv_file['M03'][i])/(2*csv_file['M00'][i]))) 
                            Wavelength_LD_new[j+1].append((-1.070135)*((csv_file['M10'][i]+csv_file['M01'][i])/(2*csv_file['M00'][i])))  
                            Wavelength_LDp_new[j+1].append((-1.063424)*((csv_file['M20'][i]+csv_file['M02'][i])/(2*csv_file['M00'][i]))) 
                            Wavelength_CB_new[j+1].append(0.285787*1000*math.degrees(2*np.arcsin((csv_file['M12'][i]-csv_file['M21'][i])/(2*csv_file['M00'][i]))))
                            Wavelength_LB_new[j+1].append((-0.0193343)*math.degrees(np.arcsin((csv_file['M23'][i]-csv_file['M32'][i])/(2*csv_file['M00'][i]))))
                            Wavelength_LBp_new[j+1].append((-0.2056925)*math.degrees(np.arcsin((csv_file['M31'][i]-csv_file['M13'][i])/(2*csv_file['M00'][i]))))
                            Wavelength_g_factor_new[j+1].append((((csv_file['M30'][i]+csv_file['M03'][i])/(2*csv_file['M00'][i]))/(math.log10(1/csv_file['M00'][i]))))
                    
                    else:
                        j += 1
                        Wavelength_CD[j+1].append(csv_file['CD'][i])
                        Wavelength_CR[j+1].append((csv_file['CR'][i]))
                        Wavelength_LR[j+1].append((csv_file['LR'][i]))
                        Wavelength_LD[j+1].append(csv_file['LD'][i])
                        Wavelength_LRp[j+1].append((csv_file['LRp'][i]))
                        Wavelength_LDp[j+1].append(csv_file['LDp'][i])
                        Wavelength_g_factor[j+1].append(csv_file['CD'][i]/32980/(math.log10(1/csv_file['M00'][i])))
                        Wavelength_M00[j+1].append(csv_file['M00'][i])
                        Wavelength_M01[j+1].append(csv_file['M01'][i])
                        Wavelength_M02[j+1].append(csv_file['M02'][i])
                        Wavelength_M03[j+1].append(csv_file['M03'][i])
                        Wavelength_M10[j+1].append(csv_file['M10'][i])
                        Wavelength_M11[j+1].append(csv_file['M11'][i])
                        Wavelength_M12[j+1].append(csv_file['M12'][i])
                        Wavelength_M13[j+1].append(csv_file['M13'][i])
                        Wavelength_M20[j+1].append(csv_file['M20'][i])
                        Wavelength_M21[j+1].append(csv_file['M21'][i])
                        Wavelength_M22[j+1].append(csv_file['M22'][i])
                        Wavelength_M23[j+1].append(csv_file['M23'][i])
                        Wavelength_M30[j+1].append(csv_file['M30'][i])
                        Wavelength_M31[j+1].append(csv_file['M31'][i])
                        Wavelength_M32[j+1].append(csv_file['M32'][i])
                        Wavelength_M33[j+1].append(csv_file['M33'][i])
                        if str(reply5) == 'Yes':

                            M = []
                            M.append(csv_file['M00'][i])
                            M.append(csv_file['M01'][i])
                            M.append(csv_file['M02'][i])
                            M.append(csv_file['M03'][i])
                            M.append(csv_file['M10'][i])
                            M.append(csv_file['M11'][i])
                            M.append(csv_file['M12'][i])
                            M.append(csv_file['M13'][i])
                            M.append(csv_file['M20'][i])
                            M.append(csv_file['M21'][i])
                            M.append(csv_file['M22'][i])
                            M.append(csv_file['M23'][i])
                            M.append(csv_file['M30'][i])
                            M.append(csv_file['M31'][i])
                            M.append(csv_file['M32'][i])
                            M.append(csv_file['M33'][i])

                            matrix = np.array(M).reshape(4,4)

                            LM = -1*logm(matrix)

                            B = []
                            B.append(csv_base['M00'][i])    # base = baseline
                            B.append(csv_base['M01'][i])
                            B.append(csv_base['M02'][i])
                            B.append(csv_base['M03'][i])
                            B.append(csv_base['M10'][i])
                            B.append(csv_base['M11'][i])
                            B.append(csv_base['M12'][i])
                            B.append(csv_base['M13'][i])
                            B.append(csv_base['M20'][i])
                            B.append(csv_base['M21'][i])
                            B.append(csv_base['M22'][i])
                            B.append(csv_base['M23'][i])
                            B.append(csv_base['M30'][i])
                            B.append(csv_base['M31'][i])
                            B.append(csv_base['M32'][i])
                            B.append(csv_base['M33'][i])

                            matrix_base = np.array(B).reshape(4,4)

                            LM_base = -1*logm(matrix_base)

                            Wavelength_mCD[j+1].append(((LM[0, 3] + LM[3, 0])/-2) - ((LM_base[0, 3] + LM_base[3, 0])/-2)) 
                            Wavelength_mCB[j+1].append(((LM[1, 2] - LM[2, 1])/2) - ((LM_base[1, 2] - LM_base[2, 1])/2))
                            Wavelength_mLD[j+1].append(((LM[0, 1] + LM[1, 0])/-2) - ((LM_base[0, 1] + LM_base[1, 0])/-2))
                            Wavelength_mLDp[j+1].append(((LM[0, 2] + LM[2, 0])/-2) - ((LM_base[0, 2] + LM_base[2, 0])/-2))
                            Wavelength_mLB[j+1].append(((LM[2, 3] - LM[3, 2])/2) - ((LM_base[2, 3] - LM_base[3, 2])/2))
                            Wavelength_mLBp[j+1].append(((LM[1, 3] - LM[3, 1])/2) - ((LM_base[1, 3] - LM_base[3, 1])/2))
                            Wavelength_mg_factor[j+1].append(((((LM[0, 3] + LM[3, 0])/-2) - ((LM_base[0, 3] + LM_base[3, 0])/-2))/((LM[0, 0] + LM[1, 1] + LM[2, 2] + LM[3, 3])/4) - (LM_base[0, 0] + LM_base[1, 1] + LM_base[2, 2] + LM_base[3, 3])/4))

                            r00 = math.sqrt((matrix[0, 0] + matrix[0, 1] + matrix[1, 0] + matrix[1, 1])/2)
                            r01 = math.sqrt((matrix[0, 0] - matrix[0, 1] + matrix[1, 0] - matrix[1, 1])/2)
                            r10 = math.sqrt((matrix[0, 0] + matrix[0, 1] - matrix[1, 0] - matrix[1, 1])/2)
                            r11 = math.sqrt((matrix[0, 0] - matrix[0, 1] - matrix[1, 0] + matrix[1, 1])/2)

                            e01 = ((matrix[0, 2] + matrix[1, 2]) - (matrix[0, 3] + matrix[1, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 0])**2 - (matrix[0, 1] + matrix[1, 1])**2)
                            e10 = ((matrix[2, 0] + matrix[2, 1]) + (matrix[3, 0] + matrix[3, 1])*1j) / math.sqrt((matrix[0, 0] + matrix[0, 1])**2 - (matrix[1, 0] + matrix[1, 1])**2)
                            e11 = ((matrix[2, 2] + matrix[3, 3]) + (matrix[3, 2] - matrix[2, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 1])**2 - (matrix[1, 0] + matrix[0, 1])**2)

                            K = ((r00*r11*e11 - r01*r10*e10*e01)**-0.5)
                            Tk = 2*cmath.acos((K*(r00+r11*e11))/2)
                            O = (Tk*K)/(2*cmath.sin(Tk/2))

                            LBLD = O * (r00 - r11*e11)*1j
                            LBpLDp = O * (r01*e01 + r10*e10)*1j
                            CBCD = O * (r01*e01 - r10*e10)

                            r00_base = math.sqrt((matrix_base[0, 0] + matrix_base[0, 1] + matrix_base[1, 0] + matrix_base[1, 1])/2)
                            r01_base = math.sqrt((matrix_base[0, 0] - matrix_base[0, 1] + matrix_base[1, 0] - matrix_base[1, 1])/2)
                            r10_base = math.sqrt((matrix_base[0, 0] + matrix_base[0, 1] - matrix_base[1, 0] - matrix_base[1, 1])/2)
                            r11_base = math.sqrt((matrix_base[0, 0] - matrix_base[0, 1] - matrix_base[1, 0] + matrix_base[1, 1])/2)

                            e01_base = ((matrix_base[0, 2] + matrix_base[1, 2]) - (matrix_base[0, 3] + matrix_base[1, 3])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[1, 0])**2 - (matrix_base[0, 1] + matrix_base[1, 1])**2)
                            e10_base = ((matrix_base[2, 0] + matrix_base[2, 1]) + (matrix_base[3, 0] + matrix_base[3, 1])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[0, 1])**2 - (matrix_base[1, 0] + matrix_base[1, 1])**2)
                            e11_base = ((matrix_base[2, 2] + matrix_base[3, 3]) + (matrix_base[3, 2] - matrix_base[2, 3])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[1, 1])**2 - (matrix_base[1, 0] + matrix_base[0, 1])**2)

                            K_base = ((r00_base*r11_base*e11_base - r01_base*r10_base*e10_base*e01_base)**-0.5)
                            Tk_base = 2*cmath.acos((K_base*(r00_base+r11_base*e11_base))/2)
                            O_base = (Tk_base*K_base)/(2*cmath.sin(Tk_base/2))

                            LBLD_base = O_base * (r00_base - r11_base*e11_base)*1j
                            LBpLDp_base = O_base * (r01_base*e01_base + r10_base*e10_base)*1j
                            CBCD_base = O_base * (r01_base*e01_base - r10_base*e10_base)

                            Wavelength_aLB[j+1].append(LBLD.real - LBLD_base.real)
                            Wavelength_aLD[j+1].append(-1*LBLD.imag - -1*LBLD_base.imag)

                            Wavelength_aLBp[j+1].append(LBpLDp.real - LBpLDp_base.real)
                            Wavelength_aLDp[j+1].append(-1*LBpLDp.imag - -1*LBpLDp_base.imag)

                            Wavelength_aCB[j+1].append(CBCD.real - CBCD_base.real)
                            Wavelength_aCD[j+1].append(-1*CBCD.imag - -1*CBCD_base.imag)

                            Wavelength_ag_factor[j+1].append((-1*CBCD.imag - -1*CBCD_base.imag)/(math.log10(1/(csv_file['M00'][i]/csv_base['M00'][i]))))

                            Wavelength_CD_new[j+1].append(32980*0.94*0.993557*((csv_file['M30'][i]+csv_file['M03'][i])/(2*csv_file['M00'][i])-(csv_base['M30'][i]+csv_base['M03'][i])/(2*csv_base['M00'][i])))
                            Wavelength_LD_new[j+1].append((-1.070135)*((csv_file['M10'][i]+csv_file['M01'][i])/(2*csv_file['M00'][i])-(csv_base['M10'][i]+csv_base['M01'][i])/(2*csv_base['M00'][i])))
                            Wavelength_LDp_new[j+1].append((-1.063424)*((csv_file['M20'][i]+csv_file['M02'][i])/(2*csv_file['M00'][i])-(csv_base['M20'][i]+csv_base['M02'][i])/(2*csv_base['M00'][i])))
                            Wavelength_CB_new[j+1].append(0.285787*1000*math.degrees(2*(np.arcsin((csv_file['M12'][i]-csv_file['M21'][i])/(2*csv_file['M00'][i])-np.arcsin((csv_base['M12'][i]-csv_base['M21'][i])/(2*csv_base['M00'][i]))))))
                            Wavelength_LB_new[j+1].append((-0.0193343)*math.degrees((np.arcsin((csv_file['M23'][i]-csv_file['M32'][i])/(2*csv_file['M00'][i])-np.arcsin((csv_base['M23'][i]-csv_base['M32'][i])/(2*csv_base['M00'][i]))))))
                            Wavelength_LBp_new[j+1].append((-0.2056925)*math.degrees((np.arcsin((csv_file['M31'][i]-csv_file['M13'][i])/(2*csv_file['M00'][i])-np.arcsin((csv_base['M31'][i]-csv_base['M13'][i])/(2*csv_base['M00'][i]))))))
                            Wavelength_g_factor_new[j+1].append((((0.94*0.993557*((csv_file['M30'][i]+csv_file['M03'][i])/(2*csv_file['M00'][i])-(csv_base['M30'][i]+csv_base['M03'][i])/(2*csv_base['M00'][i]))))/(math.log10(1/(csv_file['M00'][i]/csv_base['M00'][i])))))
                            Wavelength_Abs[j+1].append(math.log10(1/(csv_file['M00'][i]/csv_base['M00'][i])))
                        else:

                            M = []
                            M.append(csv_file['M00'][i])
                            M.append(csv_file['M01'][i])
                            M.append(csv_file['M02'][i])
                            M.append(csv_file['M03'][i])
                            M.append(csv_file['M10'][i])
                            M.append(csv_file['M11'][i])
                            M.append(csv_file['M12'][i])
                            M.append(csv_file['M13'][i])
                            M.append(csv_file['M20'][i])
                            M.append(csv_file['M21'][i])
                            M.append(csv_file['M22'][i])
                            M.append(csv_file['M23'][i])
                            M.append(csv_file['M30'][i])
                            M.append(csv_file['M31'][i])
                            M.append(csv_file['M32'][i])
                            M.append(csv_file['M33'][i])

                            matrix = np.array(M).reshape(4,4)

                            LM = -1*logm(matrix)

                            Wavelength_mCD[j+1].append((LM[0, 3] + LM[3, 0])/-2)
                            Wavelength_mCB[j+1].append((LM[1, 2] - LM[2, 1])/2)
                            Wavelength_mLD[j+1].append((LM[0, 1] + LM[1, 0])/-2)
                            Wavelength_mLDp[j+1].append((LM[0, 2] + LM[2, 0])/-2)
                            Wavelength_mLB[j+1].append((LM[2, 3] - LM[3, 2])/2)
                            Wavelength_mLBp[j+1].append((LM[1, 3] - LM[3, 1])/2)
                            Wavelength_mg_factor[j+1].append((((LM[0, 3] + LM[3, 0])/-2)/((LM[0, 0] + LM[1, 1] + LM[2, 2] + LM[3, 3])/4)))

                            r00 = math.sqrt((matrix[0, 0] + matrix[0, 1] + matrix[1, 0] + matrix[1, 1])/2)
                            r01 = math.sqrt((matrix[0, 0] - matrix[0, 1] + matrix[1, 0] - matrix[1, 1])/2)
                            r10 = math.sqrt((matrix[0, 0] + matrix[0, 1] - matrix[1, 0] - matrix[1, 1])/2)
                            r11 = math.sqrt((matrix[0, 0] - matrix[0, 1] - matrix[1, 0] + matrix[1, 1])/2)

                            e01 = ((matrix[0, 2] + matrix[1, 2]) - (matrix[0, 3] + matrix[1, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 0])**2 - (matrix[0, 1] + matrix[1, 1])**2)
                            e10 = ((matrix[2, 0] + matrix[2, 1]) + (matrix[3, 0] + matrix[3, 1])*1j) / math.sqrt((matrix[0, 0] + matrix[0, 1])**2 - (matrix[1, 0] + matrix[1, 1])**2)
                            e11 = ((matrix[2, 2] + matrix[3, 3]) + (matrix[3, 2] - matrix[2, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 1])**2 - (matrix[1, 0] + matrix[0, 1])**2)

                            K = ((r00*r11*e11 - r01*r10*e10*e01)**-0.5)
                            Tk = 2*cmath.acos((K*(r00+r11*e11))/2)
                            O = (Tk*K)/(2*cmath.sin(Tk/2))

                            LBLD = O * (r00 - r11*e11)*1j
                            LBpLDp = O * (r01*e01 + r10*e10)*1j
                            CBCD = O * (r01*e01 - r10*e10)

                            Wavelength_aLB[j+1].append(LBLD.real)
                            Wavelength_aLD[j+1].append(-1*LBLD.imag)

                            Wavelength_aLBp[j+1].append(LBpLDp.real)
                            Wavelength_aLDp[j+1].append(-1*LBpLDp.imag)

                            Wavelength_aCB[j+1].append(CBCD.real)
                            Wavelength_aCD[j+1].append(-1*CBCD.imag)

                            Wavelength_ag_factor[j+1].append((-1*CBCD.imag)/(math.log10(1/csv_file['M00'][i])))

                            Wavelength_Abs[j+1].append(math.log10(1/csv_file['M00'][i]))
                            Wavelength_CD_new[j+1].append(32980*0.94*0.993557*((csv_file['M30'][i]+csv_file['M03'][i])/(2*csv_file['M00'][i]))) 
                            Wavelength_LD_new[j+1].append((-1.070135)*((csv_file['M10'][i]+csv_file['M01'][i])/(2*csv_file['M00'][i])))  
                            Wavelength_LDp_new[j+1].append((-1.063424)*((csv_file['M20'][i]+csv_file['M02'][i])/(2*csv_file['M00'][i]))) 
                            Wavelength_CB_new[j+1].append(0.285787*1000*math.degrees(2*np.arcsin((csv_file['M12'][i]-csv_file['M21'][i])/(2*csv_file['M00'][i])))) 
                            Wavelength_LB_new[j+1].append((-0.0193343)*math.degrees(np.arcsin((csv_file['M23'][i]-csv_file['M32'][i])/(2*csv_file['M00'][i]))))
                            Wavelength_LBp_new[j+1].append((-0.2056925)*math.degrees(np.arcsin((csv_file['M31'][i]-csv_file['M13'][i])/(2*csv_file['M00'][i]))))
                            Wavelength_g_factor_new[j+1].append((((csv_file['M30'][i]+csv_file['M03'][i])/(2*csv_file['M00'][i]))/(math.log10(1/csv_file['M00'][i]))))
                            Wavelength_Abs[j+1].append(math.log10(1/csv_file['M00'][i]))
                    
                for i in range(1, len(csv_file)):
                    if csv_file['Wavelength'][i] != t:
                        Wavelength_new.append(csv_file['Wavelength'][i])
                    else:
                        break

                M00_list = [[] for i in range(k)] 
                M01_list = [[] for i in range(k)] 
                M02_list = [[] for i in range(k)] 
                M03_list = [[] for i in range(k)] 
                M10_list = [[] for i in range(k)] 
                M11_list = [[] for i in range(k)] 
                M12_list = [[] for i in range(k)] 
                M13_list = [[] for i in range(k)] 
                M20_list = [[] for i in range(k)] 
                M21_list = [[] for i in range(k)] 
                M22_list = [[] for i in range(k)] 
                M23_list = [[] for i in range(k)] 
                M30_list = [[] for i in range(k)] 
                M31_list = [[] for i in range(k)] 
                M32_list = [[] for i in range(k)] 
                M33_list = [[] for i in range(k)]
                Abs_list = [[] for i in range(k)] 

                CD_list = [[] for i in range(k)] 
                CB_list = [[] for i in range(k)] 
                LD_list = [[] for i in range(k)] 
                LB_list = [[] for i in range(k)] 
                LDp_list = [[] for i in range(k)] 
                LBp_list = [[] for i in range(k)] 
                g_factor_list = [[] for i in range(k)]

                CD_list_new = [[] for i in range(k)] 
                CB_list_new = [[] for i in range(k)] 
                LD_list_new = [[] for i in range(k)] 
                LB_list_new = [[] for i in range(k)] 
                LDp_list_new = [[] for i in range(k)] 
                LBp_list_new = [[] for i in range(k)]
                g_factor_list_new = [[] for i in range(k)]

                mCD_list = [[] for i in range(k)] 
                mCB_list = [[] for i in range(k)] 
                mLD_list = [[] for i in range(k)] 
                mLB_list = [[] for i in range(k)] 
                mLDp_list = [[] for i in range(k)] 
                mLBp_list = [[] for i in range(k)]
                mg_factor_list = [[] for i in range(k)]

                aCD_list = [[] for i in range(k)] 
                aCB_list = [[] for i in range(k)] 
                aLD_list = [[] for i in range(k)] 
                aLB_list = [[] for i in range(k)] 
                aLDp_list = [[] for i in range(k)] 
                aLBp_list = [[] for i in range(k)] 
                ag_factor_list = [[] for i in range(k)]

                M00_list[0].append(csv_file['M00'][0])
                M01_list[0].append(csv_file['M01'][0])
                M02_list[0].append(csv_file['M02'][0])
                M03_list[0].append(csv_file['M03'][0])
                M10_list[0].append(csv_file['M10'][0])
                M11_list[0].append(csv_file['M11'][0])
                M12_list[0].append(csv_file['M12'][0])
                M13_list[0].append(csv_file['M13'][0])
                M20_list[0].append(csv_file['M20'][0])
                M21_list[0].append(csv_file['M21'][0])
                M22_list[0].append(csv_file['M22'][0])
                M23_list[0].append(csv_file['M23'][0])
                M30_list[0].append(csv_file['M30'][0])
                M31_list[0].append(csv_file['M31'][0])
                M32_list[0].append(csv_file['M32'][0])
                M33_list[0].append(csv_file['M33'][0])

                CD_list[0].append(csv_file['CD'][0])
                CB_list[0].append((csv_file['CR'][0]))
                LD_list[0].append(csv_file['LD'][0])
                LB_list[0].append((csv_file['LR'][0]))
                LDp_list[0].append(csv_file['LDp'][0])
                LBp_list[0].append((csv_file['LRp'][0]))
                g_factor_list[0].append(csv_file['CD'][0]/32980/(math.log10(1/csv_file['M00'][0])))

                if str(reply5) == 'Yes':

                    M = []
                    M.append(csv_file['M00'][0])
                    M.append(csv_file['M01'][0])
                    M.append(csv_file['M02'][0])
                    M.append(csv_file['M03'][0])
                    M.append(csv_file['M10'][0])
                    M.append(csv_file['M11'][0])
                    M.append(csv_file['M12'][0])
                    M.append(csv_file['M13'][0])
                    M.append(csv_file['M20'][0])
                    M.append(csv_file['M21'][0])
                    M.append(csv_file['M22'][0])
                    M.append(csv_file['M23'][0])
                    M.append(csv_file['M30'][0])
                    M.append(csv_file['M31'][0])
                    M.append(csv_file['M32'][0])
                    M.append(csv_file['M33'][0])

                    matrix = np.array(M).reshape(4,4)

                    LM = -1*logm(matrix)

                    B = []
                    B.append(csv_base['M00'][0])    # base = baseline
                    B.append(csv_base['M01'][0])
                    B.append(csv_base['M02'][0])
                    B.append(csv_base['M03'][0])
                    B.append(csv_base['M10'][0])
                    B.append(csv_base['M11'][0])
                    B.append(csv_base['M12'][0])
                    B.append(csv_base['M13'][0])
                    B.append(csv_base['M20'][0])
                    B.append(csv_base['M21'][0])
                    B.append(csv_base['M22'][0])
                    B.append(csv_base['M23'][0])
                    B.append(csv_base['M30'][0])
                    B.append(csv_base['M31'][0])
                    B.append(csv_base['M32'][0])
                    B.append(csv_base['M33'][0])

                    matrix_base = np.array(B).reshape(4,4)

                    LM_base = -1*logm(matrix_base)

                    mCD_list[0].append(((LM[0, 3] + LM[3, 0])/-2) - ((LM_base[0, 3] + LM_base[3, 0])/-2)) 
                    mCB_list[0].append(((LM[1, 2] - LM[2, 1])/2) - ((LM_base[1, 2] - LM_base[2, 1])/2))
                    mLD_list[0].append(((LM[0, 1] + LM[1, 0])/-2) - ((LM_base[0, 1] + LM_base[1, 0])/-2))
                    mLDp_list[0].append(((LM[0, 2] + LM[2, 0])/-2) - ((LM_base[0, 2] + LM_base[2, 0])/-2))
                    mLB_list[0].append(((LM[2, 3] - LM[3, 2])/2) - ((LM_base[2, 3] - LM_base[3, 2])/2))
                    mLBp_list[0].append(((LM[1, 3] - LM[3, 1])/2) - ((LM_base[1, 3] - LM_base[3, 1])/2))
                    mg_factor_list[0].append(((((LM[0, 3] + LM[3, 0])/-2) - ((LM_base[0, 3] + LM_base[3, 0])/-2))/((LM[0, 0] + LM[1, 1] + LM[2, 2] + LM[3, 3])/4) - (LM_base[0, 0] + LM_base[1, 1] + LM_base[2, 2] + LM_base[3, 3])/4))

                    r00 = math.sqrt((matrix[0, 0] + matrix[0, 1] + matrix[1, 0] + matrix[1, 1])/2)
                    r01 = math.sqrt((matrix[0, 0] - matrix[0, 1] + matrix[1, 0] - matrix[1, 1])/2)
                    r10 = math.sqrt((matrix[0, 0] + matrix[0, 1] - matrix[1, 0] - matrix[1, 1])/2)
                    r11 = math.sqrt((matrix[0, 0] - matrix[0, 1] - matrix[1, 0] + matrix[1, 1])/2)

                    e01 = ((matrix[0, 2] + matrix[1, 2]) - (matrix[0, 3] + matrix[1, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 0])**2 - (matrix[0, 1] + matrix[1, 1])**2)
                    e10 = ((matrix[2, 0] + matrix[2, 1]) + (matrix[3, 0] + matrix[3, 1])*1j) / math.sqrt((matrix[0, 0] + matrix[0, 1])**2 - (matrix[1, 0] + matrix[1, 1])**2)
                    e11 = ((matrix[2, 2] + matrix[3, 3]) + (matrix[3, 2] - matrix[2, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 1])**2 - (matrix[1, 0] + matrix[0, 1])**2)

                    K = ((r00*r11*e11 - r01*r10*e10*e01)**-0.5)
                    Tk = 2*cmath.acos((K*(r00+r11*e11))/2)
                    O = (Tk*K)/(2*cmath.sin(Tk/2))

                    LBLD = O * (r00 - r11*e11)*1j
                    LBpLDp = O * (r01*e01 + r10*e10)*1j
                    CBCD = O * (r01*e01 - r10*e10)

                    r00_base = math.sqrt((matrix_base[0, 0] + matrix_base[0, 1] + matrix_base[1, 0] + matrix_base[1, 1])/2)
                    r01_base = math.sqrt((matrix_base[0, 0] - matrix_base[0, 1] + matrix_base[1, 0] - matrix_base[1, 1])/2)
                    r10_base = math.sqrt((matrix_base[0, 0] + matrix_base[0, 1] - matrix_base[1, 0] - matrix_base[1, 1])/2)
                    r11_base = math.sqrt((matrix_base[0, 0] - matrix_base[0, 1] - matrix_base[1, 0] + matrix_base[1, 1])/2)

                    e01_base = ((matrix_base[0, 2] + matrix_base[1, 2]) - (matrix_base[0, 3] + matrix_base[1, 3])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[1, 0])**2 - (matrix_base[0, 1] + matrix_base[1, 1])**2)
                    e10_base = ((matrix_base[2, 0] + matrix_base[2, 1]) + (matrix_base[3, 0] + matrix_base[3, 1])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[0, 1])**2 - (matrix_base[1, 0] + matrix_base[1, 1])**2)
                    e11_base = ((matrix_base[2, 2] + matrix_base[3, 3]) + (matrix_base[3, 2] - matrix_base[2, 3])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[1, 1])**2 - (matrix_base[1, 0] + matrix_base[0, 1])**2)

                    K_base = ((r00_base*r11_base*e11_base - r01_base*r10_base*e10_base*e01_base)**-0.5)
                    Tk_base = 2*cmath.acos((K_base*(r00_base+r11_base*e11_base))/2)
                    O_base = (Tk_base*K_base)/(2*cmath.sin(Tk_base/2))

                    LBLD_base = O_base * (r00_base - r11_base*e11_base)*1j
                    LBpLDp_base = O_base * (r01_base*e01_base + r10_base*e10_base)*1j
                    CBCD_base = O_base * (r01_base*e01_base - r10_base*e10_base)

                    aLB_list[0].append(LBLD.real - LBLD_base.real)
                    aLD_list[0].append(-1*LBLD.imag - -1*LBLD_base.imag)

                    aLBp_list[0].append(LBpLDp.real - LBpLDp_base.real)
                    aLDp_list[0].append(-1*LBpLDp.imag - -1*LBpLDp_base.imag)

                    aCB_list[0].append(CBCD.real - CBCD_base.real)
                    aCD_list[0].append(-1*CBCD.imag - -1*CBCD_base.imag)

                    ag_factor_list[0].append((-1*CBCD.imag - -1*CBCD_base.imag)/(math.log10(1/(csv_file['M00'][0]/csv_base['M00'][0]))))

                    CD_list_new[0].append(32980*0.94*0.993557*((csv_file['M30'][0]+csv_file['M03'][0])/(2*csv_file['M00'][0])-(csv_base['M30'][0]+csv_base['M03'][0])/(2*csv_base['M00'][0])))
                    CB_list_new[0].append(0.285787*1000*math.degrees(2*(np.arcsin((csv_file['M12'][0]-csv_file['M21'][0])/(2*csv_file['M00'][0])-np.arcsin((csv_base['M12'][0]-csv_base['M21'][0])/(2*csv_base['M00'][0]))))))
                    LD_list_new[0].append((-1.070135)*((csv_file['M10'][0]+csv_file['M01'][0])/(2*csv_file['M00'][0])-(csv_base['M10'][0]+csv_base['M01'][0])/(2*csv_base['M00'][0])))
                    LB_list_new[0].append((-0.0193343)*math.degrees(np.arcsin((csv_file['M23'][0]-csv_file['M32'][0])/(2*csv_file['M00'][0])-np.arcsin((csv_base['M23'][0]-csv_base['M32'][0])/(2*csv_base['M00'][0])))))
                    LDp_list_new[0].append((-1.063424)*((csv_file['M20'][0]+csv_file['M02'][0])/(2*csv_file['M00'][0])-(csv_base['M20'][0]+csv_base['M02'][0])/(2*csv_base['M00'][0])))
                    LBp_list_new[0].append((-0.2056925)*math.degrees(np.arcsin((csv_file['M31'][0]-csv_file['M13'][0])/(2*csv_file['M00'][0])-np.arcsin((csv_base['M31'][0]-csv_base['M13'][0])/(2*csv_base['M00'][0])))))
                    g_factor_list_new[0].append((((0.94*0.993557*((csv_file['M30'][0]+csv_file['M03'][0])/(2*csv_file['M00'][0])-(csv_base['M30'][0]+csv_base['M03'][0])/(2*csv_base['M00'][0]))))/(math.log10(1/(csv_file['M00'][0]/csv_base['M00'][0])))))
                    Abs_list[0].append(math.log10(1/(csv_file['M00'][0]/csv_base['M00'][0])))
                else:

                    M = []
                    M.append(csv_file['M00'][0])
                    M.append(csv_file['M01'][0])
                    M.append(csv_file['M02'][0])
                    M.append(csv_file['M03'][0])
                    M.append(csv_file['M10'][0])
                    M.append(csv_file['M11'][0])
                    M.append(csv_file['M12'][0])
                    M.append(csv_file['M13'][0])
                    M.append(csv_file['M20'][0])
                    M.append(csv_file['M21'][0])
                    M.append(csv_file['M22'][0])
                    M.append(csv_file['M23'][0])
                    M.append(csv_file['M30'][0])
                    M.append(csv_file['M31'][0])
                    M.append(csv_file['M32'][0])
                    M.append(csv_file['M33'][0])

                    matrix = np.array(M).reshape(4,4)

                    LM = -1*logm(matrix)

                    mCD_list[0].append((LM[0, 3] + LM[3, 0])/-2)
                    mCB_list[0].append((LM[1, 2] - LM[2, 1])/2)
                    mLD_list[0].append((LM[0, 1] + LM[1, 0])/-2)
                    mLDp_list[0].append((LM[0, 2] + LM[2, 0])/-2)
                    mLB_list[0].append((LM[2, 3] - LM[3, 2])/2)
                    mLBp_list[0].append((LM[1, 3] - LM[3, 1])/2)
                    mg_factor_list[0].append((((LM[0, 3] + LM[3, 0])/-2)/((LM[0, 0] + LM[1, 1] + LM[2, 2] + LM[3, 3])/4)))

                    r00 = math.sqrt((matrix[0, 0] + matrix[0, 1] + matrix[1, 0] + matrix[1, 1])/2)
                    r01 = math.sqrt((matrix[0, 0] - matrix[0, 1] + matrix[1, 0] - matrix[1, 1])/2)
                    r10 = math.sqrt((matrix[0, 0] + matrix[0, 1] - matrix[1, 0] - matrix[1, 1])/2)
                    r11 = math.sqrt((matrix[0, 0] - matrix[0, 1] - matrix[1, 0] + matrix[1, 1])/2)

                    e01 = ((matrix[0, 2] + matrix[1, 2]) - (matrix[0, 3] + matrix[1, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 0])**2 - (matrix[0, 1] + matrix[1, 1])**2)
                    e10 = ((matrix[2, 0] + matrix[2, 1]) + (matrix[3, 0] + matrix[3, 1])*1j) / math.sqrt((matrix[0, 0] + matrix[0, 1])**2 - (matrix[1, 0] + matrix[1, 1])**2)
                    e11 = ((matrix[2, 2] + matrix[3, 3]) + (matrix[3, 2] - matrix[2, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 1])**2 - (matrix[1, 0] + matrix[0, 1])**2)

                    K = ((r00*r11*e11 - r01*r10*e10*e01)**-0.5)
                    Tk = 2*cmath.acos((K*(r00+r11*e11))/2)
                    O = (Tk*K)/(2*cmath.sin(Tk/2))

                    LBLD = O * (r00 - r11*e11)*1j
                    LBpLDp = O * (r01*e01 + r10*e10)*1j
                    CBCD = O * (r01*e01 - r10*e10)

                    aLB_list[0].append(LBLD.real)
                    aLD_list[0].append(-1*LBLD.imag)

                    aLBp_list[0].append(LBpLDp.real)
                    aLDp_list[0].append(-1*LBpLDp.imag)

                    aCB_list[0].append(CBCD.real)
                    aCD_list[0].append(-1*CBCD.imag)

                    ag_factor_list[0].append((-1*CBCD.imag)/(math.log10(1/csv_file['M00'][0])))

                    CD_list_new[0].append(32980*0.94*0.993557*((csv_file['M30'][0]+csv_file['M03'][0])/(2*csv_file['M00'][0])))
                    CB_list_new[0].append(0.285787*1000*math.degrees(2*np.arcsin((csv_file['M12'][0]-csv_file['M21'][0])/(2*csv_file['M00'][0]))))
                    LD_list_new[0].append((-1.070135)*((csv_file['M10'][0]+csv_file['M01'][0])/(2*csv_file['M00'][0])))
                    LB_list_new[0].append((-0.0193343)*math.degrees(np.arcsin((csv_file['M23'][0]-csv_file['M32'][0])/(2*csv_file['M00'][0]))))
                    LDp_list_new[0].append((-1.063424)*((csv_file['M20'][0]+csv_file['M02'][0])/(2*csv_file['M00'][0])))
                    LBp_list_new[0].append((-0.2056925)*math.degrees(np.arcsin((csv_file['M31'][0]-csv_file['M13'][0])/(2*csv_file['M00'][0]))))
                    g_factor_list_new[0].append((((csv_file['M30'][0]+csv_file['M03'][0])/(2*csv_file['M00'][0]))/(math.log10(1/csv_file['M00'][0]))))
                    Abs_list[0].append(math.log10(1/csv_file['M00'][0]))
                    
                j = 0

                for i in range(1, len(csv_file)):
                    if csv_file['Wavelength'][i] != t:
                        M00_list[j].append(csv_file['M00'][i])
                        M01_list[j].append(csv_file['M01'][i])
                        M02_list[j].append(csv_file['M02'][i])
                        M03_list[j].append(csv_file['M03'][i])
                        M10_list[j].append(csv_file['M10'][i])
                        M11_list[j].append(csv_file['M11'][i])
                        M12_list[j].append(csv_file['M12'][i])
                        M13_list[j].append(csv_file['M13'][i])
                        M20_list[j].append(csv_file['M20'][i])
                        M21_list[j].append(csv_file['M21'][i])
                        M22_list[j].append(csv_file['M22'][i])
                        M23_list[j].append(csv_file['M23'][i])
                        M30_list[j].append(csv_file['M30'][i])
                        M31_list[j].append(csv_file['M31'][i])
                        M32_list[j].append(csv_file['M32'][i])
                        M33_list[j].append(csv_file['M33'][i])

                        CD_list[j].append(csv_file['CD'][i])
                        CB_list[j].append((csv_file['CR'][i]))
                        LD_list[j].append(csv_file['LD'][i])
                        LB_list[j].append((csv_file['LR'][i]))
                        LDp_list[j].append(csv_file['LDp'][i])
                        LBp_list[j].append((csv_file['LRp'][i]))
                        g_factor_list[j].append(csv_file['CD'][i]/32980/(math.log10(1/csv_file['M00'][i])))

                        if str(reply5) == 'Yes':

                            M = []
                            M.append(csv_file['M00'][i])
                            M.append(csv_file['M01'][i])
                            M.append(csv_file['M02'][i])
                            M.append(csv_file['M03'][i])
                            M.append(csv_file['M10'][i])
                            M.append(csv_file['M11'][i])
                            M.append(csv_file['M12'][i])
                            M.append(csv_file['M13'][i])
                            M.append(csv_file['M20'][i])
                            M.append(csv_file['M21'][i])
                            M.append(csv_file['M22'][i])
                            M.append(csv_file['M23'][i])
                            M.append(csv_file['M30'][i])
                            M.append(csv_file['M31'][i])
                            M.append(csv_file['M32'][i])
                            M.append(csv_file['M33'][i])

                            matrix = np.array(M).reshape(4,4)

                            LM = -1*logm(matrix)

                            B = []
                            B.append(csv_base['M00'][i])    # base = baseline
                            B.append(csv_base['M01'][i])
                            B.append(csv_base['M02'][i])
                            B.append(csv_base['M03'][i])
                            B.append(csv_base['M10'][i])
                            B.append(csv_base['M11'][i])
                            B.append(csv_base['M12'][i])
                            B.append(csv_base['M13'][i])
                            B.append(csv_base['M20'][i])
                            B.append(csv_base['M21'][i])
                            B.append(csv_base['M22'][i])
                            B.append(csv_base['M23'][i])
                            B.append(csv_base['M30'][i])
                            B.append(csv_base['M31'][i])
                            B.append(csv_base['M32'][i])
                            B.append(csv_base['M33'][i])

                            matrix_base = np.array(B).reshape(4,4)

                            LM_base = -1*logm(matrix_base)

                            mCD_list[j].append(((LM[0, 3] + LM[3, 0])/-2) - ((LM_base[0, 3] + LM_base[3, 0])/-2)) 
                            mCB_list[j].append(((LM[1, 2] - LM[2, 1])/2) - ((LM_base[1, 2] - LM_base[2, 1])/2))
                            mLD_list[j].append(((LM[0, 1] + LM[1, 0])/-2) - ((LM_base[0, 1] + LM_base[1, 0])/-2))
                            mLDp_list[j].append(((LM[0, 2] + LM[2, 0])/-2) - ((LM_base[0, 2] + LM_base[2, 0])/-2))
                            mLB_list[j].append(((LM[2, 3] - LM[3, 2])/2) - ((LM_base[2, 3] - LM_base[3, 2])/2))
                            mLBp_list[j].append(((LM[1, 3] - LM[3, 1])/2) - ((LM_base[1, 3] - LM_base[3, 1])/2))
                            mg_factor_list[j].append(((((LM[0, 3] + LM[3, 0])/-2) - ((LM_base[0, 3] + LM_base[3, 0])/-2))/((LM[0, 0] + LM[1, 1] + LM[2, 2] + LM[3, 3])/4) - (LM_base[0, 0] + LM_base[1, 1] + LM_base[2, 2] + LM_base[3, 3])/4))

                            r00 = math.sqrt((matrix[0, 0] + matrix[0, 1] + matrix[1, 0] + matrix[1, 1])/2)
                            r01 = math.sqrt((matrix[0, 0] - matrix[0, 1] + matrix[1, 0] - matrix[1, 1])/2)
                            r10 = math.sqrt((matrix[0, 0] + matrix[0, 1] - matrix[1, 0] - matrix[1, 1])/2)
                            r11 = math.sqrt((matrix[0, 0] - matrix[0, 1] - matrix[1, 0] + matrix[1, 1])/2)

                            e01 = ((matrix[0, 2] + matrix[1, 2]) - (matrix[0, 3] + matrix[1, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 0])**2 - (matrix[0, 1] + matrix[1, 1])**2)
                            e10 = ((matrix[2, 0] + matrix[2, 1]) + (matrix[3, 0] + matrix[3, 1])*1j) / math.sqrt((matrix[0, 0] + matrix[0, 1])**2 - (matrix[1, 0] + matrix[1, 1])**2)
                            e11 = ((matrix[2, 2] + matrix[3, 3]) + (matrix[3, 2] - matrix[2, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 1])**2 - (matrix[1, 0] + matrix[0, 1])**2)

                            K = ((r00*r11*e11 - r01*r10*e10*e01)**-0.5)
                            Tk = 2*cmath.acos((K*(r00+r11*e11))/2)
                            O = (Tk*K)/(2*cmath.sin(Tk/2))

                            LBLD = O * (r00 - r11*e11)*1j
                            LBpLDp = O * (r01*e01 + r10*e10)*1j
                            CBCD = O * (r01*e01 - r10*e10)

                            r00_base = math.sqrt((matrix_base[0, 0] + matrix_base[0, 1] + matrix_base[1, 0] + matrix_base[1, 1])/2)
                            r01_base = math.sqrt((matrix_base[0, 0] - matrix_base[0, 1] + matrix_base[1, 0] - matrix_base[1, 1])/2)
                            r10_base = math.sqrt((matrix_base[0, 0] + matrix_base[0, 1] - matrix_base[1, 0] - matrix_base[1, 1])/2)
                            r11_base = math.sqrt((matrix_base[0, 0] - matrix_base[0, 1] - matrix_base[1, 0] + matrix_base[1, 1])/2)

                            e01_base = ((matrix_base[0, 2] + matrix_base[1, 2]) - (matrix_base[0, 3] + matrix_base[1, 3])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[1, 0])**2 - (matrix_base[0, 1] + matrix_base[1, 1])**2)
                            e10_base = ((matrix_base[2, 0] + matrix_base[2, 1]) + (matrix_base[3, 0] + matrix_base[3, 1])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[0, 1])**2 - (matrix_base[1, 0] + matrix_base[1, 1])**2)
                            e11_base = ((matrix_base[2, 2] + matrix_base[3, 3]) + (matrix_base[3, 2] - matrix_base[2, 3])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[1, 1])**2 - (matrix_base[1, 0] + matrix_base[0, 1])**2)

                            K_base = ((r00_base*r11_base*e11_base - r01_base*r10_base*e10_base*e01_base)**-0.5)
                            Tk_base = 2*cmath.acos((K_base*(r00_base+r11_base*e11_base))/2)
                            O_base = (Tk_base*K_base)/(2*cmath.sin(Tk_base/2))

                            LBLD_base = O_base * (r00_base - r11_base*e11_base)*1j
                            LBpLDp_base = O_base * (r01_base*e01_base + r10_base*e10_base)*1j
                            CBCD_base = O_base * (r01_base*e01_base - r10_base*e10_base)

                            aLB_list[j].append(LBLD.real - LBLD_base.real)
                            aLD_list[j].append(-1*LBLD.imag - -1*LBLD_base.imag)

                            aLBp_list[j].append(LBpLDp.real - LBpLDp_base.real)
                            aLDp_list[j].append(-1*LBpLDp.imag - -1*LBpLDp_base.imag)

                            aCB_list[j].append(CBCD.real - CBCD_base.real)
                            aCD_list[j].append(-1*CBCD.imag - -1*CBCD_base.imag)

                            ag_factor_list[j].append((-1*CBCD.imag - -1*CBCD_base.imag)/(math.log10(1/(csv_file['M00'][i]/csv_base['M00'][i]))))

                            CD_list_new[j].append(32980*0.94*0.993557*((csv_file['M30'][i]+csv_file['M03'][i])/(2*csv_file['M00'][i])-(csv_base['M30'][i]+csv_base['M03'][i])/(2*csv_base['M00'][i])))
                            CB_list_new[j].append(0.285787*1000*math.degrees(2*(np.arcsin((csv_file['M12'][i]-csv_file['M21'][i])/(2*csv_file['M00'][i])-np.arcsin((csv_base['M12'][i]-csv_base['M21'][i])/(2*csv_base['M00'][i]))))))
                            LD_list_new[j].append((-1.070135)*((csv_file['M10'][i]+csv_file['M01'][i])/(2*csv_file['M00'][i])-(csv_base['M10'][i]+csv_base['M01'][i])/(2*csv_base['M00'][i])))
                            LB_list_new[j].append((-0.0193343)*math.degrees((np.arcsin((csv_file['M23'][i]-csv_file['M32'][i])/(2*csv_file['M00'][i])-np.arcsin((csv_base['M23'][i]-csv_base['M32'][i])/(2*csv_base['M00'][i]))))))
                            LDp_list_new[j].append((-1.063424)*((csv_file['M20'][i]+csv_file['M02'][i])/(2*csv_file['M00'][i])-(csv_base['M20'][i]+csv_base['M02'][i])/(2*csv_base['M00'][i])))
                            LBp_list_new[j].append((-0.2056925)*math.degrees((np.arcsin((csv_file['M31'][i]-csv_file['M13'][i])/(2*csv_file['M00'][i])-np.arcsin((csv_base['M31'][i]-csv_base['M13'][i])/(2*csv_base['M00'][i]))))))
                            g_factor_list_new[j].append((((0.94*0.993557*((csv_file['M30'][i]+csv_file['M03'][i])/(2*csv_file['M00'][i])-(csv_base['M30'][i]+csv_base['M03'][i])/(2*csv_base['M00'][i]))))/(math.log10(1/(csv_file['M00'][i]/csv_base['M00'][i])))))
                            Abs_list[j].append(math.log10(1/(csv_file['M00'][i]/csv_base['M00'][i])))
                        else:

                            M = []
                            M.append(csv_file['M00'][i])
                            M.append(csv_file['M01'][i])
                            M.append(csv_file['M02'][i])
                            M.append(csv_file['M03'][i])
                            M.append(csv_file['M10'][i])
                            M.append(csv_file['M11'][i])
                            M.append(csv_file['M12'][i])
                            M.append(csv_file['M13'][i])
                            M.append(csv_file['M20'][i])
                            M.append(csv_file['M21'][i])
                            M.append(csv_file['M22'][i])
                            M.append(csv_file['M23'][i])
                            M.append(csv_file['M30'][i])
                            M.append(csv_file['M31'][i])
                            M.append(csv_file['M32'][i])
                            M.append(csv_file['M33'][i])

                            matrix = np.array(M).reshape(4,4)

                            LM = -1*logm(matrix)

                            mCD_list[j].append((LM[0, 3] + LM[3, 0])/-2)
                            mCB_list[j].append((LM[1, 2] - LM[2, 1])/2)
                            mLD_list[j].append((LM[0, 1] + LM[1, 0])/-2)
                            mLDp_list[j].append((LM[0, 2] + LM[2, 0])/-2)
                            mLB_list[j].append((LM[2, 3] - LM[3, 2])/2)
                            mLBp_list[j].append((LM[1, 3] - LM[3, 1])/2)
                            mg_factor_list[j].append((((LM[0, 3] + LM[3, 0])/-2)/((LM[0, 0] + LM[1, 1] + LM[2, 2] + LM[3, 3])/4)))

                            r00 = math.sqrt((matrix[0, 0] + matrix[0, 1] + matrix[1, 0] + matrix[1, 1])/2)
                            r01 = math.sqrt((matrix[0, 0] - matrix[0, 1] + matrix[1, 0] - matrix[1, 1])/2)
                            r10 = math.sqrt((matrix[0, 0] + matrix[0, 1] - matrix[1, 0] - matrix[1, 1])/2)
                            r11 = math.sqrt((matrix[0, 0] - matrix[0, 1] - matrix[1, 0] + matrix[1, 1])/2)

                            e01 = ((matrix[0, 2] + matrix[1, 2]) - (matrix[0, 3] + matrix[1, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 0])**2 - (matrix[0, 1] + matrix[1, 1])**2)
                            e10 = ((matrix[2, 0] + matrix[2, 1]) + (matrix[3, 0] + matrix[3, 1])*1j) / math.sqrt((matrix[0, 0] + matrix[0, 1])**2 - (matrix[1, 0] + matrix[1, 1])**2)
                            e11 = ((matrix[2, 2] + matrix[3, 3]) + (matrix[3, 2] - matrix[2, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 1])**2 - (matrix[1, 0] + matrix[0, 1])**2)

                            K = ((r00*r11*e11 - r01*r10*e10*e01)**-0.5)
                            Tk = 2*cmath.acos((K*(r00+r11*e11))/2)
                            O = (Tk*K)/(2*cmath.sin(Tk/2))

                            LBLD = O * (r00 - r11*e11)*1j
                            LBpLDp = O * (r01*e01 + r10*e10)*1j
                            CBCD = O * (r01*e01 - r10*e10)

                            aLB_list[j].append(LBLD.real)
                            aLD_list[j].append(-1*LBLD.imag)

                            aLBp_list[j].append(LBpLDp.real)
                            aLDp_list[j].append(-1*LBpLDp.imag)

                            aCB_list[j].append(CBCD.real)
                            aCD_list[j].append(-1*CBCD.imag)

                            ag_factor_list[j].append((-1*CBCD.imag)/(math.log10(1/csv_file['M00'][i])))

                            CD_list_new[j].append(32980*0.94*0.993557*((csv_file['M30'][i]+csv_file['M03'][i])/(2*csv_file['M00'][i])))
                            CB_list_new[j].append(0.285787*1000*math.degrees(2*np.arcsin((csv_file['M12'][i]-csv_file['M21'][i])/(2*csv_file['M00'][i]))))
                            LD_list_new[j].append((-1.070135)*((csv_file['M10'][i]+csv_file['M01'][i])/(2*csv_file['M00'][i])))
                            LB_list_new[j].append((-0.0193343)*math.degrees(np.arcsin((csv_file['M23'][i]-csv_file['M32'][i])/(2*csv_file['M00'][i]))))
                            LDp_list_new[j].append((-1.063424)*((csv_file['M20'][i]+csv_file['M02'][i])/(2*csv_file['M00'][i])))
                            LBp_list_new[j].append((-0.2056925)*math.degrees(np.arcsin((csv_file['M31'][i]-csv_file['M13'][i])/(2*csv_file['M00'][i]))))
                            g_factor_list_new[j].append((((csv_file['M30'][i]+csv_file['M03'][i])/(2*csv_file['M00'][i]))/(math.log10(1/csv_file['M00'][i]))))
                            Abs_list[j].append(math.log10(1/csv_file['M00'][i]))

                    else:
                        j += 1
                        M00_list[j].append(csv_file['M00'][i])
                        M01_list[j].append(csv_file['M01'][i])
                        M02_list[j].append(csv_file['M02'][i])
                        M03_list[j].append(csv_file['M03'][i])
                        M10_list[j].append(csv_file['M10'][i])
                        M11_list[j].append(csv_file['M11'][i])
                        M12_list[j].append(csv_file['M12'][i])
                        M13_list[j].append(csv_file['M13'][i])
                        M20_list[j].append(csv_file['M20'][i])
                        M21_list[j].append(csv_file['M21'][i])
                        M22_list[j].append(csv_file['M22'][i])
                        M23_list[j].append(csv_file['M23'][i])
                        M30_list[j].append(csv_file['M30'][i])
                        M31_list[j].append(csv_file['M31'][i])
                        M32_list[j].append(csv_file['M32'][i])
                        M33_list[j].append(csv_file['M33'][i])
                        CD_list[j].append(csv_file['CD'][i])
                        CB_list[j].append((csv_file['CR'][i]))
                        LD_list[j].append(csv_file['LD'][i])
                        LB_list[j].append((csv_file['LR'][i]))
                        LDp_list[j].append(csv_file['LDp'][i])
                        LBp_list[j].append((csv_file['LRp'][i]))
                        g_factor_list[j].append(csv_file['CD'][i]/32980/(math.log10(1/csv_file['M00'][i])))
                        if str(reply5) == 'Yes':

                            M = []
                            M.append(csv_file['M00'][i])
                            M.append(csv_file['M01'][i])
                            M.append(csv_file['M02'][i])
                            M.append(csv_file['M03'][i])
                            M.append(csv_file['M10'][i])
                            M.append(csv_file['M11'][i])
                            M.append(csv_file['M12'][i])
                            M.append(csv_file['M13'][i])
                            M.append(csv_file['M20'][i])
                            M.append(csv_file['M21'][i])
                            M.append(csv_file['M22'][i])
                            M.append(csv_file['M23'][i])
                            M.append(csv_file['M30'][i])
                            M.append(csv_file['M31'][i])
                            M.append(csv_file['M32'][i])
                            M.append(csv_file['M33'][i])

                            matrix = np.array(M).reshape(4,4)

                            LM = -1*logm(matrix)

                            B = []
                            B.append(csv_base['M00'][i])    # base = baseline
                            B.append(csv_base['M01'][i])
                            B.append(csv_base['M02'][i])
                            B.append(csv_base['M03'][i])
                            B.append(csv_base['M10'][i])
                            B.append(csv_base['M11'][i])
                            B.append(csv_base['M12'][i])
                            B.append(csv_base['M13'][i])
                            B.append(csv_base['M20'][i])
                            B.append(csv_base['M21'][i])
                            B.append(csv_base['M22'][i])
                            B.append(csv_base['M23'][i])
                            B.append(csv_base['M30'][i])
                            B.append(csv_base['M31'][i])
                            B.append(csv_base['M32'][i])
                            B.append(csv_base['M33'][i])

                            matrix_base = np.array(B).reshape(4,4)

                            LM_base = -1*logm(matrix_base)

                            mCD_list[j].append(((LM[0, 3] + LM[3, 0])/-2) - ((LM_base[0, 3] + LM_base[3, 0])/-2)) 
                            mCB_list[j].append(((LM[1, 2] - LM[2, 1])/2) - ((LM_base[1, 2] - LM_base[2, 1])/2))
                            mLD_list[j].append(((LM[0, 1] + LM[1, 0])/-2) - ((LM_base[0, 1] + LM_base[1, 0])/-2))
                            mLDp_list[j].append(((LM[0, 2] + LM[2, 0])/-2) - ((LM_base[0, 2] + LM_base[2, 0])/-2))
                            mLB_list[j].append(((LM[2, 3] - LM[3, 2])/2) - ((LM_base[2, 3] - LM_base[3, 2])/2))
                            mLBp_list[j].append(((LM[1, 3] - LM[3, 1])/2) - ((LM_base[1, 3] - LM_base[3, 1])/2))
                            mg_factor_list[j].append(((((LM[0, 3] + LM[3, 0])/-2) - ((LM_base[0, 3] + LM_base[3, 0])/-2))/((LM[0, 0] + LM[1, 1] + LM[2, 2] + LM[3, 3])/4) - (LM_base[0, 0] + LM_base[1, 1] + LM_base[2, 2] + LM_base[3, 3])/4))

                            r00 = math.sqrt((matrix[0, 0] + matrix[0, 1] + matrix[1, 0] + matrix[1, 1])/2)
                            r01 = math.sqrt((matrix[0, 0] - matrix[0, 1] + matrix[1, 0] - matrix[1, 1])/2)
                            r10 = math.sqrt((matrix[0, 0] + matrix[0, 1] - matrix[1, 0] - matrix[1, 1])/2)
                            r11 = math.sqrt((matrix[0, 0] - matrix[0, 1] - matrix[1, 0] + matrix[1, 1])/2)

                            e01 = ((matrix[0, 2] + matrix[1, 2]) - (matrix[0, 3] + matrix[1, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 0])**2 - (matrix[0, 1] + matrix[1, 1])**2)
                            e10 = ((matrix[2, 0] + matrix[2, 1]) + (matrix[3, 0] + matrix[3, 1])*1j) / math.sqrt((matrix[0, 0] + matrix[0, 1])**2 - (matrix[1, 0] + matrix[1, 1])**2)
                            e11 = ((matrix[2, 2] + matrix[3, 3]) + (matrix[3, 2] - matrix[2, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 1])**2 - (matrix[1, 0] + matrix[0, 1])**2)

                            K = ((r00*r11*e11 - r01*r10*e10*e01)**-0.5)
                            Tk = 2*cmath.acos((K*(r00+r11*e11))/2)
                            O = (Tk*K)/(2*cmath.sin(Tk/2))

                            LBLD = O * (r00 - r11*e11)*1j
                            LBpLDp = O * (r01*e01 + r10*e10)*1j
                            CBCD = O * (r01*e01 - r10*e10)

                            r00_base = math.sqrt((matrix_base[0, 0] + matrix_base[0, 1] + matrix_base[1, 0] + matrix_base[1, 1])/2)
                            r01_base = math.sqrt((matrix_base[0, 0] - matrix_base[0, 1] + matrix_base[1, 0] - matrix_base[1, 1])/2)
                            r10_base = math.sqrt((matrix_base[0, 0] + matrix_base[0, 1] - matrix_base[1, 0] - matrix_base[1, 1])/2)
                            r11_base = math.sqrt((matrix_base[0, 0] - matrix_base[0, 1] - matrix_base[1, 0] + matrix_base[1, 1])/2)

                            e01_base = ((matrix_base[0, 2] + matrix_base[1, 2]) - (matrix_base[0, 3] + matrix_base[1, 3])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[1, 0])**2 - (matrix_base[0, 1] + matrix_base[1, 1])**2)
                            e10_base = ((matrix_base[2, 0] + matrix_base[2, 1]) + (matrix_base[3, 0] + matrix_base[3, 1])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[0, 1])**2 - (matrix_base[1, 0] + matrix_base[1, 1])**2)
                            e11_base = ((matrix_base[2, 2] + matrix_base[3, 3]) + (matrix_base[3, 2] - matrix_base[2, 3])*1j) / math.sqrt((matrix_base[0, 0] + matrix_base[1, 1])**2 - (matrix_base[1, 0] + matrix_base[0, 1])**2)

                            K_base = ((r00_base*r11_base*e11_base - r01_base*r10_base*e10_base*e01_base)**-0.5)
                            Tk_base = 2*cmath.acos((K_base*(r00_base+r11_base*e11_base))/2)
                            O_base = (Tk_base*K_base)/(2*cmath.sin(Tk_base/2))

                            LBLD_base = O_base * (r00_base - r11_base*e11_base)*1j
                            LBpLDp_base = O_base * (r01_base*e01_base + r10_base*e10_base)*1j
                            CBCD_base = O_base * (r01_base*e01_base - r10_base*e10_base)

                            aLB_list[j].append(LBLD.real - LBLD_base.real)
                            aLD_list[j].append(-1*LBLD.imag - -1*LBLD_base.imag)

                            aLBp_list[j].append(LBpLDp.real - LBpLDp_base.real)
                            aLDp_list[j].append(-1*LBpLDp.imag - -1*LBpLDp_base.imag)

                            aCB_list[j].append(CBCD.real - CBCD_base.real)
                            aCD_list[j].append(-1*CBCD.imag - -1*CBCD_base.imag)

                            ag_factor_list[j].append((-1*CBCD.imag - -1*CBCD_base.imag)/(math.log10(1/(csv_file['M00'][i]/csv_base['M00'][i]))))

                            CD_list_new[j].append(32980*0.94*0.993557*((csv_file['M30'][i]+csv_file['M03'][i])/(2*csv_file['M00'][i])-(csv_base['M30'][i]+csv_base['M03'][i])/(2*csv_base['M00'][i])))
                            CB_list_new[j].append(0.285787*1000*math.degrees(2*(np.arcsin((csv_file['M12'][i]-csv_file['M21'][i])/(2*csv_file['M00'][i])-np.arcsin((csv_base['M12'][i]-csv_base['M21'][i])/(2*csv_base['M00'][i]))))))
                            LD_list_new[j].append((-1.070135)*((csv_file['M10'][i]+csv_file['M01'][i])/(2*csv_file['M00'][i])-(csv_base['M10'][i]+csv_base['M01'][i])/(2*csv_base['M00'][i])))
                            LB_list_new[j].append((-0.0193343)*math.degrees((np.arcsin((csv_file['M23'][i]-csv_file['M32'][i])/(2*csv_file['M00'][i])-np.arcsin((csv_base['M23'][i]-csv_base['M32'][i])/(2*csv_base['M00'][i]))))))
                            LDp_list_new[j].append((-1.063424)*((csv_file['M20'][i]+csv_file['M02'][i])/(2*csv_file['M00'][i])-(csv_base['M20'][i]+csv_base['M02'][i])/(2*csv_base['M00'][i])))
                            LBp_list_new[j].append((-0.2056925)*math.degrees((np.arcsin((csv_file['M31'][i]-csv_file['M13'][i])/(2*csv_file['M00'][i])-np.arcsin((csv_base['M31'][i]-csv_base['M13'][i])/(2*csv_base['M00'][i]))))))
                            g_factor_list_new[j].append((((0.94*0.993557*((csv_file['M30'][i]+csv_file['M03'][i])/(2*csv_file['M00'][i])-(csv_base['M30'][i]+csv_base['M03'][i])/(2*csv_base['M00'][i]))))/(math.log10(1/(csv_file['M00'][i]/csv_base['M00'][i])))))
                            Abs_list[j].append(math.log10(1/(csv_file['M00'][i]/csv_base['M00'][i])))
                        else:

                            M = []
                            M.append(csv_file['M00'][i])
                            M.append(csv_file['M01'][i])
                            M.append(csv_file['M02'][i])
                            M.append(csv_file['M03'][i])
                            M.append(csv_file['M10'][i])
                            M.append(csv_file['M11'][i])
                            M.append(csv_file['M12'][i])
                            M.append(csv_file['M13'][i])
                            M.append(csv_file['M20'][i])
                            M.append(csv_file['M21'][i])
                            M.append(csv_file['M22'][i])
                            M.append(csv_file['M23'][i])
                            M.append(csv_file['M30'][i])
                            M.append(csv_file['M31'][i])
                            M.append(csv_file['M32'][i])
                            M.append(csv_file['M33'][i])

                            matrix = np.array(M).reshape(4,4)

                            LM = -1*logm(matrix)

                            mCD_list[j].append((LM[0, 3] + LM[3, 0])/-2)
                            mCB_list[j].append((LM[1, 2] - LM[2, 1])/2)
                            mLD_list[j].append((LM[0, 1] + LM[1, 0])/-2)
                            mLDp_list[j].append((LM[0, 2] + LM[2, 0])/-2)
                            mLB_list[j].append((LM[2, 3] - LM[3, 2])/2)
                            mLBp_list[j].append((LM[1, 3] - LM[3, 1])/2)
                            mg_factor_list[j].append((((LM[0, 3] + LM[3, 0])/-2)/((LM[0, 0] + LM[1, 1] + LM[2, 2] + LM[3, 3])/4)))

                            r00 = math.sqrt((matrix[0, 0] + matrix[0, 1] + matrix[1, 0] + matrix[1, 1])/2)
                            r01 = math.sqrt((matrix[0, 0] - matrix[0, 1] + matrix[1, 0] - matrix[1, 1])/2)
                            r10 = math.sqrt((matrix[0, 0] + matrix[0, 1] - matrix[1, 0] - matrix[1, 1])/2)
                            r11 = math.sqrt((matrix[0, 0] - matrix[0, 1] - matrix[1, 0] + matrix[1, 1])/2)

                            e01 = ((matrix[0, 2] + matrix[1, 2]) - (matrix[0, 3] + matrix[1, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 0])**2 - (matrix[0, 1] + matrix[1, 1])**2)
                            e10 = ((matrix[2, 0] + matrix[2, 1]) + (matrix[3, 0] + matrix[3, 1])*1j) / math.sqrt((matrix[0, 0] + matrix[0, 1])**2 - (matrix[1, 0] + matrix[1, 1])**2)
                            e11 = ((matrix[2, 2] + matrix[3, 3]) + (matrix[3, 2] - matrix[2, 3])*1j) / math.sqrt((matrix[0, 0] + matrix[1, 1])**2 - (matrix[1, 0] + matrix[0, 1])**2)

                            K = ((r00*r11*e11 - r01*r10*e10*e01)**-0.5)
                            Tk = 2*cmath.acos((K*(r00+r11*e11))/2)
                            O = (Tk*K)/(2*cmath.sin(Tk/2))

                            LBLD = O * (r00 - r11*e11)*1j
                            LBpLDp = O * (r01*e01 + r10*e10)*1j
                            CBCD = O * (r01*e01 - r10*e10)

                            aLB_list[j].append(LBLD.real)
                            aLD_list[j].append(-1*LBLD.imag)

                            aLBp_list[j].append(LBpLDp.real)
                            aLDp_list[j].append(-1*LBpLDp.imag)

                            aCB_list[j].append(CBCD.real)
                            aCD_list[j].append(-1*CBCD.imag)

                            ag_factor_list[j].append((-1*CBCD.imag)/(math.log10(1/csv_file['M00'][i])))

                            CD_list_new[j].append(32980*0.94*0.993557*((csv_file['M30'][i]+csv_file['M03'][i])/(2*csv_file['M00'][i])))
                            CB_list_new[j].append(0.285787*1000*math.degrees(2*np.arcsin((csv_file['M12'][i]-csv_file['M21'][i])/(2*csv_file['M00'][i]))))
                            LD_list_new[j].append((-1.070135)*((csv_file['M10'][i]+csv_file['M01'][i])/(2*csv_file['M00'][i])))
                            LB_list_new[j].append((-0.0193343)*math.degrees(np.arcsin((csv_file['M23'][i]-csv_file['M32'][i])/(2*csv_file['M00'][i]))))
                            LDp_list_new[j].append((-1.063424)*((csv_file['M20'][i]+csv_file['M02'][i])/(2*csv_file['M00'][i])))
                            LBp_list_new[j].append((-0.2056925)*math.degrees(np.arcsin((csv_file['M31'][i]-csv_file['M13'][i])/(2*csv_file['M00'][i]))))
                            g_factor_list_new[j].append((((csv_file['M30'][i]+csv_file['M03'][i])/(2*csv_file['M00'][i]))/(math.log10(1/csv_file['M00'][i]))))
                            Abs_list[j].append(math.log10(1/csv_file['M00'][i]))

                for i in range(0, len(CD_list[0])):
                    CD_avg = 0
                    Abs_avg = 0
                    g_factor_avg = 0
                    CB_avg = 0
                    LD_avg = 0
                    LB_avg = 0
                    LDp_avg = 0
                    LBp_avg = 0

                    CD_new_avg = 0
                    g_factor_new_avg = 0
                    CB_new_avg = 0
                    LD_new_avg = 0
                    LB_new_avg = 0
                    LDp_new_avg = 0
                    LBp_new_avg = 0

                    mCD_avg = 0
                    mg_factor_avg = 0
                    mCB_avg = 0
                    mLD_avg = 0
                    mLB_avg = 0
                    mLDp_avg = 0
                    mLBp_avg = 0

                    aCD_avg = 0
                    ag_factor_avg = 0
                    aCB_avg = 0
                    aLD_avg = 0
                    aLB_avg = 0
                    aLDp_avg = 0
                    aLBp_avg = 0

                    for j in range(0, k):
                        CD_avg = CD_avg + CD_list[j][i]
                        Abs_avg = Abs_avg + Abs_list[j][i]
                        g_factor_avg = g_factor_avg + g_factor_list[j][i]
                        CB_avg = CB_avg + CB_list[j][i]
                        LD_avg = LD_avg + LD_list[j][i]
                        LB_avg = LB_avg + LB_list[j][i]
                        LDp_avg = LDp_avg + LDp_list[j][i]
                        LBp_avg = LBp_avg + LBp_list[j][i]

                        CD_new_avg = CD_new_avg + CD_list_new[j][i]
                        g_factor_new_avg = g_factor_new_avg + g_factor_list_new[j][i]
                        CB_new_avg = CB_new_avg + CB_list_new[j][i]
                        LD_new_avg = LD_new_avg + LD_list_new[j][i]
                        LB_new_avg = LB_new_avg + LB_list_new[j][i]
                        LDp_new_avg = LDp_new_avg + LDp_list_new[j][i]
                        LBp_new_avg = LBp_new_avg + LBp_list_new[j][i]

                        mCD_avg = mCD_avg + mCD_list[j][i]
                        mg_factor_avg = mg_factor_avg + mg_factor_list[j][i]
                        mCB_avg = mCB_avg + mCB_list[j][i]
                        mLD_avg = mLD_avg + mLD_list[j][i]
                        mLB_avg = mLB_avg + mLB_list[j][i]
                        mLDp_avg = mLDp_avg + mLDp_list[j][i]
                        mLBp_avg = mLBp_avg + mLBp_list[j][i]

                        aCD_avg = aCD_avg + aCD_list[j][i]
                        ag_factor_avg = ag_factor_avg + ag_factor_list[j][i]
                        aCB_avg = aCB_avg + aCB_list[j][i]
                        aLD_avg = aLD_avg + aLD_list[j][i]
                        aLB_avg = aLB_avg + aLB_list[j][i]
                        aLDp_avg = aLDp_avg + aLDp_list[j][i]
                        aLBp_avg = aLBp_avg + aLBp_list[j][i]


                    Abs_avg = Abs_avg/len(Abs_list)
                    CD_avg = CD_avg/len(CD_list)
                    g_factor_avg = g_factor_avg/len(g_factor_list)
                    CB_avg = CB_avg/len(CB_list)
                    LD_avg = LD_avg/len(LD_list)
                    LB_avg = LB_avg/len(LB_list)
                    LDp_avg = LDp_avg/len(LDp_list)
                    LBp_avg = LBp_avg/len(LBp_list)

                    CD_new_avg = CD_new_avg/len(CD_list)
                    g_factor_new_avg = g_factor_new_avg/len(g_factor_list)
                    CB_new_avg = CB_new_avg/len(CB_list)
                    LD_new_avg = LD_new_avg/len(LD_list)
                    LB_new_avg = LB_new_avg/len(LB_list)
                    LDp_new_avg = LDp_new_avg/len(LDp_list)
                    LBp_new_avg = LBp_new_avg/len(LBp_list)

                    mCD_avg = mCD_avg/len(CD_list)
                    mg_factor_avg = mg_factor_avg/len(g_factor_list)
                    mCB_avg = mCB_avg/len(CB_list)
                    mLD_avg = mLD_avg/len(LD_list)
                    mLB_avg = mLB_avg/len(LB_list)
                    mLDp_avg = mLDp_avg/len(LDp_list)
                    mLBp_avg = mLBp_avg/len(LBp_list)

                    aCD_avg = aCD_avg/len(CD_list)
                    ag_factor_avg = ag_factor_avg/len(g_factor_list)
                    aCB_avg = aCB_avg/len(CB_list)
                    aLD_avg = aLD_avg/len(LD_list)
                    aLB_avg = aLB_avg/len(LB_list)
                    aLDp_avg = aLDp_avg/len(LDp_list)
                    aLBp_avg = aLBp_avg/len(LBp_list)

                    Wavelength_Abs[k+1].append(Abs_avg)
                    Wavelength_CD[k+1].append(CD_avg)
                    Wavelength_g_factor[k+1].append(g_factor_avg)
                    Wavelength_CR[k+1].append(CB_avg)
                    Wavelength_LR[k+1].append(LB_avg)
                    Wavelength_LD[k+1].append(LD_avg)
                    Wavelength_LDp[k+1].append(LDp_avg)
                    Wavelength_LRp[k+1].append(LBp_avg)

                    Wavelength_CD_new[k+1].append(CD_new_avg)
                    Wavelength_g_factor_new[k+1].append(g_factor_new_avg)
                    Wavelength_CB_new[k+1].append(CB_new_avg)
                    Wavelength_LD_new[k+1].append(LD_new_avg)
                    Wavelength_LB_new[k+1].append(LB_new_avg)
                    Wavelength_LDp_new[k+1].append(LDp_new_avg)
                    Wavelength_LBp_new[k+1].append(LBp_new_avg)

                    Wavelength_mCD[k+1].append(mCD_avg)
                    Wavelength_mg_factor[k+1].append(mg_factor_avg)
                    Wavelength_mCB[k+1].append(mCB_avg)
                    Wavelength_mLB[k+1].append(mLB_avg)
                    Wavelength_mLD[k+1].append(mLD_avg)
                    Wavelength_mLDp[k+1].append(mLDp_avg)
                    Wavelength_mLBp[k+1].append(mLBp_avg)

                    Wavelength_aCD[k+1].append(aCD_avg)
                    Wavelength_ag_factor[k+1].append(ag_factor_avg)
                    Wavelength_aCB[k+1].append(aCB_avg)
                    Wavelength_aLB[k+1].append(aLB_avg)
                    Wavelength_aLD[k+1].append(aLD_avg)
                    Wavelength_aLDp[k+1].append(aLDp_avg)
                    Wavelength_aLBp[k+1].append(aLBp_avg)


            # df = pd.read_csv(
            #     files[0], 
            #     engine = 'python',
            #     skipinitialspace = True, 
            #     sep = '[ ]+')

            x = Wavelength_new
            y = mCD_list[0]

            fig.add_subplot().plot(x, y)
            canvas.draw()
            self.progressbar_stop()

        if files: plotGraph()

if __name__ == '__main__':
    q = mp.Queue()
    results = []

    root = tk.Tk()
    root.wm_title("Embedding in Tk")
    fig = Figure(figsize=(10, 8), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    pb = ttk.Progressbar(master=root, orient='horizontal', mode='indeterminate', length=500)

    window = MyWindow(root, pb, fig, canvas, q)
    window.test()           # call main method
    tk.mainloop()
