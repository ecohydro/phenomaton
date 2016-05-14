"""Instagram API."""
import os

env_variables = 'variables-common.json'
if os.path.exists(env_variables):
    print('Importing environment from {}'.format(env_variables))
    with open(env_variables) as file:
        data = json.load(file)
    for key in data.keys():
        os.environ[key] = data[key]

api = InstagramAPI(
    client_id=os.getenv('INSTAGRAM_CLIENT_ID'),
    client_secret=os.getenv('INSTAGRAM_CLIENT_SECRET')
)
