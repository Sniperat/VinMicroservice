# VinMicroservice

## First step is:

Copy that command
```sh
git clone git@github.com:Sniperat/VinMicroservice.git && cd VinMicroservice/
```
and run on your terminal

Create a file named   <i><b>`.env`</b></i>   inside of <b>`config/`</b> package and fill it with the following information:

```sh
SECRET_KEY='wwf*2#86t64!fgh6yav$aoeuo@u2o@fy&*gg76q!&%4i_tbouau'
DEBUG=True
DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASS=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
ALLOWED_HOSTS='*'
VIN_DECODER_URL={decode url}
```

First make sure you have docker installed on your computer
And run this command on your terminal

```sh
docker-compose up -d --build
```

After that on your [localhost](http://127.0.0.1:8000/) running that web application with port `8000` 

You can test application with VIN data by using a postman to send get method with url parameter like:
#### `http://127.0.0.1:8000/?vinId={VIN_ID}`

I write it to return all the data from response to check result

After all you can see all information in [admin panel](http://127.0.0.1:8000/admin/) but first you must create a 
user to access the information following this command

```sh
docker-compose exec web python manage.py createsuperuser
```
and go `http://127.0.0.1:8000/admin/`
```sh
docker-compose down
```
to stop application
#### Thank's
Any question `+998995047024` or [telegram](https://t.me/just_akbarov)
