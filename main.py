from password_manager import *
from converter import *

frontend = FrontendPass()
frontend.root.mainloop()
KEY = frontend.KEY
KEY = bytes(KEY, 'utf-8')
app = App(KEY)
app.root.mainloop()