import environ

env = environ.Env()
environ.Env.read_env()

# PREFIX_URL="https://res.cloudinary.com/docvlyucw/image/upload/v1662390258/Alpha%20Protocol"
# EMAIL="varadprabhu@student.sfit.ac.in"
# PASSWORD="codewizard763"
PREFIX_URL=env('PREFIX_URL')
EMAIL=env('EMAIL')
PASSWORD=env('PASSWORD')