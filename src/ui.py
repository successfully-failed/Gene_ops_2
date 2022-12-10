#this is the ui version of Gene-ops 
#this branch is meant to simplify the code and to work without the glade file

import gi
from Uber_object import Powerobject as Obj
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk

class Main (gtk.Window):
    def __init__ (self):
        super().__init__(title = "Gene-ops")
        obj = Obj()
#methods to functions
        
        def refresh (self):
                repl_show.button.set_active(False)
                transc_show.button.set_active(False)
                transl_show.button.set_active(False)
                show_button2.set_active(False)
                obj.refresh()
                repl_buffer.set_text("")
                transc_buffer.set_text("")
                transl_buffer.set_text("")

        def repl_go (self):
                obj.string = repl_entry.get_text()
                obj.do_all_replication()
                repl_buffer.set_text(obj.repl_out, len(obj.repl_out))
                obj.refresh()
        def transc_go (self):
                obj.string = transc_entry.get_text()
                obj.do_all_transcription()
                transc_buffer.set_text(obj.transc_out, len(obj.transc_out))
                obj.refresh()
        def transl_go (self):
                obj.string = transl_entry.get_text()
                obj.do_all_translation()
                transl_buffer.set_text(obj.transl_out, len(obj.transl_out))
                obj.refresh()
        def show (self):
                obj.opt_a = "1"
        def show2 (self):
                obj.opt_b = "1"

#Setup of the window parameters
        gtk.Window.set_default_size(self, 400,300)

#Other objects
        refresh_button = gtk.Button(label = "refresh")
        refresh_button.connect("clicked",refresh)
        stack_switcher = gtk.StackSwitcher(orientation = gtk.Orientation.VERTICAL)
        welcome_label = gtk.Label(label="select\nthe task")
        

#objects in boxes
        
        class Label:
                def __init__ (self, name):
                        self.label = gtk.Label(label = name + " options")
                def __del__ (self):
                        del self.label
        
        class Show_button:
                def __init__ (self):
                        self.button = gtk.CheckButton(label = "Do you want to print gene string?")
                        self.button.connect("toggled", show)
                def __del__ (self):
                        del self.button


        repl_results = gtk.TextView()
        repl_buffer = repl_results.get_buffer()
        transc_results = gtk.TextView()
        transc_buffer = transc_results.get_buffer()
        transl_results = gtk.TextView()
        transl_buffer = transl_results.get_buffer()
        repl_go_btt = gtk.Button(label= "Go")
        repl_go_btt.connect("clicked", repl_go) 
        transc_go_btt = gtk.Button(label= "Go")
        transc_go_btt.connect("clicked", transc_go)
        transl_go_btt = gtk.Button(label= "Go")
        transl_go_btt.connect("clicked", transl_go)
        show_button2 = gtk.CheckButton(label= "Do you want to see codons list?")
        show_button2.connect("toggled", show2)


#stack boxes
        repl_box = gtk.Box(orientation = gtk.Orientation.VERTICAL)
        repl_label = Label("replication")
        repl_box.pack_start(repl_label.label, False, False, 5)
        repl_entry = gtk.Entry()
        repl_box.pack_start(repl_entry, False, False, 0)
        repl_show = Show_button()
        repl_box.pack_start(repl_show.button, False, False, 0)  
        repl_box.pack_start(repl_go_btt, False, False, 0)
        repl_box.pack_start(repl_results,True,True, 0)

        transc_box = gtk.Box(orientation = gtk.Orientation.VERTICAL)
        transc_label = Label("transcription")
        transc_box.pack_start(transc_label.label, False, False, 5)
        transc_entry = gtk.Entry()
        transc_box.pack_start(transc_entry, False, False, 0)
        transc_show = Show_button()
        transc_box.pack_start(transc_show.button, False, False, 0)  
        transc_box.pack_start(transc_go_btt, False, False, 0)
        transc_box.pack_start(transc_results,True,True, 0)
        
        transl_box = gtk.Box(orientation = gtk.Orientation.VERTICAL)
        transl_label = Label("translation")
        transl_box.pack_start(transl_label.label, False, False, 5)
        transl_entry = gtk.Entry()
        transl_box.pack_start(transl_entry, False, False, 0)
        transl_show = Show_button()
        transl_box.pack_start(transl_show.button, False, False, 0) 
        transl_box.pack_start(show_button2, False, False, 0)
        transl_box.pack_start(transl_go_btt, False, False, 0)
        transl_box.pack_start(transl_results,True,True, 0)

#Grid options
        stack = gtk.Stack()
        #stack objects
        stack.add_titled(repl_box, "replication", "replication" )
        stack.add_titled(transc_box, "transcription", "transcription")
        stack.add_titled(transl_box, "translation", "translation")
        stack_switcher.set_stack(stack)
        side_panel = gtk.Box(orientation = gtk.Orientation.VERTICAL)
        side_panel.pack_start(welcome_label, False , True, 0)
        side_panel.pack_start(stack_switcher, True, True, 0)
        side_panel.pack_end(refresh_button, False, False,0)
        main_box = gtk.Box(orientation = gtk.Orientation.HORIZONTAL)
        main_box.pack_start(side_panel, False, False, 10)
        main_box.pack_start(stack, True, True, 0)





        self.add(main_box)
        
        
         
main = Main()
main.connect("destroy", gtk.main_quit)
main.show_all()
gtk.main()

