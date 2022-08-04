"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
Örnek Olarak:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]
"""
liste = [[1, 2], [3, 4], [5, 6, 7]]
def döndür(liste):
    result = []
    prot = liste[::-1]
    for k in prot:
        result.append(k[::-1])
    print(result)
    return result
döndür(liste)