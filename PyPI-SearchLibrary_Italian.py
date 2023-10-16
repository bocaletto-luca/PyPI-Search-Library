# Nome del Software: PyPI Search Library
# Autore: Bocaletto Luca
import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QListWidget, QListWidgetItem

class PyPIBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Impostazioni della finestra principale
        self.setWindowTitle("PyPI Search Library")  # Imposta il titolo della finestra
        self.setGeometry(100, 100, 800, 600)  # Imposta la posizione e le dimensioni della finestra

        # Creazione del widget centrale
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)  # Imposta il widget centrale per la finestra

        # Creazione del layout verticale
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)  # Imposta il layout come layout centrale

        # Campo di input per la ricerca
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Cerca librerie su PyPI")  # Imposta un testo di esempio nel campo di input
        self.layout.addWidget(self.search_input)  # Aggiunge il campo di input al layout

        # Pulsante di ricerca
        self.search_button = QPushButton("Cerca", self)
        self.layout.addWidget(self.search_button)  # Aggiunge il pulsante di ricerca al layout

        # Lista per i risultati
        self.result_list = QListWidget(self)
        self.layout.addWidget(self.result_list)  # Aggiunge la lista al layout

        # Collega il clic del pulsante all'azione di ricerca
        self.search_button.clicked.connect(self.search_pypi)

    def search_pypi(self):
        query = self.search_input.text()  # Ottieni il testo inserito dall'utente
        if query:
            self.result_list.clear()  # Cancella i risultati precedenti dalla lista
            url = f"https://pypi.org/simple/{query}/"  # Costruisci l'URL per la ricerca su PyPI
            response = requests.get(url)  # Effettua una richiesta HTTP per ottenere i dati
            if response.status_code == 200:  # Verifica se la richiesta ha avuto successo
                data = response.text  # Ottieni i dati dalla risposta
                package_names = self.extract_package_names(data)  # Estrai i nomi delle librerie
                for package_name in package_names:
                    item = QListWidgetItem(package_name)  # Crea un elemento per la lista
                    self.result_list.addItem(item)  # Aggiungi l'elemento alla lista

    def extract_package_names(self, data):
        package_names = data.split('\n')  # Suddivide i dati in linee per ottenere i nomi delle librerie
        return package_names

def main():
    app = QApplication(sys.argv)  # Crea un'applicazione Qt
    window = PyPIBrowser()  # Crea la finestra principale
    window.show()  # Mostra la finestra
    sys.exit(app.exec_())  # Esegui l'applicazione

if __name__ == "__main__":
    main()  # Avvia l'applicazione quando il modulo è eseguito direttamente
