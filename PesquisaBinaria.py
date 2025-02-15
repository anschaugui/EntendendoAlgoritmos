def pesquisa_binaria(lista, item):
        baixo = 0
        alto = len(lista) - 1
        while baixo <= alto:
            meio = (baixo + alto) // 2
            chute = lista[meio]
            if chute == item:
                return meio
                alto = meio - 1
            else:
                baixo = meio + 1
                return None
        minha_lista = [1, 3, 5, 7, 9]
        print(pesquisa_binaria(minha_lista, 3)) # => 1
        print(pesquisa_binaria(minha_lista, -1)) # => None5


# def pesquisa_binaria(lista_de_numeros, valor_pesquisado):
#     primeiro_indice = 0
#     tamanho = len(lista_de_numeros)
#     ultimo_indice = tamanho - 1
#     indice_elemento_do_meio = (primeiro_indice + ultimo_indice) // 2
#     elemento_do_meio = lista_de_numeros[indice_elemento_do_meio]
#     encontrado = True
#     while encontrado:
#         if primeiro_indice == ultimo_indice:
#             if indice_elemento_do_meio != valor_pesquisado:
#                 encontrado: False
#                 return "Não aparee na lista"
#
#             elif elemento_do_meio > valor_pesquisado:
#                 nova_posicao = indice_elemento_do_meio - 1
#                 ultimo_indice = nova_posicao
#                 indice_elemento_do_meio = (primeiro_indice + ultimo_indice) // 2
#                 elemento_do_meio = lista_de_numeros[indice_elemento_do_meio]
#                 if elemento_do_meio == valor_pesquisado:
#                     return f"{elemento_do_meio} encontrado na posição {indice_elemento_do_meio}"
#
#                 elif elemento_do_meio < valor_pesquisado:
#                     nova_posicao = indice_elemento_do_meio + 1
#                     primeiro_indice = nova_posicao
#                     indice_elemento_do_meio = (primeiro_indice + ultimo_indice) // 2
#                     elemento_do_meio = lista_de_numeros[indice_elemento_do_meio]
#                     if elemento_do_meio == valor_pesquisado:
#                         return f"{elemento_do_meio} encontrado na posição {indice_elemento_do_meio}"
#
#                     lista = [16 , 18 , 20 , 50 , 60 , 81 , 84 , 89]
#                     print(pesquisa_binaria(lista , 81)) # -> 5
#                     print(pesquisa_binaria(lista , 10)) # -> Não aparece na lista (none)