"""2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:
input: [[1, 2], [3, 4], [5, 6, 7]] output: [[[7, 6, 5], [4, 3], [2, 1]] """

def reverse(lst):
    reversed_list = []
    for i in reversed(lst):
        if isinstance(i, list):
            reversed_list.append(reverse(i))
        else:
            reversed_list.append(i)
    return reversed_list

input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse(input_list)
print(output_list)
