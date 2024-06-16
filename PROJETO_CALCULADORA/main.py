import PySimpleGUI as sg
import math

sg.theme('Black')

# Variáveis para realização das operações
salvanumero1 = float(-1000)
salvanumero2 = float(-1000)

# flags para determinação de operação que será feita:
numero1preenchido = False
flag_soma = False
flag_subtracao = False
flag_multiplicacao = False
flag_divisao = False

resultado = 0
numerosprimeirotrio = '1 2 3'.split(' ')
numerosegundotrio = '4 5 6'.split(' ')
numerosterceirotrio = '7 8 9'.split(' ')
numerosquartotrio = '0'.split(' ')
layout = [
    [sg.Input(key='-IN-', size=22, font='Arial', do_not_clear=False)],
    [sg.Push()] + [sg.Button(word, size=6, font='Arial') for word in numerosprimeirotrio],
    [sg.Push()] + [sg.Button(word, size=6, font='Arial') for word in numerosegundotrio],
    [sg.Push()] + [sg.Button(word, size=6, font='Arial') for word in numerosterceirotrio],
    [sg.Push()] + [sg.Button(word, size=22, font='Arial') for word in numerosquartotrio],

    [
        sg.Button('+', font='Arial', size=6, key='soma'),
        sg.Button('-', font='Arial', size=6, key='subtração'),
        sg.Button('X', font='Arial', size=6, key='multiplicação'),
    ],

    [
        sg.Button('÷', font='Arial', size=6, key='divisão'),
        sg.Button('²', font='Arial', size=6, key='quadrado'),
        sg.Button('³', font='Arial', size=6, key='cubo')
    ],

    [
        sg.Button('%', font='Arial', size=6, key='porcentagem'),
        sg.Button('√', font='Arial', size=6, key='raiz_quadrada'),
        sg.Button('∛', font='Arial', size=6, key='raiz_cubica')
    ],

    [
        sg.Button('C', font='Arial', size=6, key='apaga'),
        sg.Button('.', font='Arial', size=6, key='.'),
        sg.Button('=', font='Arial', size=6, button_color='Red', key='resultado')
    ]
]
window = sg.Window("Calculadora", layout, element_justification='c', finalize=True)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event in numerosprimeirotrio:
        text = values['-IN-'].strip()
        text = text + ('' if text else '') + event
        window['-IN-'].update(text)

        if numero1preenchido == False:
            salvanumero1 = float(text)
        else:
            salvanumero2 = float(text)

    elif event in numerosegundotrio:
        text = values['-IN-'].strip()
        text = text + ('' if text else '') + event
        window['-IN-'].update(text)

        if numero1preenchido == False:
            salvanumero1 = float(text)
        else:
            salvanumero2 = float(text)

    elif event in numerosterceirotrio:
        text = values['-IN-'].strip()
        text = text + ('' if text else '') + event
        window['-IN-'].update(text)

        if numero1preenchido == False:
            salvanumero1 = float(text)
        else:
            salvanumero2 = float(text)

    elif event in numerosquartotrio:
        text = values['-IN-'].strip()
        text = text + ('' if text else '') + event
        window['-IN-'].update(text)

        if numero1preenchido == False:
            salvanumero1 = float(text)
        else:
            salvanumero2 = float(text)

    elif event == 'apaga':
        window['-IN-'].update('')
        salvanumero1 = -1000
        salvanumero2 = -1000
        numero1preenchido = False
        flag_soma = False

    # Operação de soma:
    elif event == 'soma':
        window['-IN-'].update('')
        numero1preenchido = True
        flag_soma = True

    elif event == 'resultado' and flag_soma == True:
        resultado = salvanumero1 + salvanumero2
        resultado = str(resultado)
        text = text + ('' if text else '') + resultado
        window['-IN-'].update(resultado)
        resultado = float(resultado)
        salvanumero1 = resultado
        salvanumero2 = -1000
        flag_soma = False


    # Operação de Subtração:
    elif event == 'subtração':
        window['-IN-'].update('')
        numero1preenchido = True
        flag_subtracao = True

    elif event == 'resultado' and flag_subtracao == True:
        resultado = salvanumero1 - salvanumero2
        resultado = str(resultado)
        text = text + ('' if text else '') + resultado
        window['-IN-'].update(resultado)
        resultado = float(resultado)
        salvanumero1 = resultado
        salvanumero2 = -1000
        flag_subtracao = False

    # Operação de Multiplicação:
    elif event == 'multiplicação':
        window['-IN-'].update('')
        numero1preenchido = True
        flag_multiplicacao = True

    elif event == 'resultado' and flag_multiplicacao == True:
        resultado = salvanumero1 * salvanumero2
        resultado = str(resultado)
        text = text + ('' if text else '') + resultado
        window['-IN-'].update(resultado)
        resultado = float(resultado)
        salvanumero1 = resultado
        salvanumero2 = -1000
        flag_multiplicacao = False

    # Operação de Divisão:
    elif event == 'divisão':
        window['-IN-'].update('')
        numero1preenchido = True
        flag_divisao = True

    elif event == 'resultado' and flag_divisao == True:
        resultado = salvanumero1 / salvanumero2
        resultado = str(resultado)
        text = text + ('' if text else '') + resultado
        window['-IN-'].update(resultado)
        resultado = float(resultado)
        salvanumero1 = resultado
        salvanumero2 = float(-1000)
        flag_divisao = False

    # Operação de elevar número ao quadrado:
    elif event == 'quadrado':
        window['-IN-'].update('')
        resultado = salvanumero1 * salvanumero1
        resultado = str(resultado)
        text = text + ('' if text else '') + resultado
        window['-IN-'].update(resultado)
        resultado = float(resultado)
        salvanumero1 = resultado
        salvanumero2 = float(-1000)

    #Operação de elevar número ao cubo:
    elif event == 'cubo':
        window['-IN-'].update('')
        resultado = salvanumero1 * salvanumero1 * salvanumero1
        resultado = str(resultado)
        text = text + ('' if text else '') + resultado
        window['-IN-'].update(resultado)
        resultado = float(resultado)
        salvanumero1 = resultado
        salvanumero2 = float(-1000)

    #Operação de porcentagem:
    elif event == 'porcentagem':
        window['-IN-'].update('')
        resultado = salvanumero1 / 100
        resultado = str(resultado)
        text = text + ('' if text else '') + resultado
        window['-IN-'].update(resultado)
        resultado = float(resultado)
        salvanumero1 = resultado
        salvanumero2 = float(-1000)

    #Operação de raiz quadrada:
    elif event == 'raiz_quadrada':
        window['-IN-'].update('')
        resultado = math.sqrt(salvanumero1)
        resultado = str(resultado)
        text = text + ('' if text else '') + resultado
        window['-IN-'].update(resultado)
        resultado = float(resultado)
        salvanumero1 = resultado
        salvanumero2 = float(-1000)

    #Operação de raiz cúbica:
    elif event == 'raiz_cubica':
        window['-IN-'].update('')
        resultado = math.cbrt(salvanumero1)
        resultado = str(resultado)
        text = text + ('' if text else '') + resultado
        window['-IN-'].update(resultado)
        resultado = float(resultado)
        salvanumero1 = resultado
        salvanumero2 = float(-1000)

    #Vírgula:
    elif event == '.':
        text = values['-IN-'].strip()
        text = text + ('' if text else '') + event
        window['-IN-'].update(text)

        if numero1preenchido == False:
            salvanumero1 = float(text)
        else:
            salvanumero2 = float(text)


window.close()
