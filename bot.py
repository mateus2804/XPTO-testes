from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import sys

my_email = '32daypython@gmail.com'
password = 'cmbh jyti bvwy mpsl'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://localhost:44379/Servicos")


test_name = "BotSeleniumTest"
cnpj_default = '00.000.000/0000-00'
cpf_default = '000.000.000-00'

driver.maximize_window()




# FUNCAO PARA TESTAR SERVICOS
def testServico():
    #Testando função de registrar
    registerButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/p/a')))
    registerButton.click()
    submitRegisterButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/form/div[3]/input')))
    try:
        submitRegisterButton.click()
        driver.save_screenshot('test.png')
        driver.find_element(By.XPATH, '/html/body/div/div')
        tituloInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Titulo"]')))
        tituloInput.send_keys(test_name)
        tituloInput.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
    except NoSuchElementException:
        sys.exit("ERRO: O Programa esta aceitando servico vazio localizado em https://localhost:44379/Servicos/Create!")


    #Testando função de olhar detalhes
    try:
        elements = driver.find_elements(By.CLASS_NAME, 'datails-service')
        elements[-1].click()
        driver.save_screenshot('test.png')
    except:
        sys.exit("ERRO: Não é possível acessar a página details de serviço localizado em: https://localhost:44379/Servicos/Details")




    #Testando funcoes de editar
    try:
        edit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/a[1]')))
        edit_button.click()
        submitEditButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Titulo"]')))
        submitEditButton.clear()
        submitEditButton.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
        driver.find_element(By.XPATH, '//*[@id="Titulo-error"]')
        submitEditButton.send_keys(test_name)
        submitEditButton.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
    except NoSuchElementException:
        sys.exit("ERRO: O Programa está permitindo submeter serviço editado com titulo em branco: https://localhost:44379/Servicos/Edit")



    #Testando Nome repetido
    serviceButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/div/div[2]/ul/li[1]/a')))
    serviceButton.click()
    registerButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/p/a')))
    registerButton.click()
    try:
        tituloInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Titulo"]')))
        tituloInput.send_keys(test_name)
        tituloInput.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
        driver.find_element(By.XPATH, '/html/body/div/h2')
        serviceButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/div/div[2]/ul/li[1]/a')))
        serviceButton.click()
        driver.save_screenshot('test.png')
    except NoSuchElementException:
        sys.exit("ERRO: O Programa está permitindo criação de serviços com titulos iguais: https://localhost:44379/Servicos/Create")


    # Testando deletar
    try:
        elements = driver.find_elements(By.CLASS_NAME, 'delete-service')
        elements[-1].click()
        delete_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/form/input[1]')))
        delete_button.click()
        driver.save_screenshot('test.png')
    except:
        sys.exit("ERRO: O Programa falhou ao tentar deletar um serviço: https://localhost:44379/Servicos/Delete")








