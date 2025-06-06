Bryan Willian – RM 551305

Gabriel Doms – RM 98630

Lucas Braga – RM 98607


# Sistema de Orientação Sonora Inteligente em Caso de Apagão

##  Objetivo

O projeto **SafePath** foi desenvolvido com o intuito de auxiliar **pessoas com deficiência visual** (ou qualquer pessoa em situação de risco) durante quedas de energia elétrica, oferecendo uma **rota sonora de evacuação segura**. A proposta combina **visão computacional com MediaPipe** e processamento de vídeo para criar um fluxo automatizado de reconhecimento de escuridão, solicitação de ajuda e orientação por alarmes sonoros.

---
 
##  Como funciona

O sistema segue a seguinte lógica de operação:

1. **Detecção de apagão**:
   - O vídeo é analisado quadro a quadro para verificar a **luminosidade média**.
   - Caso a luz caia (ambiente escureça), o sistema entende que houve um **apagão**.

2. **Solicitação de gesto**:
   - É tocado um áudio solicitando que a pessoa levante a mão caso precise de ajuda.

3. **Reconhecimento do gesto**:
   - Utilizando **MediaPipe Pose**, o sistema detecta se a **mão da pessoa foi levantada** (gesto simples com o punho acima do ombro).
   - Ao reconhecer o gesto, toca-se o áudio `Alerta.mp3`, informando que a orientação sonora será iniciada.

4. **Rota sonora de evacuação**:
   - O sistema toca em sequência os alarmes , **cada um repetido 3 vezes**, com **intervalos de 5 segundos** entre os blocos.
   - Isso simula alarmes espalhados fisicamente por diferentes pontos de um ambiente, guiando a pessoa por som até a saída.

5. **Confirmação de saída**:
   - Ao final do processo, é tocado o áudio `sucesso.mp3`, indicando que a pessoa chegou à saída com sucesso.

---


---

##  Tecnologias utilizadas

- **Python 3.10+**
- **MediaPipe Pose**
- **OpenCV** (para detecção de luminosidade)
- **Pygame** (para reprodução de sons)
- **NumPy** (processamento de imagem)

---

## Aplicabilidade

Além de ajudar **pessoas com deficiência visual** durante quedas de energia, o sistema pode ser útil em:

- Hospitais com pacientes com mobilidade reduzida.
- Prédios corporativos com evacuação assistida.
- Centros de comando e segurança.
- Escolas ou universidades com alunos com necessidades especiais.


!!!  O VÍDEO ESTÁ ANEXADO DENTRO DA PASTA COM O NOME: "Video_Explicativo.mp4"

---

##  Execução

1. Instale as dependências
2. execute "python safepath_gesto_alerta.py"

