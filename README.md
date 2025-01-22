<!-- Step by step guide to Flask web app -->

I assume that you have python installed and text editor like vs code installed.
.Open your editor and integrated terminal
.set a path such as desktop c drive
.In that path mkdir name of the project as root directory
.cd to that directory
.In the root directory create virtual environment by:
python -m venv .env here .env is the name you can set any name of virt environment
.Activate that .env with: source .env/Scripts/activate. It is active.
.You can see the (.env) preceding the folder path.
.Once active now start installing necessary libraries. For this app I have:
pip install flask, pip install flask_alchemy
.open a server file naming main.py, app.py or server.py by creating a file in the
root directory. I have here server.py.

In this file (server.py) you will write code by importing flask and sqlalchemy. The
code is in the file.

To render the app create templates folder under the root folder. In the templates
create index.html, base.html, form.html, edit.html like files where you can create
functionalities for adding, updating and deleting items.

for data scheme, create a file call it data.txt or user.txt in the root folder.
In that file, write a json data sample. This file will be read in the server as data.db.

For styling I have used tailwind cdn in every template file. You can create a base.html file and extend it to other html files without repeating styling, footer and navigation if you choose to have one. In this app, I do not have that because I want
to show how easy it is to achieve CRUD functionality.
