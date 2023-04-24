from faker import Faker
import random

fake = Faker()
fake = Faker('pt_BR')

for i in range(100):
    nome = fake.company()
    razao_social = fake.company_suffix()
    descricao = fake.text()
    avaliacoes = random.randint(0, 10000000)
    print(f"'{nome}', '{razao_social}', '{descricao}', '{avaliacoes}',")