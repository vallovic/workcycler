import gtk

class WorkcyclePreferences():
    
    def __init__(self, client, gconf_dir):
        dialog = gtk.Dialog("Workcycle Applet Preferences", None, 0, (gtk.STOCK_CANCEL, 
                                                                      gtk.RESPONSE_CANCEL, 
                                                                      gtk.STOCK_OK, 
                                                                      gtk.RESPONSE_OK))
        
        worktime_hbox = gtk.HBox(True)
        worktime_label = gtk.Label("Worktime:")
        worktime_input = gtk.Entry()
        worktime_input.set_text(str(client.get_int(gconf_dir + '/worktime')))
        worktime_hbox.pack_start(worktime_label)
        worktime_hbox.pack_start(worktime_input)
        worktime_hbox.pack_start(gtk.Label(" minutes"))
        
        funtime_hbox = gtk.HBox(True)
        funtime_label = gtk.Label("Funtime:")
        funtime_input = gtk.Entry()
        funtime_input.set_text(str(client.get_int(gconf_dir + '/funtime')))
        funtime_hbox.pack_start(funtime_label)
        funtime_hbox.pack_start(funtime_input)
        funtime_hbox.pack_start(gtk.Label(" minutes"))
        
        sound_hbox = gtk.HBox(True)
        sound_label = gtk.Label("Enable sound:")
        sound_input = gtk.CheckButton()
        sound_input.set_active(client.get_bool(gconf_dir + '/enable_sound'))
        sound_hbox.pack_start(sound_label)
        sound_hbox.pack_start(sound_input)
        sound_hbox.pack_start(gtk.Label(" "))
        
        dialog.vbox.pack_start(worktime_hbox, True, True, 0)
        dialog.vbox.pack_start(funtime_hbox, True, True, 0)
        dialog.vbox.pack_start(sound_hbox, True, True, 0)
        dialog.show_all()
        
        response = dialog.run()
        
        if response == gtk.RESPONSE_OK:
            client.set_int(gconf_dir + '/worktime', int(worktime_input.get_text()))
            client.set_int(gconf_dir + '/funtime', int(funtime_input.get_text()))
            client.set_bool(gconf_dir + '/enable_sound', sound_input.get_active())
            
        dialog.destroy()
