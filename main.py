import os
import random
import subprocess
import configparser
from typing import Optional


def carregar_configuracao(config_file: str = "config.ini") -> dict:
    """
    Carrega as configurações do arquivo config.ini.

    Args:
        config_file (str): Caminho para o arquivo de configuração.

    Returns:
        dict: Dicionário contendo as configurações carregadas.
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    return config["Config"]


def selecionar_imagem(diretorio: str) -> Optional[str]:
    """
    Seleciona uma imagem aleatória de um diretório especificado.

    Args:
        diretorio (str): Caminho para o diretório contendo as imagens.

    Returns:
        Optional[str]: Caminho da imagem selecionada ou None se não houver imagens.
    """
    if not os.path.isdir(diretorio):
        return None

    extensoes_validas = {".jpg", ".jpeg", ".png", ".bmp", ".gif"}
    imagens = [
        os.path.join(diretorio, f)
        for f in os.listdir(diretorio)
        if os.path.isfile(os.path.join(diretorio, f))
        and os.path.splitext(f)[1].lower() in extensoes_validas
    ]

    if not imagens:
        return None

    return random.choice(imagens)


def trocar_papel_de_parede(imagem_uri: str, modo: str = "claro") -> bool:
    """
    Troca o papel de parede do GNOME utilizando o comando gsettings.

    Args:
        imagem_uri (str): URI da imagem a ser definida como papel de parede.
        modo (str, optional): Modo de aplicação ('claro', 'escuro'). Defaults to "claro".

    Returns:
        bool: True se o comando foi bem-sucedido, False caso contrário.
    """
    chave = "picture-uri" if modo == "claro" else "picture-uri-dark"
    comando = ["gsettings", "set", "org.gnome.desktop.background", chave, imagem_uri]
    result = subprocess.run(comando, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Erro ao tentar trocar o papel de parede para o modo {modo}.")
        print("Erro:", result.stderr)

    return result.returncode == 0


def main():
    """
    Função principal para selecionar uma imagem e trocar o papel de parede.
    """
    config = carregar_configuracao()
    WALLPAPER_DIR = config.get("wallpaper_dir")

    if not WALLPAPER_DIR:
        print("Diretório do papel de parede não encontrado na configuração.")
        return

    imagem_selecionada = selecionar_imagem(WALLPAPER_DIR)

    if not imagem_selecionada:
        print("Nenhuma imagem encontrada.")
        return

    imagem_uri = f"file://{imagem_selecionada}"

    sucesso_claro = trocar_papel_de_parede(imagem_uri, "claro")
    sucesso_escuro = trocar_papel_de_parede(imagem_uri, "escuro")

    if sucesso_claro and sucesso_escuro:
        print("Papel de parede trocado com sucesso.")
    else:
        print("Falha ao trocar o papel de parede.")


if __name__ == "__main__":
    main()
