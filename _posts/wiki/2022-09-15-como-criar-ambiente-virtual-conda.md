---
title: Como criar um conda virtual environment
author: paaatcha
classes: wide
header:
  teaser: "/assets/imgs/posts/conda.png"
categories:
  - Wiki
---

Um ambiente virtual (ou em inglês *virtual environment*) pode ser criado a usando o gerenciador `conda`. Para mais informações sobre ambientes virtuais, de uma olhada no post [Como criar um ambiente virtual em Python](http://pachecoandre.com.br/2021/09/13/como-criar-python-env.html)


## Criação do ambiente usando `conda`

Antes de mais nada, duas observações imporantes:

- **Observação 1:** obviamente, para criar um ambiente virtual com `conda` você precisa ter o gerenciador instalado na sua máquina. Você pode obter isso instalando o [miniconda](https://docs.conda.io/en/latest/miniconda.html#installing) ou o [anaconda](https://www.anaconda.com/products/individual).
  
- **Observação 2:** esse tutorial é um resumo da documentação oficial do `conda`. Portanto, para uma versão mais completa, [acesse aqui](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#specifying-a-location-for-an-environmenthttps://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#specifying-a-location-for-an-environment)


___

**Nota**: o ambiente será criado usando o sistema operacional Linux. Se você usa windows e possui o miniconda ou anaconda instalado, você consegue repetir esses passos utilizando o [PowerShell](https://docs.microsoft.com/en-us/powershell/).

___



### Passo a passo da criação do ambiente virtual
1. O comando padrão para criar um ambiente usando conda é o seguinte:
    ```
    $ conda create --name <nome_do_ambiente>
    ```
    O termo `<nome_do_ambiente>` é o nome que você vai dar para o seu ambiente, por exemplo, `gandalf` (vamos usar esse nome daqui para frente). Esse comando vai criar um ambiente dentro da pasta padrão do `conda` (normalmente, `(ana)conda/env`). Para criar um ambiente em outra pasta qualquer, você pode usar:
    ```
    $ conda create --prefix <path/nome_do_ambiente>
    ```

2. Para tivar o ambiente, você deve usar o seguinte comando:
    ```
    $ conda activate <path/nome_do_ambiente>
    ```
    Após ativado, você vai ver algo do tipo no seu terminal:
    ```
    (path/ate/seu/ambiente) $
    ```

___

Criar um ambiente fora da pasta padrão do `conda`, ou seja, passando um `path` junto com o nome da imagem, possui algumas vantagens, dentre elas:
-  Organizar melhor os seus projetos
-  Se você estiver em um servidor, normalmente você não quer instalar um ambiente na sua pasta de usuário (normalmente falta espaço de memória) e sim em um storage ligado ao servidor  


Porém, o `conda` não sabe onde esse ambiente foi criado e por isso temos que informar o caminho inteiro para ativá-lo. Isso gera alguns efeitos colaterais:
- Como o `conda` não sabe que o ambiente existe, ele não é listado quando você roda o comando `conda env list`, por exemplo.
- Quando você ativa o ambiente a indicação `(path/ate/seu/ambiente) $` pode ficar muito grande no terminal
- Você precisa passar o caminho completo para ativar o ambiente e não apenas o nome dele

Para solucionar esse problema, precisamos informar o `conda` que esse ambiente existe. Para isso vamos editar o arquivo de configuração `.condarc`. Se você estiver no Windows, esse arquivo fica no `C:/Users/<nome_de_usuario>/.condarc`. Já no Linux, você o encontra em `~/home/<nome_de_usuario>/.condarc`. 

Abra esse arquivo e inclua a seguinte informação:
```
envs_dirs:
  - <path/completo/nome_do_ambiente>
```

Agora sim informamos para o `conda` que existe um outro ambiente que criamos fora da pasta padrão. Dessa maneita, podemos ativá-lo usando apenas `conda activate <nome_do_ambiente>`, sem precisar do caminho completo.



