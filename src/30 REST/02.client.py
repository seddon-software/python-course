import requests

base = "http://localhost:8000/customer/"

# This information is now in the SQLLite DB:

# john =   {'age': '27', 'city': 'London'}
# susan =  {'age': '31', 'city': 'Glasgow'}
# istvan = {'age': '44', 'city': 'Paris'}
# joel =   {'age': '21', 'city': 'Milan'}
# leo =    {'age': '25', 'city': 'New York'}
# requests.post(base + "john",   params = john)
# requests.post(base + "susan",  params = susan)
# requests.post(base + "istvan", params = istvan)
# requests.post(base + "joel",   params = joel)
# requests.post(base + "leo",    params = leo)

r = requests.get(base + "john")
print(r.content.decode())

susan =  {'age': '34', 'city': 'Stirling'}
r = requests.put(base + "susan",  params = susan)

r = requests.get(base + "susan")
print(r.content.decode())

r = requests.post(base + "steven", params = {'age': 40, 'city': 'Birmingham'})
print(f"{r.status_code}: {r.content.decode()}")

r = requests.get(base + "steven")
print(r.content.decode())

r = requests.get(base)
print(r.content.decode())

r = requests.delete(base + "steven")
print(f"{r.status_code}: {r.content.decode()}")
