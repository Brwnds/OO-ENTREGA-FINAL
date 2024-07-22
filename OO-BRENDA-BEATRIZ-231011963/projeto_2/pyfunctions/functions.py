import turtle

class Shape:
    def __init__(self):
        self.shapeType = "Forma Geométrica"
        self.string = ""

    def draw(self):
        raise NotImplementedError("Método 'draw' não implementado")

class ShapePoint(Shape):
    def __init__(self):
        super().__init__()
        self.shapeType = "Ponto"
        self.x = float(input('Digite a coordenada x: '))
        self.y = float(input('Digite a coordenada y: '))
        self.string = f"Ponto({self.x}, {self.y})"

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.dot(5, "black")

class ShapeLine(Shape):
    def __init__(self):
        super().__init__()
        self.shapeType = "Linha"
        self.x1 = float(input('Digite a coordenada x do Ponto A: '))
        self.y1 = float(input('Digite a coordenada y do Ponto A: '))
        self.x2 = float(input('Digite a coordenada x do Ponto B: '))
        self.y2 = float(input('Digite a coordenada y do Ponto B: '))
        self.string = f"Linha de ({self.x1}, {self.y1}) a ({self.x2}, {self.y2})"

    def draw(self):
        turtle.penup()
        turtle.goto(self.x1, self.y1)
        turtle.pendown()
        turtle.goto(self.x2, self.y2)

class ShapeSquare(Shape):
    def __init__(self):
        super().__init__()
        self.shapeType = "Quadrado"
        self.x1 = float(input('Digite a coordenada x do Ponto A: '))
        self.y1 = float(input('Digite a coordenada y do Ponto A: '))
        self.side = float(input('Digite o comprimento do lado: '))
        self.string = f"Quadrado com vértice em ({self.x1}, {self.y1}) e lado {self.side}"

    def draw(self):
        turtle.penup()
        turtle.goto(self.x1, self.y1)
        turtle.pendown()
        for _ in range(4):
            turtle.forward(self.side)
            turtle.right(90)

class ShapeRectangle(Shape):
    def __init__(self):
        super().__init__()
        self.shapeType = "Retângulo"
        self.x1 = float(input('Digite a coordenada x do Ponto A: '))
        self.y1 = float(input('Digite a coordenada y do Ponto A: '))
        self.x2 = float(input('Digite a coordenada x do Ponto B: '))
        self.y2 = float(input('Digite a coordenada y do Ponto B: '))
        self.string = f"Retângulo com vértices em ({self.x1}, {self.y1}) e ({self.x2}, {self.y2})"

    def draw(self):
        turtle.penup()
        turtle.goto(self.x1, self.y1)
        turtle.pendown()
        turtle.goto(self.x1, self.y2)
        turtle.goto(self.x2, self.y2)
        turtle.goto(self.x2, self.y1)
        turtle.goto(self.x1, self.y1)

class ShapeCircle(Shape):
    def __init__(self):
        super().__init__()
        self.shapeType = "Círculo"
        self.x = float(input('Digite a coordenada x do Centro do Círculo: '))
        self.y = float(input('Digite a coordenada y do Centro do Círculo: '))
        self.radius = float(input('Digite o raio do Círculo: '))
        self.string = f"Círculo com centro em ({self.x}, {self.y}) e raio {self.radius}"

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y - self.radius)
        turtle.pendown()
        turtle.circle(self.radius)

class ShapeTriangle(Shape):
    def __init__(self):
        super().__init__()
        self.shapeType = "Triângulo"
        self.x1 = float(input('Digite a coordenada x do Ponto A: '))
        self.y1 = float(input('Digite a coordenada y do Ponto A: '))
        self.x2 = float(input('Digite a coordenada x do Ponto B: '))
        self.y2 = float(input('Digite a coordenada y do Ponto B: '))
        self.x3 = float(input('Digite a coordenada x do Ponto C: '))
        self.y3 = float(input('Digite a coordenada y do Ponto C: '))
        self.string = f"Triângulo com vértices em ({self.x1}, {self.y1}), ({self.x2}, {self.y2}), ({self.x3}, {self.y3})"

    def draw(self):
        turtle.penup()
        turtle.goto(self.x1, self.y1)
        turtle.pendown()
        turtle.goto(self.x2, self.y2)
        turtle.goto(self.x3, self.y3)
        turtle.goto(self.x1, self.y1)

class ShapeHexagon(Shape):
    def __init__(self):
        super().__init__()
        self.shapeType = "Hexágono"
        self.vertices = []
        for i in range(6):
            x = float(input(f'Digite a coordenada x do Vértice {i + 1}: '))
            y = float(input(f'Digite a coordenada y do Vértice {i + 1}: '))
            self.vertices.append((x, y))
        self.string = f"Hexágono com vértices {self.vertices}"

    def draw(self):
        turtle.penup()
        turtle.goto(self.vertices[0])
        turtle.pendown()
        for vertex in self.vertices[1:]:
            turtle.goto(vertex)
        turtle.goto(self.vertices[0])

class ShapeStar(Shape):
    def __init__(self):
        super().__init__()
        self.shapeType = "Estrela"
        self.x = float(input('Digite a coordenada x do Centro da Estrela: '))
        self.y = float(input('Digite a coordenada y do Centro da Estrela: '))
        self.radius = float(input('Digite o raio da Estrela: '))
        self.points = []
        for i in range(5):
            px = float(input(f'Digite a coordenada x do Ponto {i + 1}: '))
            py = float(input(f'Digite a coordenada y do Ponto {i + 1}: '))
            self.points.append((px, py))
        self.string = f"Estrela com centro em ({self.x}, {self.y}), raio {self.radius}, e pontos {self.points}"

    def draw(self):
        turtle.penup()
        turtle.goto(self.points[0])
        turtle.pendown()
        for point in self.points[1:]:
            turtle.goto(point)
        turtle.goto(self.points[0])

def userSelection():
    print("Escolha uma opção:")
    print("1. Cadastrar Ponto")
    print("2. Cadastrar Linha")
    print("3. Cadastrar Quadrado")
    print("4. Cadastrar Retângulo")
    print("5. Cadastrar Círculo")
    print("6. Cadastrar Triângulo")
    print("7. Cadastrar Hexágono")
    print("8. Cadastrar Estrela")
    print("9. Listar Formas Geométricas")
    print("10. Visualizar Forma Geométrica")
    print("0. Sair")

    choice = input("Digite o número da opção desejada: ")

    try:
        choice = int(choice)
    except ValueError:
        choice = -1

    class UserSelection:
        def __init__(self):
            self.mode = choice
    
    return UserSelection()
