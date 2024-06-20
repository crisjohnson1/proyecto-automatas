import tkinter as tk
from tkinter import messagebox

class AutomataDePila:
    def __init__(self):
        self.stack = []
        self.prices = []
        self.price_list = {
            "caldo de huevo": 10000,
            "carne asada": 18000,
            "arepa de queso": 5000,
            "arepa de maíz": 3000,
            "arepa sin sal": 2000,
            "chocolate": 3000,
            "jugo de naranja": 2000,
            "con fruta": 1000,
            "sin fruta": 0.0,
            "calentado": 12000,
            "chorizo": 8000,
            "envuelto": 4000,
            "carne": 15000,
            "pan": 1000,
            "papa cocida": 1200,
            "cayeye": 7000,
            "bollo": 5000,
            "chicharrón": 12000,
            "queso costeño": 8000,
            "jugo de corozo": 4000,
            "café con leche": 2000,
            "wafle": 3000,
            "sin wafle": 0,
            "milo caliente": 2000,
            "sandwich de jamón": 5500,
            "sandwich de queso": 7000
        }
        self.create_interface()

    def create_interface(self):
        self.root = tk.Tk()
        self.root.title("Desayuno Sorpresa")

        # Labels
        self.label = tk.Label(self.root, text="Selecciona tu tipo de desayuno:")
        self.label.pack()

        # Dropdown menu for type of breakfast
        self.breakfast_var = tk.StringVar(self.root)
        self.breakfast_var.set("Santandereana")  # default value

        self.breakfast_menu = tk.OptionMenu(self.root, self.breakfast_var, "Santandereana", "Antioqueña", "Boyacense", "Costeña", "Dulce")
        self.breakfast_menu.pack()

        # Button to proceed
        self.start_button = tk.Button(self.root, text="Iniciar", command=self.seleccionar_tipo_comida)
        self.start_button.pack()

        self.root.mainloop()

    def seleccionar_tipo_comida(self):
        opcion = self.breakfast_var.get()
        if opcion == "Santandereana":
            self.santandereana()
        elif opcion == "Antioqueña":
            self.antioquena()
        elif opcion == "Boyacense":
            self.boyacense()
        elif opcion == "Costeña":
            self.costena()
        elif opcion == "Dulce":
            self.desayuno_dulce()

    def santandereana(self):
        self.show_options(["Caldo de huevo", "Carne asada"], self.arepa)

    def antioquena(self):
        self.show_options(["Calentado", "Chorizo"], self.arepa)

    def boyacense(self):
        self.show_options(["Envuelto", "Carne"], lambda: self.show_options(["Pan", "Papa cocida"], self.bebida))

    def costena(self):
        self.show_options(["Cayeye", "Bollo"], lambda: self.show_options(["Chicharrón", "Queso costeño"], self.bebida))

    def desayuno_dulce(self):
        self.show_options(["Wafle", "Sin wafle"], lambda: self.show_options(["Milo caliente", "Jugo de naranja"], self.sandwich))

    def arepa(self):
        self.show_options(["Arepa de queso", "Arepa de maíz", "No"], self.bebida)

    def bebida(self):
        self.show_options(["Chocolate", "Jugo de naranja"], self.fruta)

    def fruta(self):
        self.show_options(["Con fruta", "Sin fruta"], self.imprimir_desayuno)

    def sandwich(self):
        self.show_options(["Sandwich de jamón", "Sandwich de queso"], self.imprimir_desayuno)

    def show_options(self, options, next_step):
        self.option_var = tk.StringVar(self.root)
        self.option_var.set(options[0])

        self.option_menu = tk.OptionMenu(self.root, self.option_var, *options)
        self.option_menu.pack()

        self.next_button = tk.Button(self.root, text="Siguiente", command=lambda: self.handle_selection(next_step))
        self.next_button.pack()

    def handle_selection(self, next_step):
        item = self.option_var.get().lower()
        self.agregar_a_pila(item)
        self.option_menu.pack_forget()
        self.next_button.pack_forget()
        next_step()

    def agregar_a_pila(self, item):
        self.stack.append(item)
        precio = self.price_list.get(item, 0.0)
        self.prices.append(precio)
        messagebox.showinfo("Añadido", f"{item.capitalize()} añadido a tu desayuno. Precio: ${precio:.2f}")

    def imprimir_desayuno(self):
        total_precio = sum(self.prices)
        desayuno = "\n".join([f"{item.capitalize()}: ${precio:.2f}" for item, precio in zip(self.stack, self.prices)])
        messagebox.showinfo("Desayuno Completo", f"Tu desayuno consiste en:\n{desayuno}\n\nPrecio total del desayuno: ${total_precio:.2f}")

        self.stack.clear()
        self.prices.clear()
        self.root.destroy()

# Ejecución del autómata con interfaz gráfica
automata = AutomataDePila()
automata.iniciar()
automata.imprimir_desayuno()

