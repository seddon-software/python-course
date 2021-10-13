# website to get Mah symbols
import webbrowser
webbrowser.open("https://math.typeit.org/")


from numpy import array, cos, sin, arctan
import numpy as np

def rotate(vector, θ, 𝜙):
     matrix = [
               [sin(θ)*cos(𝜙), cos(θ)*cos(𝜙), -sin(𝜙)],
               [sin(θ)*sin(𝜙), cos(θ)*sin(𝜙),  cos(𝜙)],
               [       cos(θ),       -sin(θ),      0  ]
              ]
     mattrix = np.array(matrix)
     return matrix @ vector     # note: @ denote matrix multiplication 
 
π = 4 * arctan(1.0)
print(rotate(np.array([10, 10, 10]), π/3, π/4))
