#Developed by Niranjan Kumar G S
from pywinauto import application
from pywinauto.findwindows import WindowAmbiguousError, WindowNotFoundError


def show_select_app():
    # Init App object
    app = application.Application()

    select_app = 'python.exe'
    try:
        print 'Select "%s"' % select_app
        app.connect(title_re=".*%s.*" % select_app)

        # Access app's window object
        app_dialog = app.top_window_()

        app_dialog.Minimize()
        app_dialog.Restore()
        app_dialog.SetFocus()
    except(WindowNotFoundError):
        print '"%s" not found' % select_app
        pass
    except(WindowAmbiguousError):
        print 'There are too many "%s" windows found' % select_app
        pass

show_select_app()
