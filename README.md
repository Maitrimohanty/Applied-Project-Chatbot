# Maitri Mohanty Applied Project Chatbot_Project
## ChatBot with interactive UI
### Downloads:
*ChatterBot-0.8.4  - you can download from https://pypi.org/project/ChatterBot/
*simple-websocket-server  - you can download from https://github.com/dpallot/simple-websocket-server
* The data is already attached but if you want to download you can do it from https://github.com/gunthercox/chatterbot-corpus as given in https://chatterbot.readthedocs.io/en/stable/corpus.html.

### Description of files
* train_chatbot.py file trains the data available in the data folder. Once it is trained , the result will be stored as db.sqlite.
* Chatbot.py uses this db.sqlite to generate responses for user queries.
* server.py sends back message to the UI.

### How to run
* Once you downloaded this project , Make sure you install the python packages mentioned in requirement.txt.
* Go to Chatbot_Project directory and run python server.py.
* Above step will open the server. Now right click the index.html page and open with brower. You will be able to see the chat window where you can start the conversation and test.
