# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        area = self.width * self.height
        perimeter = 2 * self.width + 2 * self.height
        print(f'Width: {self.width} \nHeight: {self.height} \nArea: {area} \nPerimter: {perimeter}')
              
shape1 = Shape(5, 3)
shape1.print_info()