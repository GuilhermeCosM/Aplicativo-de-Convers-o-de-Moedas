class Carro:

  def __init__(self, nome, tipo, consumo, capacidade, preco):
    self.nome = nome
    self.tipo = tipo
    self.consumo = consumo
    self.capacidade = capacidade
    self.preco = preco


carros_por_tipo = {
    "Híbrido": [
        Carro("Toyota Prius", "Híbrido", 25, 5, 30000),
        Carro("Hyundai Ioniq", "Híbrido", 28, 5, 28000),
        Carro("Kia Niro", "Híbrido", 29, 5, 26000),
        Carro("Lexus ES Hybrid", "Híbrido", 32, 5, 45000),
        Carro("Audi A3 Sportback e-tron", "Híbrido", 27, 5, 38000),
    ],
    "Sedan": [
        Carro("Honda Civic", "Sedan", 30, 5, 25000),
        Carro("Nissan Altima", "Sedan", 27, 5, 27000),
        Carro("Toyota Camry", "Sedan", 26, 5, 29000),
        Carro("Hyundai Sonata", "Sedan", 29, 5, 26000),
        Carro("Mazda 6", "Sedan", 28, 5, 28000),
    ],
    "SUV": [
        Carro("Ford Explorer", "SUV", 20, 7, 40000),
        Carro("Mazda CX-5", "SUV", 28, 5, 35000),
        Carro("Subaru Outback", "SUV", 26, 5, 32000),
        Carro("Toyota RAV4", "SUV", 25, 5, 33000),
        Carro("Honda CR-V", "SUV", 29, 5, 31000),
    ],
    "Compacto": [
        Carro("Chevrolet Spark", "Compacto", 35, 4, 15000),
        Carro("Volkswagen Golf", "Compacto", 32, 4, 20000),
        Carro("Ford Fiesta", "Compacto", 30, 4, 18000),
        Carro("Honda Fit", "Compacto", 33, 5, 17000),
        Carro("Hyundai Accent", "Compacto", 31, 5, 16000),
    ],
    "Esportivo": [
        Carro("Porsche 911", "Esportivo", 12, 2, 100000),
        Carro("Chevrolet Corvette", "Esportivo", 18, 2, 70000),
        Carro("Ford Mustang", "Esportivo", 15, 4, 65000),
        Carro("BMW M4", "Esportivo", 17, 4, 75000),
        Carro("Audi R8", "Esportivo", 14, 2, 120000),
    ],
}


def calcular_aluguel(carro):
  return carro.preco * 0.02


def recomendar_carro(preferencias):
  carros_filtrados = []

  for lista_carros in carros_por_tipo.values():
    for carro in lista_carros:
      aluguel = calcular_aluguel(carro)
      if ((preferencias.get("tipo") is None
           or preferencias["tipo"].lower() == carro.tipo.lower())
          and (preferencias["consumo"] is None
               or preferencias["consumo"] >= carro.consumo)
          and (preferencias["capacidade"] is None
               or preferencias["capacidade"] == carro.capacidade)
          and (preferencias.get("aluguel_max") is None
               or preferencias["aluguel_max"] >= aluguel)):
        carro.aluguel = aluguel
        carros_filtrados.append(carro)

  return carros_filtrados


preferencias_usuario = {
    "tipo": None,
    "aluguel_max": None,
    "consumo": None,
    "capacidade": None,
}

resultados = recomendar_carro(preferencias_usuario)

if resultados:
  print("Carros Disponíveis:")
  for carro in resultados:
    print(
        f"\n{carro.nome} - Tipo: {carro.tipo}, Consumo: {carro.consumo} km/l, Capacidade: {carro.capacidade}, Aluguel/Dia: ${carro.aluguel:.2f}"
    )
else:
  print("Nenhum carro disponível.")