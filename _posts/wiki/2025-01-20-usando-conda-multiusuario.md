---
title: "Utilizando o Miniconda para multiusuarios"
author: paaatcha
classes: wide
header:
  teaser: "https://www.fabriziomusacchio.com/assets/images/posts/miniconda_thumb.jpg"
categories:
  - Wiki
---

Quando estamos usando um servidor compartilhado, é comum que tenhamos que instalar pacotes e ambientes virtuais para diferentes usuários. O Miniconda é uma ótima opção para isso, pois permite a instalação de pacotes e ambientes virtuais de forma isolada para cada usuário. Porém, a instalação padrão do Miniconda é feita no diretório `/home/usuario/miniconda3`, o que pode ser um problema se você precisar instalar o Miniconda para vários usuários. 

Neste tutorial, vamos ver como instalar o Miniconda de forma que ele possa ser utilizado por vários usuários. Tudo está descrito na documentação oficial do Anaconda [neste link](https://docs.anaconda.com/anaconda/advanced-install/multi-user/). Este é apenas um guia rápido para facilitar a instalação.


## Instalando o Miniconda

1. Faça o Download do Miniconda [neste link](https://docs.anaconda.com/miniconda/install/#quick-command-line-install).

2. Inicialize a instalação do Miniconda como root utilizando o comando:
    
  ```bash
    sudo bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3
  ```    
  - Observação: pode ser que o nome do arquivo baixado seja diferente. Neste caso, substitua `Miniconda3-latest-Linux-x86_64.sh` pelo nome do arquivo baixado.

3. **Importante:** Como queremos instalar o Miniconda para vários usuários, é necessário instalar o Miniconda em um diretório compartilhado. Para isso, quando a instação te perguntar o path de instalação, digite `/opt/miniconda3`. **Não** instale dentro do diretório `/home/usuario`.

4. Quando perguntado se deseja inicializar o Miniconda automaticamente, digite `no` (dizer sim significa inicializar apenas para o root)

5. Agora, vamos dar acesso aos usuários utilizando grupos. Para isso, vamos criar um grupo com o nome `Miniconda` (ou qualquer outro de seu gosto) e adicionar os usuários que terão acesso ao Miniconda a este grupo. Para criar o grupo, utilize o comando:
    
  ```bash
    sudo groupadd Miniconda
    sudo chgrp -R Miniconda /opt/miniconda3
    sudo chmod 770 -R /opt/miniconda3
  ```

6. Agora, adicione os usuários que terão acesso ao Miniconda ao grupo `Miniconda` utilizando o comando:
    
  ```bash
    sudo adduser usuario Miniconda
  ```

7. Por fim, cada usuário que deseja utilizar o Miniconda deve adicionar o diretório `/opt/miniconda3/bin` ao seu PATH. Para isso, adicione a seguinte linha ao final do arquivo `~/.bashrc` ou `~/.bash_profile` do usuário:
    
  ```bash
    source /opt/anaconda3/bin/activate
    conda init
  ```

  - Observação: alternativamente, você pode sempre ativar o Miniconda manualmente utilizando o comando `source /opt/miniconda3/bin/activate`.

Pronto! Agora o Miniconda está instalado de forma que pode ser utilizado por vários usuários. Cada usuário pode criar seus próprios ambientes virtuais e instalar pacotes sem interferir nos ambientes dos outros usuários.


## Extra: problemas com o Tmux

Se você utiliza o Tmux e está tendo problemas para ativar o Miniconda, é possível que o Tmux não esteja carregando o arquivo `~/.bashrc` e sim o `~/.bash_profile` ou `~/.profile`. Para solucionar o problema, adicione a seguinte linha ao arquivo `~/.bash_profile` ou `~/.profile`:

```bash
  if [ -f ~/.bashrc ]; then
       . ~/.bashrc
  fi
```

Feche o terminal e abra novamente. Se o problema persistir, é possível que o Tmux não esteja carregando a variável de ambiente `PATH`. Para resolver isso, adicione a seguinte linha ao arquivo `~/.tmux.conf`:

```bash
set-option -g update-environment "PATH"
```

Feche o Tmux e abra novamente. Agora o Miniconda deve funcionar corretamente no Tmux.



  


