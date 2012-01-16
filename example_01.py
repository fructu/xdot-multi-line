#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# example of xdot with multiline support
# author: F. Manuel Hevia (fructu@gmail.com)
# part of abidos https://github.com/fructu/abidos
#
# original code_
#  http://code.google.com/p/jrfonseca/wiki/XDot
#  Copyright 2008 Jose Fonseca
#

import os
import gtk
import gtk.gdk

import xdot

class MyDotWindow(xdot.DotWindow):

    def __init__(self):
        #activate/desactivate the feature here:
        xdot.options.set_multi_line_activate(1)
        #separator is ';' bye default
        xdot.options.set_multi_line_separator('|')
        xdot.DotWindow.__init__(self)
        self.widget.connect('clicked', self.on_url_clicked)

    def on_url_clicked(self, widget, url, event):            
        dialog = gtk.MessageDialog(
                parent = self, 
                buttons = gtk.BUTTONS_OK,
                message_format="%s clicked" % url)
        dialog.connect('response', lambda dialog, response: dialog.destroy())
        dialog.run()
        return True

def main():
    window = MyDotWindow()
    window.set_filter("dot")
    window.open_file("example_01.dot");
    window.connect('destroy', gtk.main_quit)
    gtk.main()

if __name__ == '__main__':
    main()

