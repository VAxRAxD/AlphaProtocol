import environ

env = environ.Env()
environ.Env.read_env()

EMAIL=env('EMAIL')
PASSWORD=env('PASSWORD')