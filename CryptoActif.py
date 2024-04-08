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
        self.root.geometry("800x740")
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

        self.delete_button = tk.Button(self.root, text="Delete Selected Crypto", command=self.delete_crypto)
        self.delete_button.grid(row=5, column=0, columnspan=2)
        self.update_prices_button = tk.Button(self.root, text="Update Prices", command=self.update_prices)
        self.update_prices_button.grid(row=6, column=0, columnspan=2)

        self.portfolio_tree = ttk.Treeview(self.root, columns=("Symbol", "Quantity", "Value ($)", "Total ($)"), show="headings", height=30)

        self.portfolio_tree.grid(row=3, column=0, columnspan=2)
        self.portfolio_tree.heading("Symbol", text="Symbol")
        self.portfolio_tree.heading("Quantity", text="Quantity")
        self.portfolio_tree.heading("Value ($)", text="Value ($)")
        self.portfolio_tree.heading("Total ($)", text="Total ($)")

        self.portfolio_tree.bind("<Double-1>", self.on_item_double_click)

        self.total_label = tk.Label(self.root, text="Total Portfolio Value: $0")
        self.total_label.grid(row=4, column=0, columnspan=2)


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


    def update_prices(self):
        symbols = ','.join(self.portfolio_data.keys()).upper()
        url = f"https://min-api.cryptocompare.com/data/pricemulti?fsyms={symbols}&tsyms=USD"
        
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                prices = response.json()
                for symbol, data in self.portfolio_data.items():
                    if symbol.upper() in prices:  # Utiliser des symboles en majuscules pour la correspondance
                        new_price = prices[symbol.upper()]['USD']
                        self.portfolio_data[symbol]['price'] = new_price  # Mise à jour du prix
                        print(f"Mise à jour du prix pour {symbol}: {new_price}")  # Pour le débogage
                self.save_data()
                self.update_treeview()  # Mise à jour de l'affichage
            else:
                print(f"Réponse API non réussie: Statut {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de l'obtention des prix: {e}")



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
        # Efface tous les éléments existants dans le Treeview
        for i in self.portfolio_tree.get_children():
            self.portfolio_tree.delete(i)
    
        total_value = 0
        # Création d'une liste à partir des éléments du portfolio pour les trier
        sorted_items = sorted(self.portfolio_data.items(), key=lambda item: item[1]['quantity'] * item[1]['price'], reverse=True)
    
        # Parcourt chaque élément trié du portfolio pour l'afficher
        for symbol, data in sorted_items:
            # Calcule le total pour chaque crypto
            total = data['price'] * data['quantity']
            # Insère chaque crypto dans le Treeview avec le symbole en majuscules
            self.portfolio_tree.insert("", tk.END, values=(symbol.upper(), data['quantity'], f"${data['price']:.2f}", f"${total:.2f}"))
            # Calcule la valeur totale du portfolio
            total_value += total
    
        # Met à jour l'affichage de la valeur totale du portfolio
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
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
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





