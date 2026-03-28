from task_9_checks import Checks


class Rectangle(Checks):
    def __init__(self, width: float, height: float, loc: str) -> None:
        super().__init__(loc)
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Math(Checks):
    def __init__(self, a: float, b: float, loc: str) -> None:
        super().__init__(loc)
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


class SidebarButton(Checks):
    def __init__(self, text: str, loc: str = "", button_type: str = "Кнопка") -> None:
        super().__init__(loc)
        self.text = text
        self.button_type = button_type

    def click(self) -> str:
        return f"Клик по кнопке {self.text}"


class Car(Checks):
    def __init__(self, color: str, car_type: str, year: int, loc: str) -> None:
        super().__init__(loc)
        self.color = color
        self.car_type = car_type
        self.year = year

    def start(self) -> None:
        print("Автомобиль заведен")

    def stop(self) -> None:
        print("Автомобиль заглушен")

    def set_year(self, year: int) -> None:
        self.year = year

    def set_type(self, car_type: str) -> None:
        self.car_type = car_type

    def set_color(self, color: str) -> None:
        self.color = color


rect = Rectangle(5, 10, "Прямоугольник")
math_obj = Math(20, 5, "Математика")
button = SidebarButton("Text Box", "Кнопка Text Box")
car = Car("Черный", "Седан", 2022, "Автомобиль")

print(rect.check_text())
print(math_obj.check_text())
print(button.check_text())
print(car.check_text())
