#Primeiro passo anotar o passo a passo do projeto de automação

- Entrar na planilha
- Copiar informações de um campo e colar no seu campo correspondente
- Repetir o passo até finalizar a página
- clicar em próxima
- Repetir os passos e ir para a próxima página (pg 2)
- Repetir os passos e finalizar o cadastro daquele produto e clicar em concluir
- Clicar em ok, para finalizar o processo
- Clicar em ok na msg de confirmação de salvamento no banco de dados
- Clicar em add mais um e repetir o processo até finalizar a planilha

Baixar
#PyAutoGUI (automação de clicks e teclado)
#Openpyxl (leitura e automação de planilhas)

--
pip install openpyxl pyAutoGUI   
--

no terminal da maq é preciso instalar para pegar as coordenadas do mouse
---
pip install mouseinfo
---
após instalar use os comandos
 python
 from mouseinfo import mouseInfo
 mouseInfo()

 esse comando vai abrir a janela de coordenadas
 F6 grava a coordenada 

