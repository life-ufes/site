---
title: "Como criar um usuário no linux via terminal"
author: paaatcha
classes: wide
header:
  teaser: "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/220px-Tux.svg.png"
categories:
  - Wiki
---

De maneira simples, para criar um usuário no linux via terminal, basta utilizar o comando `useradd`. Porém, tem alguns passos extras de configuração que são interessantes de serem seguidos.


1. Para criar um usuário, utilize o comando `useradd` seguido do nome do usuário que deseja criar. Por exemplo, para criar um usuário chamado "fulano", utilize o comando:

```bash
sudo useradd -m -s /bin/bash fulano
```

O parametro `-m` cria um diretório home para o usuário, que é o diretório onde ele irá acessar ao logar no sistema. Neste caso seria criado o diretório `/home/fulano`.

O parametro `-s` define o shell padrão do usuário. Neste caso, o shell padrão é o bash.


2. Defina uma senha para o usuário criado com o comando `passwd`:

```bash
sudo passwd fulano
```

Será solicitado que você digite a senha desejada duas vezes.


3. [Opcional] Adicionar o usuário a grupos específicos. Por exemplo, para adicionar o usuário "fulano" ao grupo `sudo`, `docker`, etc. Basta usar o comando:

```bash
sudo usermod -aG sudo,docker fulano
```

Colocando tudo junto, o comando para criar um usuário chamado "fulano", com diretório home e shell padrão bash, e adicioná-lo ao grupo `sudo` seria:

```bash
sudo useradd -m -s /bin/bash fulano
sudo passwd fulano
sudo usermod -aG sudo fulano
```



