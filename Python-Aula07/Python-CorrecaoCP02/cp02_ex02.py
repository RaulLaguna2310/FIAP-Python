def calcular_media(notas):
    return sum(notas) / len(notas)

def obter_notas():
    notas = []
    while True:
        nota = input("Digite a nota (ou 'sair' para finalizar): ")
        if nota.lower() == 'sair':
            break
        try:
            notas.append(float(nota))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    return notas

def exibir_resultado(media):
    if media is not None:
        print(f"A média das notas é: {media:.2f}")

def main():
    notas = obter_notas()
    if notas:
        media = calcular_media(notas)
        exibir_resultado(media)
    else:
        print("Nenhuma nota válida foi inserida.")

if __name__ == "__main__":
    main()