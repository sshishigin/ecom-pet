# djangoApp

Чтобы запустить весь бэк в докере нужно:

git clone https://github.com/sshishigin/djangoApp master

Далее в корне проекта:

docker-compose build  (только в первый раз)

Чтобы запустить контейнеры(по сути Django/redis/postegre):

docker-compose up 


Вроде все

Для этого тебе понадобиться установить docker и docker-compose, как это сделать можно найти по первой ссылке в гугле

api будет доступно по адресу 128.0.0.1:7000 ( в последней версии front проекта все настройки уже выставлены, обновись)

Возможно у тебя другой локальный адрес, тогда тебе его надо узнать и прописать в файле scr/api/instance.js в параметрах axios

Возможно файл entrypoint.sh не запустится, тогда его надо сделать исполняемым с помощью команды:

chmod u+x entrypoint.sh находясь в корне проекта

По дефолту создается юзер с правами админа:
admin@django.com
password
