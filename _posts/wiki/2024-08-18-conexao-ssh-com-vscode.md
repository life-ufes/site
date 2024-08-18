---
title: Como criar uma conexão `ssh` com o VScode
author: paaatcha
classes: wide
header:
  teaser: "https://code.visualstudio.com/assets/home/home-screenshot-mac-2x-v2-light.png"
categories:
  - Wiki
---

# Como criar uma conexão `ssh` com o VScode

Neste tutorial, mostramos como criar uma conexão `ssh` com o VScode. A ideia aqui é acessar um servidor remoto e editar arquivos diretamente no VScode.

## Passo 1: instalar a extensão `Remote - SSH`

Para criar uma conexão `ssh` com o VScode, você precisa instalar a extensão `Remote - SSH`. Para fazer isso, siga os passos:

1. Abra o VScode.
2. Clique no ícone de extensões no canto esquerdo da tela ou pressione `Ctrl + Shift + X`.
3. Na barra de pesquisa, digite `Remote - SSH`.
4. Clique em `Install` na extensão `Remote - SSH`.
5. Após a instalação, clique em `Reload` para ativar a extensão.
6. Pronto! A extensão `Remote - SSH` está instalada.

## Passo 2: configurando o plugin-in `Remote - SSH`

Agora que a extensão `Remote - SSH` está instalada, você precisa configurar a conexão `ssh`. Basicamente, você deve criar um arquivo de configuração para o servidor remoto como é descrito no tutorial [Como criar uma conexão `ssh`](2024-08-18-criando-conexao-ssh.md).

Agora que você tem o plug-in Remote-SSH instalado, verá uma pequena caixa verde no canto inferior esquerdo da interface do Visual Studio Code. Se você passar o ponteiro do mouse pela caixa, o pop-up dirá Open a remote window (Abrir uma janela remota). O botão se parece com isso `><`. 

Clique neste botão e uma caixa de diálogo aparecerá. Você verá uma lista de servidores que você configurou no arquivo `~/.ssh/config`. Se você não configurou o arquivo `~/.ssh/config`, você pode clicar em `Add New SSH Host` e inserir as informações do servidor manualmente (ver tutorial linkado acima).

Para se conectar a um servidor, basta clicar no servidor desejado na lista. O Visual Studio Code abrirá uma nova janela com o servidor remoto. Você pode ver o nome do servidor no canto inferior esquerdo da janela do Visual Studio Code.

## Passo 3: editando arquivos no servidor remoto

Agora que você está conectado ao servidor remoto, você pode editar arquivos diretamente no VScode. Você pode abrir arquivos, criar novos arquivos, editar arquivos, etc. Todas as alterações feitas no VScode serão refletidas no servidor remoto.


## Passo 4: executando comandos no terminal do servidor remoto

Além de editar arquivos, você também pode executar comandos no terminal do servidor remoto. Para abrir o terminal, vá em `Terminal > New Terminal` ou pressione `Ctrl + ``. Você verá que o terminal é um terminal do servidor remoto. 





