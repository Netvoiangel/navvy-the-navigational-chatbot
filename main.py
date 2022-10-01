import eel

eel.init("dist")
eel.start("index.html", size=(450, 900))

@eel.expose
def set_color_red():
    return "red"

