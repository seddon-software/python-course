#         {key:value, key:value, key:value ...}
salary = {
          'jim'  : 30000,
          'sue'  : 28000,
          'peter': 41000,
          'zoe'  : 51000,
          'kwazi': 500000
         }


name = "peter"
salary[name] = 33333
salary['peter'] = 22222
salary['george'] = 22222
print(f"{name}'s salary is {salary[name]}")
print(salary)
