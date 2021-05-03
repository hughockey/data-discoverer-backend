# Getting started with Docker and VSCode for development
1. Make sure you have the prerequisites setup as per these instructions: https://code.visualstudio.com/docs/remote/containers
2. Open the project folder in VSCode and click the green button in the bottom left: ![Green button in bottom left corner of VSCode screenshot](screenshots/open-folder-in-vscode-arrow.png)
3. Click "Remote-Containers: Open Folder in Container..." in the menu that opens:
![Remote-Containers: Open Folder in Container... screenshot](screenshots/open-folder-in-container.png)
4. Open the project folder in the explorer window that opens, vscode will open this folder inside of the docker container
5. Click "From 'docker-compose.yml' in the menu that opens:
![From 'docker-compose.yml' menu screenshot](screenshots/open-from-docker-compose.png)
6. VSCode will ask which container will be used for development, you should choose the flask container since we will primarily be doing python/flask development for the back-end:
![Choose development container screenshot](screenshots/open-flask-container.png)
7. Wait while Docker works its magic downloading and building all of the images(You won't have ot wait so long every time you open the project, just this first time, docker caches everything)
8. Voila, the project should now be up and running, if you open a new terminal in VSCode it will be running inside of the flask container with all the project dependencies setup correctly. This container also hass access to the mongodb container through the following connection string `mongodb://root:root@mongo:27017/`

# Accessing mongo-express to interact with the mongo database through a GUI
1. Make sure you have completed all of the steps under [Getting started with Docker and VSCode for development](#Getting started with Docker and VSCode for development) and you have the project running in your editor currently
2. Navigate to `http://localhost:8081/`
3. Login with the credentials: `admin:admin`
4. You should see a screen which looks like this:
![mongo-express screenshot](screenshots/mongo-express.png)

# Accessing mongodb in python
Here's a short snippet demonstrating how to interact with MongoDB in python when flask and mongodb are running through docker

```python  
import pymongo

client = pymongo.MongoClient("mongodb://root:root@mongo:27017/")

mydb = client["mydatabase"]
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)
```