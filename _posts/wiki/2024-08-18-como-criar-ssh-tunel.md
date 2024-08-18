---
title: Como criar um túnel `ssh` para um servidor
author: paaatcha
classes: wide
header:
  teaser: "https://miro.medium.com/v2/resize:fit:512/1*8ebQwZcMBgsZ6prLW8p-HA.png"
categories:
  - Wiki
---

O túnel `ssh` (também conhecido como encaminhamento de porta `ssh`) é simplesmente rotear o tráfego da rede local por meio do `ssh` para hosts remotos.

Existem três tipos de encaminhamento de porta: Local, Remoto e Dinâmico. Neste tutorial, focamos no **Encaminhamento de Porta Local**.

- **Avisos**:
    - Se você não sabe como criar um `ssh`, [vá para este tutorial](2024-08-18-criando-conexao-ssh.md).
    - Para uma visão geral completa sobre túnel `ssh` [clique aqui](https://linuxize.com/post/how-to-setup-ssh-tunneling/)
      ou [aqui](https://www.tecmint.com/create-ssh-tunneling-port-forwarding-in-linux/)


# Encaminhamento de porta local

Primeiramente, vamos supor que temos o arquivo `.ssh/config` como segue:

```
Host servidor
    HostName 114.100.180.35
    User andre
    Port 22
```

Assim, podemos nos conectar ao servidor apenas usando o comando `> ssh servidor`.

Também, vamos supor que temos uma aplicação rodando em `localhost:4000` no `servidor`.
O encaminhamento de porta local nos permite conectar do nosso computador local para esta aplicação no `servidor`, que é nosso servidor remoto.

Podemos encaminhar uma porta local (vamos supor que seja a 8088) para acessar a aplicação localmente. Para fazer isso, devemos usar a 
flag `-L`, que define a porta encaminhada para o host remoto e a porta remota. Por exemplo:

```
ssh -L localhost:8088:localhost:4000 servidor
```

Após executar este comando, quando você acessar o `localhost:8088` em sua máquina local, ele acessará a aplicação 
rodando em `localhost:4000` no `servidor`.

**Nota:** você pode alterar os números das portas se desejar.

Para concluir, você pode adicionar outras flags, por exemplo:
- `-N`: significa não executar um comando remoto (você obterá um shell neste caso)
- `-f`: a flag instrui o `ssh` a ser executado em segundo plano
