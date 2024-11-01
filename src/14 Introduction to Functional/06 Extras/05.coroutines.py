'''
Originally generators could only produce output, but PEP 342 (Python 2.5) enhanced generators such that they
can now also consume input.  When yield is used on the right hand side of an = it is an input yield; if there 
is no = then yield produces output.  You can send data to a generator with the "send()" builtin.

In this example we create a "sentenceBuilder()" generator.  We send words to the generator and it adds the input
to the current sentence and returns the current state of the sentence.

'''
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

for word in "The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog":
    next(g)     # advance to the next yield
    # send previous value of sentence and new word to the generator and get new sentence on return
    sentence = g.send([sentence, word])    
    print(sentence)

