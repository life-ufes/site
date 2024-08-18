---
title: Como usar Jupyter Notebook com túnel `ssh`
author: paaatcha
classes: wide
header:
  teaser: "https://jupyter.org/assets/homepage/main-logo.svg"
categories:
  - Wiki
---

Neste tutorial, mostramos como usar o Jupyter lab com um túnel `ssh`. A ideia aqui é executar um Jupyter em um servidor,
e usá-lo em sua máquina. Para fazer isso, precisamos usar o túnel `ssh`.

**Nota 1:** este tutorial pressupõe que você conhece o básico sobre conexão e túnel `ssh`. Se você não os conhece,
você pode verificar os tutoriais sobre eles:
- [Como criar uma conexão `ssh`](2024-08-18-criando-conexao-ssh.md) e/ou
- [Como criar um túnel `ssh`](2024-08-18-como-criar-ssh-tunel.md)

## Passo 1: iniciando o Jupyter lab no servidor
Para iniciar o Jupyter lab no servidor, primeiro, você precisa se conectar no servidor. Usando o **servidor** como exemplo e assumindo que
temos o `.ssh/config` configurado, só precisamos executar:

```text
> ssh servidor
```

Em seguida, assumindo que o Jupyter lab está instalado no servidor, precisamos iniciá-lo:

```text
jupyter-lab --ip 0.0.0.0 --port <NÚMERO>
```

O `<NÚMERO>` é o número da porta (por exemplo, 8989). Certifique-se de escolher uma porta disponível.

Depois de executar o comando anterior, você verá algo como:

```text
[I 13:59:29.940 LabApp] JupyterLab extension loaded from /home/andre.cp/.conda/envs/gandalf/lib/python3.8/site-packages/jupyterlab
[I 13:59:29.940 LabApp] JupyterLab application directory is /home/andre.cp/.conda/envs/gandalf/share/jupyter/lab
[I 13:59:29.943 LabApp] Serving notebooks from local directory: /home/andre.cp
[I 13:59:29.943 LabApp] Jupyter Notebook 6.1.3 is running at:
[I 13:59:29.943 LabApp] http://node1:8989/?token=3e8655ec3f45213437931dff89fe15eb228811ebdb48d10d
[I 13:59:29.943 LabApp]  or http://127.0.0.1:8989/?token=3e8655ec3f45213437931dff89fe15eb228811ebdb48d10d
[I 13:59:29.943 LabApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 13:59:29.968 LabApp] No web browser found: could not locate runnable browser.
[C 13:59:29.968 LabApp]

    To access the notebook, open this file in a browser:
        file:///home/andre.cp/.local/share/jupyter/runtime/nbserver-18541-open.html
    Or copy and paste one of these URLs:
        http://node1:8989/?token=3e8655ec3f45213437931dff89fe15eb228811ebdb48d10d
     or http://127.0.0.1:8989/?token=3e8655ec3f45213437931dff89fe15eb228811ebdb48d10d
```

O endereço `http://127.0.0.1:8989/?token=3e8655ec3f45213437931dff89fe15eb228811ebdb48d10d` é o que vamos usar em nosso navegador. Mas primeiro, precisamos configurar o túnel `ssh`.

**Dica**: se você tiver um ambiente Python ou Conda, você pode ativá-lo antes de executar o comando Jupyter lab.
Dessa forma, o Jupyter vai usar as bibliotecas disponíveis dentro do ambiente. Obviamente, o ambiente deve conter o próprio Jupyter.


## Passo 2: criando o túnel `ssh`
Agora, só precisamos criar a conexão com o servidor. Para fazer isso, só precisamos executar:

```text
> ssh -L localhost:<NÚMERO_DA_PORTA_LOCAL>:localhost:<NÚMERO_DA_PORTA_DO_SERVIDOR>
```

Se usarmos a porta 8989, você pode substituir tanto `<NÚMERO_DA_PORTA_LOCAL>` quanto `<NÚMERO_DA_PORTA_DO_SERVIDOR>` por este número (se estiver disponível em sua máquina, caso contrário, você pode configurar outro número).

O tutorial [como criar um túnel `ssh`](2024-08-18-como-criar-ssh-tunel.md) detalha esse processo. Portanto, não vamos descrever tudo novamente aqui.

## Passo 3: conexão com o Jupyter
Este é o passo mais fácil. Só precisamos acessar o endereço que o Jupyter nos retorna em nosso navegador. Neste caso, é:

```text 
http://127.0.0.1:8989/?token=3e8655ec3f45213437931dff89fe15eb228811ebdb48d10d
```

Se tudo estiver funcionando corretamente, o Jupyter, rodando no servidor, vai iniciar em seu navegador.


