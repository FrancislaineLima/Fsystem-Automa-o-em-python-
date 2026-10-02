import pyautogui as py
import time

py.PAUSE=0.5



py.press("win")
py.write("Sistema de Controle de Produto")
py.press("enter")
time.sleep(10)#faz 3seg de pausa para entrar no site

py.click(x=801, y=534) #uso a posição (que foi feita com o auxiliar) para fazer o bot clicar na parte do email
py.typewrite("francislaine@gmail.com", interval=0.15)#aqui vc põe o seu loguin
time.sleep(1)   
py.press("tab")
#py.click(x=812, y=635)#usar a posiçao novamente, mas agora para colocar a senha
#mas irei usar o tab
py.write("francislaine123", interval=0.1)#aqui vc põe o seu loguin
py.press("enter")
time.sleep(3)


import pandas as pd

tabela= pd.read_csv("AULA 1/produtos.csv")
print (tabela)

for linha in tabela.index:

    py.click(x=229, y=339)
    
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    py.write(str(codigo))
    # passar para o proximo campo
    py.press("tab")
    # preencher o campo
    py.write(str(tabela.loc[linha, "marca"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "tipo"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "categoria"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "preco_unitario"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "custo"]))
    py.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        py.write(str(tabela.loc[linha, "obs"]))
    py.press("tab")
    py.press("enter") # cadastra o produto (botao enviar)
    time.sleep(0.5)