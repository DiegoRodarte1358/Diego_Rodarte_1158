#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Array:
    def __init__(self, n):
        self.__data = []
        for i in range(n):
            self.__data.append(None)

    def to_string(self):
        print(self.__data)

    def get_length(self):
        return len(self.__data)

    def set_item(self, index, value):
        if index >= 0 and index <= len(self._data):
            self.__data[index] = value
        else:
            print("No es posible ese número")

    def get_item(self, index):
        if index >= 0 and index <= len(self.__data):
            return self.__data[index]
        else:
            print("No es posible ese número")

    def clearing(self, valor):
        for i in range(len(self.__data)):
            self.__data[i] = valor

def main():
    arreglo = Array(5)
    arreglo.to_string()
    print(f"El tamaño es de: {arreglo.get_length()}")
    arreglo.set_item(1, 10)
    arreglo.to_string()
    print(f"El elemento 1 es {arreglo.get_item(1)}")
    arreglo.get_item(20)
    arreglo.clearing(10)
    arreglo.to_string()

main()


# In[4]:


class Array2D:
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__data = []
        for r in range(rows):
            tmp = []
        for c in range(cols):
            tmp.append(None)
        self.__data.append(tmp)

    def to_string(self):
        print(self.__data)

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def clearing(self, value):
        for r in range(self.__rows):
            for c in range(self.__cols):
                self.__data[rows][cols] = value

    def set_item(self, row, col, value):
        if (row >= 0 and row < self.__rows) and (c >= 0 and c < self.__cols):
            self.__data[r][c] = value              

    def get_item(self, row, col):
        if (row >= 0 and row < self.__rows) and (c >= 0 and c < self.__cols):
            return self.__data[row][col]
       

def main():
    Array = Array2D(5,5)
    Array.to_string()
    print(f"El numero de renglones", Array.get_num_rows())
    print(f"El numero de columnas", Array.get_num_cols())
   
main()


# In[ ]:




