import argparse 
 
# With choices you are only allowed to supply ONE of the alternatives 
parser = argparse.ArgumentParser() 
parser.add_argument('food', choices=['spam','eggs','ham']) 
args = parser.parse_args() 
print(args.food)  
print(args.__dict__)

