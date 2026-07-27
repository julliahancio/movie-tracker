filmes = []


while True:

    print("\n" + "=" * 35)
    print("🎬 MOVIE TRACKER")
    print("=" * 35)

    print("1 - Adicionar filme")
    print("2 - Listar filmes")
    print("3 - Pesquisar filme")
    print("4 - Remover filme")
    print("5 - Sair")

    opcao = input("\nEscolha uma opção: ")

    # -----------------------------
    # ADICIONAR FILME
    # -----------------------------
    if opcao == "1":

        titulo = input("Título: ")
        genero = input("Gênero: ")

        nota = float(input("Nota (0 a 10): "))

        assistido = input("Já assistiu? (S/N): ").upper()

        filme = {
            "titulo": titulo,
            "genero": genero,
            "nota": nota,
            "assistido": assistido
        }

        filmes.append(filme)

        print("\n✅ Filme cadastrado!")

    # -----------------------------
    # LISTAR FILMES
    # -----------------------------
    elif opcao == "2":

        if len(filmes) == 0:

            print("\nNenhum filme cadastrado.")

        else:

            print("\n===== SEUS FILMES =====\n")

            for i, filme in enumerate(filmes, start=1):

                status = "Sim" if filme["assistido"] == "S" else "Não"

                print(f"{i}. {filme['titulo']}")
                print(f"   🎭 Gênero: {filme['genero']}")
                print(f"   ⭐ Nota: {filme['nota']}")
                print(f"   👀 Assistido: {status}")
                print()

    # -----------------------------
    # PESQUISAR
    # -----------------------------
    elif opcao == "3":

        busca = input("Digite o nome do filme: ").lower()

        encontrado = False

        for filme in filmes:

            if busca in filme["titulo"].lower():

                print("\nFilme encontrado!\n")

                print(f"Título: {filme['titulo']}")
                print(f"Gênero: {filme['genero']}")
                print(f"Nota: {filme['nota']}")

                encontrado = True

        if not encontrado:

            print("\nFilme não encontrado.")

    # -----------------------------
    # REMOVER
    # -----------------------------
    elif opcao == "4":

        if len(filmes) == 0:

            print("\nNenhum filme para remover.")

        else:

            for i, filme in enumerate(filmes, start=1):

                print(f"{i} - {filme['titulo']}")

            remover = int(input("\nNúmero do filme: "))

            if 1 <= remover <= len(filmes):

                apagado = filmes.pop(remover - 1)

                print(f"\n'{apagado['titulo']}' removido.")

            else:

                print("\nNúmero inválido.")

    # -----------------------------
    # SAIR
    # -----------------------------
    elif opcao == "5":

        print("\nAté logo!")

        break

    else:

        print("\nEscolha uma opção válida.")
    