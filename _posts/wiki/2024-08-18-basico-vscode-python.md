---
title: Tutorial básico de uso do VScode (com foco em Python)
author: paaatcha
classes: wide
header:
  teaser: "https://code.visualstudio.com/assets/home/home-screenshot-mac-2x-v2-light.png"
categories:
  - Wiki
---

# Tutorial básico de uso do VScode

Tutorial de funcionalidades básicas do VScode para programação (principalmente) em Python.

### Configurações

O VScode permite diversas configurações de customização. Podemos abrir a aba de configuração que fica no canto inferior com icone de engrenagem ou com o atalho `Ctrl + ,`. Nessa aba podemos configurar diversas coisas, como o tema, tamanho da fonte, etc.

Existem dois tipos de configuração: `user` e `workspace`. A configuração `user` é a configuração padrão do VScode, que é aplicada a todos os projetos. A configuração `workspace` é a configuração específica de um projeto, que sobrepõe a configuração `user`. Para criar uma configuração `workspace`, basta clicar no botão `Workspace` no canto superior direito da aba de configuração. Essa última é mais interessante para forçar um projeto a usar um determinado estilo de formatação, por exemplo.

### Paleta de comandos

Todos os comandos do VScode podem ser acessados pela paleta de comandos, que pode ser aberta com o atalho `Ctrl + Shift + P`. Essa paleta permite que você procure por comandos específicos, como por exemplo, `Open Settings (JSON)`, que abre o arquivo de configuração `settings.json` do VScode.

Também é possível usar identificadores especiais. Por exemplo, se você quiser verificar todas as configurações modificadas, pode buscar por `@modified`. Se você quiser verificar todas as configurações que foram sobrescritas, pode buscar por `@overwritten`.

### Terminal

É possível usar um ou mais terminal dentro do VSCode. Para abrir um terminal, vá no menu superior na opção `Terminal > New Terminal`. É possível abrir mais de um terminal, basta clicar no `+` no canto superior direito do terminal. Também é possível ter várias abas de terminal.

### Principais atalhos

- `Ctrl + Shift + P`: Abre a paleta de comandos

- `Ctrl + P`: Abre a paleta de comandos para abrir arquivos. Basta digitar o nome do arquivo que ele acha

- `Ctrl + Shift + L` e/ou `Ctrl + D`: Seleciona todas as ocorrências da palavra selecionada. Funcional na vertical

- `Ctrl + L`: seleciona uma linha interia (mesma coisa que usar o `home` e `end` para selecionar a linha)

- `Ctrl + G`: Vai para uma linha específica

- `Ctrl + /`: Comenta a linha selecionada
  
- `ALT + UP/DOWN`: Move a linha selecionada para cima ou para baixo

- `Ctrl + Shift +  UP/DOWN`: Duplica a linha selecionada para cima ou para baixo

### Editar atalhos
Dependendo do SO, os atalhos podem ser diferentes. É possível editar atalhos. Por exemplo, o atalho `ALT + Left/Right` é muito útil, mas não existe no linux. Para editar, vá no menu superior em `File > Preferences > Keyboard Shortcuts` ou `Ctrl + Shift + P` e `Open shortcut preferences`. É possível editar os atalhos padrões ou criar novos atalhos.

Ao editar `ALT + Left/Right`, agora é possível ir ou voltar para o arquivo extamente na linha onde está o cursor.

### Sugestão de extensões para Python
- Code spell checker: Verifica a ortografia do código
- Prettier: Formata o código
- Python: Extensão oficial da Microsoft para Python
- Git lens: Mostra informações do git no VScode
- Black Formatter: Formata o código com o Black
- Reload: recarrega a janela do VScode
- Copilot: Autocomplete do código usando IA
- Remote - SSH: Permite acessar um servidor remoto via SSH
- Remote - Containers: Permite acessar um container remoto


# Configurar interpretador do Python
Você pode configurar o interpretador do Python para cada projeto, inclusive usando Conda. Basta selecionar no canto inferior direito. Ou, alternativamente, acessar a paleta de comando e digitar `Python: Select Interpreter`.

### Colocar pasta de código visível no Python
Existem códigos do Python que não ficam instalados no ambiente padrão. Mas você pode adicionar via Path. A execução funciona, mas o VScode não reconhece (fica marcando com sublinhado colorido) e não reconhece autocompletar.

Para solucionar isso, precisamos adicionar a pasta do código no `settings.json`. Para isso, vá no menu superior em `File > Preferences > Settings` ou `Ctrl + Shift + P` e `Open Settings (JSON)`. 

Ou simplesmente procurar na paleta por `python.autoComplete.extraPaths`. Na sequência, adicionar:

```json
"python.autoComplete.extraPaths": ["./caminho do pacote"]
```

Feito isso, o VScode vai reconhecer o pacote e vai permitir autocompletar.