# FUNCAO PARA TESTAR CLIENTES
def testCliente():
    #testando criação de cliente
    ClientesButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/div/div[2]/ul/li[2]/a')))
    ClientesButton.click()
    registerButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/p/a')))
    registerButton.click()

    status = 0
    error_dict = {
        1 : "ERRO: O Programa está permitindo registro de clientes em branco: https://localhost:44379/Servicos/Create",
        2 : "ERRO: O Programa está permitindo registro de clientes com CNPJ em branco: https://localhost:44379/Servicos/Create",
        3 : "ERRO: O Programa está permitindo registro de clientes com nome em branco: https://localhost:44379/Servicos/Create",
        4 : "ERRO: O Programa está permitindo registro de clientes com CNPJ fora do formato: https://localhost:44379/Servicos/Create",
        5 : "ERRO: O Programa está permitindo registro de clientes com CNPJ no formato, mas com letras ao invés de letras: https://localhost:44379/Servicos/Create"
    }
    try:
        submitButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/form/div[3]/input')))
        name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Nome"]')))
        cnpj_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CNPJ"]')))

        #testando se o programa aceita dados vazios
        submitButton.click()
        driver.save_screenshot('test.png')
        status = 1
        driver.find_element(By.XPATH, '//*[@id="Nome-error"]')
        driver.find_element(By.XPATH, '//*[@id="CNPJ-error"]')

        # testando se o programa aceita CNPJ vazio
        name_input.send_keys(test_name)
        submitButton.click()
        driver.save_screenshot('test.png')
        status = 2
        driver.find_element(By.XPATH, '//*[@id="CNPJ-error"]')
        name_input.clear()

        # testando se o programa aceita Nome vazio
        cnpj_input.send_keys(cnpj_default)
        submitButton.click()
        driver.save_screenshot('test.png')
        status = 3
        driver.find_element(By.XPATH, '//*[@id="Nome-error"]')
        cnpj_input.clear()

        # testando se o programa aceita CNPJ fora do formato
        name_input.send_keys(test_name)
        cnpj_input.send_keys(test_name)
        driver.save_screenshot('test.png')
        status = 4
        driver.find_element(By.XPATH, '//*[@id="CNPJ-error"]')
        cnpj_input.send_keys(Keys.ENTER)
        cnpj_input.clear()

        #testando se o programa aceita CNPJ dentro do formato, mas com letras ao invés de números
        cnpj_input.send_keys('aa.aaa.aaa/aaaa-aa')
        cnpj_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
        status = 5
        driver.find_element(By.XPATH, '//*[@id="CNPJ-error"]')
        cnpj_input.clear()
        cnpj_input.send_keys(cnpj_default)
        cnpj_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
    except NoSuchElementException:
        sys.exit(error_dict[status])
    except:
        sys.exit("ERRO: criação de cliente: https://localhost:44379/Clientes/Create")



    #testando acesso a detalhes de clientes
    try:
        elements = driver.find_elements(By.CLASS_NAME, 'details-cliente')
        elements[-1].click()
        driver.save_screenshot('test.png')
    except:
        sys.exit("ERRO: O programa não consegue acessar os detalhes dos clientes!")




    #testando edição de clientes
    error_dict = {
        1: "ERRO: O Programa está permitindo edição de clientes em branco: https://localhost:44379/Servicos/Edit",
        2: "ERRO: O Programa está permitindo edição de clientes com CNPJ em branco: https://localhost:44379/Servicos/Edit",
        3: "ERRO: O Programa está permitindo edição de clientes com nome em branco: https://localhost:44379/Servicos/Edit",
        4: "ERRO: O Programa está permitindo edição de clientes com CNPJ fora do formato: https://localhost:44379/Servicos/Edit",
        5: "ERRO: O Programa está permitindo edição de clientes com CNPJ no formato, mas com letras ao invés de letras: https://localhost:44379/Servicos/Edit"
    }
    try:
        edit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/a[1]')))
        edit_button.click()
        name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Nome"]')))
        cnpj_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CNPJ"]')))

        # testando se o programa aceita dados vazios
        name_input.clear()
        cnpj_input.clear()
        cnpj_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
        status = 1
        driver.find_element(By.XPATH, '//*[@id="Nome-error"]')
        driver.find_element(By.XPATH, '//*[@id="CNPJ-error"]')

        # testando se o programa aceita CNPJ vazio
        name_input.send_keys(test_name)
        name_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
        status = 2
        driver.find_element(By.XPATH, '//*[@id="CNPJ-error"]')
        name_input.clear()

        # testando se o programa aceita Nome vazio
        cnpj_input.send_keys(cnpj_default)
        cnpj_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
        status = 3
        driver.find_element(By.XPATH, '//*[@id="Nome-error"]')
        cnpj_input.clear()

        # testando se o programa aceita CNPJ fora do formato
        name_input.send_keys(test_name)
        cnpj_input.send_keys(test_name)
        driver.save_screenshot('test.png')
        status = 4
        driver.find_element(By.XPATH, '//*[@id="CNPJ-error"]')
        cnpj_input.send_keys(Keys.ENTER)

        cnpj_input.clear()

        # testando se o programa aceita CNPJ dentro do formato, mas com letras ao invés de números
        cnpj_input.send_keys('aa.aaa.aaa/aaaa-aa')
        cnpj_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
        status = 5
        driver.find_element(By.XPATH, '//*[@id="CNPJ-error"]')
        cnpj_input.clear()

        cnpj_input.send_keys(cnpj_default)
        cnpj_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
    except NoSuchElementException:
        sys.exit(error_dict[status])
    except:
        sys.exit("ERRO: edição do cliente https://localhost:44379/Clientes/Edit/")



        # testando criar um cliente com cnpj repetido
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/p/a'))).click()
        name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Nome"]')))
        cnpj_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CNPJ"]')))
        name_input.send_keys(test_name)
        cnpj_input.send_keys(cnpj_default)
        cnpj_input.send_keys(Keys.ENTER)
        driver.find_element(By.XPATH, '/html/body/div/h2')
        driver.save_screenshot('test.png')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/div/div[2]/ul/li[2]/a'))).click()
        driver.save_screenshot('test.png')
    except NoSuchElementException:
        sys.exit(
            "ERRO: Programa está permitindo CNPJ idêntico ser registrado em dois clientes: https://localhost:44379/Clientes/Create")
    except:
        sys.exit("ERRO: erro na criação de cliente: https://localhost:44379/Clientes/Create")



    #testando deletar cliente
    try:
        elements = driver.find_elements(By.CLASS_NAME, 'delete-cliente')
        elements[-1].click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/form/input[1]'))).click()
        driver.save_screenshot('test.png')
    except:
        sys.exit("ERRO: O Programa falhou ao tentar deletar um cliente: https://localhost:44379/Clientes/Delete/")









