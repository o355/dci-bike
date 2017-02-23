# (c) 2017 o355
# Licensed under the GNU GPL 3.0

from appJar import gui

app = gui("Bike")

def loginbuttons(btnName):
    username = app.getEntry("userEnt")
    password = app.getEntry("passEnt")
    print(username)
    print(password)

app.addLabel("title", "Welcome! Please login.", 0)
app.addLabel("user", "Username:", 1, 0)
app.addEntry("userEnt", 1, 1)
app.addLabel("pass", "Password:", 2, 0)
app.addEntry("passEnt", 2, 1)
app.addButtons( ["Submit"], loginbuttons, colspan=2)

app.go()
