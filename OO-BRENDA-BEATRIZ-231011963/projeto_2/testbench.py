import turtle
from pyfunctions.functions import userSelection, ShapePoint, ShapeLine, ShapeSquare, ShapeRectangle, ShapeCircle, ShapeTriangle, ShapeHexagon, ShapeStar

registry_list = []

def draw_shapes():
    turtle.clearscreen()
    turtle.speed(0)  # Máxima velocidade de desenho
    for shape in registry_list:
        shape.draw()
    turtle.done()

def show_shape(shape):
    turtle.clearscreen()
    turtle.speed(0)  # Máxima velocidade de desenho
    shape.draw()
    turtle.done()

def visualize_drawing(shape):
    turtle.clearscreen()
    turtle.speed(1)  # Velocidade lenta para visualizar o desenho em tempo real
    shape.draw()
    turtle.done()

def exibir_menu():
    print("=== MENU ===")
    print("1. Cadastrar Ponto")
    print("2. Cadastrar Linha")
    print("3. Cadastrar Quadrado")
    print("4. Cadastrar Retângulo")
    print("5. Cadastrar Círculo")
    print("6. Cadastrar Triângulo")
    print("7. Cadastrar Hexágono")
    print("8. Cadastrar Estrela")
    print("9. Listar Formas Geométricas")
    print("10. Visualizar Forma Geométrica em Tempo Real")
    print("0. Sair")

i = 0
while True:
    exibir_menu()
    user = userSelection()
    
    if user.mode == 1:
        registry_list.append(ShapePoint())
        i += 1
        input('\nForma registrada! Pressione Enter para voltar: ')
    
    elif user.mode == 2:
        registry_list.append(ShapeLine())
        i += 1
        input('\nForma registrada! Pressione Enter para voltar: ')
    
    elif user.mode == 3:
        registry_list.append(ShapeSquare())
        i += 1
        input('\nForma registrada! Pressione Enter para voltar: ')
    
    elif user.mode == 4:
        registry_list.append(ShapeRectangle())
        i += 1
        input('\nForma registrada! Pressione Enter para voltar: ')
    
    elif user.mode == 5:
        registry_list.append(ShapeCircle())
        i += 1
        input('\nForma registrada! Pressione Enter para voltar: ')
    
    elif user.mode == 6:
        registry_list.append(ShapeTriangle())
        i += 1
        input('\nForma registrada! Pressione Enter para voltar: ')
    
    elif user.mode == 7:
        registry_list.append(ShapeHexagon())
        i += 1
        input('\nForma registrada! Pressione Enter para voltar: ')
    
    elif user.mode == 8:
        registry_list.append(ShapeStar())
        i += 1
        input('\nForma registrada! Pressione Enter para voltar: ')
    
    elif user.mode == 9:
        if i == 0:
            input('Nenhuma forma geométrica registrada. Pressione Enter para voltar: ')
        
        if i > 0:
            print('\nFormas geométricas registradas:')
            for x in range(0, i):
                print(f'{x}. {registry_list[x].shapeType}')
                
            userRegistry = input('\nInsira o número da forma geométrica a ser verificada: ')
            try:
                userRegistry = int(userRegistry)
            except ValueError:
                input('ERRO: Número selecionado é inválido. Pressione Enter para voltar: ')
                continue
            
            if userRegistry <= i-1:
                print(f'- Forma geométrica: {registry_list[userRegistry].shapeType}')
                print(registry_list[userRegistry].string)
                input('Pressione Enter para visualizar a forma: ')
                show_shape(registry_list[userRegistry])
            else:
                input('ERRO: Número selecionado é inválido. Pressione Enter para voltar: ')
    
    elif user.mode == 10:
        if i == 0:
            input('Nenhuma forma geométrica registrada. Pressione Enter para voltar: ')
        
        if i > 0:
            print('\nFormas geométricas registradas:')
            for x in range(0, i):
                print(f'{x}. {registry_list[x].shapeType}')
                
            userRegistry = input('\nInsira o número da forma geométrica a ser visualizada: ')
            try:
                userRegistry = int(userRegistry)
            except ValueError:
                input('ERRO: Número selecionado é inválido. Pressione Enter para voltar: ')
                continue
            
            if userRegistry <= i-1:
                print(f'- Forma geométrica: {registry_list[userRegistry].shapeType}')
                print(registry_list[userRegistry].string)
                input('Pressione Enter para visualizar a forma em tempo real: ')
                visualize_drawing(registry_list[userRegistry])
            else:
                input('ERRO: Número selecionado é inválido. Pressione Enter para voltar: ')
    
    elif user.mode == 0:
        draw_shapes()
        break
    
    else:
        input('Escolha inválida. Pressione Enter para voltar: ')
