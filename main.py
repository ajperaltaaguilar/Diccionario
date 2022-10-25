dict1 = {'plátanos': 7, 'manzanas': 3, 'peras': 14}
dict2 = {'plátanos': 3, 'manzanas': 6, 'uvas': 9}

def merge_max_mappings(a, b):
    aux = a.copy()
    for key in b:  # si la clave banana
        if key in aux:
            aux[key] = max(aux[key], b[key])
        else:
            aux[key] = b[key]
            print(aux)
