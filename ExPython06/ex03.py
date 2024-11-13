marcas = ["GM", "FIAT", "Volkswagen", "Ford", "Honda", "Toyota", "Gurgel", "Dodge"]
marcas.insert(3, "Hyundai")
marcas.insert(4, "BMW")
marcas.insert(5, "Nissan")
indice_gm = marcas.index("GM")
marcas[indice_gm] = "Chevrolet"
marcas.remove("Gurgel")
marcas.sort()
print("Lista de marcas atualizada:")
for marca in marcas:
    print(marca)
    