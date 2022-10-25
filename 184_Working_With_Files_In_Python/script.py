my_file = open('test.txt')

# so é possivel abrior um arquivo para ler uma unica vez
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)

# # === Printi multiple lines ===
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

# === Print multiple lines in a list ===
print(my_file.readlines())

my_file.close()
