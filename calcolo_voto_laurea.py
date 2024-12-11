import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class GraduationScoreCalculator:
    def __init__(self):
        # Inizializzazione finestra
        self.root = tk.Tk()
        self.root.title("Calcolatore Voto Laurea N46 - \"Federico II\"")
        self.root.geometry("700x700")
        
        # Colori personalizzati
        bg_color = '#1a1a2e'
        text_color = '#e0e0e0'
        accent_color = '#6a5acd'
        
        # Configurazione colori
        self.root.configure(background=bg_color)
        
        # Inizializzazione variabili
        self.setup_variables()
        
        # Creazione UI
        self.create_ui(bg_color, text_color, accent_color)
        
    def setup_variables(self):
        # Input variables
        self.media_ponderata_var = tk.StringVar()
        self.numero_lodi_9_var = tk.StringVar()
        self.numero_lodi_6_var = tk.StringVar()
        self.anni_fuoricorso_var = tk.StringVar()
        
        # Output variables
        self.media_ponderata_110_var = tk.StringVar(value="0")
        self.bonus_100_var = tk.StringVar(value="0")
        self.bonus_lodi_var = tk.StringVar(value="0")
        self.bonus_anni_var = tk.StringVar(value="0")
        self.voto_finale_var = tk.StringVar(value="0")
        
    def create_ui(self, bg_color, text_color, accent_color):
        # Container principale
        main_frame = tk.Frame(self.root, bg=bg_color)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Titolo
        title_label = tk.Label(
            main_frame, 
            text="Calcolatore Voto Laurea N46", 
            font=('Arial', 16, 'bold'),
            bg=bg_color,
            fg=accent_color
        )
        title_label.pack(pady=(0, 20))
        
        # Sezione warning
        warning_frame = tk.Frame(main_frame, bg='#4b0082')
        warning_frame.pack(fill='x', pady=10)
        
        warning_label = tk.Label(
            warning_frame, 
            text="⚠️ ATTENZIONE ⚠️: Ricorda che al punteggio va aggiunta\n"
                "la valutazione della commissione (0-3 punti) ",
            font=('Arial', 12, 'bold'),
            bg='#4b0082',
            fg='white'
        )
        warning_label.pack(pady=10)
        
        # Sezione input
        input_frame = tk.Frame(main_frame, bg=bg_color)
        input_frame.pack(fill='x', pady=10)
        
        input_fields = [
            ("Media ponderata su 30:", self.media_ponderata_var),
            ("Numero lodi 9 cfu:", self.numero_lodi_9_var),
            ("Numero lodi 6 cfu:", self.numero_lodi_6_var),
            ("Anni fuoricorso:", self.anni_fuoricorso_var)
        ]
        
        for i, (label_text, var) in enumerate(input_fields):
            row_frame = tk.Frame(input_frame, bg=bg_color)
            row_frame.pack(fill='x', pady=5)
            
            label = tk.Label(
                row_frame, 
                text=label_text, 
                width=20, 
                anchor='w',
                bg=bg_color,
                fg=text_color,
                font=('Arial', 14)  # Increased font size for input labels
            )
            label.pack(side='left', padx=10)
            
            entry = tk.Entry(
                row_frame, 
                textvariable=var, 
                font=('Arial', 12),
                bg='#2c3e50',
                fg='white'
            )
            entry.pack(side='left', expand=True, fill='x', padx=10)
            entry.bind('<KeyRelease>', self.calcola_voto)
        
        # Separatore
        separator = tk.Frame(main_frame, height=2, bg='#4b0082')
        separator.pack(fill='x', pady=10)
        
        # Sezione output
        output_frame = tk.Frame(main_frame, bg=bg_color)
        output_frame.pack(fill='x', pady=10)
        
        output_fields = [
            ("Media ponderata su 110:", self.media_ponderata_110_var),
            ("Bonus > 100:", self.bonus_100_var),
            ("Bonus Lodi:", self.bonus_lodi_var),
            ("Bonus Anni Svolti:", self.bonus_anni_var),
            ("Voto finale:", self.voto_finale_var)
        ]
        
        for label_text, var in output_fields:
            row_frame = tk.Frame(output_frame, bg=bg_color)
            row_frame.pack(fill='x', pady=5)
            
            label = tk.Label(
                row_frame, 
                text=label_text, 
                width=20, 
                anchor='w',
                bg=bg_color,
                fg=text_color,
                font=('Arial', 14)  # Increased font size for output labels
            )
            label.pack(side='left', padx=10)
            
            value_label = tk.Label(
                row_frame, 
                textvariable=var, 
                font=('Arial', 16, 'bold'),  # Increased font size for output values
                bg=bg_color,
                fg=accent_color
            )
            value_label.pack(side='left', expand=True, fill='x', padx=10)
   
   
    def calcola_voto(self, event=None):
        try:
            # Calcolo logica invariata rispetto all'originale
            media_ponderata_30 = float(self.media_ponderata_var.get() or 0)
            numero_lodi_9 = int(self.numero_lodi_9_var.get() or 0)
            numero_lodi_6 = int(self.numero_lodi_6_var.get() or 0)
            anni_fuoricorso = int(self.anni_fuoricorso_var.get() or -1)

            media_ponderata_110 = media_ponderata_30 * (11 / 3)
            media_ponderata_110 = round(media_ponderata_110, 3)

            bonus_100 = 1 if media_ponderata_110 >= 100 else 0
            bonus_lodi = (numero_lodi_9 * 9) + (numero_lodi_6 * 6)
            bonus_lodi = bonus_lodi / 180
            bonus_lodi = bonus_lodi * (11 / 3)
            bonus_lodi = round(bonus_lodi, 1)

            bonus_anni = 4 - anni_fuoricorso if 0 <= anni_fuoricorso <= 4 else 0

            voto_finale = media_ponderata_110 + bonus_100 + bonus_lodi + bonus_anni
            voto_finale = round(voto_finale, 3)

            # Aggiornamento variabili
            self.media_ponderata_110_var.set(str(media_ponderata_110))
            self.bonus_100_var.set(str(bonus_100))
            self.bonus_lodi_var.set(str(bonus_lodi))
            self.bonus_anni_var.set(str(bonus_anni))
            self.voto_finale_var.set(str(voto_finale))

        except ValueError:
            # Gestione errori più elegante
            messagebox.showerror("Errore", "Inserisci valori numerici validi")
        
    def run(self):
        self.root.mainloop()

def main():
    app = GraduationScoreCalculator()
    app.run()

if __name__ == "__main__":
    main()
