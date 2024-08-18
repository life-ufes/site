---
title: Como criar uma conexão SSH
author: paaatcha
classes: wide
header:
  teaser: "https://miro.medium.com/v2/resize:fit:512/1*8ebQwZcMBgsZ6prLW8p-HA.png"
categories:
  - Wiki
---


Neste tutorial, você vai aprender como configurar sua máquina para ser capaz de estabelecer conexões ssh com um servidor/cluster.

**Nota:** se você não sabe o que é `ssh`, dê uma olhada [neste artigo](https://www.ucl.ac.uk/isd/what-ssh-and-how-do-i-use-it)

## Criando uma conexão usando apenas a linha de comando
A maneira mais fácil de criar uma nova conexão ssh é usando o seguinte comando:

```
> ssh <NOME_DO_USUÁRIO>@<ENDEREÇO_IP_DO_SERVIDOR>
```

Após pressionar enter, ele solicitará sua senha para se conectar ao servidor.

Por padrão, o comando `ssh` tenta se conectar na porta 22. Se esta porta foi alterada no servidor, você precisa usar o parâmetro `-p` e indicar a porta:

```
> ssh <NOME_DO_USUÁRIO>@<ENDEREÇO_IP_DO_SERVIDOR> -p <NÚMERO_DA_PORTA>
```

Por exemplo:

```
> ssh andre@100.152.158.21 -p 22 
```

Neste caso, você não precisa informar a senha do usuário (exceto se a chave tiver uma).

### Conectando usando uma chave criptográfica
Às vezes, queremos/precisamos usar uma chave privada em vez de uma senha. Nesse caso, você precisa informar a chave no comando usando o parâmetro `-i` da seguinte forma:

```
> ssh <NOME_DO_USUÁRIO>@<ENDEREÇO_IP_DO_SERVIDOR> -p <NÚMERO_DA_PORTA> -i <CAMINHO_COMPLETO_PARA_A_CHAVE>
```

Por exemplo:

```
> ssh andre@100.152.158.21 -p 22 -i /home/andre/ssh_key
```

Neste caso, você não precisa informar a senha do usuário (exceto se a chave tiver uma).

## Configurando o arquivo `.ssh/config`
Usar o comando `ssh` como na seção anterior funciona corretamente. No entanto, escrever sempre o comando completo é cansativo. Felizmente, há uma maneira mais rápida de usar o `ssh`, mas precisamos configurar o arquivo `.ssh/config`. Para fazer isso, basta seguir estas etapas:

1. Primeiro, vá para o diretório do seu `usuário`. Se você estiver usando o Windows, geralmente está localizado em `C:Users\<SEU_NOME_DE_USUÁRIO>`. Para Linux, `/home/<SEU_NOME_DE_USUÁRIO>`
2. Neste diretório, verifique se há uma pasta oculta chamada `.ssh` e, se estiver ausente, crie uma nova.
3. Na pasta `.ssh`, verifique se há um arquivo chamado `config`. Se estiver ausente, crie-o. **Importante**: este arquivo não tem extensão!
4. Dentro deste arquivo, vamos inserir os parâmetros `ssh` usados na seção anterior de acordo com o seguinte padrão:

   ```
   Host <TAG_DO_SERVIDOR>
       HostName <ENDEREÇO_IP_DO_SERVIDOR>
       User <NOME_DO_USUÁRIO>
       Port <NÚMERO_DA_PORTA>
   ```  
   **Nota:** `<TAG_DO_SERVIDOR>` é apenas um alias que você cria para o servidor. Poderia ser `servidor1`, por exemplo.
   
   Esta configuração gera o mesmo comando apresentado na seção anterior: `ssh <NOME_DO_USUÁRIO>@<ENDEREÇO_IP_DO_SERVIDOR> -p <NÚMERO_DA_PORTA>`

5. Finalmente, para estabelecer a conexão `ssh` com o servidor, você só precisa usar o seguinte comando: 
   ```
    > ssh <TAG_DO_SERVIDOR>
    ```
6. Se você precisar/quiser usar a chave pública como na seção anterior, da mesma forma, precisamos informar o caminho para a chave:

   ```
   Host <TAG_DO_SERVIDOR>
      HostName <ENDEREÇO_IP_DO_SERVIDOR>
      User <NOME_DO_USUÁRIO>
      Port <NÚMERO_DA_PORTA>
      IdentityFile <CAMINHO_COMPLETO_PARA_A_CHAVE>
   ```
   
   O resultado é o mesmo discutido na seção anterior.

___

Este arquivo `config` poupa muito tempo da sua vida quando você precisa se conectar a diferentes servidores. Na verdade, você pode criar quantos `TAG_DO_SERVIDOR` quiser. Basta separá-los usando uma quebra de linha. Um exemplo de arquivo `.ssh/config` válido seria:

```
Host golfinho
    HostName 110.111.124.96
    User andre

Host baleia
    HostName 110.111.124.95
    User andre123
    Port 123

Host boto
    HostName 110.111.124.97
    User andrel
    Port 22
    IdentityFile /home/andre/chaves/goku_key.pub
```

Para se conectar ao host `baleia`, por exemplo, você só precisa usar 

```
> ssh baleia
```





