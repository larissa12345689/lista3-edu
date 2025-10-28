
# def adicionar_livro(listaLivros):
#     if livro == disponível:
#         obra = str(input("digite o título da obra: "))
#         autor = str(input("digite o autor da obra: "))
#         if status == disponivel:
#             print('esse livro está disponivel!')

# def emprestar_livro(listaLivros):
#     adicionar_livro()
#     if status != disponivel:
#         print('seu livro não está disponivel')

def adicionar_livro(listaLivros):
    obra = str(input("digite o título da obra: "))
    autor = str(input("digite o autor da obra: "))
    status = "disponível"

    dict = {
        "nome":obra,
        "autor":autor,
        "status": status
    }
    listaLivros.append(dict)
    return "status"
    return listaLivros


def emprestar_livro(listaLivros):
    livro = str(input("qual livro vc deseja pegar?:  "))
    for i in listaLivros:
        if livro == i:
            print("livro disponível")
            resp = str(input("vc deseja pegar esse livro? digite sim ou não: "))
            if resp == "sim":
                for i[livro] in listaLivros:
                    listaLivros.remove(livro)
                    status = "indisponível"

listaLivros = ['pequeno pricipe', 'alice no pais das maravilhas', 'vento nos salgueiros']

adicionar_livro(listaLivros)
emprestar_livro(listaLivros)












