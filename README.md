<h1 align="center">
  <br>
  <a><img src="https://github.com/guilhermerodrigues680/gopro-timelapse-group-photos/blob/master/docs/images/gopro1.svg" alt="GoPro" height="208" width="208"></a>
  <br>
  GoPro Photo Organizer
  <br>
</h1>

<h2 align="center">Organizador de fotos time-lapse da GoPro em pastas</h2>

<p align="center">
    <a alt="Python 3">
        <img src="https://img.shields.io/badge/Python-3-brightgreen.svg" />
    </a>
    <a alt="License">
        <img src="https://img.shields.io/badge/license-MIT-blue.svg" />
    </a>
</p>

### Tabela de Conteúdo ###
1. [Exemplo de uso](#Exemplo-de-uso)
2. [Exemplo da estrutura gerada pelo `python3 gopro-photo-organizer.py`](#Exemplo-da-estrutura-gerada-pelo-python3-gopro-photo-organizerpy)
3. [Contributor](#Contributor)
4. [License](#License)

### Exemplo de uso ###

**Sintaxe**
```sh
python3 gopro-photo-organizer.py <caminho-do-diretorio-das-fotos>
```

**Caminho com aspas ou sem aspas**
```sh
# Sem aspas
python3 gopro-photo-organizer.py /Users/guilherme/Desktop/python-organize-gopro/pasta 

# Ou Com aspas
python3 gopro-photo-organizer.py '/Users/guilherme/Desktop/python-organize-gopro/pasta'
```

**Erro por não especificar o caminho**
```sh
# Executar sem passar o ar
python3 gopro-photo-organizer.py

# Traceback (most recent call last):
#   File "gopro-photo-organizer.py", line 62, in <module>
#     main(sys.argv[1:])
#   File "gopro-photo-organizer.py", line 50, in main
#     raise Exception('É preciso especificar o diretorios que contém as fotos')
# Exception: É preciso especificar o diretorios que contém as fotos
```

### Exemplo da estrutura gerada pelo `python3 gopro-photo-organizer.py` ###

Após copiar arquivos do SD da GoPro
```txt
folder/
    G0261749.JPG
    G0261750.JPG
    G0261751.JPG
    G0261752.JPG
    G0261753.JPG
    G0261754.JPG
    G0261755.JPG
    G0261756.JPG
    G0271757.JPG
    G0271758.JPG
    G0271759.JPG
    G0271760.JPG
    G0271761.JPG
    G0271762.JPG
    G0271763.JPG
```

Após executar o `gopro-photo-organizer.py`
```txt
folder/
    G026/
        G0261749.JPG
        G0261750.JPG
        G0261751.JPG
        G0261752.JPG
        G0261753.JPG
        G0261754.JPG
        G0261755.JPG
        G0261756.JPG
    G027/
        G0271757.JPG
        G0271758.JPG
        G0271759.JPG
        G0271760.JPG
        G0271761.JPG
        G0271762.JPG
        G0271763.JPG
```

### Contributor ###
[LinkedIn: Guilherme Rodrigues](https://www.linkedin.com/in/guilherme-r-54380b106/)

### License ###
This project is licensed under the terms of the MIT license.