
# Site do Life

O site do laboratório é construído utilizando o framework Jekyll usando o template Minimal-Mistakes.

Para atualizar o conteúdo do site você não precisa conhecer Jekyll a fundo. Sabendo um pouco de Markdown e como funciona o template utilizado, que é descrito na sequência desta documentação, já é suficiente para conseguir atualizar as informações do site.

Todavia, qualquer alteração estrutural do site (por exemplo, criar um layout novo ou alterar paleta de cor) é necessário entender um pouco de desenvolvimento web, bem como aprofundar no Jekyll e no template Minimal Mistakes.

## Ferramentas utilizadas para criar o site

### Markdown
O primeiro elemento que você precisa conhecer para escrever para o site é o [Markdown](https://www.markdownguide.org). Markdown é uma ferramenta de conversão de text-to-HTML. Com ele é possível você marcar títulos, listas, tabelas, etc., de forma muito mais limpa, legível e precisa, do que se fosse fazer com HTML. Essa ferramenta é usada, por exemplo, para criar READMEs em repositórios do Github. É bem simples aprender como se usa, e [neste link](https://blog.da2k.com.br/2015/02/08/aprenda-markdown/) você encontra um bom tutorial que vai te entregar basicamente tudo que precisa.

### Jekyll
Como já foi dito, você não precisa dominar Jekyll para atualizar o site. Porém, caso queira saber o que é isso, como funcionar, para que serve, etc., você pode ler o tutorial [O que é Jekyll e para que ele serve](http://blog.virtuacreative.com.br/jekyll-for-beginners-introduction.html).

Se você quiser ir mais a fundo e aprender Jekyll, você pode assistir as [vídeos aulas disponibilizadas neste canal](https://www.youtube.com/watch?v=7lI5BfHK-kA). Porém, como Jekyll é um framework web, é necessários conhecimentos mínimos de HTML e CSS.

### Minimal Mistakes
[Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) é o nome do template/tema que utilizamos dentro do Jekyll para criar o nosso site. A ideia é que não precisamos reinventar a roda para ter algo funcinal e útil. Logo, utilizamos utilizamos o template como base a alteramos o que foi necessário para montar o site.

Uma vantagem de utilizar esse template é que a documentação dele é muito boa. Sempre que quiser fazer algo diferente no site, você pode consultá-la para verificar se já não está implementado.

Todavia, o básico para alterar o site é descrito na próxima seção.

tilizar esse template é que [a documentação dele é muito boa](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/). Sempre que quiser fazer algo diferente no site, você pode consultá-la para verificar se já não está implementado.

Todavia, o básico para alterar o site é descrito na próxima seção.

## Funcionamento do site
Primeiramente, o site está disponível dentro deste repositório. Abrindo o repositório, ou clonando-o, você vai observar uma organização que a esperada pelo Jekyll e pelo Minimal Mistakes. Na sequência, é descrito tudo que você precisa saber para atualizar o site.

### Subindo o ambiente de produção
Dentro deste repositório você encontra um `Dockerfile` e um `docker-compose`. Tudo que você precisa fazer para subir o ambiente na sua máquina é executar o comando:
```
docker compose up -d
```
Após isso, o site vai estar disponível em `localhost:4000`. Você pode acessar o site e fazer as alterações que desejar. Toda vez que você alterar algo, o site vai ser atualizado automaticamente. Para encerrar o container, basta executar o comando:

```
docker compose down
```

### Subindo o ambiente de desenvolvimento
Similar ao ambiente de produção, você pode subir o ambiente de desenvolvimento para fazer as alterações no site. Para isso, execute o comando:

```
docker compose -f docker-compose-dev.yml up
```
Após isso, o site vai estar disponível em `localhost:4000`. Você pode acessar o site e fazer as alterações que desejar. Toda vez que você alterar algo, o site vai ser atualizado automaticamente. Para encerrar o container, basta executar o comando:



### Configuração do site
Parte da configuração do site fica disponível dentro do arquivo `_config.yml`, que é um arquivo YAML. Se você não sabe nada sobre YAML, [dê uma lida neste artigo](https://www.treinaweb.com.br/blog/o-que-e-yaml). Porém, nada mais é do que um arquivo estruturado no estilo xml.

Normalmente, não tem muita coisa para alterar neste arquivo no dia-a-dia, mas caso seja necessário, você pode alterar aqui, por exemplo:

- Língua do site através da tag `locale`
- Título do site através da tag `title`
- Nome, descrição e URL base através das tags `name`, `description` e `baseurl`, respectivamente
- Dentre várias outras coisas auto explicativas, como:
  - Favicon
  - Redes sociais
  - Setar comentários
- Diversas outras configurações mais avançadas de markdown, sass, etc. (você não precisa se preocupar com isso em 99% dos casos)

### Pastas do template
Existem algumas pastas que são relativas ao template. Elas existem para guardar código para criar layouts, por exemplo. Os códigos dessas pastas você só vai acessar se quiser mudar algo bem estrutural do site. São elas:

- `_includes`: essa pasta possui todo código HTML necessário para criar toda parte estrutural do site. É necessário conhecimento de web e Jekyll para alterar algo aqui
* `layouts`: nesta pasta são armazenadas os arquivos para criação dos Layouts do template. Só é necessários alterar algo aqui caso queira criar um layout novo, o que é muito raro
* `_sass`: essa pasta contém os arquivos de configuração do SASS, que é uma evolução do CSS. Na pasta `_sass/minimal-mistakes` existe um arquivo chamado `_variables.scss` que guarda informações de cores, fontes, tamanhos, etc. Talvez, este seja o único arquivo que você possa ter interesse em alterar algo no futuro.

Com já foi dito, é raro precisar alterar algo nessas pastas. Caso seja necessário alterar, talvez seja melhor consultar a [documentação do próprio Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/).

### Alterando o menu do site e alterar tradução
No topo do site existe um menu com algumas opções. Esse menu pode ser alterado no arquivo `_data/navigation.yml`. Neste arquivo, você pode alterar o que já existe ou criar um menu novo. Por exemplo, poderiamos criar um item novo no menu fazendo:

```
main:
   - title: "Novo item no menu"
     url: /novo-item-menu
```

As tags são auto explicativas, você deve informar o título, que é o que aparece no menu, e a url para acessar quando ele for clicado. Sobre essa URL, vamos falor em breve.

Outra alteração que pode ser realizada dentro da pasta `_data` é no arquivo `ui-text.yml`. O Minimal Mistakes é utilizado é diversas línguas, incluido português (pt-BR). Pode acontecer de que alguma tradução não seja muito boa. Caso queira trocar, basta buscar ela neste arquivo e alterar.

### Criando paǵinas estáticas
As paǵinas do site estão disponibilizadas dentro da pasta `_pages`. Na verdade, elas poderiam estar em qualquer lugar (e você vai entender em breve). Porém, para organizar tudo em um mesmo local, elas se encontram nesta pasta.

A única exceção a essa regra é a pagina principal, a `index.md`. Essa, fica na raíz do projeto e é necessário que assim seja pois é o ponto de partida para o site.

Agora, precisamos entender um pouco mais de como funciona a criação de páginaas dentro do Jekyll.

## Funcionamento das páginas
Todas as páginas dentro do Jekyll são cridas usando arquivos Markdown (extensão `.md`) ou HTML (extensão `.html`). Em qualquer uma das opções, é necessário criar um cabeçalho com as informações da página. Esse cabeçalho é a primeira coisa que vem no arquivo e é delimitado pelos caracteres `---`, por exemplo:

```
---
 layout: single
 permalink: /sobre/
 title: "Sobre a Equipe"
 classes: wide
 author_profile: true
---
```

Esse cabeçalho basicamente avisa ao Jekyll que ali dentro será criado arquivos de configuração usando YAML. Essas configurações são definidas pelo template Minimal Mistakes e elas mudam como que a página será exibida no navegador. Na sequência, vamos passar pelo pontos mais importantes.

- `layout`: essa tag determina qual o layout do template essa página vai utilizar. Existem vários, por exemplo, `single`, `splash`, `post`, `tags`, etc. Na [documentação do template](https://mmistakes.github.io/minimal-mistakes/docs/layouts/) existe a descrição de cada um deles e um exemplo visual de como eles são exibidos.
- 
- `permalink`: define qual vai ser o link que vai aparecer no navegador para ser acessaro. No exemplo anterior é usado `/sobre/`. Neste caso, ele vai aparecer como `<URL_SITE>/sobre`. Essa URL do site vai depender da hospedagem dele (mas se ele já está funcionando, não se preocupe com isso). O que é importante aqui é que se você for usar essa página no menu, que foi descrito na seção anterior, você deve usar essa informação na tag `url`.
  
- `title`: é o título que vai aparecer na página
  
- `classes`: altera a maneira que o layout exibe a tela. Existem diversos atributos, como `wide`, `landing`, `dark-theme`, etc. Novamente, para mais informações, vá até a [documentação do template](https://mmistakes.github.io/minimal-mistakes/docs/layouts/).
  
- `author_profile`: se for `true` exibe uma caixa ao lado da página com informações do autor da página ou post. Normalmente é deixado como `false`.
  
- `toc`: é opcional, mas se for colocado como `true` cria um sumário, ou table of content, da página
  
- `taxonomy`: é opcional, mas se for utilizado define a taxonomia da página. Você pode encontrar mais informações sobre [nesta parte da documentação do template](https://mmistakes.github.io/minimal-mistakes/docs/layouts/#taxonomy-archives).

Essas são as configurações básicas de uma página. Após a delimitação `---`, você pode escrever a página usando Markdown de maneira habitual. Quando o Jekyll rodar, ele vai transformar tudo em HTML e preparar os arquivos necessários para criar o site. Porém, a gente não precisa se preocupar com isso, ele faz automaticamente. O que precisamos é apenas inserir o conteúdo nas páginas.

Outro ponto importante aqui é que essas páginas precisam ser linkadas no site para que o usuário acesse. Por exemplo, podemos criar um item no menu superior chamado Sobre e direcionar para a página `<URL_SITE>/sobre` utilizando a configuração de navegação que já foi descrita anteriormente. Se você não linkar, elas vão existir, mas só podem ser acessadas digitando a URL completa no navegador.

## Criando posts para seção de blog e/ou notícias
A criação de posts para o blog é realizada de maneira similar a criação de páginas estáticas. Porém, precisamos de algumas configurações extra.

Primeiramente, para organizar o site, todos os posts são colocados dentro da pasta `_posts`. Também vamos usar arquivos em Markdown com a configuração em YAML no topo dele (como já descrito). Porém, agora vem a primeira diferença: precisamos criar o nome do arquivo seguindo o padrão `aaaa-mm-dd-nome-do-arquivo.md`. Esse padrão é obrigatório e ele é quem vai criar a organização dos posts no blog de acordo com a data que passamos no começo (que está no padrão `aaaa-mm-dd`).

Dentro do arquivo, vamos usar as tags descritas anteriormente, exceto a `permlink`, uma vez que os posts são colocados automaticamente dentro do post. Neste caso, você não precisa disponibilizar o link para o usuário, ele já va aparecer pra ele na seção de posts pois o Jekyll já faz isso automaticamente.
Outros atributos interessantes que podemos usar:

- `header`
  - `teaser`: podemos passar o caminho para uma imagem para que ela aparece em posts recomendados. Por exemplo, `/assets/imgs/posts/casa.png`, vai fazer com que essa imagem seja a imagem de chamada para o post.
  
  - `categories`: podemos criar categorias para o blog. Neste site, usamos `Blog` e `Wiki`. Logo, esse atributo fica:
  
  ```
  categories:
    - Blog
  ```
  
  Esse nome criado (no caso `Blog`), é usado como taxonomia para criar uma página de `\blog` do site. Obviamente, pode ser alterado ou criado outras (ex: tutoriais).

  - `tags`: podemos criar `tags` para os posts para que eles sejam organizados em grupos similares. Neste caso, podemos criar quantas forem necessárias. Por exemplo:
  ```
  tags:
    - Artigo
    - Python
    - ROS
    - VSS
  ```
       
Uma vez feita as configurações, podemos escrever o post usando Markdown normalmente. Quando ele for criado, o Jekyll vai colocar junto ao outros posts do Blog organizados por data.

**Dica**: sempre que for iniciar um novo post, copia e cola arquivo de post já criado e altere as informações que são necessárias.


## Páginas especiais
Além da `index.md`, existem outras páginas especiais que utilizamos. Elas estão dentro da pasta `_pages` e são listadas a seguir:

* `404.md`: define uma página padrão para caso o usuário tente acessar um link que não existe (ex: `life.inf.ufes.br/asdasdasd`).
* `arquivo.md`: cria uma página que arquiva todos os posts do blog de acordo com ano.
* `noticias.md`: cria uma página que mostra os posts em ordem cronológica. Isso é feito usando `layout: category` e `taxonomy: Notícias`</code>. Por isso é importante incluir a `Notícias` em todos os posts que criamos pois é assim que o Jekyll sabe que é para colocar todos aqui.
* `tags.md`: cria uma página que mostra os posts organizados por tags. Isso é feito usando `layout: tags`. O Jekyll vai pegar todas as tags que criamos nos posts e organizar nesta página automaticamente.

## Incluindo imagens e outros arquivos
Todos os arquivos do site (por exemplo, imagens, PDFs e similares) devem ser colocados dentro da pasta `assets`. Para acessar o arquivo dentro de uma página ou post, basta usar o caminho do mesmo. Por exemplo, `assets/imgs/profile.png`, que o logo da equipe que está sendo usado como perfil.

Sempre que for usar uma imagem em um post, você pode criar uma pasta com o nome do post e incluir a imagem dentro dele.

## Considerações finais
Com este tutorial, e os links fornecidos nele, você já tem o que é necessário para realizar alterações no site do Life. É claro que no começo pode parecer um pouco obscuro, mas fazendo uma ou duas modificações, já ficará habitual.

Por falar em modificações, uma vez finalizado as alterações, para publicá-las basta commitar o código para o repositório do mesmo que está na organização do Github do time. Se não houver erros, o site vai atualizar automaticamente (`wip`).

# Como configurar o webhook

Altere o arquivo de configuração do Git para permitir um pull dentro do container.

```
nano .git/config
```
E atualize:

```
url = https://<NOME_USUARIO>:<TOKEN></TOKEN>@github.com/life-ufes/site.git
```
