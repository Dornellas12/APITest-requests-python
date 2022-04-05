# Testes de API relacionado a entidade USER

import requests
import pytest

base_url = 'https://petstore.swagger.io/v2'
headers = {'Content-Type': 'application/json'}

def testar_incluir_user():  # POST
    # Configura
    status_code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = '35700'

    # Executa

    resultado_obtido = requests.post(url=base_url + '/user',
                                     data=open('C:\\Users\\Particular\\PycharmProjects\\133pets\\vendors\\json\\user.json','rb'),
                                     headers=headers
                                     )  # Post com dados requisitados (Body, Dados e Headers)

    #Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperada

def testar_consultar_user():  # GET
    # Configura
    username_atual = 'Dornellas12'
    email_esperado = 'teste123@hotmail.com'
    phone_esperado = '19994030550'
    status_code_esperado = 200

    # Executa
    resultado_obtido = requests.get(url=base_url + '/user/' + username_atual,
                                    headers=headers)
    # Valida
    print(resultado_obtido)
    message_body = resultado_obtido.json()
    print(message_body)
    assert resultado_obtido.status_code == status_code_esperado
    assert message_body['email'] == email_esperado
    assert message_body['username'] == username_atual
    assert message_body['phone'] == phone_esperado

def testar_editar_user():  # PUT
    # Configura
    status_code_esperado = 200
    username_atual = 'Dornellas12'
    type_esperado = 'unknown'
    message_esperada = '35700'


    # Executa
    resultado_obtido = requests.put(url=base_url + '/user/' + username_atual,
                                    data=open('C:\\Users\\Particular\\PycharmProjects\\133pets\\vendors\\json\\user2.json','rb'),
                                    headers=headers)

    # Valida
    print(resultado_obtido)
    message_body = resultado_obtido.json()
    print(message_body)
    assert resultado_obtido.status_code == status_code_esperado
    assert message_body['type'] == type_esperado
    assert message_body['message'] == message_esperada

def testar_deletar_user():  # DELETE
    # Configura
    username_atual = "Dornellas13"
    status_code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = 'Dornellas13'

    # Executa
    resultado_obtido = requests.delete(url=base_url + "/user/" + username_atual,
                                       headers=headers
                                       )

    # Valida
    print(resultado_obtido)
    message_body = resultado_obtido.json()
    print(message_body)
    assert resultado_obtido.status_code == status_code_esperado
    assert message_body['type'] == type_esperado
    assert message_body['message'] == message_esperada
