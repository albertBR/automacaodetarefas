# PROGRAMAÇÃO EM PYTHON - AUTOMAÇÃO

# 1 - ABRIR UM SITE
# 2 - FAZER LOGIN
# 3 - IMPORTAR DADOS
# 4 - CADASTRAR 1 PRODUTO
# 5 - REPETIR ATÉ FINALIZAR TODOS OS PRODUTOS

#link usado para automação na aula:  https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
import pandas

pyautogui.PAUSE = 1

# 1 - ABRIR UM SITE
pyautogui.press('win') 
pyautogui.write('chrome') 
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

#informando as informações para o login. 2 - Fazer Login

time.sleep(3)
pyautogui.click(x=470, y=409)
pyautogui.write('albert@gmail.com')
pyautogui.press('tab') #passa para o próximo formulário
pyautogui.write('123456')
pyautogui.press('tab')
pyautogui.press('enter')

#3 -  Importando dados 
# Usaremos a biblioteca pandas para ler a nossa tabela e poder cadastrar os produtos.
tabela = pandas.read_csv('produtos.csv') # Esse código ira o ler o arquivo dentro do diretório
print(tabela)

time.sleep(2)

# 4 - CADASTRAR 1 PRODUTO

# Irei usar uma estrutura de repetição para cadastrar os produtos
for linha  in tabela.index:  # Para cada linha da minha tabela
    
    #codigo
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.click(x=504, y=294)
    pyautogui.write(codigo)
    pyautogui.press('tab')
    
    #marca
    marca =  tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')
    
    #Tipo
    tipo = tabela.loc[linha, 'tipo']  
    pyautogui.write(tipo)
    pyautogui.press('tab')
    
    #Categoria
    categoria = tabela.loc[linha, 'categoria']   
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    
    #Preço
    preco_unitario = tabela.loc[linha, 'preco_unitario']  
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')
    
    #custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')
    
    #Observação
    obs = str(tabela.loc[linha, 'obs'])
    
    if obs != 'nan':                   """Fiz uma condição para saber se terá ou não observação, caso sim o script irá digitar,
                                            caso contrário ñ"""
        pyautogui.write(obs)
        time.sleep(2)  
    pyautogui.press('tab')

    # Salvar
    pyautogui.press('enter')
    
    pyautogui.scroll('10000')
    
    """Para subir a tela use o scroll
    # número positivo = scroll para cima
    # número negativo = scroll para baixo
    """
# Ou # poderá usar esse código: pyautogui.press('home')
   
#4 -  Como repetir esse processo até acabar os produtos no cadastro?

"""Estrei criando uma variavel para receber a tabela usando a função localizador e dentro de colchetes
passarei as informações de linha e a variavel na qual desejo que ele execute
Exemplo do código:
custo = tabela.loc[]
variavel recebe tabela dentro do localizador irei passar de onde eu quero pegar e o local do item.
"""
     
     
