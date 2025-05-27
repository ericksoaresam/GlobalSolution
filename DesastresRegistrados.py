tipos_desastres = []
paises = []
cidades = []
bairros = []
ruas = []
total_afetados = []
criancas = []
adultos = []
idosos = []
mobilidade_reduzida = []
feridos = []

while True:
    try:
        quantidade_desastres = int(input("Insira a quantidade de desastres que deseja registrar: "))
        if quantidade_desastres < 1:
            print("Insira um número válido (mínimo 1).")
            continue
        break
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

for i in range(quantidade_desastres):
    print(f"\n--- Desastre {i+1} ---")
    print("Digite 0 para sair ou qualquer outra tecla para continuar.")
    escolha = input("Sua escolha: ")
    if escolha == "0":
        print("\nEncerrando o registro de desastres...")
        break

    tipo = input("Tipo de desastre: ")
    pais = input("País: ")
    cidade = input("Cidade: ")
    bairro = input("Bairro: ")
    rua = input("Rua: ")

    while True:
        try:
            total = int(input("Total de pessoas afetadas: "))
            c = int(input("Número de crianças: "))
            a = int(input("Número de adultos: "))
            id_ = int(input("Número de idosos: "))
            mr = int(input("Número de pessoas com mobilidade reduzida: "))
            f = int(input("Número de feridos: "))

            if c + a + id_ + mr != total:
                print("Erro: A soma das categorias não corresponde ao total de afetados. Tente novamente.\n")
                continue
            break
        except ValueError:
            print("Insira apenas números inteiros válidos.")

    # Armazenar dados
    tipos_desastres.append(tipo)
    paises.append(pais)
    cidades.append(cidade)
    bairros.append(bairro)
    ruas.append(rua)
    total_afetados.append(total)

    criancas.append(c)
    adultos.append(a)
    idosos.append(id_)
    mobilidade_reduzida.append(mr)
    feridos.append(f)

# Relatório
total_desastres = len(tipos_desastres)
soma_criancas = sum(criancas)
soma_adultos = sum(adultos)
soma_idosos = sum(idosos)
soma_mob = sum(mobilidade_reduzida)
soma_feridos = sum(feridos)
soma_total_afetados = sum(total_afetados)

maior_valor = soma_criancas
categoria_mais_afetada = "Crianças"

if soma_adultos > maior_valor:
    maior_valor = soma_adultos
    categoria_mais_afetada = "Adultos"
if soma_idosos > maior_valor:
    maior_valor = soma_idosos
    categoria_mais_afetada = "Idosos"
if soma_mob > maior_valor:
    maior_valor = soma_mob
    categoria_mais_afetada = "Mobilidade reduzida"
if soma_feridos > maior_valor:
    maior_valor = soma_feridos
    categoria_mais_afetada = "Feridos"

if total_desastres > 0:
    maior_afetados = total_afetados[0]
    indice_maior = 0
    for i in range(1, total_desastres):
        if total_afetados[i] > maior_afetados:
            maior_afetados = total_afetados[i]
            indice_maior = i

    print("\n\n===== RELATÓRIO FINAL =====\n")
    print(f"Total de desastres registrados: {total_desastres}\n")
    print("Resumo de pessoas afetadas por categoria:")
    print(f"Crianças: {soma_criancas} | Adultos: {soma_adultos} | Idosos: {soma_idosos} | Mobilidade reduzida: {soma_mob} | Feridos: {soma_feridos}\n")
    print(f"Categoria mais afetada: {categoria_mais_afetada}")
    print(f"Total geral de pessoas afetadas: {soma_total_afetados}\n")
    print("Desastre com maior número de afetados:")
    print(f"Tipo: {tipos_desastres[indice_maior]}")
    print(f"Local: {ruas[indice_maior]}, {bairros[indice_maior]}, {cidades[indice_maior]}, {paises[indice_maior]}")
else:
    print("\nNenhum desastre foi registrado.")
