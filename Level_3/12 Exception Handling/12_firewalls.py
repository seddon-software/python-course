class BigProblem(Exception): pass
class SmallProblem(Exception): pass

# example to demonstrate structuring of try blocks
# to handle minor errors in low level code, 
# but major problems in top level code.

def main():
    try:
        part1()
        part2(50)
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
