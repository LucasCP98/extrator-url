# url = 'http://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real'
url = ' '

# Sanitização da URL.
url = url.strip()

# Validação da url
if url == "":
    # "Raise" Serve para quando você quer retorna um erro para o usuario.
    raise ValueError("A url está vazia.")

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao + 1:]
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
    print(valor)
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
    print(valor)


