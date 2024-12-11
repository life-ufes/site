---
title: "Tutorial de uso da impressora térmica"
classes: wide
header:
  teaser: "https://d2u2qhufg0q9tn.cloudfront.net/assets/arquivos/imgDetProduto_2abd6164-4089-41da-8127-b02433ba0527_L42%20PRO%20FULL%2007.png"
categories:
  - Wiki
---
### Passo 1: Instalação do driver da impressora

  - Para começar, vá até o [site oficial da Elgin](https://www.elgin.com.br/Produtos/automacao/impressoras-de-etiqueta/impressora-de-etiqueta-l42pro) e desça a página até o final, onde estará a aba "Download Center". 
  - Lá, clique para baixar o Linux Driver. Isso instalará uma pasta do tipo ".zip", que deve ser extraída no local de interesse de instalação. 
  - Dentro da pasta extraída, abra a subpasta "setup" no terminal e execute os seguintes comandos:
  ```python
  chmod +x install
  sudo ./install
  ```
  - Pronto, agora o driver deve estar instalado.

### Passo 2: Calibrar a impressora

  - Ligue a impressora, conectando-a à tomada e clicando no botão em sua parte traseira.
  - Aguarde até que as luzes vermelha e amarela se apaguem, restando acesa apenas a verde.
  - Aperte e segure o botão **"FEED"** até que a luz verde pisque 2 vezes.
  - Feito isso, a impressora se auto calibrará, liberando algumas etiquetas no processo. 
  - Aguarde até que a impressora pare de fazer barulho.

### Passo 3: Conectar a impressora ao computador

  - Conecte o cabo USB branco à impressora e ao computador.
  - Procure por **"Printers"/"Impressoras"** na barra de pesquisa do menu e selecione a opção de mesmo nome.
  - Clique em **"Add"/"Adicionar"** e, em seguida, no nome da sua impressora.
  - Prossiga clicando em **"Forward"/"Seguinte"** e **"Apply"/"Aplicar"**, para adicionar a impressora recém conectada ao computador.
  - Vá em **"Printers"/"Impressoras"**, clique na impressora e, em seguida, em **"Printer Options"/ "Opções de impressão"**.
  - Lá, altere o campo **"Method"/ "Método"** para **"Direct Thermal"**.
  - A partir daqui, a impressora está **pronta para uso**.

### Observações:

  - A impressora pode apresentar um offset no topo da impressão, então conte com isso no desenvolvimento do seu projeto.
  - É possível imprimir em vários formatos distintos de etiquetas na impressora em questão, então são necessários ajustes no modo de impressão e testes a cada mudança.
  - Para a etiqueta de 9x15cm, utilizamos o formato de impressão 100x150mm. Com ele, obtivemos o melhor resultado de impressão, mas isso pode variar dependendo do projeto.
  - Já para a etiqueta de 4x6cm, utilizamos o modo de impressão 57x45mm.

  - Fizemos esse exemplo para a etiqueta grande: [link do canva](https://www.canva.com/design/DAGVm2Vhz3o/Gb82Dhqk3eZMw0oMMPSggQ/edit?utm_content=DAGVm2Vhz3o&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

  - Fizemos esse exemplo para a etiqueta pequena: [link do canva](https://www.canva.com/design/DAGVm8v9dQM/z2wqgofF6_v916d9Byz-nQ/edit?utm_content=DAGVm8v9dQM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
