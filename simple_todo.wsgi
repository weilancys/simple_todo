# using a virtual environment
activate_this = '/path/to/env/bin/activate_this.py'  # change this line to match your actual virtualenv absolute path
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from simple_todo import create_app
application = create_app()