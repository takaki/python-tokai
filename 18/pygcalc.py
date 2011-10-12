#!/usr/bin/python
from gi.repository import Gtk

class GCalc:
    def __init__(self):
        self.gladefile = "pygcalc.glade"  
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
          
        self.sum  = 0

        self.btn_plus = self.builder.get_object('togglebutton1')

        menu_quit = self.builder.get_object('imagemenuitem5')
        menu_quit.connect('activate', Gtk.main_quit)

        menu_info = self.builder.get_object('imagemenuitem10')
        menu_info.connect('activate', self.show_dialog)

        dialog_btn = self.builder.get_object('aboutdialog-action_area1')
        dialog_btn.connect('button-press-event', Gtk.main_quit)
        
        for i in range(10):
            button = self.builder.get_object('button_' + str(i))
            button.connect('clicked', self.button_clicked, i)

        button = self.builder.get_object('button_plus')
        button.connect('clicked', self.button_clicked_plus)

        button = self.builder.get_object('button_ac')
        button.connect('clicked', self.button_clicked_ac)
        button.emit('clicked')


        window1 = self.builder.get_object('window1')
        window1.connect('delete-event', Gtk.main_quit)
        window1.show_all()
		
    def show_dialog(self, widget):
        dialog = self.builder.get_object('aboutdialog1')
        dialog.run()
        dialog.hide()

    def button_clicked(self, widget, arg):
        entry = self.builder.get_object('entry1')
        if self.btn_plus.get_active() == True and arg == 0:
            pass
        else:
            if self.btn_plus.get_active() == True:
                entry.set_text('')
                self.btn_plus.set_active(False)

            text = entry.get_text()
            entry.set_text(text + str(arg))

    def button_clicked_plus(self, widget):
        entry = self.builder.get_object('entry1')
        text = entry.get_text()
        if self.btn_plus.get_active() == False:
            self.btn_plus.set_active(True)
            self.sum = self.sum + int(text)
            entry.set_text(str(self.sum))
        else:
            pass

    def button_clicked_ac(self, widget):
        entry = self.builder.get_object('entry1')
        self.btn_plus.set_active(True)
        self.sum = 0
        entry.set_text('0')


if __name__ == "__main__":
    win = GCalc()
    Gtk.main()
