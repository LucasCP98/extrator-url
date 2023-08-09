"""
Verifica se a base da URL está de acordo com o padrão correto.

Exemplos de URLs válidas:
    bytebank.com/cambio
    bytebank.com.br/cambio CERTO
    www.bytebank.com/cambio CERTO
    www.bytebank.com.br/cambio CERTO
    http://www.bytebank.com/cambio CERTO
    http://www.bytebank.com.br/cambio CERTO
    https://www.bytebank.com/cambio CERTO
    https://www.bytebank.com.br/cambio CERTO

"""
import re

texto = "https://www.bytebank.com.br/cambio"

regex_url = re.compile("(https(s)?://)?(www.)?(bytebank.com)(.br)?/cambio")
corresponde_url = regex_url.match(texto)  # Match(corresponde) Ele verifica se o padrão corresponde.

if not corresponde_url:
    raise ValueError("A URL não está de acordo com o padrão setado.")

print("A url é válida.")
