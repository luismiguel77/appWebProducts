import sqlite3
import random

class Product:
    def __connect__(self):
        self.connection = sqlite3.connect("./db/Northwind.sqlite")
        self.cursor = self.connection.cursor()

    def __disconnect__(self, commit=True):
        if commit:
            self.connection.commit()
        self.connection.close()

    def mostrarDadosProduct(self):
        self.__connect__()
        self.cursor.execute("SELECT Product.Id, Product.ProductName, Supplier.CompanyName FROM Product INNER JOIN Supplier ON Product.SupplierId = Supplier.Id")
        products = self.cursor.fetchall()
        self.__disconnect__(False)
        return products
    
    def mostrarNomeProduct(self, id):
        self.__connect__()
        self.cursor.execute("SELECT ProductName FROM Product WHERE Id=?", (id,))
        productName = str(self.cursor.fetchone()[0])
        self.__disconnect__(False)
        return productName
    
    def mostrarPrecoProduct(self, id):
        self.__connect__()
        self.cursor.execute("SELECT UnitPrice FROM Product WHERE Id=?", (id,))
        precoProduct = int(self.cursor.fetchone()[0])
        self.__disconnect__(False)
        return precoProduct
    
    def mostrarStockProduct(self, id):
        self.__connect__()
        self.cursor.execute("SELECT UnitsInStock FROM Product WHERE Id=?", (id,))
        stockProduct = int(self.cursor.fetchone()[0])
        self.__disconnect__(False)
        return stockProduct
    
    def mostrarPrecoTaxes(self, id, taxes):
        precoWithoutTaxes = self.mostrarPrecoProduct(id)
        taxes = (taxes * precoWithoutTaxes) / 100
        precoWithTaxes = precoWithoutTaxes + taxes
        return precoWithTaxes
    
    def mostrarUnitsOnOrder(self, id):
        self.__connect__()
        self.cursor.execute("SELECT SUM(Quantity) FROM OrderDetail WHERE ProductId=?", (id,))
        unitsOnOrder = str(self.cursor.fetchone()[0])
        self.__disconnect__(False)
        return unitsOnOrder
    
    def createProduct(self, name, idSupplier, price, stock):
        self.__connect__()
        idProductRandom = random.randint(80, 200)
        self.cursor.execute("INSERT INTO Product VALUES (?,?,?,0,0,?,?,0,0,0)", (idProductRandom, name, idSupplier, price, stock))
        self.connection.commit()
    
    def removeProduct(self, key):
        self.__connect__()
        self.cursor.execute("DELETE FROM Product WHERE Id = ?", (key,))
        self.connection.commit()
    
    # def removerVarios(self, keys):
    #     self.__connect__()
    #     for produtos in range(len(keys)):
    #         self.cursor.execute("DELETE FROM Product WHERE Id = ?", (keys[produto]),)
    #         self.connection.commit()

    def updateProduct(self, name, idSupplier, price, stock, key):
        self.__connect__()
        self.cursor.execute("UPDATE Product SET ProductName=?, SupplierId=?, UnitPrice=?, UnitsInStock=? WHERE Id=?", (name, idSupplier, price, stock, key))
        self.connection.commit()

# products = Product()

# for p in products.mostrarDadosProduct():
#     print(p)

# for p in products.mostrarPrecoProduct():
#     print(p)