# FUNCAO PARA TESTAR PRESTADORES
def testPrestador():
    #testando criação de prestador
    PrestadorButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/div/div[2]/ul/li[3]/a')))
    PrestadorButton.click()
    registerButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/p/a')))
    registerButton.click()

    status = 0
    error_dict = {
        1 : "ERRO: O Programa está permitindo registro de prestadores em branco: https://localhost:44379/PrestadorServicos/Create",
        2 : "ERRO: O Programa está permitindo registro de prestadores com CPF em branco: https://localhost:44379/PrestadorServicos/Create",
        3 : "ERRO: O Programa está permitindo registro de prestadores com nome em branco: https://localhost:44379/PrestadorServicos/Create",
        4 : "ERRO: O Programa está permitindo registro de prestadores com CPF fora do formato: https://localhost:44379/PrestadorServicos/Create",
        5 : "ERRO: O Programa está permitindo registro de prestadores com CPF no formato, mas com letras ao invés de letras: https://localhost:44379/PrestadorServicos/Create"
    }
    try:
        submitButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/form/div[3]/input')))
        name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Nome"]')))
        cpf_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CPF"]')))

        #testando se o programa aceita dados vazios
        submitButton.click()
        driver.save_screenshot('test.png')
        status = 1
        driver.find_element(By.XPATH, '//*[@id="Nome-error"]')
        driver.find_element(By.XPATH, '//*[@id="CPF-error"]')

        # testando se o programa aceita CPF vazio
        name_input.send_keys(test_name)
        submitButton.click()
        driver.save_screenshot('test.png')
        status = 2
        driver.find_element(By.XPATH, '//*[@id="CPF-error"]')
        name_input.clear()

        # testando se o programa aceita Nome vazio
        cpf_input.send_keys(cpf_default)
        submitButton.click()
        driver.save_screenshot('test.png')
        status = 3
        driver.find_element(By.XPATH, '//*[@id="Nome-error"]')
        cpf_input.clear()

        # testando se o programa aceita CPF fora do formato
        name_input.send_keys(test_name)
        cpf_input.send_keys(test_name)
        driver.save_screenshot('test.png')
        status = 4
        driver.find_element(By.XPATH, '//*[@id="CPF-error"]')
        cpf_input.send_keys(Keys.ENTER)
        cpf_input.clear()

        #testando se o programa aceita CPF dentro do formato, mas com letras ao invés de números
        cpf_input.send_keys('aaa.aaa.aaa-aa')
        cpf_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
        status = 5
        driver.find_element(By.XPATH, '//*[@id="CPF-error"]')
        cpf_input.clear()
        cpf_input.send_keys(cpf_default)
        cpf_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
    except NoSuchElementException:
        sys.exit(error_dict[status])
    except:
        sys.exit("ERRO: criação de prestador: https://localhost:44379/PrestadorServicos/Create")



    #testando acesso a detalhes de prestador
    try:
        elements = driver.find_elements(By.CLASS_NAME, 'details-prestador')
        elements[-1].click()
        driver.save_screenshot('test.png')
    except:
        sys.exit("ERRO: O programa não consegue acessar os detalhes dos prestadores!")
    #testando edição de prestador
    error_dict = {
        1: "ERRO: O Programa está permitindo edição de prestadores em branco: https://localhost:44379/PrestadorServicos/Edit",
        2: "ERRO: O Programa está permitindo edição de prestadores com CPF em branco: https://localhost:44379/PrestadorServicos/Edit",
        3: "ERRO: O Programa está permitindo edição de prestadores com nome em branco: https://localhost:44379/PrestadorServicos/Edit",
        4: "ERRO: O Programa está permitindo edição de prestadores com CPF fora do formato: https://localhost:44379/PrestadorServicos/Edit",
        5: "ERRO: O Programa está permitindo edição de prestadores com CPF no formato, mas com letras ao invés de letras: https://localhost:44379/PrestadorServicos/Edit"
    }
    try:
        edit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/a[1]')))
        edit_button.click()
        name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Nome"]')))
        cpf_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CPF"]')))

        # testando se o programa aceita dados vazios
        name_input.clear()
        cpf_input.clear()
        cpf_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
        status = 1
        driver.find_element(By.XPATH, '//*[@id="Nome-error"]')
        driver.find_element(By.XPATH, '//*[@id="CPF-error"]')

        # testando se o programa aceita CPF vazio
        name_input.send_keys(test_name)
        name_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
        status = 2
        driver.find_element(By.XPATH, '//*[@id="CPF-error"]')
        name_input.clear()

        # testando se o programa aceita Nome vazio
        cpf_input.send_keys(cpf_default)
        cpf_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
        status = 3
        driver.find_element(By.XPATH, '//*[@id="Nome-error"]')
        cpf_input.clear()

        # testando se o programa aceita CPF fora do formato
        name_input.send_keys(test_name)
        cpf_input.send_keys(test_name)
        driver.save_screenshot('test.png')
        status = 4
        driver.find_element(By.XPATH, '//*[@id="CPF-error"]')
        cpf_input.send_keys(Keys.ENTER)

        cpf_input.clear()

        # testando se o programa aceita CPF dentro do formato, mas com letras ao invés de números
        cpf_input.send_keys('aaa.aaa.aaa-aa')
        cpf_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
        status = 5
        driver.find_element(By.XPATH, '//*[@id="CPF-error"]')
        cpf_input.clear()

        cpf_input.send_keys(cpf_default)
        cpf_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
    except NoSuchElementException:
        sys.exit(error_dict[status])
    except:
        sys.exit("ERRO: edição do prestador https://localhost:44379/PrestadorServicos/Edit/")




    #testando criar um cliente com CPF repetido
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/p/a'))).click()
        name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Nome"]')))
        cpf_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CPF"]')))
        name_input.send_keys(test_name)
        cpf_input.send_keys(cpf_default)
        cpf_input.send_keys(Keys.ENTER)
        driver.find_element(By.XPATH, '/html/body/div/h2')
        driver.save_screenshot('test.png')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/div/div[2]/ul/li[3]/a'))).click()
        driver.save_screenshot('test.png')
    except NoSuchElementException:
        sys.exit("ERRO: Programa está permitindo CPF idêntico ser registrado em dois prestadores: https://localhost:44379/PrestadorServicos/Create")
    except:
        sys.exit("ERRO: erro na criação de prestador: https://localhost:44379/PrestadorServicos/Create")



    #testando deletar prestador
    try:
        elements = driver.find_elements(By.CLASS_NAME, 'delete-prestador')
        elements[-1].click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/form/input[1]'))).click()
        driver.save_screenshot('test.png')
    except:
        sys.exit("ERRO: O Programa falhou ao tentar deletar um prestador: https://localhost:44379/PrestadorServicos/Delete/")




