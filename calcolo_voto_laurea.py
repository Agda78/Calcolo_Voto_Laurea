import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class GraduationScoreCalculator:
    def __init__(self):
        # Inizializzazione finestra
        self.root = tk.Tk()
        self.root.title("Calcolatore Voto Laurea - \"Federico II")
        self.root.geometry("700x700")

        # Colori personalizzati
        bg_color = '#1a1a2e'
        text_color = '#e0e0e0'
        accent_color = '#6a5acd'

        # Configurazione colori
        self.root.configure(background=bg_color)

        # Inizializzazione variabili
        self.is_m63 = tk.BooleanVar(value=False)
        self.media_ponderata_var = tk.StringVar()
        self.numero_lodi_9_var = tk.StringVar()
        self.numero_lodi_6_var = tk.StringVar()
        self.numero_lodi_12_var = tk.StringVar()
        self.anni_fuoricorso_var = tk.StringVar()
        self.voto_triennale = tk.StringVar()

        self.media_ponderata_110_var = tk.StringVar(value="0")
        self.bonus_lodi_var = tk.StringVar(value="0")
        self.bonus_anni_var = tk.StringVar(value="0")
        self.bonus_triennale = tk.StringVar(value="0")
        self.bonus_100 = tk.StringVar(value="0")
        self.voto_finale_var = tk.StringVar(value="0")

        # Creazione UI iniziale
        self.create_selection_ui(bg_color, text_color, accent_color)

    def create_selection_ui(self, bg_color, text_color, accent_color):
        # Interfaccia per la selezione del tipo di matricola
        selection_frame = tk.Frame(self.root, bg=bg_color)
        selection_frame.pack(fill='both', expand=True, padx=20, pady=20)

        label = tk.Label(
            selection_frame, 
            text="Seleziona il tipo di matricola", 
            font=('Arial', 20, 'bold'),
            bg=bg_color, 
            fg=accent_color
        )
        label.pack(pady=20)

        triennale_button = tk.Button(
            selection_frame, 
            text="Triennale (N46)", 
            command=lambda: self.setup_calculator(False), 
            font=('Arial', 16, 'bold'), 
            bg=accent_color, 
            fg='white'
        )
        triennale_button.pack(pady=10)

        magistrale_button = tk.Button(
            selection_frame, 
            text="Magistrale (M63)", 
            command=lambda: self.setup_calculator(True), 
            font=('Arial', 16, 'bold'), 
            bg=accent_color, 
            fg='white'
        )
        magistrale_button.pack(pady=10)

    def setup_calculator(self, is_m63):
        # Configurazione dell'interfaccia in base al tipo di matricola
        self.is_m63.set(is_m63)
        for widget in self.root.winfo_children():
            widget.destroy()

        self.create_calculator_ui()

    def create_calculator_ui(self):
        bg_color = '#1a1a2e'
        text_color = '#e0e0e0'
        accent_color = '#6a5acd'

        main_frame = tk.Frame(self.root, bg=bg_color)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        title = "Calcolatore Voto Laurea M63" if self.is_m63.get() else "Calcolatore Voto Laurea N46"
        title_label = tk.Label(
            main_frame, 
            text=title, 
            font=('Arial', 20, 'bold'),
            bg=bg_color, 
            fg=accent_color
        )
        title_label.pack(pady=20)

        if self.is_m63.get():
            warning_label = tk.Label(
                main_frame,
                text="⚠️ ATTENZIONE ⚠️: Ricorda che al punteggio va aggiunta la valutazione della commissione (0-5 punti)",
                font=('Arial', 14, 'bold'),
                bg=bg_color,
                fg='red',
                wraplength=600,
                justify="center"
            )
            warning_label.pack(pady=10)
        else:
            warning_label = tk.Label(
                main_frame,
                text="⚠️ ATTENZIONE ⚠️: Ricorda che al punteggio va aggiunta la valutazione della commissione (0-3 punti)",
                font=('Arial', 14, 'bold'),
                bg=bg_color,
                fg='red',
                wraplength=600,
                justify="center"
            )
            warning_label.pack(pady=10)
        
        input_fields = [
            ("Media ponderata su 30:", self.media_ponderata_var),
            ("Numero lodi 9 cfu:", self.numero_lodi_9_var),
            ("Numero lodi 6 cfu:", self.numero_lodi_6_var)
        ]

        if self.is_m63.get():
            input_fields.append(("Numero lodi 12 cfu:", self.numero_lodi_12_var))
            input_fields.append(("Voto triennale (110L = 111):", self.voto_triennale))
        else:
            input_fields.append(("Anni fuoricorso:", self.anni_fuoricorso_var))

        for label_text, var in input_fields:
            row_frame = tk.Frame(main_frame, bg=bg_color)
            row_frame.pack(fill='x', pady=5)

            label = tk.Label(
                row_frame, 
                text=label_text, 
                width=25, 
                anchor='w',
                bg=bg_color, 
                fg=text_color,
                font=('Arial', 16)
            )
            label.pack(side='left', padx=10)

            entry = tk.Entry(row_frame, textvariable=var, bg='#2c3e50', fg='white', font=('Arial', 14))
            entry.pack(side='left', expand=True, fill='x', padx=10)
            entry.bind('<KeyRelease>', self.calculate_score)

        output_fields = [
            ("Media ponderata su 110:", self.media_ponderata_110_var),
            ("Bonus Lodi:", self.bonus_lodi_var)
        ]

        if self.is_m63.get():
            output_fields.append(("Bonus Triennale:", self.bonus_triennale))
        else:
            output_fields.append(("Bonus Anni Svolti:", self.bonus_anni_var))
            output_fields.append(("Bonus > 100:", self.bonus_100))

        output_fields.append(("Voto finale:", self.voto_finale_var))

        for label_text, var in output_fields:
            row_frame = tk.Frame(main_frame, bg=bg_color)
            row_frame.pack(fill='x', pady=5)

            label = tk.Label(
                row_frame, 
                text=label_text, 
                width=25, 
                anchor='w',
                bg=bg_color, 
                fg=text_color,
                font=('Arial', 16)
            )
            label.pack(side='left', padx=10)

            value_label = tk.Label(row_frame, textvariable=var, bg=bg_color, fg=accent_color, font=('Arial', 16, 'bold'))
            value_label.pack(side='left', expand=True, fill='x', padx=10)

        back_button = tk.Button(
            main_frame,
            text="Torna alla Selezione",
            command=self.return_to_selection,
            font=('Arial', 16, 'bold'),
            bg=accent_color,
            fg='white'
        )
        back_button.pack(pady=20)

    def return_to_selection(self):
        # Resetta i campi di input
        self.media_ponderata_var.set("")
        self.numero_lodi_9_var.set("")
        self.numero_lodi_6_var.set("")
        self.numero_lodi_12_var.set("")
        self.anni_fuoricorso_var.set("")
        self.voto_triennale.set("")

        # Ritorna alla schermata di selezione
        for widget in self.root.winfo_children():
            widget.destroy()
        bg_color = '#1a1a2e'
        text_color = '#e0e0e0'
        accent_color = '#6a5acd'
        self.create_selection_ui(bg_color, text_color, accent_color)

    def calculate_score(self, event=None):
        try:
            media_ponderata_30 = float(self.media_ponderata_var.get() or 0)
            numero_lodi_9 = int(self.numero_lodi_9_var.get() or 0)
            numero_lodi_6 = int(self.numero_lodi_6_var.get() or 0)
            media_ponderata_110 = media_ponderata_30 * (11 / 3)

            if self.is_m63.get():
                numero_lodi_12 = int(self.numero_lodi_12_var.get() or 0)
                voto_triennale = int(self.voto_triennale.get() or 0)
                bonus_lodi = ((numero_lodi_9 * 9 + numero_lodi_6 * 6 + numero_lodi_12 * 12) / 120) * (11 / 3)
                bonus_triennale = max((voto_triennale - 100 + 1) * 0.25, 0)
                voto_finale = media_ponderata_110 + bonus_lodi + bonus_triennale
                self.bonus_triennale.set(round(bonus_triennale, 3))
            else:
                anni_fuoricorso = int(self.anni_fuoricorso_var.get() or -1)
                bonus_lodi = ((numero_lodi_9 * 9 + numero_lodi_6 * 6) / 180) * (11 / 3)
                bonus_anni = max(4 - anni_fuoricorso, 0)
                bonus_100_var = 1 if media_ponderata_110 >= 100 else 0
                voto_finale = media_ponderata_110 + bonus_lodi + bonus_anni + bonus_100_var
                self.bonus_100.set(bonus_100_var)
                self.bonus_anni_var.set(round(bonus_anni, 3))

            self.media_ponderata_110_var.set(round(media_ponderata_110, 3))
            self.bonus_lodi_var.set(round(bonus_lodi, 3))
            self.voto_finale_var.set(round(voto_finale, 3))
        except ValueError:
            event.widget.delete(0, 'end')
            messagebox.showerror("Errore", "Inserisci valori numerici validi")

    def run(self):
        self.root.mainloop()

def main():
    app = GraduationScoreCalculator()
    app.run()

if __name__ == "__main__":
    main()
