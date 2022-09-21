import environ

env = environ.Env()
environ.Env.read_env()

EMAIL=env('EMAIL')
PASSWORD=env('PASSWORD')
DBNAME=env('NAME')
DBPASS=env('DBPASS')
DBUSER=env('DBUSER')