import pytest  # Engine do teste
import requests  # Biblioteca para manipular API's (comunicação)

base_url = 'https://petstore.swagger.io/v2'  # Endereço da API (BaseURL)
headers = {'Content-Type': 'application/json'}  # Informando que os dados serão em Json

class TestApi:

    def testar_incluir_pet(self): # POST
        # Configura (Dados de entrada - valores, resultado esperado)
        status_code_esperado = 200
        nome_pet_esperado = 'Caramelinho'
        tag_esperada = 'Vacinado'

        # Executa os testes
        resultado_obtido = requests.post(url=base_url + '/pet',
                      data=open('C:\\Users\\Particular\\PycharmProjects\\133pets\\vendors\\json\\pet1.json', 'rb'),
                      headers=headers
                      ) # comando POST da API

        # Valida a assertividade dos resultados
        print(resultado_obtido)
        corpo_da_resposta = resultado_obtido.json() # Extrai a reposta no formato JSON para análise dos dados
        print(corpo_da_resposta)
        assert resultado_obtido.status_code == status_code_esperado
        assert corpo_da_resposta['name'] == nome_pet_esperado
        assert corpo_da_resposta['tags'][0]['name'] == tag_esperada

    def testar_consultar_pet(self): # GET

        # 1. Configura
        # 1.1 Dados de Entrada
        pet_id = 410504

        # 1.2 Resultados Esperados
        status_code_esperado = 200
        nome_pet_esperado = 'Caramelinho'
        tag_esperada = 'Vacinado'

        # 2. Executa
        resultado_obtido = requests.get(url=base_url + '/pet/' + '410504',
                                        headers=headers) # Comando GET

        # 3. Valida
        print(resultado_obtido)
        corpo_da_resposta = resultado_obtido.json()
        print(corpo_da_resposta)
        assert resultado_obtido.status_code == status_code_esperado
        assert corpo_da_resposta['name'] == nome_pet_esperado
        assert corpo_da_resposta['tags'][0]['name'] == tag_esperada


    def testar_alterar_pet(self):  # PUT
        # 1. Configura
        # Resultados Esperados
        status_code_esperado = 200
        nome_pet_esperado = 'Caramelinho'
        status_esperado = 'Vendido'

        # 2. Executa
        resultado_obtido = requests.put(url=base_url + '/pet',
                                        data=open('C:\\Users\\Particular\\PycharmProjects\\133pets\\vendors\\json\\pet2.json', 'rb'),
                                        headers=headers)

        # 3. Valida
        assert resultado_obtido.status_code == status_code_esperado
        corpo_da_resposta = resultado_obtido.json() # Exrtai o arquivo Json para consulta
        print(corpo_da_resposta)
        assert corpo_da_resposta['name'] == nome_pet_esperado # Busca o campo Name e compara com Variavel declarada
        assert corpo_da_resposta['status'] == status_esperado # Busca o campo status e compara com Variavel declarada

    def testar_deletar_pet(self): # Delete
        # Configura
        pet_id = 410504
        status_code_esperado = 200  # Pet Not Found
        code_esperado = 200  # Endpoint
        type_esperado = 'unknown'  # Endpoint
        message_esperada = str(pet_id)  # Endpoint

        # Executa
        resultado_obtido = requests.delete(url=base_url + '/pet/' + '410504',
                                           headers=headers) # Comando DELETE

        # Valida
        print(resultado_obtido)
        response_body = resultado_obtido.json()
        print(response_body)
        assert resultado_obtido.status_code == status_code_esperado
        assert response_body['code'] == code_esperado
        assert response_body['type'] == type_esperado
        assert response_body['message'] == message_esperada

    def testar_consultar_pet_deleted(self): # GET (Consultar apos Delete)
        # 1. Configura
        pet_id = 410504
        status_code_esperado = 404

        # 2. Executa
        resultado_obtido = requests.get(url=base_url + '/pet/' + '410504',
                                        headers=headers) # Comando GET

        # 3. Valida
        print(resultado_obtido)
        corpo_da_resposta = resultado_obtido.json()
        assert resultado_obtido.status_code == status_code_esperado
