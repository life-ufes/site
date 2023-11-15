---
title: Como criar um ambiente virtual em Python
author: paaatcha
classes: wide
toc: true
categories:
  - Wiki
---

Um ambiente virtual (ou em inglês *virtual environment*) é uma ferramenta para gerenciar dependências e isolar projetos em Python. A ideia é que funcione similar a um container Docker, mas de maneira muito mais simples. Se você não sabe nada sobre o assunto, sugiro que dê uma olhada [neste vídeo](https://www.youtube.com/watch?v=f_Rf2ZnV1Mk) ou [neste artigo.](https://docs.python.org/pt-br/3/library/venv.html)

De forma bem resumida, você vai criar um ambiente e instalar todos os seus pacotes via `pip` e eles ficarão isolados lá dentro. Toda vez que você quiser usar esse ambiente você vai ter que **ativá-lo**. A grande vantagem é que tudo dentro desse ambiente fica isolado, o que facilita o gerenciamento de dependências de um projeto.


## Criação do ambiente usando `virtualenv`

A criação de um ambiente virtual é relativamente simples. Neste tutorial vamos utilizar o `virtualenv`. Mas é possível obter resultados similares usando `conda` e/ou `PyEnv`.

___

**Nota**: o ambiente será criado usando o sistema operacional Linux. Se você usa windows e possui o miniconda ou anaconda instalado, você consegue repetir esses passos utilizando o [PowerShell](https://docs.microsoft.com/en-us/powershell/).

___


### Passo a passo da criação do ambiente virtual
1. **Instalação**: primeiro precisamos instalar o `virtualenv`. Para isso, utilizaremos o seguinte comando no terminal:
    ```
    $ python -m pip install --user virtualenv
    ```

2. **Criação do ambiente**: para criar o ambiente virtual, execute o seguinte comando no terminal:

    ```
    $ python -m venv <nome_do_ambiente>
    ```
    O termo `<nome_do_ambiente>` é o nome que você vai dar para o seu ambiente, por exemplo, `gandalf` (vamos usar esse nome daqui para frente).

3. **Ativando o ambiente**: agora que você criou o ambiente, você precisa ativá-lo para começar a utilizar. Para ativar você executa o seguinte comando na mesma pasta que você executou o passo anterior:
      ```
      $ source gandalf/bin/activate
      ```
      Assim que você ativar, você vai ver algo do tipo no seu terminal:
      ```
      (gandalf) [user@machine] $
      ```
      Isso significa que você está **dentro** do ambiente virtual de nome `gandalf`. Se você instalar algum pacote, usando `pip` por exemplo, ele só existirá dentro desse ambiente. Em outras palavras, ele está isolado da sua máquina. Se você apagar o ambiente, nada é afetado na sua máquina ou em outros ambientes que você possuir. Todavia, sempre que você quiser usar o ambiente, você vai ter que ativá-lo.

4. **Desativando o ambiente**: para desativar um ambiente, basta executar:
      ```
      $ deactivate
      ```
      Obviamente, o ambiente precisa estar ativo para ser desativado. Além disso, se você fechar o terminal, ele também será desativado.


