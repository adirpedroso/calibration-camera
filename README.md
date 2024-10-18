# Calibração de Câmera com OpenCV

Este projeto tem como objetivo realizar a calibração de câmeras utilizando o OpenCV, corrigindo distorções e obtendo parâmetros intrínsecos da câmera. Ele contém dois scripts principais:

- `opencv_calibration_camera.py:` Realiza a calibração da câmera a partir de imagens de um tabuleiro de xadrez.
- `getimages.py:` Captura imagens da câmera conectada ao computador para uso no processo de calibração.

## Estrutura do Repositório

```bash
├── dataset/
│   ├── iphone/               # Imagens capturadas pelo celular (opcional)
│   ├── ipad/                 # Imagens capturadas pelo tablet (opcional)
│   └── webcam/               # Imagens capturadas pela webcam do PC usando o script getimages.py
├── output_calibration/       # Diretório onde serão salvos os resultados da calibração
│   ├── iphone_calibration_output.yaml   # Parâmetros de calibração do celular
│   └── ipad_calibration_output.yaml     # Parâmetros de calibração do tablet
├── opencv_calibration_camera.py  # Script para realizar a calibração de câmera
├── getimages.py              # Script para capturar imagens de uma webcam
└── README.md                 # Instruções sobre o projeto (este arquivo)

```

## Pré-requisitos

Antes de começar, você precisa garantir que seu ambiente tenha as seguintes ferramentas instaladas:

- **Python 3.x** (preferencialmente 3.7 ou superior)
- **Bibliotecas Python necessárias**:
  - OpenCV
  - Numpy

Você pode instalar essas bibliotecas executando o seguinte comando:

```bash
pip install opencv-python numpy
```

Em seguida, clone este repositório em seu computador local usando o comando:
```bash
git clone https://github.com/adirpedroso/calibration-camera.git
```

## Capturar de imagens 
Este script serve para facilitar a criação de um dataset, usando uma câmera conectada ao computador, usando a tecla `S` para salvar as imagens.

```bash
python getimages.py
```

## Calibração da câmera 

Após capturar as imagens com o script **getimages.py** ou usar suas próprias imagens, você pode realizar a calibração com o script `opencv_calibration_camera.py`.

```bash
python opencv_calibration_camera.py

```
 
## Resultados
Após executar o script de calibração, os seguintes resultados serão gerados:

1. **Imagens corrigidas:** Imagens sem a distorção causada pela lente da câmera, salvas no diretório `output_calibration/`.

2. **Arquivo de calibração:** Um arquivo .yaml contendo os parâmetros intrínsecos e os coeficientes de distorção da câmera, também salvo no diretório `output_calibration/`.

## Parâmetros de Calibração
O arquivo de calibração .yaml inclui os seguintes parâmetros:

- **Matriz intrínseca da câmera (mtx):** Define a distância focal e o centro ótico.
- **Coeficientes de distorção (dist):** Descrevem as distorções radial e tangencial da lente.
- **Erro médio de reprojeção (err):** Mede a precisão da calibração.



## Desenvolvimento do Código

O desenvolvimento do código foi baseado em um projeto open-source disponível no GitHub, onde os princípios de calibração de câmera com o uso de OpenCV foram baseados. O código original pode ser encontrado no seguinte link:

[https://github.com/niconielsen32/CameraCalibration.git](https://github.com/niconielsen32/CameraCalibration.git)

Além disso, o projeto também fez uso de materiais de um site para auxiliar no entendimento dos parâmetros e no processo de conversão e calibração de câmeras. Você pode acessar o site no link abaixo:

[Learn OpenCV: Camera Calibration](https://www.learnopencv.com/camera-calibration-using-opencv/)





