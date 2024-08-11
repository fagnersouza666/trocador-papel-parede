
# Wallpaper Changer Script

Este script em Python permite que você selecione uma imagem aleatória de um diretório e a defina como papel de parede no ambiente GNOME do Linux. Ele suporta tanto modos claro quanto escuro, ajustando automaticamente o papel de parede para ambos.

## Características

- Seleção aleatória de imagens de um diretório especificado.
- Suporte a rotação automática de logs com o uso de `RotatingFileHandler`.
- Configuração fácil através de um arquivo `config.ini`.
- Logs gravados em um arquivo para auditoria e depuração.
- Configurável para ser executado periodicamente através do cron.

## Configuração

### 1. Requisitos

- Python 3.x instalado.
- Ambiente GNOME no Linux.
- Acesso ao terminal para configurar o cron.

### 2. Instalação

1. **Clone o repositório ou copie os arquivos para o seu sistema**.

2. **Instale as dependências necessárias** (se houver). Por exemplo, se você estiver usando um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Configuração do `config.ini`**:
    - Crie um arquivo `config.ini` no diretório raiz do projeto com o seguinte conteúdo:
    
    ```ini
    [Config]
    wallpaper_dir = /caminho/completo/para/o/diretorio/das/imagens
    ```

    - **`wallpaper_dir`**: Especifique o caminho completo para o diretório onde as imagens do papel de parede estão armazenadas.

### 3. Execução Manual

Para trocar o papel de parede manualmente, execute o script `main.py`:

```bash
python3 main.py
```

### 4. Configuração de Execução Automática no Linux (Cron)

Para trocar o papel de parede automaticamente em intervalos regulares, você pode usar o `cron` para agendar a execução do script.

1. **Abra o crontab para edição**:

    ```bash
    crontab -e
    ```

2. **Adicione uma linha para agendar o script**. Por exemplo, para executar a cada hora:

    ```bash
    0 * * * * /caminho/para/o/python3 /caminho/para/o/script/main.py
    ```

    - **`0 * * * *`**: Executa o script na primeira minuto de cada hora.
    - **`/caminho/para/o/python3`**: Especifique o caminho completo para o Python 3.
    - **`/caminho/para/o/script/main.py`**: Especifique o caminho completo para o arquivo `main.py`.

3. **Salve e saia do editor**. O cron agora executará o script nos intervalos definidos.

### 5. Logs

Os logs são gravados no arquivo `wallpaper_changer.log`, que é rotacionado automaticamente quando atinge um tamanho específico.

- **Ver logs**:
    ```bash
    tail -f wallpaper_changer.log
    ```

- **Configuração de rotação de logs**: A rotação de logs é configurada no script `logging_config.py`, onde você pode ajustar o tamanho máximo dos arquivos de log e o número de arquivos de backup mantidos.

### 6. Contribuições

Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

### 7. Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
