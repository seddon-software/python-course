'''
Using Unicode Variables
=======================
Not only do all Python strings use Unicode, but you can use a restricted set of Unicode for variable names.
This is particularly helpful in expressing mathematical expressions using Greek letters.

You can use the following website to copy and paste common Math symbols:
            https://math.typeit.org/
'''

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
print("After rotation [10, 10, 10] becomes ...")
print(rotate(np.array([10, 10, 10]), π/3, π/4))
