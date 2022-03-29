'''
Try Block Firewalls
===================
All of this leads us into what stategy should we employ when using exception handling in our code?  My
personal preference if to use what I term as "try block firewalls".

The idea is to split an application into parts and create try blocks in each of these parts; you can use
function boundaries to define these parts.  The main program can also define a "master" try block.  Now, if 
anything goes wrong in one of the parts we attempt to handle the exception locally and prevent the exception 
propagating to the master try block; hence the firewall idea.  

Of course, sometimes we will encounter a problem that cannot be handled locally; a major error that breaks through 
the firewall and has to be handled in the master try block.  Of course if this happens then all the code in the 
parts that haven't yet been called will be skipped because of the "GOTO" nature of exception handling. 

Clearly this idea could be extended to several levels of firewalls, but in practice two or three levels work
out best.  Any deeper level than three, leads to the code becoming too complicated.
'''

class BigProblem(Exception): pass
class SmallProblem(Exception): pass

# example to demonstrate structuring of try blocks
# to handle minor errors in low level code, 
# but major problems in top level code.

def main():
    try:
        part1()
        part2(500)
        part3()
        part4()
    except BigProblem as e:
        print(e)

def part1():
    print("part 1")

def part2(x):
    try:
        if x > 100:
            raise BigProblem("part 2 failed spectacularly")
        elif x > 10:
            raise SmallProblem("part 2 failed")
        else:
            print("part 2 completed")
    # handle small problems locally, but
    # big problems break through the firewall
    except SmallProblem as e:
        print(e)

def part3():
    print("part 3")

def part4():
    print("part 4")
    
main()
