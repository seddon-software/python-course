import requests

base = "http://localhost:8001/customer/"
john =   {'age': '27', 'city': 'London'}
susan =  {'age': '31', 'city': 'Glasgow'}
istvan = {'age': '44', 'city': 'Paris'}
joel =   {'age': '21', 'city': 'Milan'}
leo =    {'age': '25', 'city': 'New York'}
requests.post(base + "john",   params = john)
requests.post(base + "susan",  params = susan)
requests.post(base + "istvan", params = istvan)
requests.post(base + "joel",   params = joel)
requests.post(base + "leo",    params = leo)

r = requests.get(base)
print(r.json())

r = requests.delete(base + "jim")
print(r.json())

r = requests.delete(base + "istvan")
print(r.json())

r = requests.get(base + "susan")
print(r.json())

# this should generate an error ("susan" exists)
r = requests.post(base + "susan")
print(r.json())

# but update should work
susan =  {'age': '32', 'city': 'Edinburgh'}
r = requests.put(base + "susan",  params = susan)
print(r.json())

r = requests.get(base + "susan")
print(r.json())

# this should generate an error
r = requests.get(base + "/xyz")
print(r.json())

1