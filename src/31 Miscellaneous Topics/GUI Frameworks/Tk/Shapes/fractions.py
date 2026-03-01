
f1 = "2/3"
f2 = "3/8"

import tkinter as tk
import math
from fractions import Fraction

class FractionCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Fraction Addition Calculator")
        self.root.geometry("800x600")
        
        self.stage = 0
        self.f1 = f1
        self.f2 = f2
        self.f1_n = Fraction(f1).numerator
        self.f1_d = Fraction(f1).denominator
        self.f2_n = Fraction(f2).numerator
        self.f2_d = Fraction(f2).denominator
        self.d = math.lcm(self.f1_d, self.f2_d)

        self.text_display = tk.Text(root, width=60, font=("Courier", 16, "bold"))
        self.text_display.pack(pady=10)
        
        self.button = tk.Button(root, text="Next Stage", command=self.show_next_stage, font=("Arial", 16))
        self.button.pack()
        
        self.show_stage()
    
    def show_stage(self):
        self.text_display.delete(1.0, tk.END)
        content = ""
        
        if self.stage >= 0:
            content += f"Step 1: Write the fractions\n"
            content += f"{self.f1} + {self.f2}\n\n"
        
        if self.stage >= 1:
            content += f"Step 2: Find the LCD (Least Common Denominator)\n"
            content += f"LCD of {self.f1_d} and {self.f2_d} = {self.d}\n\n"
        
        if self.stage >= 2:
            content += f"Step 3: Convert to equivalent fractions\n"
            f1n = int(self.f1_n*self.d/self.f1_d)
            f2n = int(self.f2_n*self.d/self.f2_d)
            f1 = Fraction(f1n, self.d, _normalize=False)
            f2 = Fraction(f2n, self.d, _normalize=False)
            content += f"{self.f1} = {f1}\n"
            content += f"{self.f2} = {f2}\n\n"
        
        if self.stage >= 3:
            content += f"Step 4: Add the numerators\n"
            result = Fraction(f1.numerator + f2.numerator, self.d)
            content += f"{f1} + {f2} = {result}\n\n"
        
        if self.stage >= 4:
            if result > 1:
                whole = int(result)
                fraction = result - whole
                content += f"Step 5: Reduce fraction\n"
                content += f"{f1} + {f2} = {whole} {fraction}\n\n"

        if self.stage >= 5:
            content += f"Finished\n"
                                
        self.text_display.insert(1.0, content)
        self.text_display.config(state=tk.DISABLED)
    
    def show_next_stage(self):
        if self.stage < 5:
            self.stage += 1
            self.text_display.config(state=tk.NORMAL)
            self.show_stage()

root = tk.Tk()
app = FractionCalculator(root)
root.mainloop()