def testOS():
    # Testando função de registrar servico
    driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/ul/li[1]/a').click()
    registerButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/p/a')))
    registerButton.click()
    submitRegisterButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/form/div[3]/input')))
    try:
        submitRegisterButton.click()
        driver.save_screenshot('test.png')
        driver.find_element(By.XPATH, '/html/body/div/div')
        tituloInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Titulo"]')))
        tituloInput.send_keys(test_name)
        tituloInput.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
    except NoSuchElementException:
        sys.exit("ERRO: O Programa esta aceitando servico vazio localizado em https://localhost:44379/Servicos/Create!")

    # testando criação de cliente
    ClientesButton = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/div/div[2]/ul/li[2]/a')))
    ClientesButton.click()
    registerButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/p/a')))
    registerButton.click()

    status = 0
    error_dict = {
        1: "ERRO: O Programa está permitindo registro de clientes em branco: https://localhost:44379/Servicos/Create",
        2: "ERRO: O Programa está permitindo registro de clientes com CNPJ em branco: https://localhost:44379/Servicos/Create",
        3: "ERRO: O Programa está permitindo registro de clientes com nome em branco: https://localhost:44379/Servicos/Create",
        4: "ERRO: O Programa está permitindo registro de clientes com CNPJ fora do formato: https://localhost:44379/Servicos/Create",
        5: "ERRO: O Programa está permitindo registro de clientes com CNPJ no formato, mas com letras ao invés de letras: https://localhost:44379/Servicos/Create"
    }
    try:
        submitButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/form/div[3]/input')))
        name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Nome"]')))
        cnpj_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CNPJ"]')))

        # testando se o programa aceita dados vazios
        submitButton.click()
        driver.save_screenshot('test.png')
        status = 1
        driver.find_element(By.XPATH, '//*[@id="Nome-error"]')
        driver.find_element(By.XPATH, '//*[@id="CNPJ-error"]')

        # testando se o programa aceita CNPJ vazio
        name_input.send_keys(test_name)
        submitButton.click()
        driver.save_screenshot('test.png')
        status = 2
        driver.find_element(By.XPATH, '//*[@id="CNPJ-error"]')
        name_input.clear()

        # testando se o programa aceita Nome vazio
        cnpj_input.send_keys(cnpj_default)
        submitButton.click()
        driver.save_screenshot('test.png')
        status = 3
        driver.find_element(By.XPATH, '//*[@id="Nome-error"]')
        cnpj_input.clear()

        # testando se o programa aceita CNPJ fora do formato
        name_input.send_keys(test_name)
        cnpj_input.send_keys(test_name)
        driver.save_screenshot('test.png')
        status = 4
        driver.find_element(By.XPATH, '//*[@id="CNPJ-error"]')
        cnpj_input.send_keys(Keys.ENTER)
        cnpj_input.clear()

        # testando se o programa aceita CNPJ dentro do formato, mas com letras ao invés de números
        cnpj_input.send_keys('aa.aaa.aaa/aaaa-aa')
        cnpj_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
        status = 5
        driver.find_element(By.XPATH, '//*[@id="CNPJ-error"]')
        cnpj_input.clear()
        cnpj_input.send_keys(cnpj_default)
        cnpj_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
    except NoSuchElementException:
        sys.exit(error_dict[status])
    except:
        sys.exit("ERRO: criação de cliente: https://localhost:44379/Clientes/Create")

    # testando criação de prestador
    PrestadorButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/div/div[2]/ul/li[3]/a')))
    PrestadorButton.click()
    registerButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/p/a')))
    registerButton.click()

    status = 0
    error_dict = {
        1: "ERRO: O Programa está permitindo registro de prestadores em branco: https://localhost:44379/PrestadorServicos/Create",
        2: "ERRO: O Programa está permitindo registro de prestadores com CPF em branco: https://localhost:44379/PrestadorServicos/Create",
        3: "ERRO: O Programa está permitindo registro de prestadores com nome em branco: https://localhost:44379/PrestadorServicos/Create",
        4: "ERRO: O Programa está permitindo registro de prestadores com CPF fora do formato: https://localhost:44379/PrestadorServicos/Create",
        5: "ERRO: O Programa está permitindo registro de prestadores com CPF no formato, mas com letras ao invés de letras: https://localhost:44379/PrestadorServicos/Create"
    }
    try:
        submitButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/form/div[3]/input')))
        name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Nome"]')))
        cpf_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CPF"]')))

        # testando se o programa aceita dados vazios
        submitButton.click()
        driver.save_screenshot('test.png')
        status = 1
        driver.find_element(By.XPATH, '//*[@id="Nome-error"]')
        driver.find_element(By.XPATH, '//*[@id="CPF-error"]')

        # testando se o programa aceita CPF vazio
        name_input.send_keys(test_name)
        submitButton.click()
        driver.save_screenshot('test.png')
        status = 2
        driver.find_element(By.XPATH, '//*[@id="CPF-error"]')
        name_input.clear()

        # testando se o programa aceita Nome vazio
        cpf_input.send_keys(cpf_default)
        submitButton.click()
        driver.save_screenshot('test.png')
        status = 3
        driver.find_element(By.XPATH, '//*[@id="Nome-error"]')
        cpf_input.clear()

        # testando se o programa aceita CPF fora do formato
        name_input.send_keys(test_name)
        cpf_input.send_keys(test_name)
        driver.save_screenshot('test.png')
        status = 4
        driver.find_element(By.XPATH, '//*[@id="CPF-error"]')
        cpf_input.send_keys(Keys.ENTER)
        cpf_input.clear()

        # testando se o programa aceita CPF dentro do formato, mas com letras ao invés de números
        cpf_input.send_keys('aaa.aaa.aaa-aa')
        cpf_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
        status = 5
        driver.find_element(By.XPATH, '//*[@id="CPF-error"]')
        cpf_input.clear()
        cpf_input.send_keys(cpf_default)
        cpf_input.send_keys(Keys.ENTER)
        driver.save_screenshot('test.png')
    except NoSuchElementException:
        sys.exit(error_dict[status])
    except:
        sys.exit("ERRO: criação de prestador: https://localhost:44379/PrestadorServicos/Create")


    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/div/div[2]/ul/li[4]/a'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/p[1]/a'))).click()
    error_dict = {
        1 : "ERRO: Programa aceita ordem de serviço vazia: https://localhost:44379/OSs/Create",
        2 : "ERRO: Programa aceita letra em valor decimal: https://localhost:44379/OSs/Create",
        3 : "ERRO: Programa aceita valor = 0: https://localhost:44379/OSs/Create",
        4 : "ERRO: Programa aceita valores menores que 0: https://localhost:44379/OSs/Create",
    }
    try:
        submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/form/div[6]/input')))
        submit_button.click()
        driver.save_screenshot('test.png')
        status = 1
        driver.find_element(By.XPATH, '// *[ @ id = "OS_ValorServico-error"]')
        servicos = driver.find_elements(By.CSS_SELECTOR, '#OS_ServicoId option')
        for s in servicos:
            if s.text == test_name:
                s.click()
        clientes = driver.find_elements(By.CSS_SELECTOR, '#OS_ClienteId option')
        for s in clientes:
            if s.text == test_name:
                s.click()
        prestadores = driver.find_elements(By.CSS_SELECTOR, '#OS_PrestadorServicoId option')
        for s in prestadores:
            if s.text == test_name:
                s.click()
        valor_input = driver.find_element(By.XPATH, '//*[@id="OS_ValorServico"]')
        valor_input.send_keys(test_name)
        submit_button.click()
        valor_input.clear()
        driver.save_screenshot('test.png')
        status = 2
        driver.find_element(By.XPATH, '// *[ @ id = "OS_ValorServico-error"]')
        valor_input.send_keys(str(0))
        submit_button.click()
        valor_input.clear()
        driver.save_screenshot('test.png')
        status = 3
        driver.find_element(By.XPATH, '// *[ @ id = "OS_ValorServico-error"]')
        valor_input.send_keys(str(-1))
        submit_button.click()
        valor_input.clear()
        driver.save_screenshot('test.png')
        status = 4
        driver.find_element(By.XPATH, '// *[ @ id = "OS_ValorServico-error"]')
        valor_input.send_keys(str(123123))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="OS_DataExecucao"]'))).send_keys("12/04/2024")
        valor_input.send_keys(Keys.ENTER)
    except NoSuchElementException:
        sys.exit(error_dict[status])

        # Testando deletar servicos
    try:
        driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/ul/li[1]/a').click()
        elements = driver.find_elements(By.CLASS_NAME, 'delete-service')
        elements[-1].click()
        delete_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/form/input[1]')))
        delete_button.click()
        driver.save_screenshot('test.png')
    except:
        sys.exit("ERRO: O Programa falhou ao tentar deletar um serviço: https://localhost:44379/Servicos/Delete")



        # testando deletar prestador
    try:
        driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/ul/li[3]/a').click()
        elements = driver.find_elements(By.CLASS_NAME, 'delete-prestador')
        elements[-1].click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/form/input[1]'))).click()
        driver.save_screenshot('test.png')
    except:
        sys.exit(
            "ERRO: O Programa falhou ao tentar deletar um prestador: https://localhost:44379/PrestadorServicos/Delete/")



    # testando deletar cliente
    try:
        driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/ul/li[2]/a').click()
        elements = driver.find_elements(By.CLASS_NAME, 'delete-cliente')
        elements[-1].click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/form/input[1]'))).click()
        driver.save_screenshot('test.png')
    except:
        sys.exit("ERRO: O Programa falhou ao tentar deletar um cliente: https://localhost:44379/Clientes/Delete/")



testServico()
testCliente()
testPrestador()
testOS()
driver.quit()
print("Todos os teste foram bem sucedidos!")