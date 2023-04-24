from faker import Faker
import random

fake = Faker()
fake = Faker('pt_BR')

for i in range(100):
    nome = fake.company()
    descricao = fake.text()
    avaliacoes = random.randint(0, 9)
    print(f"'{nome}', '{descricao}', '{avaliacoes}',")

