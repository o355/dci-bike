from appJar import gui

# create the GUI & set a title
app = gui("Login to DCI-Bike 1!")
app.showSplash(text, fill='red', stripe='black', fg='white', font=44)

def press(btnName):
    if btnName == "Cancel":
        app.stop()
        return

    if app.getEntry("userEnt") == "testuser":
        if app.getEntry("passEnt") == "testpassword":
            app.infoBox("Success", "Congratulations, you are logged in!")
            app.infoBox("Logging you in welcome user!")
           
        else:
            app.errorBox("User login Failed!", "Invalid password")
    else:
        app.errorBox("User Login Failed!", "Invalid username")

# add labels & entries
# in the correct row & column
app.addLabel("userLab", "Username:", 0, 0)
app.addEntry("userEnt", 0, 1)
app.addLabel("passLab", "Password:", 1, 0)
app.addSecretEntry("passEnt", 1, 1)

# changed this line to call a function
app.addButtons( ["Submit", "Cancel"], press, colspan=2)

# add some enhancements
app.setFocus("userEnt")
app.go
