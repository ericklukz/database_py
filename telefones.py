from faker import Faker
import random

fake = Faker()
fake = Faker('pt_BR')

def generate_id():
    id = ""
    for i in range(1):
        id += str(random.randint(1,100))
    return id

def generate_phone():
    numero = ""
    for i in range(8):
        numero += str(random.randint(1,9))
    return numero

ddds = ["61", "62", "64", "65", "66", "67", "82", "71", "73", "74", "75", "77", "85",
         "88", "98", "99", "83", "81", "87", "86", "89", "84", "79", "68", "96", "92",
         "97", "91", "93", "94", "69", "95", "63", "27", "28", "31", "32", "33", "34",
         "35", "37", "38", "21", "22", "24", "11", "12", "13", "14", "15", "16", "17",
         "18", "19", "41", "42", "43", "44", "45", "46", "51", "53", "54", "55", "47",
         "48", "49"]

for i in range(100):
    id_telefone = generate_id()
    telefone = generate_phone()
    ddd = random.choice(ddds)
    ddi = "55"
    status = random.choice(['A', 'I'])
    print(f"{id_telefone}, '9{telefone}', '{ddd}', '{ddi}', '{status}',")
