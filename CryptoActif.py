import tkinter as tk
from tkinter import ttk
import json
import requests
import time
import os

class CryptoPortfolioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Portfolio Tracker")
        self.file_name = "portfolio_data.json"
        self.portfolio_data = self.load_data()
        self.root.geometry("1000x800")
        self.setup_layout()
        self.update_treeview()


    def setup_layout(self):
        tk.Label(self.root, text="Crypto Symbol:").grid(row=0, column=0)
        self.crypto_entry = tk.Entry(self.root)
        self.crypto_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Quantity:").grid(row=1, column=0)
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.grid(row=1, column=1)

        self.add_button = tk.Button(self.root, text="Add/Update Quantity", command=self.add_crypto)
        self.add_button.grid(row=2, column=0, columnspan=2)

        self.update_location_button = tk.Button(self.root, text="Update Location", command=self.open_update_location_window)
        self.update_location_button.grid(row=9, column=0, columnspan=2)

        self.delete_button = tk.Button(self.root, text="Delete Selected Crypto", command=self.delete_crypto)
        self.delete_button.grid(row=5, column=0, columnspan=2)
        self.update_prices_button = tk.Button(self.root, text="Update Prices", command=self.update_prices)
        self.update_prices_button.grid(row=8, column=0, columnspan=2)

        self.portfolio_tree = ttk.Treeview(self.root, columns=("Symbol", "Quantity", "Value ($)", "Total ($)", "Location"), show="headings", height=30)
        self.portfolio_tree.grid(row=3, column=0, columnspan=2)
        self.portfolio_tree.heading("Symbol", text="Symbol")
        self.portfolio_tree.heading("Quantity", text="Quantity")
        self.portfolio_tree.heading("Value ($)", text="Value ($)")
        self.portfolio_tree.heading("Total ($)", text="Total ($)")
        self.portfolio_tree.heading("Location", text="Location")


        self.portfolio_tree.bind("<Double-1>", self.on_item_double_click)

        self.total_label = tk.Label(self.root, text="Total Portfolio Value: $0")
        self.total_label.grid(row=4, column=0, columnspan=2)

        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=200, mode='determinate')
        self.progress.grid(row=7, column=0, columnspan=2, pady=10)


    def load_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                return json.load(file)
        else:
            return {}


    def save_data(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.portfolio_data, file, indent=4)
        self.update_treeview()


    def add_crypto(self):
        # Récupérer le symbole en majuscules
        symbol = self.crypto_entry.get().upper()
        try:
            quantity = float(self.quantity_entry.get())
        except ValueError:
            print("Invalid quantity")
            return
        # Mise à jour du prix à utiliser le symbole en majuscules
        price = self.get_crypto_price(symbol)
        if symbol in self.portfolio_data:
            self.portfolio_data[symbol]['quantity'] += quantity
        else:
            self.portfolio_data[symbol] = {'quantity': quantity, 'price': price}
        self.save_data()
        self.update_treeview()  # Assurez-vous de mettre à jour l'affichage après ajout/modification


    def open_update_location_window(self):
        selected_item = self.portfolio_tree.selection()
        if selected_item:
            symbol = self.portfolio_tree.item(selected_item, 'values')[0].upper()
            self.location_update_window = tk.Toplevel(self.root)
            self.location_update_window.title(f"Update Location for {symbol}")
    
            tk.Label(self.location_update_window, text="New Location:").pack()
            self.new_location_entry = tk.Entry(self.location_update_window)
            self.new_location_entry.pack()
    
            update_button = tk.Button(self.location_update_window, text="Update Location",
                                      command=lambda: self.update_location(symbol))
            update_button.pack()
        else:
            print("Please select a cryptocurrency to update.")

    def update_location(self, symbol):
        new_location = self.new_location_entry.get()
        if symbol in self.portfolio_data:
            self.portfolio_data[symbol]['location'] = new_location
        else:
            print(f"Error: {symbol} not found in portfolio.")
        self.save_data()
        self.location_update_window.destroy()
        self.update_treeview()


    def update_prices(self):
        symbols_list = list(self.portfolio_data.keys())
        if not symbols_list:
            print("Aucun symbole à mettre à jour.")
            return
    
        chunk_size = 10  # Ajustez selon la taille moyenne des symboles pour rester sous la limite de 300 caractères
        total_chunks = len(symbols_list) // chunk_size + (1 if len(symbols_list) % chunk_size else 0)
    
        # Initialiser la barre de progression
        self.progress['maximum'] = total_chunks
        self.progress['value'] = 0
    
        for i in range(0, len(symbols_list), chunk_size):
            # Sélection des symboles pour le chunk actuel
            chunk_symbols = symbols_list[i:i+chunk_size]
            symbols = ','.join(chunk_symbols).upper()
            url = f"https://min-api.cryptocompare.com/data/pricemulti?fsyms={symbols}&tsyms=USD"
            print(f"Updating prices for: {symbols}")
            
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    prices = response.json()
                    if 'Response' in prices and prices['Response'] == 'Error':
                        print(f"API Response Error: {prices['Message']}")
                        continue  # Passe au prochain chunk si erreur
                    for symbol in chunk_symbols:
                        if symbol.upper() in prices:
                            new_price = prices[symbol.upper()]['USD']
                            self.portfolio_data[symbol]['price'] = new_price
                            print(f"Updated price for {symbol}: {new_price}")
                else:
                    print(f"API Response unsuccessful: Status {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error obtaining prices: {e}")
            
            # Mise à jour de la barre de progression après chaque chunk traité
            self.progress['value'] += 1
            self.root.update_idletasks()  # Force la mise à jour de l'UI pour refléter le changement
    
        self.save_data()
        self.update_treeview()
    
        # Remise à zéro de la barre de progression à la fin
        self.progress['value'] = 0



    def delete_crypto(self):
        selected_item = self.portfolio_tree.selection()
        if selected_item:
            # Extraire le symbole en majuscules pour correspondre à la clé du dictionnaire
            symbol = self.portfolio_tree.item(selected_item, 'values')[0].upper()
            if symbol in self.portfolio_data:
                del self.portfolio_data[symbol]
                self.save_data()
                # Mise à jour de l'affichage après suppression
                self.update_treeview()
            else:
                print(f"Error: {symbol} not found in portfolio.")


    def update_treeview(self):
        for i in self.portfolio_tree.get_children():
            self.portfolio_tree.delete(i)
        
        total_value = 0
        sorted_items = sorted(self.portfolio_data.items(), key=lambda item: item[1]['quantity'] * item[1]['price'], reverse=True)
        
        for symbol, data in sorted_items:
            total = data['price'] * data['quantity']
            location = data.get('location', 'N/A')  # Récupère l'emplacement ou retourne 'N/A' si non spécifié
            self.portfolio_tree.insert("", tk.END, values=(symbol.upper(), data['quantity'], f"${data['price']:.2f}", f"${total:.2f}", location))
            total_value += total
        
        self.total_label.config(text=f"Total Portfolio Value: ${total_value:.2f}")



    def update_quantity(self, symbol):
        # Assurer que le symbole est en majuscules
        symbol = symbol.upper()
        try:
            new_quantity = float(self.new_quantity_entry.get())
            if symbol in self.portfolio_data:
                self.portfolio_data[symbol]['quantity'] += new_quantity
            else:
                # Cette branche ne devrait normalement pas être atteinte dans ce contexte
                print(f"Error: {symbol} not found in portfolio.")
                return
            self.save_data()
            self.update_window.destroy()  # Ferme la fenêtre pop-up après la mise à jour
            self.update_treeview()  # Mise à jour de l'affichage
        except ValueError:
            print("Invalid quantity")


    def on_item_double_click(self, event):
        # Obtenir l'élément sélectionné
        selected_item = self.portfolio_tree.selection()[0]
        # Assurez-vous que le symbole est en majuscules pour la cohérence
        symbol = self.portfolio_tree.item(selected_item, 'values')[0].upper()
        
        # Créer une fenêtre secondaire pour la mise à jour de la quantité
        self.update_window = tk.Toplevel(self.root)
        self.update_window.title(f"Update {symbol} Quantity")
        
        tk.Label(self.update_window, text="New Quantity:").pack()
        self.new_quantity_entry = tk.Entry(self.update_window)
        self.new_quantity_entry.pack()
        
        # Bouton pour confirmer la mise à jour
        confirm_button = tk.Button(self.update_window, text="Update Quantity",
                                   command=lambda: self.update_quantity(symbol))
        confirm_button.pack()

    def get_crypto_price(self, symbol):
        # Notez que CryptoCompare utilise les symboles plutôt que les ID pour référencer les cryptomonnaies
        url = f"https://min-api.cryptocompare.com/data/price?fsym={symbol.upper()}&tsyms=USD"
        print(f"Getting price for: {symbol}")
        print(f"Request URL: {url}")
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                print(f"API Response: {data}")
                if 'USD' in data:
                    return data['USD']
                else:
                    print(f"Prix non trouvé pour {symbol}")
            else:
                print(f"Réponse API non réussie pour {symbol}: Statut {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de l'obtention du prix pour {symbol}: {e}")
        return 0


if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoPortfolioApp(root)
    root.mainloop()


