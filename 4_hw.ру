class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Math:
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def addition(self, a: float, b: float) -> None:
        print(a + b)

    def multiplication(self, a: float, b: float) -> None:
        print(a * b)

    def division(self, a: float, b: float) -> None:
        if b == 0:
            print("Деление на ноль невозможно")
        else:
            print(a / b)

    def subtraction(self, a: float, b: float) -> None:
        print(a - b)


class SidebarButton:
    def __init__(self, text: str, button_type: str = "Кнопка", locator: str = "") -> None:
        self.text = text
        self.button_type = button_type
        self.locator = locator

    def click(self) -> str:
        return f"Клик по кнопке {self.text}"


# 1. Прямоугольники
rect_1 = Rectangle(5, 10)
rect_2 = Rectangle(7, 3)
rect_3 = Rectangle(4.5, 8)

for index, rect in enumerate([rect_1, rect_2, rect_3], start=1):
    print(f"Прямоугольник {index}")
    print(f"Площадь: {rect.area()}")
    print(f"Периметр: {rect.perimeter()}")
    print("-" * 30)


# 2. Math
math_obj = Math(20, 5)
print("Сложение:")
math_obj.addition(20, 5)
print("Умножение:")
math_obj.multiplication(20, 5)
print("Деление:")
math_obj.division(20, 5)
print("Вычитание:")
math_obj.subtraction(20, 5)
print("-" * 30)


# 3. Кнопки сайдбара DemoQA
button_1 = SidebarButton("Text Box")
button_2 = SidebarButton("Check Box")
button_3 = SidebarButton("Radio Button")
button_4 = SidebarButton("Web Tables")
button_5 = SidebarButton("Buttons")
button_6 = SidebarButton("Links")
button_7 = SidebarButton("Broken Links - Images")
button_8 = SidebarButton("Upload and Download")
button_9 = SidebarButton("Dynamic Properties")

buttons = [
    button_1,
    button_2,
    button_3,
    button_4,
    button_5,
    button_6,
    button_7,
    button_8,
    button_9,
]

for button in buttons:
    print(f"Текст кнопки: {button.text}")
    print(button.click())
    print("-" * 30)
