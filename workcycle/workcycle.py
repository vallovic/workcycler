import os
import pynotify
import gconf
from pygame import mixer
from threading import Timer

class Workcycle(object):
    
    is_worktime = True;
    root_dir = os.path.abspath(os.path.curdir)
    image_dir = root_dir + "/images"
    sound_dir = root_dir + "/sounds"
    gconf_dir = '/apps/workcycler'
    timer = None
    
    def __init__(self):
        self._init_gui()
        self._init_notify()
        self._init_mixer()
        self._init_gconf()
        
    def _init_gui(self):
        pass
        
    def _init_notify(self):
        pynotify.init("workcycler")
        ##TODO: random funny comments for the notifications
        self.worktime_notification = pynotify.Notification("Worktime", 
                                                           "Start working now",
                                                           self.image_dir + "/appointment-soon.png")
        self.funtime_notification = pynotify.Notification("Funtime", 
                                                          "Have some fun", 
                                                          self.image_dir + "/appointment-soon.png")
        self.workcycle_notification = pynotify.Notification("Workcycle",
                                                            "Stopped workcycle",
                                                            self.image_dir + "/appointment-soon.png")
                                                            
    def _init_mixer(self):
        mixer.init()
        self.sound = mixer.Sound(self.sound_dir + "/ring.wav")
    
    def _init_gconf(self):
        self.client = gconf.client_get_default()
        self.client.add_dir(self.gconf_dir, gconf.CLIENT_PRELOAD_NONE)
        self.client.notify_add(self.gconf_dir + '/worktime', self.update_worktime)
        self.client.notify_add(self.gconf_dir + '/funtime', self.update_funtime)
        self.client.notify_add(self.gconf_dir + '/enable_sound', self.update_sound)
        self.update_worktime()
        self.update_funtime()
        self.update_sound()
        
    def update_worktime(self, *args):
        self.worktime = self.client.get_int(self.gconf_dir + '/worktime')
    
    def update_funtime(self, *args):
        self.funtime = self.client.get_int(self.gconf_dir + '/funtime')
        
    def update_sound(self, *args):
        self.enable_sound = self.client.get_bool(self.gconf_dir + '/enable_sound')
    
    def toggle(self, *args):        
        if not self.timer == None: 
            self.timer.cancel()
        if self.is_worktime:
            self.timer = Timer(self.worktime * 60, self.toggle)
            self.worktime_notification.show()
        else:
            self.timer = Timer(self.funtime * 60, self.toggle)
            self.funtime_notification.show()
        if self.enable_sound:
            self.sound.play()
        self.timer.start()
        self.toggle_child()
        self.is_worktime = not self.is_worktime
    
    def toggle_child(self, *args):
        pass
    
    def stop(self, *args):
        if not self.timer == None:
            self.timer.cancel()
        self.workcycle_notification.show()
        self.stop_child()
        
    def stop_child(self, *args):
        pass
    
    def show_about_dialog(self, widget):
        pass
        
    def show_preferences_dialog(self, widget):
        pass
    
    def quit(self, *args):
        if not self.timer == None: 
            self.timer.cancel()
        self.quit_child()
    
    def quit_child(self, *args):
        pass
