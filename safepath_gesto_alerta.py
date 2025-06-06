import cv2
import mediapipe as mp
import pygame
import time
import numpy as np

# Inicialização do MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Inicialize o pygame mixer para tocar áudio
pygame.init()
pygame.mixer.init()

# Caminhos de arquivos
caminho_video = "movimento.mp4"
audios = {
    "pedido": "pedido.mp3",
    "alerta": "Alerta.mp3",
    "sucesso": "sucesso.mp3",
    "alarmes": ["alarme1.mp3", "alarme2.mp3", "alarme3.mp3", "alarme4.mp3", "alarme5.mp3"]
}

# Função para tocar um som e esperar terminar
def tocar_audio(caminho):
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

# Função para verificar escuridão (luminosidade baixa)
def ambiente_escuro(frame, limiar=150):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    luminosidade = np.mean(gray)
    print(f"Luminosidade média: {luminosidade}")
    return luminosidade < limiar

# Função que verifica se a mão está levantada (punho acima do ombro)
def mao_levantada(landmarks):
    try:
        pulso_dir = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]
        ombro_dir = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
        return pulso_dir.y < ombro_dir.y
    except:
        return False

# Carrega o vídeo
cap = cv2.VideoCapture(caminho_video)
apagao_detectado = False
gesto_detectado = False

while cap.isOpened():
    sucesso, frame = cap.read()
    if not sucesso:
        break

    if not apagao_detectado and ambiente_escuro(frame):
        print("🔦 Apagão detectado! Tocando áudio de orientação inicial...")
        tocar_audio(audios["pedido"])
        apagao_detectado = True

    elif apagao_detectado and not gesto_detectado:
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resultado = pose.process(img_rgb)

        if resultado.pose_landmarks and mao_levantada(resultado.pose_landmarks.landmark):
            print("🖐️ Mão levantada detectada! Iniciando rota sonora...")
            tocar_audio(audios["alerta"])
            for nome in audios["alarmes"]:
                for _ in range(3):
                    print(f"Tocando {nome}")
                    tocar_audio(nome)
                    time.sleep(1)
                time.sleep(5)
            tocar_audio(audios["sucesso"])
            gesto_detectado = True
            break

cap.release()
cv2.destroyAllWindows()
