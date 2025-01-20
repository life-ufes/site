---
title: Guia básico de utilização do TMUX
author: paaatcha
classes: wide
header:
  teaser: "https://github.com/tmux/tmux/raw/master/logo/tmux-logo-medium.png?raw=true"
categories:
  - Wiki
---

O TMUX (Terminal Multiplexer) é uma ferramenta que permite dividir uma única sessão de terminal em várias sessões menores (chamadas de "paines") e alternar entre elas sem fechar as sessões ativas. Ele é muito útil para desenvolvedores e administradores de sistemas que precisam gerenciar várias tarefas simultaneamente.


As principais funcionalidades incluem:

- **Divisão de janelas:** permite dividir a tela do terminal em múltiplos painéis.
  
- **Sessões persistentes:** as sessões TMUX podem continuar em execução em segundo plano mesmo após o terminal ser fechado.
  - Isso é extremamente útil para deixar código rodando em um servidor
- 
- **Multiplexação de terminais:** várias janelas e painéis podem ser criados dentro de uma única sessão TMUX.
  
- **Compartilhamento de sessões:** permite que várias pessoas compartilhem a mesma sessão TMUX.
  
- **Configuração e scripts:** o TMUX é altamente configurável e suporta scripts.


## Como Funciona?

TMUX cria uma camada adicional entre o usuário e o terminal, permitindo a gestão de múltiplas sessões de terminal de maneira eficiente. Cada sessão pode conter múltiplas janelas, e cada janela pode ser dividida em múltiplos painéis.

Dessa forma, o TMUX permite que você execute várias tarefas simultaneamente em um único terminal, sem a necessidade de abrir várias janelas de terminal. A sessão TMUX pode ser facilmente dividida em painéis horizontais ou verticais, permitindo que você visualize várias janelas ao mesmo tempo. 

![tmux](https://i.ytimg.com/vi/BHhA_ZKjyxo/maxresdefault.jpg)

Além disso, o **TMUX suporta sessões persistentes**, o que significa que você pode desconectar-se de uma sessão TMUX e reconectar-se mais tarde, mantendo todas as janelas e painéis abertos.


## Instalação

Em sistemas baseados em Ubuntu/Debian, você pode instalar o TMUX usando o gerenciador de pacotes apt:

```
sudo apt-get update
sudo apt-get install tmux
```

## Como Usar o TMUX

Para iniciar uma nova sessão TMUX, basta digitar o seguinte comando no terminal:

```
tmux
```

Isso abrirá uma nova sessão TMUX. Ele vai ter a mesma aparência de um terminal normal, mas com uma barra de status na parte inferior da tela. Você pode executar comandos dentro da sessão TMUX como faria normalmente em um terminal.

Também é possível iniciar uma nova sessão TMUX com um nome específico:

```
tmux new -s <nome-da-sessão>
```

Para listar todas as sessões TMUX ativas, você pode usar o seguinte comando:

```
tmux ls
```

Todas as seções TMUX ativas ficam em segundo plano, mesmo que você feche o terminal, elas não serão encerradas. Para se reconectar a uma sessão TMUX existente, você pode usar o seguinte comando:

```
tmux attach -t <nome-da-sessão>
```

Para sair de uma sessão TMUX, você deve o usar o atalho `Ctrl + b` seguido de `d` (para *detach*). Isso irá desconectar você da sessão TMUX, mas a sessão continuará em execução em segundo plano.

Para encerrar uma sessão TMUX, você pode usar o seguinte comando:

```
tmux kill-session -t <nome-da-sessão>
```

Apenas com essas funcionalidades já é possível fazer muita coisa, mas o TMUX oferece muitas outras funcionalidades avançadas que podem ser úteis para usuários avançados.


## Principais Atalhos

O TMUX é altamente configurável e suporta muitos atalhos de teclado para facilitar a navegação e a gestão de sessões. O principal atalho do TMUX é `Ctrl + b`, que é usado para ativar a maioria dos comandos do TMUX. Aqui estão alguns dos atalhos mais comuns:

- `Ctrl + b` + `d` (*detach*): desconecta da sessão TMUX, mas mantém a sessão em execução em segundo plano.

- `Ctrl + b` + `c` (*create*): cria uma nova janela dentro da sessão TMUX. Ela aparece na barra de status na parte inferior da tela.

- `Ctrl + b` + `n` (*next*): muda para a próxima janela na sessão TMUX.

- `Ctrl + b` + `p` (*previous*): muda para a janela anterior na sessão TMUX.

- `Ctrl + b` + `<seta>`: move o foco para o painel na direção da seta.

- `Ctrl + b` + `<id-sessão>`: muda para a janela com o ID especificado.

- `Ctrl + b` + `x` (*kill-pane*): fecha o painel atual e mata o processo em execução nele.

- `Ctrl + b` + `%` (*split-window*): divide a janela atual em dois painéis verticais.

- `Ctrl + b` + `"` (*split-window -h*): divide a janela atual em dois painéis horizontais.

- `Ctrl + b` + `?` (*list-keys*): exibe uma lista de todos os atalhos de teclado disponíveis no TMUX.


## Recursos adicionais

Para mais informações sobre o TMUX e seus recursos avançados, você pode consultar os seguintes recursos:

- [Documentação oficial do TMUX](https://github.com/tmux/tmux/wiki)
- [Guia de referência rápida do TMUX](https://tmuxcheatsheet.com/)
- [Tutorial do TMUX no Hostinger](https://www.hostinger.com.br/tutoriais/como-usar-tmux-lista-de-comandos)





