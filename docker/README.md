# Docker

*Образ (Image)* - чертёж для контейнеров, содержит код приложения и окружение. На основе образа создаются контейнеры. 

*Контейнеры* - пакеты, экземпляры образа. Контейнер - единица программного обеспечения, которую мы можем запустить. На основе одного образа создаётся n-ное количество контейнеров.


Где найти образ?
* Взять готовый на [Docker Hub](https://hub.docker.com/).
* Создать свой на основе готового из хаба.

```sh
# Скачать образ "Python"
docker pull python

# Запустить контейнер на базе образа "Python". Если он не скачен, докер его скачает из хаба.
docker run python

# Запустить контейнер и открыть интерактивную консоль
docker run -it python

# Показать запущенные контейнеры
docker ps

# Показать все контейнеры
docker ps -a

# Остановить контейнер
docker stop имя_контейнера
```
Для создания кастомного образа, в корне проекта создаём `Dockerfile`. В нём пишутся инструкции, которые выполнит докер при билде образа и при запуске контейнера.

Для поддержки докерфайла в VS Code есть [расширение от Майкрософт](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker).

## Dockerfile

1. Первая инструкция - на основе какого образа создаём свой:
```docker
FROM python
```

2. Какие файлы из папки проекта нужны и куда их поместить в образе. Пути работают с юниксовыми абсолютными и относительными путями.
```docker
COPY папка_на_хосте папка_в_образе

# Копируем все файлы проекта в корень образа
COPY . .

# Копируем все файлы проекта в папку app (папка будет создана)
COPY . /app
```

3. Меняем рабочую папку. Команды будут выполнятся из-под неё. После этого `COPY . /app` можно поменять на `COPY . .`
```docker
WORKDIR /app
```

4. Запускаем нужные команды:
```docker
RUN pip install -r requirements.txt
```

5. Запускаем приложение. Если запустим через `RUN`, то приложение запустится в образе, а не в контейнере. Для этого есть команда `CMD`. Она запустит сервер, когда запустится контейнер, основанный на нашем готовом образе. Синтаксис похож на массив.
```docker
CMD ["python", "main.py"]
```

6. Также нужно открыть порт, на котором работает наше приложение:
```docker
EXPOSE 80
```

Докерфайл готов. 
```sh
# Билдим образ:
docker build путь_к_докерфайлу

# Если докерфайл в рабочей папке
docker build .

# Запускаем контейнер на основе нашего образа
docker run id_образа
docker run 0e0c44d8c8e17148fdc5e8124fe15f14931f79e7075af1f7cec28efb67ee0416

# Также нужно открыть порт при запуске контейнера
docker run -p порт_хоста:порт_внутри_контейнера id_образа
docker run -p 5000:80 0e0c44d8c8e17148fdc5e8124fe15f14931f79e7075af1f7cec28efb67ee0416

# Остановить контейнер (имя_образа можно посмотреть командой 'docker ps')
docker stop имя_образа

# Запустить контейнер опять
docker start имя_образа
```

Теперь наше приложение доступно по адресу `localhost:5000`.

## Кэш

Образы имеют многослойную архитектуру. Если изменить код или поменять инструкции в докерфайле, только изменённые инструкции будут выполнены. Всё, что не тронуто, будет взято из кэша.

Чтобы каждый раз не переустанавливать зависимости и т.д. можно их подтянуть заранее, перед копированием кода. Они будут кэшированы и больше не будут загружаться.

```docker
COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app
```

```
❯ docker build .
...
 => [1/5] FROM docker.io/library/python                         
 => [internal] load build context                               
 => => transferring context: 349B                               
 => CACHED [2/5] WORKDIR /app                                   
 => CACHED [3/5] COPY requirements.txt /app                     
 => CACHED [4/5] RUN pip install -r requirements.txt            
 => [5/5] COPY . /app                                           
...
```

## Привязанный и отвязанный режим

`docker run` запускает контейнер в привязанном режиме. То есть наш терминал блокируется и мы видим терминал внутри контейнера. Можно этого избежать, запустив контейнер в отвязанном режиме:
```
docker run -d id_образа
```

Запустить контейнер опять + привязаться к нему:
```
docker start -a контейнер
```

Можно привязаться к контейнеру с помощью `attach`:
```
docker attach контейнер
```

Посмотреть логи:
```
docker logs контейнер
```

## Управление образами и контейнерами

```
# Вывести список образов:
docker images

# Удалить образ:
docker rmi образ [образ образ...]

# Удалить неиспользуемые образы
docker image prune

# Удалить контейнер, когда он закончит работу
docker --rm run контейнер

# Вывести всю информацию об образе
docker image inspect образ
```

## Наименование образов и контейнеров
Назвать контейнер myapp
```
docker run --name myapp ...
```
```
❯ docker run -d -p 5000:80 --name myapp 1609a7b5123735f1f91d7e90830302d7167ed04bf039d788f166b80f4086369a
55f2dc5921aa93690df7f9b233d02c55dcd634d989921eeba7f8c7c1a8a810eb

❯ docker ps
CONTAINER ID   IMAGE          ...   NAMES
55f2dc5921aa   1609a7b51237   ...   myapp

❯ docker stop myapp
myapp
```

Образы именуются именуются тэгами
```
name:tag

python:3.9.4
node:latest
```
Задать имя и тэг:
```
docker build -t myapp:whatever
```
```
❯ docker build -t myapp:whatever .
[+] Building 0.2s (10/10) FINISHED
...
 => => naming to docker.io/library/myapp:whatever

❯ docker images
REPOSITORY   TAG        IMAGE ID       CREATED        SIZE
myapp        whatever   1609a7b51237   11 hours ago   895MB
...
python       latest     49e3c70d884f   2 weeks ago    885MB

❯ docker run -d --name appcont myapp:whatever
2d2b3dcc928ddab059e50af4ba95a230df3d37f3e44bdeb8f19fb8ecf3df599a

❯ docker ps
CONTAINER ID   IMAGE            COMMAND            CREATED          STATUS          PORTS     NAMES
2d2b3dcc928d   myapp:whatever   "python main.py"   2 seconds ago    Up 1 second     80/tcp    appcont
```

## Копирование файлов

```
# Скопировать в/из контейнера
docker cp файл_или_папка контейнер:куда_копировать
docker cp контейнер:куда_копировать файл_или_папка
```