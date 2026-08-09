'''
R1+R2+R3=15206
3.7*R2 + 3.9*R3=54631.127
R2/(R3-3.593)=R3/(R2-3.593)
'''
from scipy.optimize import fsolve
cog=2.626
def equations(vars):
    R1,R2,R3 = vars

    eq1=R1+R2+R3-4300
    eq2=3.7*R2 + 3.9*R3-11290
    eq3=R2*(3.7-cog)-R3*(3.9-cog)
    return [eq1, eq2, eq3]

# initial guess
guess = [1300,1300,1300]

solution = fsolve(equations, guess)

print("R1 =", solution[0])
print("R2 =", solution[1])
print("R3 =", solution[2])