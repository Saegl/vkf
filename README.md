# Vkontakte friends (vkf)

Use this app to import all your vk friends to JSON, CSV or TSV

## Usage

You need python 3.10 or higher

0. Clone this app

```bash
git clone https://github.com/Saegl/vkf.git
cd vkf
```

1. Install app using pip. (Consider using [virtual environment](https://docs.python.org/3/library/venv.html))

```bash
pip install .
```

2. Auth to your existing app or [create one](docs/create_app.md)

```bash
vkf auth <client_id>
```

You will get output like this

```
Access token successfully catched and parsed
Access token: <YOUR_ACCESS_TOKEN>
Expires in: 86400 seconds
UserID: <YOUR_USER_ID>
```

3. Import your friends

```bash
vkf load_friends <YOUR_ACCESS_TOKEN> <USER_ID> <format> <OUTPUT_NAME>
```

You can use any <USER_ID>, for example <YOUR_USER_ID>  
format is json, csv or tsv  
You can specify <OUTPUT_NAME>, by default it is ('report.' + format) in current dir

## For developers

info - [developer notes](docs/developers.md)
