# VinMicroservice

## First step is:

Copy that command
```sh
git clone git@github.com:Sniperat/VinMicroservice.git && cd VinMicroservice/
```
and run on your terminal

### Create a file named   <i><b>`.env`</b></i>   inside of <b>`config/`</b> package and fill it with the following information:

>```SECRET_KEY={something}``` <br>
>```DEBUG=True```<br>
>```DATABASE_NAME=postgres```<br>
>```DATABASE_USER=postgres```<br>
>```DATABASE_PASS=postgres```<br>
>```DATABASE_HOST=db```<br>
>```DATABASE_PORT=5432```<br>
>```VIN_DECODER_URL={decode url}```


### First make sure you have docker installed on your computer
### And run this command on your terminal

```sh
docker-compose up -d --build
```

### After that on your [localhost](http://127.0.0.1:8000/) running that web application with port `8000` 

### You can easily check the endpoint url by entering swagger via the [link](http://127.0.0.1:8000/swagger/) below

###    `http://127.0.0.1:8000/swagger/`

### Finally you can test application with VIN data!
### I write it like to return all the data from response to check result
### After all you can see all informatsions in [admin panel](http://127.0.0.1:8000/admin/) but first you must create a 
### user to access the iformation following this command

```sh
docker-compose exec web python manage.py createsuperuser
```
#### and go `http://127.0.0.1:8000/admin/`
```sh
docker-compose down
```
#### to stop application
## Thank's
Any question `+998995047024` or [telegram](https://t.me/just_akbarov)
