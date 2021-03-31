########### remove manual buttons ########################
root_window.tk.call('pack', 'forget', '.tabs_manual.spindlef.ccw')
root_window.tk.call('pack', 'forget', '.tabs_manual.spindlef.cw')
root_window.tk.call('pack', 'forget', '.tabs_manual.spindlef.stop')
root_window.tk.call('pack', 'forget', '.tabs_manual.spindlef.spindleplus')
root_window.tk.call('pack', 'forget', '.tabs_manual.spindlef.spindleminus')
root_window.tk.call('pack', 'forget', '.tabs_manual.spindlef.brake')
root_window.tk.call('pack', 'forget', '.tabs_manual.flood')
root_window.tk.call('pack', 'forget', '.tabs_manual.mist')

######################## remove toolbar ##########
root_window.tk.call('pack', 'forget', '.toolbar.machine_power')
root_window.tk.call('pack', 'forget', '.toolbar.machine_estop')
root_window.tk.call('pack', 'forget', '.toolbar.file_open')
root_window.tk.call('pack', 'forget', '.toolbar.reload')
root_window.tk.call('pack', 'forget', '.toolbar.program_run')
root_window.tk.call('pack', 'forget', '.toolbar.program_step')
root_window.tk.call('pack', 'forget', '.toolbar.program_pause')
root_window.tk.call('pack', 'forget', '.toolbar.program_stop')
root_window.tk.call('pack', 'forget', '.toolbar.program_blockdelete')
root_window.tk.call('pack', 'forget', '.toolbar.program_optpause')
root_window.tk.call('pack', 'forget', '.toolbar.view_zoomin')
root_window.tk.call('pack', 'forget', '.toolbar.view_zoomout')
root_window.tk.call('pack', 'forget', '.toolbar.view_z')
root_window.tk.call('pack', 'forget', '.toolbar.view_z2')
root_window.tk.call('pack', 'forget', '.toolbar.view_x')
root_window.tk.call('pack', 'forget', '.toolbar.view_y')
root_window.tk.call('pack', 'forget', '.toolbar.view_p')
root_window.tk.call('pack', 'forget', '.toolbar.rotate')
root_window.tk.call('pack', 'forget', '.toolbar.clear_plot')
root_window.tk.call('pack', 'forget', '.toolbar.rule0')
root_window.tk.call('pack', 'forget', '.toolbar.rule4')
root_window.tk.call('pack', 'forget', '.toolbar.rule8')
root_window.tk.call('pack', 'forget', '.toolbar.rule9')
root_window.tk.call('pack', 'forget', '.toolbar.rule12')
root_window.tk.call('grid', 'forget', '.toolbar')

###############  choose/remove sliders ########################
# root_window.tk.call('grid','forget','.pane.top.feedoverride')
root_window.tk.call('grid', 'forget', '.pane.top.rapidoverride')
# root_window.tk.call('grid','forget','.pane.top.spinoverride')
# root_window.tk.call('grid','forget','.pane.top.jogspeed')
root_window.tk.call('grid', 'forget', '.pane.top.ajogspeed')
root_window.tk.call('grid', 'forget', '.pane.top.maxvel')

############ remove active gcodes lable and codes ##########
# root_window.tk.call('grid','forget','.pane.top.gcodel')
# root_window.tk.call('grid','forget','.pane.top.gcodes')

########### move toolbar ###############
root_window.tk.call('grid', '.toolbar', '-row', '1',
                    '-column', '6', '-sticky', 'nsew')

########### move/choose toolbar buttons ################
root_window.tk.call('pack', '.toolbar.machine_estop',
                    '-side', 'top', '-fill', 'y')
root_window.tk.call('pack', '.toolbar.machine_power',
                    '-side', 'top', '-fill', 'y')
root_window.tk.call('pack', '.toolbar.file_open', '-side', 'top', '-fill', 'y')
root_window.tk.call('pack', '.toolbar.reload', '-side', 'top', '-fill', 'y')
root_window.tk.call('pack', '.toolbar.program_run',
                    '-side', 'top', '-fill', 'y')
root_window.tk.call('pack', '.toolbar.program_pause',
                    '-side', 'top', '-fill', 'y')
root_window.tk.call('pack', '.toolbar.program_stop',
                    '-side', 'top', '-fill', 'y')
# root_window.tk.call('pack','.toolbar.program_blockdelete','-side','top','-fill','y')
root_window.tk.call('pack', '.toolbar.program_optpause',
                    '-side', 'top', '-fill', 'y')
root_window.tk.call('pack', '.toolbar.view_zoomin',
                    '-side', 'top', '-fill', 'y')
root_window.tk.call('pack', '.toolbar.view_zoomout',
                    '-side', 'top', '-fill', 'y')
root_window.tk.call('pack', '.toolbar.view_z', '-side', 'top', '-fill', 'y')
# root_window.tk.call('pack','.toolbar.view_z2','-side','top','-fill','y')
# root_window.tk.call('pack','.toolbar.view_x','-side','top','-fill','y')
# root_window.tk.call('pack','.toolbar.view_y','-side','top','-fill','y')
root_window.tk.call('pack', '.toolbar.view_p', '-side', 'top', '-fill', 'y')
# root_window.tk.call('pack','.toolbar.rotate','-side','top','-fill','y')
root_window.tk.call('pack', '.toolbar.clear_plot', '-side', 'top', '-fill', 'y')

########## resize bottom pane #######
root_window.tk.call('.pane', 'paneconfigure', '.pane.bottom',
                    "-stretch", "always", "-height", "200")

######### resize top pane ########
###### smaller manual frame /11 lines of gcode ########
# root_window.tk.call('.pane', 'paneconfigure', '.pane.top',
                    # "-stretch", "never", "-minsize", "250")
#### bigger manual frame /7 lines of gcode #####
root_window.tk.call('.pane','paneconfigure','.pane.top',"-stretch","never","-minsize","300");

########### window resize #########
root_window.tk.call(".pane", "configure", "-height", "350")

########### display z plane in preview  ###########
# commands.set_view_z()

########### window resize ##################
# root_window.tk.call("wm","geometry",".","700x440")
root_window.tk.call("wm", "geometry", ".", "1024x600")
root_window.attributes("-fullscreen", 1)


# change the font

font = 'mono 10'
fname, fsize = font.split()
root_window.tk.call('font', 'configure', 'TkDefaultFont',
                    '-family', fname, '-size', fsize)

# redo the text in tabs so they resize for the new default font

root_window.tk.call('.pane.top.tabs', 'itemconfigure',
                    'manual', '-text', ' Manual - F3 ')
root_window.tk.call('.pane.top.tabs', 'itemconfigure',
                    'mdi', '-text', ' MDI - F5 ')
root_window.tk.call('.pane.top.right', 'itemconfigure',
                    'preview', '-text', ' Preview ')
root_window.tk.call('.pane.top.right', 'itemconfigure',
                    'numbers', '-text', ' DRO ')


# disable the do you want to close dialog
root_window.tk.call("wm", "protocol", ".", "WM_DELETE_WINDOW", "destroy .")

# change dro screen
root_window.tk.call('.pane.top.right.fnumbers.text', 'configure',
                    '-foreground', 'limegreen', '-background', 'black')


# modal text
# root_window.tk.call('.pane.top.gcodes','configure'
# ,'-foreground','limegreen'
# ,"-font","mono 8 bold"
# ,'-background','black')


# gcode preview text
root_window.tk.call(pane_bottom+".t.text", "configure", "-foreground",
                    "Limegreen", "-font", "mono 12 bold", "-background", "black")
