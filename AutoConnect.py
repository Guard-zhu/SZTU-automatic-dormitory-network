from request_command import connect
from tips import tip

if connect() == 200:
    tip()
