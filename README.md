# accuknox_django_trainee
This is a repository containing the responses of the technical questions for Django Trainee position at AccuKnox

## Question 1
By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

### Answer 1
Django signals are synchronous by default. Later versions of Django let you use asynchronous behavior but that is not the default.

## Question 2
Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

### Answer 2

## Question 3
By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

### Answer 3

## Custom Classes in Python 
Description: You are tasked with creating a Rectangle class with the following requirements:

1. An instance of the Rectangle class requires length:int and width:int to be initialized.
2. We can iterate over an instance of the Rectangle class 
3. When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

```{python}
class Rectangle:
    
    # initialize Rectangle with attributes length:int and width:int
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        # counter attribute will keep track of which attribute to select when iterating
        self.counter = 0
    
    # make Rectangle iteratable
    def __iter__(self):
        # reset attribute counter when an iteration process starts
        self.counter = 0
        return self
    
    # define 'next' as based on counter and depeding on its value, it will return different attributes
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return {'length': self.length}
        elif self.counter == 1:
            self.counter += 1
            return {'width': self.width}
        else:
            # indicate that the iterator reached its end
            raise StopIteration
'''
Example usage:

rectangle = Rectangle(1, 2)

for a_dimension in rectangle:
    print(a_dimension)
    
if you are in the directory of the program you can run 'python3 rectangle.py' to get as output:
{'length': 1}
{'width': 2}
'''
```

## Considerations
All answer text files (question_1.txt, question_2.txt, and question_3.txt) are inside this repository, along with a Python file 'rectangle.py' that contains the Rectangle class and an example of its usage.
