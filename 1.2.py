initial_list = [('p', 2), ('u', 1), ('l', 1), ('', 1), ('f', 1), ('i', 2), ('c', 1), ('o', 1), ('n', 1)]
list_vow = []
list_cons = []
list_sym = []
vowels = ['a', 'e', 'i', 'o', 'u']
for char, count in initial_list:
    if char in vowels:
        list_vow.append({char: count})
    elif char == ' ':
        list_sym.append({char: count})
    else:
        list_cons.append({char: count})
print("list_vow=", list_vow)
print("list_cons=", list_cons)
print("list_sym=", list_sym)
