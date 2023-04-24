# Gerador de dados em python

Cansado de perder horas tentando criar dados para inserir em tabelas de teste, percebi que o processo poderia ser automatizado.
A ideia era tentar desenvolver 100 dados da forma mais rápida possível e de forma assertiva (que pudesse ser inserida no banco de dados sem nenhum problema de dado faltando ou afins).

Foram várias opções, a mais promissora era a de usar um gerador online (que me limitava a usar os dados gerados por ele, sem mais nem menos),a conversão seria por parte do Chat GPT, onde eu enviaria estes dados e o Chat GPT traria de volta. Mas esta opção estava fora de questão por diversos motivos, os principais eram : Demora para gerar os dados (cerca de 1 minuto), não era tão assertivo (deixava alguns dados para fora, atrapalhando todo o loop do Pl/Sql) e o limite de caractéres (que fazia o Chat GPT digitar cerca de 10 dados completos).

Procurando em diversos locais encontrei uma biblioteca chamada Faker para python, e com algumas linhas de código consegui gerar 100 dados de forma assertiva em menos de 1 segundo!

Todo o cógigo fonte foi disponibilizado neste repositório, e nele tem exemplos do que eu precisa colocar dentro das tabelas. Seu funcionamento é simples, mas ele poupa muito tempo de escrita.

##O uso deste código é apenas para fins acadêmicos!!


