---
title: Como converter e usar o seu modelo com ONNX
author: paaatcha
classes: wide
header:
  teaser: "https://onnx.ai/images/ONNX-Logo.svg"
categories:
  - Wiki
---

ONNX é um formato de arquivo de modelo de aprendizado de máquina intercambiável. O objetivo do ONNX é permitir que os desenvolvedores de IA usem os modelos com o framework de sua escolha (PyTorch, TensorFlow, etc) e seja capaz de usar o modelo em qualquer lugar (na nuvem, no dispositivo móvel, etc) de maneira agnóstica ao framework. Em outras palavras, o ONNX é um formato de arquivo que permite que você exporte o seu modelo de aprendizado de máquina de um framework para outro. Obviamente, a principal intenção de usar ONNX é para colocar modelos em produção. Para mais informações, acesse a [documentação oficial](https://onnx.ai/).

O intuito deste tutorial é mostrar como converter um modelo usando Pytorch para o formato ONNX e como usar esse modelo convertido em um código Python.

## Instalação

Para instalar o ONNX, você pode usar o gerenciador de pacotes `pip`:

```
pip install onnx
```

Também é necessário instalar o pacote `onnxruntime` para poder usar o modelo convertido:

```
pip install onnxruntime
```

## Conversão do modelo

Antes de começar, não custa mencionar que, primeiramente, você precisa ter o seu modelo carregado em memória. Você pode fazer isso usando os métodos padrões do Pytorch, seja construindo o modelo do zero ou carregando um `checkpoint`. Aqui vamos apenas assumir que existe um modelo carregado em memória e que ele está sendo referenciado pela variável `model`.

Para converter o modelo, você precisa usar a função `torch.onnx.export` da seguinte forma:

```python
  torch.onnx.export(model,
                    input_data,
                    "/home/models/my_model.onnx",
                    input_names=input_names,
                    output_names=output_names,
                    dynamic_axes=dynamic_axes)
```

A seguir é apresentado uma breve descrição dos parâmetros dessa função:

- `model` é o modelo carregado em memória

- `input_data` é um exemplo completo de dado de entrada para o modelo. Esse dado deve ser exatamente como o esperado para pelo o modelo. Por exemplo, se o modelo tem mais de uma entrada, por exemplo, uma imagem e um texto, `input_data` deve ser uma tupla com esses dois dados. Esse ponto é muito importante, pois o ONNX não consegue inferir o formato de entrada do modelo. Basicamente, ele vai realizar um teste de sanidade para ver se o modelo consegue processar o dado de entrada. Se o modelo não conseguir processar o dado de entrada, o ONNX vai retornar um erro. Sendo assim, você precisa carregar os dados exatamente igual você faz com o modelo original, respeitando ordem, formato e pré-processamento. Outro ponto interessante é que você pode inserir dados _falsos_. No exemplo da imagem e do texto, supondo que o modelo use uma imagem de `224x224` e um texto de 100 palavras, você pode criar um tensor de zeros com essas dimensões e passar para o `input_data`. O ONNX vai aceitar esse dado e vai converter o modelo sem problemas. O que precisa ser respeitado é o tipo dos dados. Se a imagem for avaliada no modelo como um tensor de `float32`, você precisa passar um tensor de `float32` no `input_data`. Exemplo de `input_data`:

  ```python
  input_data = (torch.zeros(1, 3, 224, 224), torch.zeros(1, 100))
  ```

Observe que, como estamos usando Pytorch, a primeira dimensão representa o _batch_size_, que neste caso deve ser 1.

- `/home/models/my_model.onnx` é o caminho completo para salvar o modelo convertido. O nome do arquivo pode ser qualquer um, normalmente é usado a extensão `.onnx`

- `input_names` é uma lista com os nomes das entradas do modelo. Por exemplo, se o modelo tem duas entradas, uma imagem e um texto, você pode passar uma lista com os nomes `["image", "text"]`. Esses nomes são importantes, pois eles serão usados para referenciar as entradas do modelo quando você for usar o modelo convertido. Se você não passar esse parâmetro, o ONNX vai usar os nomes padrões `input_0`, `input_1`, etc.

- `output_names` mesma ideia do parâmetro `input_names`, porém para as saídas do modelo. Se houver mais de uma saída no modelo, você pode passar uma lista com os nomes `["predicao", "prob"]`. Se houver apenas uma, basta passar apenas o nome ou uma lista com apenas um item.

- `dynamic_axes` é um dicionário com as dimensões que você quer que sejam dinâmicas, normalmente usado para o _batch_size_. Usando o exemplo do modelo com imagem e texto anterior, você pode passar um dicionário com as dimensões que você quer que sejam dinâmicas, por exemplo, `{"image": {0: "batch_size"}, "text": {0: "batch_size"}}`. Isso significa que a primeira dimensão da imagem e do texto serão dinâmicas, ou seja, você pode passar qualquer valor para essa dimensão. Se você não passar esse parâmetro, o ONNX vai assumir que todas as dimensões são dinâmicas. Isso é útil para fazer avaliação em batch.

Se tudo deu certo, ao executar essa função o ONNX vai salvar o modelo convertido no caminho especificado. Agora você pode usar esse modelo convertido em qualquer lugar, seja em um servidor ou em um dispositivo móvel.

## Uso do modelo convertido

Para usar o modelo convertido, você precisa carregá-lo em memória usando a função `onnxruntime.InferenceSession`:

```python
MODEL = onnxruntime.InferenceSession("/home/models/my_model.onnx")
```

Agora você pode usar o modelo convertido da mesma forma que você usaria o modelo original. Porém, o ONNX não aceita tensores do Pytorch (se aceitasse não faria sentido ser agnóstico ao framework). É necessário usar os dados com `NumPy`. Logo, basta carregar os dados de entrada com `NumPy` e passar para o modelo carregado da seguinte forma:

```python
  MODEL.run(None, {"image": image_np, "text": text_np})
```

Observe que o método `run` recebe dois parâmetros: o primeiro é uma lista com os nomes das saídas que você quer obter do modelo. Se você quiser obter todas as saídas, basta passar `None`. O segundo parâmetro é um dicionário com os dados de entrada. Observe que os nomes das entradas devem ser os mesmos que você passou quando converteu o modelo. O retorno desse método é uma lista com os dados de saída do modelo. Se você passou apenas uma saída, o retorno será uma lista com apenas um item. Se você passou mais de uma saída, o retorno será uma lista com os dados de saída na mesma ordem que você passou no parâmetro `output_names` quando converteu o modelo.

É importante verificar o formato e tipo dos dados a ser informado. Além disso, você pode realizar a inferência em _batch_ ou individual. Obviamente isso vai alterar a quantidade de saída do modelo.
