"""
Exercise: Advanced Student Grade Management with Decorators

Task: Enhance the student grade management system using decorators to add the following functionality:

1. Create a decorator called `log_method_call` that logs when any method is called on the Student class,
    printing the method name and timestamp.

2. Create a decorator called `validate_grade` that ensures grades added are between 0 and 100.
    If not, it should raise a ValueError.

3. Create a decorator called `cache_result` that caches the result of the average_grade calculation
    and only recalculates when new grades are added.

Example template:

def log_method_call(func):
     # Your code here
     pass

def validate_grade(func):
     # Your code here
     pass

def cache_result(func):
     # Your code here
     pass

class Student:
     def __init__(self, student_id, name):
          self.student_id = student_id
          self.name = name
          self.grades = []
          self._average_cache = None

     @log_method_call
     @validate_grade
     def add_grade(self, grade):
          self.grades.append(grade)
          self._average_cache = None

     @log_method_call
     @cache_result
     def get_average_grade(self):
          if not self.grades:
                return 0
          return sum(self.grades) / len(self.grades)

Test your implementation with:
- Add grades and observe the logging
- Try to add invalid grades
- Check if average_grade caching works correctly
"""

# Expected example usage:
# student = Student("12345", "John Doe")
# student.add_grade(85)  # Should log the call
# student.add_grade(150) # Should raise ValueError
# print(student.get_average_grade())  # Should use cached value on second call