from os import environ


# env variables
token = '/?token=%s' % environ.get('API_TOKEN')
