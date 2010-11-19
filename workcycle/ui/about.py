import gtk

class WorkcycleAbout():
    def __init__(self):
        about_dialog = gtk.AboutDialog()
        about_dialog.set_name("Workcycler")
        about_dialog.set_version("0.2")
        about_dialog.set_authors(["Dominic Werner"])
        about_dialog.set_website("http://github.com/daddz/workcycler")
        about_dialog.run()
        about_dialog.destroy()
