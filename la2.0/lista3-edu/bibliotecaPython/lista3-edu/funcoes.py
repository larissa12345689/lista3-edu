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
        if livro == i["livro"]:
            print("livro disponível")
            resp = str(input("vc deseja pegar esse livro? digite sim ou não: "))
            if resp == "sim":
                i["status"] = "alugado"
    return listaLivros
listaLivros = [
    {"livro":'pequeno pricipe', "status":'disponivel'},
    {"livro":'sereia', "status":'disponivel'},
    {"livro":'castelo', "status":'disponivel'},
    {"livro":'ratimbum', "status":'disponivel'}
]
emprestar_livro(listaLivros)
print(listaLivros)


def devolver_livro(listaLivros):
    devolucao = str(input("vc deseja devolver algum livro?: "))
    if devolucao == 'sim':
        i['status'] == "disponivel"


devolver_livro(listaLivros)









