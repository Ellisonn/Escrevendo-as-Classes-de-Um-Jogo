class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        else:
            ataque = "usou um ataque desconhecido"

        return f"O {self.tipo} atacou usando {ataque}."

# Exemplos de uso:

# Criação de heróis
herois = [
    Heroi("Aragorn", 87, "guerreiro"),
    Heroi("Gandalf", 2019, "mago"),
    Heroi("Shaolin", 35, "monge"),
    Heroi("Naruto", 17, "ninja")
]

# Salvar resultados em um arquivo de texto
with open("resultados.txt", "w") as file:
    for heroi in herois:
        resultado = heroi.atacar()
        file.write(resultado + "\n")
        print(resultado)  # Opcional: Exibir no console também
