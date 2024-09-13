# Espaço Multimodal e Engenharia de Prompt
Segundo trabalho avaliativo da disciplina de Visão Computacional, ministrada pelo Prof. Dr. Cesar H. Comin

*Alunos:*
- Jayme Sakae dos Reis Furuyama ([jaymesakae](https://github.com/jaymesakae))
- Vitor Lopes Fabris ([tremefabris](https://github.com/tremefabris))
- Vinicius Gonçalves Perillo ([ViniciusPerillo](https://github.com/ViniciusPerillo))


## Experimentos avaliativos

Para os experimentos exigidos como forma de avaliação do 2º trabalho prático, rode os seguintes comandos:

#### Comparação entre `"Cat"` e `"Dog"`
```bash
python3 main.py --prompts "Cat" "Dog"
```

#### Comparação entre `"A photo of a cat"` e `"A photo of a dog"`
```bash
python3 main.py --prompts "A photo of a cat" "A photo of a dog"
```

#### Comparação entre `"A photo of a cat, a type of pet"` e `"A photo of a dog, a type of pet"`
```bash
python3 main.py --prompts "A photo of a cat, a type of pet" "A photo of a dog, a type of pet"
```

#### Avaliação de acurácia do CLIP
```bash
python3 main.py
```


## Como funciona

```bash
usage: main.py [-h] [--dataset_path PATH] [--prompts "STR" "STR"] [--seed N]

options:
  -h, --help              show this help message and exit
  --dataset_path PATH     Path for dataset (if non-existent, will be downloaded here) [Default: ./dataset/]
  --prompts "STR" "STR"   Prompts to analyze. Absence means that CLIP accuracy will be calculated
  --seed N                Number to seed randomized procedures [Default: 1917]
```