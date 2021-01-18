import sqlite3

class Supplier:
    def __connect__(self):
        self.connection = sqlite3.connect("./db/Northwind.sqlite")
        self.cursor = self.connection.cursor()
    
    def __disconnect__(self, commit=True):
        if commit:
            self.connection.commit()
        self.connection.close()
    
    def mostrarDadosSupplier(self):
        self.__connect__()
        self.cursor.execute("SELECT Id, CompanyName FROM Supplier ORDER BY CompanyName")
        suppliers = self.cursor.fetchall()
        self.__disconnect__(False)
        return suppliers
    
    def mostrarNomeSupplier(self, key):
        self.__connect__()
        self.cursor.execute("SELECT Supplier.CompanyName FROM Supplier INNER JOIN Product ON Supplier.Id = Product.SupplierId  WHERE Product.Id=?", (key,))
        supplierName = str(self.cursor.fetchone()[0])
        self.__disconnect__(False)
        return supplierName

# suppliers = Supplier()

# for s in suppliers.mostrarNomeSupplier():
#     print(s)