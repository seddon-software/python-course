############################################################
#
#    try-except-finally statements
#
############################################################

def f(x):
    if x > 50:
        raise Exception('exception thrown')

try:
    x = 10
    f(x)
except Exception as e:
    print(f'caught exception ... {e}')
else:
    print('no exception thrown')
finally:
    print('finally block is always called ...')

print("End of program")

