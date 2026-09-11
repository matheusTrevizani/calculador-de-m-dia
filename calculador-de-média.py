def calcular_media(notas):
    """Calcula a média aritmética de uma lista de notas."""
    if not notas:
        return 0
    return sum(notas) / len(notas)


def main():
    print("=== Calculadora de Média - Professor ===\n")

    try:
        qtd = int(input("Quantos alunos deseja calcular? "))
    except ValueError:
        print("Digite um número válido.")
        return

    notas = []
    for i in range(1, qtd + 1):
        while True:
            try:
                nota = float(input(f"Nota do aluno {i}: "))
                notas.append(nota)
                break
            except ValueError:
                print("Digite um número válido para a nota.")

    media = calcular_media(notas)

    print(f"\nNotas informadas: {notas}")
    print(f"Média da turma: {media:.2f}")

    if media >= 6:
        print("Situação: Aprovada(a)")
    else:
        print("Situação: Reprovada(a)")


if __name__ == "__main__":
    main()
