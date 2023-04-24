from faker import Faker
import random

fake = Faker()
fake = Faker('pt_BR')


bairros = ["Aricanduva", "Carrão", "Vila Formosa", "Cidade Tiradentes", "Ermelino Matarazzo",
           "Ponte Rasa", "Guaianases", "Lajeado", "Itaim Paulista", "Vila Curuçá", "Itaquera",
           "Cidade Líder", "José Bonifácio", "Parque do Carmo", "Mooca Água Rasa", "Belém",
           "Brás", "Moóca", "Pari", "Tatuapé", "Penha", "Artur Alvim", "Cangaíba", "Penha",
           "Vila Matilde", "São Mateus", "São Rafael", "São Miguel", "Jardim Helena", "Vila Jacuí",
           "Sapopemba", "Vila Prudente", "São Lucas"]
cidade = "São Paulo"
pais = "Brasil"
def generate_cep():
    cep = ""
    for i in range(8):
        cep += str(random.randint(0, 8))
    return cep

def generate_id():
    id = ""
    for i in range(1):
        id += str(random.randint(1,100))
    return id


for i in range(100):
    endereco = fake.street_name()
    bairro = random.choice(bairros)
    cidade = cidade
    pais = pais
    y = ""
    numero = fake.building_number()
    cep = generate_cep()
    status = random.choice(['A', 'I'])
    complemento = fake.city_suffix()
    complemento2 = random.choice([complemento , y])
    id_cliente = generate_id()
    print(f"{id_cliente}, '{cep}', '{endereco}', '{bairro}', '{pais}', '{numero}', '{status}', '{complemento2}',")