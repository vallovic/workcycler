import gtk
import about
import preferences
from .. import workcycle


gtk.gdk.threads_init()

class WorkcycleTray(workcycle.Workcycle):   
    
    def __init__(self):
        super(WorkcycleTray, self).__init__()
  
    def _init_gui(self):
        self.statusicon = gtk.StatusIcon()
        self.statusicon.set_from_file(self.image_dir + "/appointment-soon-small.png")
        self.statusicon.connect("popup-menu", self.popup_menu)
        self.statusicon.connect("activate", self.toggle)
        self.statusicon.set_tooltip("Workcycler")        
    
    def start(self):
        gtk.gdk.threads_enter()
        gtk.main()
        gtk.gdk.threads_leave()
    
    def toggle_child(self):
        if self.is_worktime:
            self.statusicon.set_tooltip("Worktime in progress")
            self.statusicon.set_from_file(self.image_dir + "/appointment-missed.png")
        else:
            self.statusicon.set_tooltip("Funtime in progress")
            self.statusicon.set_from_file(self.image_dir + "/appointment-soon-small.png")
    
    def stop_child(self):
        self.statusicon.set_from_file(self.image_dir + "/appointment-soon-small.png")
        self.statusicon.set_tooltip("Workcycler")
    
    def show_about_dialog(self, widget):
        about.WorkcycleAbout()
        
    def show_preferences_dialog(self, widget):
        preferences.WorkcyclePreferences(self.client, self.gconf_dir)
    
    def popup_menu(self, icon, button, time):
        menu = gtk.Menu()
        
        toggle = gtk.MenuItem("Toggle timer")
        stop = gtk.MenuItem("Stop timer")
        preferences = gtk.MenuItem("Preferences")
        separator = gtk.MenuItem()
        about = gtk.MenuItem("About")
        quit = gtk.MenuItem("Quit")
        
        toggle.connect("activate", self.toggle)
        stop.connect("activate", self.stop)
        preferences.connect("activate", self.show_preferences_dialog)
        about.connect("activate", self.show_about_dialog)
        quit.connect("activate", self.quit)
        
        
        menu.append(toggle)
        menu.append(stop)
        menu.append(preferences)
        menu.append(separator)
        menu.append(about)
        menu.append(quit)
        
        menu.show_all()
        
        menu.popup(None, None, gtk.status_icon_position_menu, button, time, self.statusicon) 
           
    def quit_child(self):
        gtk.main_quit()   
