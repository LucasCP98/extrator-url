# Expressoes Regulares ou Regex.
import re

# Retirar o CEP com regex dentro do texto. O padrão é: 5 digitos + hifen (opcional) + 3 digitos
endereco = "Rua das Flores, apartamento 1002, Laranjeiras," \
           " Rio de Janeiro, RJ, 23440-120, CPF: 718.457.190-85, cnpj: 00.623.904/0001-73"

"""
Explicação do regex: [0-9] - um digito valido é qualque número entre 0 e 9 | OU letras ex: [a-z]
{5} - quantas vezes o número pode aparecer no caso o padrao do cep se inicia com 5 digitos.
[-] - no padrção do cep tem um traço entre os 5 e 3 numeros.
? - a interrogação indica que pode aparecer o [-] ou não, ou pode usar {0,1} é a mesma coisa.
"""

regex_cep = re.compile("[0-9]{5}-?[0-9]{3}")
regex_cpf = re.compile("[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}")
regex_cnpj = re.compile("[0-9]{2}.?[0-9]{3}.?[0-9]{3}/?[0-9]{4}-?[0-9]{2}")
busca_cep = regex_cep.search(endereco)
busca_cpf = regex_cpf.search(endereco)
busca_cnpj = regex_cpf.search(endereco)

if busca_cep:
    cep = busca_cep.group()
    print(f"CEP: {cep}")

if busca_cpf:
    cpf = busca_cpf.group()
    print(f"CPF: {cpf}")

if busca_cnpj:
    cnpj = busca_cnpj.group()
    print(f"CNPJ: {cnpj}")
