import tkinter as tk
from tkinter import ttk
from system import ManagementSystem
from clients_tab import ClientsTab
from services_tab import ServicesTab
from reservations_tab import ReservationsTab


class SoftwareFJApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Software FJ")
        self.geometry("1100x700")
        self.minsize(1000, 650)

        self.system = ManagementSystem()

        titulo = tk.Label(
            self,
            text="Software FJ",
            font=("Segoe UI", 22, "bold")
        )

        titulo.pack(pady=10)

        notebook = ttk.Notebook(self)

        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.clients = ClientsTab(notebook, self.system)
        self.services = ServicesTab(notebook, self.system)
        self.reservations = ReservationsTab(notebook, self.system)

        notebook.add(self.clients, text="clients")
        notebook.add(self.services, text="services")
        notebook.add(self.reservations, text="reservation")