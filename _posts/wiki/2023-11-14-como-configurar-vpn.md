---
title: Configuração da VPN do DI para acesso remoto à rede do laboratório
author: paaatcha
classes: wide
toc: true
categories:
  - Wiki
---

O objetivo desta documentação é descrever o passo a passo para configurar a VPN para acesso remoto aos servidores do laboratório dentro da rede do DI da UFES.

## Acesso à VPN do DI-UFES

Para acessar a VPN do DI-UFES, siga os seguintes passos:

1. **Solicitar arquivo de configuração da VPN**
   - Envie um email para Ebenézer (analista de TI do LAR) no seguinte endereço: `ensilva@inf.ufes.br`
   - Título do e-mail: Acesso a VPN para uso dos servidores do laboratório
   - No corpo do e-mail solicite o arquivo de configuração da OpenVPN. Você precisa fornecer seu usuário do PPPoE
   - Você receberá um arquivo de configuração por e-mail. Salve-o em um local de fácil acesso.

2. **Instalação da VPN**
   - Se você utiliza o Windows :roll_eyes: é necessário fazer o download do [OpenVPN Connect 3.3.7](https://swupdate.openvpn.net/beta-downloads/connect/openvpn-connect-3.3.7.2979_signed.msi). Siga as intruções de instalação.
   - Se você utiliza o Linux :hugs: (Ubuntu ou Mint), não é necessário instalar nada. O OpenVPN já vem instalado por padrão.

3. **Configuração da VPN no Linux**
   - Vá até a configurações do sistema e abra o menu de Redes (*Networking*)
   - Na sequência, procure o botão de adicionar uma configuração (pode ser representado pelo caractere +)
   - Depois clique em Importar de Arquivo (*Import from File*) para adicionarmos a configuração
   - A imagem a seguir ilustra o processo no Linux Mint:
   ![config-1](/assets/imgs/wiki/como-configurar-vpn/config_vpn_1.png) 

   - Agora vai abrir uma outra janela e você deve selecionar o arquivo de configuração que você recebeu por e-mail
   - Feito isso, vai abrir uma janela com as configurações da VPN. Você deve preencher o nome da VPN (nome de sua preferência) e o campo de usuário e senha com os dados do PPPoE:
   ![config-2](/assets/imgs/wiki/como-configurar-vpn/config_vpn_2.png) 


### Utilização da VPN

Uma vez configurada, a VPN vai aparecer como uma opção de rede disponível para conexão. Para conectar, basta clicar no botão de ligar. A imagem a seguir ilustra o processo no Linux Mint:

![config-3](/assets/imgs/wiki/como-configurar-vpn/config_vpn_3.png) 


Uma vez conectado, você deve ser capaz de *pingar* qualquer IP disponível na rede. Por exemplo, se você quiser conectar no IP `10.8.9.10` basta fazer:

```
   ping 10.8.9.10
```

Para fazer um acesso `ssh` a um computador da rede (obviamente o computador tem que ter servidor `ssh`), basta fazer:

```
   ssh usuario@ip
```

Sendo que `ip` é i IP da máquina que você deseja acessar e `usuario` é o seu **usuário da máquina** (não do PPPoE).

### Uso de Ferramentas Adicionais

- VSCode
   - Para um acesso remoto mais confortável, você pode utilizar o VSCode com a extensão "Remote - SSH".

- JupyterLab
   - Execute o seguinte comando para acessar seus notebooks JupyterLab:
     ```
     jupyter-lab --ip 0.0.0.0
     ```
   - Acesse o JupyterLab através do navegador, utilizando o IP do computador remoto na porta 8888.
