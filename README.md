# Исходный код с ролика [DASHBOARD для Discord Bot | Python](https://www.youtube.com/watch?v=N4nEb3mCW7U) (переписанный)

## Инструменты 🛠
![Python](https://img.shields.io/badge/Python-3.8-blue?style=for-the-badge&logo=python)
![aiohttp](https://img.shields.io/badge/aiohttp-3.8.1-blue?style=for-the-badge&logo=aiohttp)
![flask](https://img.shields.io/badge/Flask-2.0.3-blue?style=for-the-badge&logo=flask)

## Установка 💾
```
$ git clone https://github.com/Fsoky/Dashboard-Discord-Bot.git
$ cd Dashboard-Discord-Bot
$ pip install -r requirements.txt
```

```
$ pip install Flask[async]
```


## Использование 🎈
В файл `config.py`, в переменные: *CLIENT_ID*, *CLIENT_SECRET*, записать соответствующие данные. [Официальный портал разработчика](https://discord.com/developers/applications/) \
**Инструкция:**
1. Выберите свое приложение (если не существует - создайте)
2. Перейдите в *Oauth2*
3. В поле *redirects* добавьте ссылку перенаправления `http://127.0.0.1:5000/login`
4. Скопируйте *CLIENT ID*, *CLIENT SECRET* и запишите в переменные.
5. Запустите файл *main.py*

```
$ python main.py
```

### Присоединяйся к нам
[![Vkontakte](https://img.shields.io/badge/Vkontakte-black?style=for-the-badge&logo=VK)](https://vk.com/fsoky)
[![YouTube](https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=YouTube)](https://youtube.com/c/Фсоки)
[![Telegram](https://img.shields.io/badge/Telegram-blue?style=for-the-badge&logo=Telegram)](https://t.me/fsokycommunity)