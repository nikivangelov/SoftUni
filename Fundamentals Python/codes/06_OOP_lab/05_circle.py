class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def calculate_circumference(self):
        return self.radius * 2 * Circle.__pi

    def calculate_area(self):
        return self.radius ** 2 * Circle.__pi

    def calculate_area_of_sector(self, angle):
        return (angle / 360) * Circle.__pi * self.radius ** 2


circle = Circle(10)
current_angle = 5
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(current_angle):.2f}")
