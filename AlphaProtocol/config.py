import environ

env = environ.Env()
environ.Env.read_env()

PREFIX_URL=env('PREFIX_URL')