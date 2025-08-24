'''
The statement:
    counter _+= 1
should not be thread safe, but seems to be in CPython.  However, if you run this example using PyPy then 
+= will not be thread safe. 

Note: You might have to run the code several times to see the data corruption.  Use the script provided:
    ./run_sharing_data_B
'''

print("This example is not thread safe if you use PyPy, but CPython never goes wrong (apparently)")

import threading
COUNT = 10000000
counter = 0

def increment_counter():
    global counter
    for _ in range(COUNT):
        counter += 1

# Create two threads to increment the counter simultaneously
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# Print the final value of the counter
print(f"Final counter value:    {counter}")
print(f"Expected counter value: {2 * COUNT}")

import dis
dis.dis(increment_counter, adaptive=True)