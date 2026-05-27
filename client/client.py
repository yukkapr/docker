import time
import urllib.request

# Имя хоста 'web-app' мы пропишем ниже в docker-compose
url = "http://web-app:8098"

print("Клиент запущен и начинает опрос сервера...", flush=True)

while True:
    try:
        with urllib.request.urlopen(url) as response:
            status = response.getcode()
            print(f"Успешный запрос! Статус-код: {status}", flush=True)
    except Exception as e:
        print(f"Ошибка при подключении к серверу: {e}", flush=True)

    time.sleep(5)
