import json
import os

ARQUIVO = "filmes.json"


# -----------------------------
# PERSISTÊNCIA
# -----------------------------
def carregar_dados():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []


def salvar_dados(filmes):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(filmes, f, ensure_ascii=False, indent=2)


# -----------------------------
# ENTRADAS COM VALIDAÇÃO
# -----------------------------
def ler_nota():
    while True:
        valor = input("Nota (0 a 10): ").replace(",", ".")
        try:
            nota = float(valor)
            if 0 <= nota <= 10:
                return nota
            print("A nota precisa estar entre 0 e 10.")
        except ValueError:
            print("Digite um número válido (ex: 8.5).")


def ler_opcao_numero(mensagem, minimo, maximo):
    while True:
        valor = input(mensagem)
        if valor.isdigit() and minimo <= int(valor) <= maximo:
            return int(valor)
        print(f"Digite um número entre {minimo} e {maximo}.")


# -----------------------------
# FUNCIONALIDADES
# -----------------------------
def adicionar_filme(filmes):
    titulo = input("Título: ").strip()
    genero = input("Gênero: ").strip()
    nota = ler_nota()
    assistido = input("Já assistiu? (S/N): ").strip().upper()
    assistido = "S" if assistido == "S" else "N"

    filme = {
        "titulo": titulo,
        "genero": genero,
        "nota": nota,
        "assistido": assistido
    }
    filmes.append(filme)
    salvar_dados(filmes)
    print("\n✅ Filme cadastrado e salvo!")


def listar_filmes(filmes):
    if not filmes:
        print("\nNenhum filme cadastrado.")
        return

    print("\n===== SEUS FILMES =====\n")
    for i, filme in enumerate(filmes, start=1):
        status = "Sim" if filme["assistido"] == "S" else "Não"
        print(f"{i}. {filme['titulo']}")
        print(f"   🎭 Gênero: {filme['genero']}")
        print(f"   ⭐ Nota: {filme['nota']}")
        print(f"   👀 Assistido: {status}")
        print()


def pesquisar_filme(filmes):
    busca = input("Digite o nome do filme: ").lower().strip()
    encontrados = [f for f in filmes if busca in f["titulo"].lower()]

    if not encontrados:
        print("\nFilme não encontrado.")
        return

    print(f"\n{len(encontrados)} filme(s) encontrado(s):\n")
    for filme in encontrados:
        status = "Sim" if filme["assistido"] == "S" else "Não"
        print(f"Título: {filme['titulo']}")
        print(f"Gênero: {filme['genero']}")
        print(f"Nota: {filme['nota']}")
        print(f"Assistido: {status}\n")


def remover_filme(filmes):
    if not filmes:
        print("\nNenhum filme para remover.")
        return

    listar_filmes(filmes)
    indice = ler_opcao_numero("Número do filme a remover: ", 1, len(filmes))
    apagado = filmes.pop(indice - 1)
    salvar_dados(filmes)
    print(f"\n'{apagado['titulo']}' removido.")


def editar_filme(filmes):
    if not filmes:
        print("\nNenhum filme para editar.")
        return

    listar_filmes(filmes)
    indice = ler_opcao_numero("Número do filme a editar: ", 1, len(filmes))
    filme = filmes[indice - 1]

    print("\nDeixe em branco para manter o valor atual.\n")

    novo_titulo = input(f"Título [{filme['titulo']}]: ").strip()
    novo_genero = input(f"Gênero [{filme['genero']}]: ").strip()
    nova_nota = input(f"Nota [{filme['nota']}]: ").strip()
    novo_assistido = input(f"Já assistiu? (S/N) [{filme['assistido']}]: ").strip().upper()

    if novo_titulo:
        filme["titulo"] = novo_titulo
    if novo_genero:
        filme["genero"] = novo_genero
    if nova_nota:
        try:
            valor = float(nova_nota.replace(",", "."))
            if 0 <= valor <= 10:
                filme["nota"] = valor
            else:
                print("Nota fora do intervalo, mantendo a anterior.")
        except ValueError:
            print("Nota inválida, mantendo a anterior.")
    if novo_assistido in ("S", "N"):
        filme["assistido"] = novo_assistido

    salvar_dados(filmes)
    print("\n✅ Filme atualizado!")


def mostrar_estatisticas(filmes):
    if not filmes:
        print("\nNenhum filme cadastrado ainda.")
        return

    total = len(filmes)
    media = sum(f["nota"] for f in filmes) / total
    assistidos = sum(1 for f in filmes if f["assistido"] == "S")
    percentual_assistido = (assistidos / total) * 100

    generos = {}
    for f in filmes:
        generos[f["genero"]] = generos.get(f["genero"], 0) + 1
    genero_top = max(generos, key=generos.get)

    melhor = max(filmes, key=lambda f: f["nota"])

    print("\n===== ESTATÍSTICAS =====\n")
    print(f"🎬 Total de filmes: {total}")
    print(f"⭐ Nota média: {media:.1f}")
    print(f"👀 Assistidos: {assistidos} ({percentual_assistido:.0f}%)")
    print(f"🎭 Gênero mais cadastrado: {genero_top} ({generos[genero_top]} filmes)")
    print(f"🏆 Melhor avaliado: {melhor['titulo']} (nota {melhor['nota']})")


# -----------------------------
# MENU PRINCIPAL
# -----------------------------
def main():
    filmes = carregar_dados()

    while True:
        print("\n" + "=" * 35)
        print("🎬 MOVIE TRACKER")
        print("=" * 35)
        print("1 - Adicionar filme")
        print("2 - Listar filmes")
        print("3 - Pesquisar filme")
        print("4 - Remover filme")
        print("5 - Editar filme")
        print("6 - Ver estatísticas")
        print("7 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            adicionar_filme(filmes)
        elif opcao == "2":
            listar_filmes(filmes)
        elif opcao == "3":
            pesquisar_filme(filmes)
        elif opcao == "4":
            remover_filme(filmes)
        elif opcao == "5":
            editar_filme(filmes)
        elif opcao == "6":
            mostrar_estatisticas(filmes)
        elif opcao == "7":
            print("\nAté logo!")
            break
        else:
            print("\nEscolha uma opção válida.")


if __name__ == "__main__":
    main()
