# Car Rental

Apps:

- Api Car rental

## Local setup

### Copy environment

```
cp .dev_env .env
```

### Copy databse

```
cp db_dev.sqlite3 db.sqlite3
```

### Run

#### Run API

```
./up
```

#### Console or for Debugging

```
./up bash
``` 

Run `./devrun` to initialize the server

#### Web

And play! Login to:
http://127.0.0.1:9000/admin/
> user `dev@gmail.com` pass `devdevdev`


#### Tests

```
./up test