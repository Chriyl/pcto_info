from typing import TypedDict

"""
qui ci scriviamo i modelli del db per rendere il codice piú elegante
e per evitare di scrivere in ogni metodo che richiama il db parametri chilometrici

GLI ATTRIBUTI DEI MODELLI DEVONO NECESSARIAMENTE MATCHARE I NOMI DELLE COLONNE DEL DB

per maggiori info vai su "/docs/models.md"

"""

class UserModel(TypedDict):
    #SupplierID: int
    SupplierName: str
    ContactName: str
    Address: str
    City: str
    PostalCode: str
    Country: str
    Phone: str






