import pytextnow

# Way 1. Include connect.sid and csrf cookie in the constructor
client = pytextnow.Client("username", sid_cookie="sid", csrf_cookie="csrf").

# Way 2. Just instantiate and a prompt will appear on the command line

# Way 3. If you inputed the wrong cookie and are getting RequestFailed. This is how to reset it
# client.auth_reset()
# will redo the prompt

client.send_sms("5108901021", "Hello World!")
