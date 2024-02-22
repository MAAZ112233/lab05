class Shape:
    def __init__(self, color):
        self.color = color

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.__width = width
        self.__height = height

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.__radius = radius
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius
class Rectangle(Shape):
    # ... (previous code)

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)

class Circle(Shape):
    # ... (previous code)

    def calculate_area(self):
        import math
        return math.pi * (self.__radius ** 2)

    def calculate_perimeter(self):
        import math
        return 2 * math.pi * self.__radius
class DataProcessor:
    def __init__(self):
        pass
class DataProcessor:
    # ... (previous code)

    def demonstrate_operations(self):
        # Example methods for operating on data structures
        my_list = [3, 1, 4, 1, 5, 9]
        my_list.sort()
        
        my_tuple = (1, 2, 3)
        
        my_dict = {'a': 1, 'b': 2}
        my_dict['c'] = 3
        del my_dict['a']
        
        my_set = {1, 2, 3}
# Testing the functionality
rectangle = Rectangle("red", 5, 4)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

circle = Circle("blue", 3)
print(circle.calculate_area())
print(circle.calculate_perimeter())

data_processor = DataProcessor()
data_processor.demonstrate_operations()
# git add shapes.py data_structures.py
# git commit -m "Implemented Rectangle and Circle classes with inheritance and encapsulation. Added DataProcessor class with data structure methods."
# git push origin master
  