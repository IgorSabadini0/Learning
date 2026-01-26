from pytubefix import YouTube
from pytubefix.cli import on_progress
import tkinter as tk
from tkinter import filedialog
import ffmpeg
import os
import re

def limpar_nome(nome):
    return re.sub(r'[\\/*?:"<>|]', "", nome)

def baixar_video_limitado():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    print("--- Downloader YouTube (Limite Máximo 1080p) ---")
    url = input("Cole a URL do vídeo: ")
    
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        titulo_limpo = limpar_nome(yt.title)
        
        print(f"\nVídeo encontrado: {yt.title}")

        # 1. Filtra as streams de vídeo (MP4)
        streams = yt.streams.filter(only_video=True, file_extension='mp4').order_by('resolution').desc()

        # 2. Lógica para limitar a 1080p
        video_stream = None
        for s in streams:
            # Extrai apenas o número da resolução (ex: "1080p" vira 1080)
            res_num = int(s.resolution[:-1]) 
            if res_num <= 1080:
                video_stream = s
                break # Pega a primeira que encontrar (que será a maior até 1080p)

        if not video_stream:
            video_stream = streams.last() # Caso extremo: pega a menor disponível

        print(f"Qualidade selecionada: {video_stream.resolution}")

        # 3. Selecionar pasta
        pasta_destino = filedialog.askdirectory()
        if not pasta_destino: return

        # 4. Downloads (Temporários)
        v_path = video_stream.download(output_path=pasta_destino, filename="temp_v.mp4")
        
        a_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        a_path = a_stream.download(output_path=pasta_destino, filename="temp_a.mp4")

        # 5. Merge com FFmpeg
        output_final = os.path.join(pasta_destino, f"{titulo_limpo}_{video_stream.resolution}.mp4")
        
        print(f"\nFinalizando vídeo em {video_stream.resolution}...")
        ffmpeg.output(ffmpeg.input(v_path), ffmpeg.input(a_path), output_final, vcodec='copy', acodec='aac').run(overwrite_output=True, quiet=True)

        # 6. Limpeza
        os.remove(v_path)
        os.remove(a_path)

        print(f"\nSucesso! Guardado em: {output_final}")
        os.startfile(pasta_destino)

    except Exception as e:
        print(f"\nOcorreu um erro: {e}")

if __name__ == "__main__":
    baixar_video_limitado()