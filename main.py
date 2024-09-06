import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging

# Configuração do logger para registrar atividades
logging.basicConfig(filename="monitoramento.log", level=logging.INFO,
                    format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

class MonitorDeDiretorio(FileSystemEventHandler):
    def __init__(self, diretorio):
        self.diretorio = diretorio

    def on_modified(self, event):
        if not event.is_directory:
            logging.info(f"Arquivo modificado: {event.src_path}")

    def on_created(self, event):
        if not event.is_directory:
            logging.info(f"Novo arquivo criado: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            logging.info(f"Arquivo excluído: {event.src_path}")

    def on_moved(self, event):
        if not event.is_directory:
            logging.info(f"Arquivo movido/renomeado: {event.src_path}")

def iniciar_monitoramento(diretorio):
    event_handler = MonitorDeDiretorio(diretorio)
    observer = Observer()
    observer.schedule(event_handler, diretorio, recursive=True)
    observer.start()
    logging.info(f"Monitoramento iniciado no diretório: {diretorio}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        logging.info("Monitoramento encerrado.")

    observer.join()

if __name__ == "__main__":
    diretorio_monitorado = "C:/Users/Advogado/Documentos/Processos"
    iniciar_monitoramento(diretorio_monitorado)
