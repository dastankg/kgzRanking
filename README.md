# Отслеживание результатов команд Кыргызстана в NERC

Веб-приложение на Flask, которое собирает и отображает результаты команд из Кыргызстана в соревнованиях Northeastern European Regional Contest (NERC).

## Описание

Веб-приложение создано для мониторинга выступлений команд из Кыргызстана на соревнованиях NERC. Приложение автоматически собирает данные о результатах и представляет их в удобном для просмотра формате.

## Требования

Приложение требует следующие пакеты Python:

- Flask
- requests
- BeautifulSoup4

Полный список зависимостей доступен в файле `requirements.txt`.

## Установка

1. Клонируйте репозиторий:
```bash
git clone <URL>
cd <folder name>
```

2. Установите необходимые пакеты:
```bash
pip install -r requirements.txt
```

## Использование

1. Запустите приложение Flask:
```bash
python app.py
```

2. Откройте веб-браузер и перейдите по адресу:


## Настройка фильтрации команд

Для изменения списка отслеживаемых команд отредактируйте список `myTeam` в файле `app.py`:

```python
myTeam = ['AUCA', 'UCA', 'Kyrgyz STU', 'KRSU']
```

Добавьте или удалите названия учебных заведений в соответствии с вашими потребностями. 
Приложение будет фильтровать команды, содержащие эти строки в их названиях.
