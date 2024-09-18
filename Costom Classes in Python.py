class Rectangle:
    def __init__(self, length: int, width: int):
        # Initialize length and width
        self.length = length
        self.width = width
        # Keep track of iteration state
        self._index = 0
    
    def __iter__(self):
        # Return the iterable (in this case, the instance itself)
        self._index = 0  # Reset the index for iteration
        return self
    
    def __next__(self):
        # Return length first, then width during iteration
        if self._index == 0:
            self._index += 1
            return {'length': self.length}
        elif self._index == 1:
            self._index += 1
            return {'width': self.width}
        else:
            # Stop iteration after returning both length and width
            raise StopIteration

# Example usage:
rect = Rectangle(10, 20)

for dimension in rect:
    print(dimension)
