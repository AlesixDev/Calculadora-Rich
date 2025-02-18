import os
from rich import print
from rich.prompt import Prompt, IntPrompt, FloatPrompt
from rich.markdown import Markdown
from rich.panel import Panel
import time
import sys

MARKDOWN = """
## *Calculadora basica en Python, con las siguientes operaciones:*

---

- 1. – Suma
- 2. – Resta
- 3. – Multiplicacion
- 4. – Division
- 5. – Salir
---
## Made with ❤️ by @AlesixDev and @Devkitty21
"""

def salir():
    imp = Prompt.ask('         [gold3]🔑 ¿Quieres salir? (Si o No)').lower()
    if imp == 'si' or imp == 's':
        print('         [red]🧨 Saliendo de la calculadora...')
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()

    elif imp == 'no' or imp == 'n':
        print('         [green]🧨 Volviendo al menu en 3 segundos...')
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print('         [red]🔖 La opcion que has introducido no es correcta...')
        time.sleep(1)
        salir()        

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Panel.fit(Markdown(MARKDOWN), title="🧮 CALCULADORA 🧮", border_style="gold3", width=70))
    opcion = IntPrompt.ask("           [gold3]:rocket: Introduce la operacion que deseas realizar")

    if opcion == 1:
        valor1 = FloatPrompt.ask('           [gold3]🪐 Introduce el valor 1: ')
        valor2 = FloatPrompt.ask('           [gold3]🪐 Introduce el valor 2: ')

        os.system('cls' if os.name == 'nt' else 'clear')
        MARKDOWNRESULT = f"""## *Resultado de la operacion:* {valor1 + valor2:.2f}"""
        print(Panel.fit(Markdown(MARKDOWNRESULT), title="🧮 RESULTADO 🧮", border_style="gold3", width=50))

        salir()

    elif opcion == 2:
        valor1 = FloatPrompt.ask('           [gold3]🪐 Introduce el valor 1: ')
        valor2 = FloatPrompt.ask('           [gold3]🪐 Introduce el valor 2: ')

        os.system('cls' if os.name == 'nt' else 'clear')
        MARKDOWNRESULT = f"""## *Resultado de la operacion:* {valor1 - valor2:.2f}"""
        print(Panel.fit(Markdown(MARKDOWNRESULT), title="🧮 RESULTADO 🧮", border_style="gold3", width=50))     

        salir()

    elif opcion == 3:
        valor1 = FloatPrompt.ask('           [gold3]🪐 Introduce el valor 1: ')
        valor2 = FloatPrompt.ask('           [gold3]🪐 Introduce el valor 2: ')

        os.system('cls' if os.name == 'nt' else 'clear')
        MARKDOWNRESULT = f"""## *Resultado de la operacion:* {valor1 * valor2:.2f}"""
        print(Panel.fit(Markdown(MARKDOWNRESULT), title="🧮 RESULTADO 🧮", border_style="gold3", width=50))

        salir()

    elif opcion == 4:
        valor1 = FloatPrompt.ask('           [gold3]🪐 Introduce el valor 1: ')
        valor2 = FloatPrompt.ask('           [gold3]🪐 Introduce el valor 2: ')

        os.system('cls' if os.name == 'nt' else 'clear')
        MARKDOWNRESULT = f"""## *Resultado de la operacion:* {valor1 / valor2:.2f}"""
        print(Panel.fit(Markdown(MARKDOWNRESULT), title="🧮 RESULTADO 🧮", border_style="gold3", width=50))

        salir()

    elif opcion == 5: 
        print(f'           [red]🧨 Saliendo de la calculadora...')
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()

    else:
        print(f'           [red]🔖 La operacion que has introducido no es correcta...')
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

