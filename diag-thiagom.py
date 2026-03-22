def imprimir_matriz(matriz, titulo=""):
    n = len(matriz)
    if titulo:
        print(f"\n  {titulo}")
    print("  " + "-" * (10 * (len(matriz[0]))))
    for i, linha in enumerate(matriz):
        valores = "  | "
        for j, v in enumerate(linha):
            if j == len(linha) - 1:
                valores += " | "
            valores += f"{v:8.2f} "
        valores += "|"
        print(valores)
    print("  " + "-" * (10 * (len(matriz[0]))))


def copiar_matriz(matriz):
    return [linha[:] for linha in matriz]


def gauss_jordan(matriz_original):
    matriz = copiar_matriz(matriz_original)
    n = len(matriz)
    passo = 1

    print("\n" + "=" * 60)
    print("  MÉTODO DE GAUSS-JORDAN — DIAGONALIZAÇÃO")
    print("=" * 60)
    print("\n  Matriz aumentada inicial (coeficientes | termos independentes):")
    imprimir_matriz(matriz)

    for i in range(n):
        print(f"\n{'=' * 60}")
        print(f"  PASSO {passo}: Trabalhando na coluna {i + 1} (variável x{i + 1})")
        print(f"{'=' * 60}")
        passo += 1

        # --- Troca de linhas se o pivô for zero ---
        if matriz[i][i] == 0:
            trocou = False
            for k in range(i + 1, n):
                if matriz[k][i] != 0:
                    print(f"\n  [!] Pivô zero detectado na linha {i + 1}.")
                    print(f"      Trocando linha {i + 1} com linha {k + 1}.")
                    matriz[i], matriz[k] = matriz[k], matriz[i]
                    imprimir_matriz(matriz, f"Após troca: L{i+1} <-> L{k+1}")
                    trocou = True
                    break
            if not trocou:
                print(f"\n  [ERRO] Sistema sem solução única (coluna {i+1} é nula).")
                return None

        # --- Normalizar a linha do pivô (tornar pivô = 1) ---
        pivo = matriz[i][i]
        if pivo != 1:
            print(f"\n  Etapa {passo - 1}a: Tornar pivô = 1")
            print(f"  Operação: L{i+1} = L{i+1} / {pivo:.2f}")
            for j in range(n + 1):
                matriz[i][j] /= pivo
            imprimir_matriz(matriz, f"Após L{i+1} = L{i+1} / {pivo:.2f}")
        else:
            print(f"\n  Etapa {passo - 1}a: Pivô já é 1, nenhuma normalização necessária.")

        # --- Zerar todos os outros elementos da coluna i ---
        print(f"\n  Etapa {passo - 1}b: Zerar os demais elementos da coluna {i + 1}")
        alguma_operacao = False
        for k in range(n):
            if k != i and matriz[k][i] != 0:
                fator = matriz[k][i]
                sinal = "-" if fator > 0 else "+"
                print(f"  Operação: L{k+1} = L{k+1} {sinal} {abs(fator):.2f} * L{i+1}")
                for j in range(n + 1):
                    matriz[k][j] -= fator * matriz[i][j]
                alguma_operacao = True

        if alguma_operacao:
            imprimir_matriz(matriz, f"Após zerar coluna {i + 1}")
        else:
            print("  Coluna já zerada, nenhuma operação necessária.")

    # --- Resultado final ---
    print(f"\n{'=' * 60}")
    print("  MATRIZ DIAGONALIZADA (Identidade | Solução)")
    print(f"{'=' * 60}")
    imprimir_matriz(matriz)

    solucao = [matriz[i][n] for i in range(n)]

    print(f"\n{'=' * 60}")
    print("  SOLUÇÃO DO SISTEMA")
    print(f"{'=' * 60}")
    for i, val in enumerate(solucao):
        print(f"  x{i + 1} = {val:.2f}")
    print()

    return solucao


def ler_sistema():
    print("=" * 60)
    print("  RESOLUÇÃO DE SISTEMA LINEAR — GAUSS-JORDAN")
    print("=" * 60)
    while True:
        try:
            n = int(input("\n  Quantas variáveis (e equações) o sistema possui? "))
            if n < 1:
                print("  Digite um número maior que 0.")
                continue
            break
        except ValueError:
            print("  Entrada inválida. Digite um número inteiro.")

    print(f"\n  Digite os coeficientes de cada equação seguidos do termo independente.")
    print(f"  Exemplo para 3 variáveis: 2 1 -1 3  (representa 2x1 + 1x2 - 1x3 = 3)\n")

    matriz = []
    for i in range(n):
        while True:
            try:
                entrada = input(f"  Equação {i + 1} ({n + 1} valores): ").split()
                if len(entrada) != n + 1:
                    print(f"  Esperado {n + 1} valores, recebeu {len(entrada)}. Tente novamente.")
                    continue
                linha = [float(v) for v in entrada]
                matriz.append(linha)
                break
            except ValueError:
                print("  Entrada inválida. Use apenas números.")

    return matriz

matriz = ler_sistema()
gauss_jordan(matriz)
