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