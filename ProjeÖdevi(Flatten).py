"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın.
Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]
"""

liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(liste):
    result = []
    for element in range(0, len(liste)):
        if (type(liste[element]) == list):
            print("1")
            for eleman in range(0, len(liste[element])):
                if (type(liste[element][eleman]) == list):
                    print(2)
                    for sayi in range(0, len(liste[element][eleman])):
                        if (type(liste[element][eleman][sayi]) == list):
                            print(3)
                            for sayma in range(0, len(liste[element][eleman][sayi])):
                                if (type(liste[element][eleman][sayi][sayma]) == list):
                                    print("son")
                                else:
                                    result.append(liste[element][eleman][sayi][sayma])
                        else:
                            result.append(liste[element][eleman][sayi])
                else:
                    result.append(liste[element][eleman])
        else:
            result.append(liste[element])
    print(result)
    return result

flatten(liste)