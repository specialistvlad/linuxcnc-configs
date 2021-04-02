########### probe tool axis custom script ########################
def my_error_task(self):
        error = e.poll()
        while error: 
            kind, text = error
            if kind in (linuxcnc.NML_ERROR, linuxcnc.OPERATOR_ERROR):
                icon = "error"
            else:
                icon = "info"
            notifications.add(icon, text)
            ucomp["error"]=True
            error = e.poll()
        self.error_after = self.win.after(200, self.error_task)

def my_remove(self, widgets):
    self.widgets.remove(widgets)
    if len(self.cache) < 10:
        widgets[0].pack_forget()
        self.cache.append(widgets)
    else:
        widgets[0].destroy()
    if len(self.widgets) == 0:
        ucomp["error"]=False
        self.place_forget()

LivePlotter.error_task = my_error_task
Notification.remove = my_remove

if hal_present == 1 :
    ucomp = hal.component("probe.user")
    ucomp.newpin("error",hal.HAL_BIT,hal.HAL_IN)
    ucomp.ready()
########### probe tool axis custom script ########################