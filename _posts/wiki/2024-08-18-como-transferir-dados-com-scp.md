---
title: Como transferir dados com `scp`
author: paaatcha
classes: wide
header:
  teaser: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/SCP_Foundation_%28emblem%29.svg/800px-SCP_Foundation_%28emblem%29.svg.png"
categories:
  - Wiki
---


O comando `scp` é usado para transferir dados de forma segura, com etapas de criptografia e autenticação no processo.

Esses dados (um arquivo ou um diretório) podem ser copiados:
- Do seu sistema local para um sistema remoto.
- De um sistema remoto para o seu sistema local.
- Entre dois sistemas remotos a partir do seu sistema local.

O comando `scp` depende do `ssh` para a transferência de dados. Portanto, verifique o [Como usar o `ssh` no Terminal/PowerShell](2024-08-18-criando-conexao-ssh.md).

**Aviso:** este tutorial vem do [artigo](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/) do Linuxize.
Confira-o para uma compreensão completa.

## A sintaxe do comando `scp`

A sintaxe do comando `scp` é a seguinte:

```
> scp <OPÇÃO> <ORIGEM> <DESTINO>
```

onde:
* `ORIGEM`: é o caminho do arquivo de origem.
* `DESTINO`: é o caminho para o arquivo de destino.
* `<OPÇÃO>`: as opções relacionadas a cifra, configuração ssh, porta ssh, limite, cópia recursiva, etc.

As opções mais utilizadas são:

* `-P`: Especifica a porta ssh do host remoto.
* `-p`: Preserva as datas de modificação e acesso dos arquivos.
* `-q`: Use esta opção se deseja suprimir a barra de progresso e mensagens não relacionadas a erros.
* `-C`: Esta opção força o `scp` a comprimir os dados ao enviá-los para a máquina de destino.
* `-r`: Esta opção diz ao `scp` para copiar diretórios recursivamente.


## Usando o `scp`

Vamos agora ver um exemplo de uso do `scp` para transferência de dados. Para copiar um arquivo do local para o servidor,
execute o seguinte comando:

```text
scp arquivo.txt usuario@10.20.10.9:/diretorio/remoto
```

onde:
- `arquivo.txt` é o nome do arquivo que queremos copiar da nossa máquina
- `usuario` é o usuário no servidor remoto
- `10.20.10.9` é o endereço IP do servidor
- `/diretorio/remoto` é o caminho no servidor que o `arquivo.txt` será copiado

Após executar o comando, a solicitação pedirá sua senha e o processo de transferência começará.

**Nota 1:** se você não especificar um diretório remoto, o arquivo será copiado para o diretório home do usuário remoto.
**Nota 2:** se o caminho do diretório remoto não existir, a solicitação retornará um erro.

___

Para transferir uma pasta, o comando é quase o mesmo. Você só precisa incluir o parâmetro `-r`:

```text
> scp -r pasta/ usuario@10.20.10.9:/diretorio/remoto
```

___

Para transferir uma pasta (ou arquivo), do servidor remoto para nossa máquina, você só precisa alterar os parâmetros `origem` 
e `destino`:

```text
> scp -r usuario@10.20.10.9:/diretorio/remoto/pasta pasta_destino/
``` 

___

**Dica:** se você tiver as credenciais de conexão configuradas no arquivo `.ssh/config`, você pode usar o comando da seguinte forma:

```text
> scp -r pasta tag_servidor:/diretorio/remoto
```
