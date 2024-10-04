---
title: Como instalar Docker no Ubuntu
author: paaatcha
classes: wide
categories:
  - Wiki
---

O objetivo deste tutorial é descrever o passo a passo para instalar o Docker em uma máquina com Ubuntu. Se você não sabe nada sobre o Docker, e gostaria de aprender os conceitos básicos, sugiro a leitura [deste artigo](https://computacaointeligente.com.br/outros/docker-basico-data-science/) que escrevi para o meu blog.


## Preparando o ambiente para instalação


#### Passo 1
O primeiro passo para instalar o Docker é atualizar os pacotes do Ubuntu. Para isso, execute o seguinte comando no terminal:

```
sudo apt update
```

#### Passo 2
Agora, vamos instalar alguns pacotes que permitem que o `apt` utilize repositórios via HTTPS:

```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

#### Passo 3
Em seguida, vamos adicionar a [chave GPG](https://www.gnupg.org/) oficial do Docker:

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

#### Passo 4
Agora, vamos adicionar o repositório do Docker às fontes do `apt`. Neste caso, precisamos saber a versão do Ubuntu que estamos utilizando. Para isso, execute o seguinte comando no terminal:
    
```
lsb_release -a
```

No campo `Codename` você vai ver a versão do Ubuntu. No meu caso, estou utilizando a versão `focal`. Sendo assim, vamos adicionar o repositório da seguinte forma:

```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
```


**Observação:** se você estiver usando uma versão diferente (por exemplo, `jammy`), basta substituir `focal` por `jammy` no comando acima. Se você estiver usando o Linux Mint (que é baseado no Ubuntu), quando você rodar o comanado `lsb_release -a` o campo `Codename` vai apresentar a versão do Mint. Neste caso, você precisa consultar a [tabela de versões](https://linuxmint.com/download_all.php) do Mint para saber qual é o Ubuntu que o Mint foi baseado. Por exemplo, neste momento estou usando a versão `Una`, que segundo a tabela, é baseada na versão `focal` do Ubuntu.


#### Passo 5
Por fim, vamos atualizar o cache do `apt`:

```
sudo apt-cache policy docker-ce
```

Feito isso, você verá uma saída semelhante a esta:

```
docker-ce:
  Installed: (none)
  Candidate: 5:24.0.7-1~ubuntu.22.04~jammy
  Version table:
     5:24.0.7-1~ubuntu.22.04~jammy 500
        500 https://download.docker.com/linux/ubuntu jammy/stable amd64 Packages
     5:24.0.6-1~ubuntu.22.04~jammy 500
     (...)
```

## Instalando o Docker

Se tudo deu certo, você pode instalar o Docker da seguinte forma:

```
sudo apt install docker-ce
```

Para verificar se o serviço está rodando, execute o comando:
```
sudo systemctl status docker
```

## Executando o Docker sem o comando `sudo`

O padrão do Docker é rodar apenas para usuários `root`. Se você (assim como eu) acha super chato sempre ter que usar o comando `sudo` para executar o Docker, pode incluir o usuário atual no grupo `docker` executando os seguintes comandos:

```
sudo usermod -aG docker ${USER}
```

Para aplicar o novo grupo:

```
su - ${USER}
```

Certifique-se que o grupo foi adicionado corretamente:

```
groups
```

Que deve retornar algo do tipo:

```
<nome_usuario> sudo docker
```

Se você quiser adicionar outro usuário, basta substituir `${USER}` pelo nome do usuário que você quer adicionar ao grupo `docker`.

Para as alterações terem efeito, é necessário fazer logout e login novamente. 


## Instalando o Docker Compose

O Docker Compose é uma ferramenta que permite definir e executar aplicativos Docker multi-container. Para instalar o Docker Compose, execute os seguintes comandos:

#### Passo 1

Baixe a versão que deseja instalar. Neste caso, estou baixando a versão 1.29.2:

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

#### Passo 2

Atribua permissões de execução ao binário:

```
sudo chmod +x /usr/local/bin/docker-compose
```

#### Passo 3

Verifique se a instalação foi bem sucedida:

```
docker-compose --version
```

Se tudo deu certo, você verá a versão do Docker Compose que você acabou de instalar.





