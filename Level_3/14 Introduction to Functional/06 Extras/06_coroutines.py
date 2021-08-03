# coroutines can use yield for inputs and outputs
# use next() for outputs
# use send() for inputs and outputs

def sentenceBuilder():     # a generator function
    print("\tjust starting")
    while True:
        print("\twaiting for send()")
        sentence,word = yield       # this blocks until a send
        print("\treturning from send")
        yield f"{sentence} {word}"  # this returns from send
        print("\tmoving to next yield")

# call the generator function to create a generator
g = sentenceBuilder()
print(f"sentenceBuilder is of type {type(sentenceBuilder)}")
print(f"g is of type {type(g)}")


sentence = ""

for n in "The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog":
    next(g)     # advance to the next yield
    sentence = g.send([sentence, n])    # send data to the generator and get result
    print(sentence)

