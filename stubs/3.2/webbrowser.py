# Stubs for webbrowser (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Undefined, Any

class Error(Exception): pass

def register(name, klass, instance=None, update_tryorder=1): pass
def get(using=None): pass
def open(url, new=0, autoraise=True): pass
def open_new(url): pass
def open_new_tab(url): pass

class BaseBrowser:
    args = Undefined(Any)
    name = Undefined(Any)
    basename = Undefined(Any)
    def __init__(self, name=''): pass
    def open(self, url, new=0, autoraise=True): pass
    def open_new(self, url): pass
    def open_new_tab(self, url): pass

class GenericBrowser(BaseBrowser):
    name = Undefined(Any)
    args = Undefined(Any)
    basename = Undefined(Any)
    def __init__(self, name): pass
    def open(self, url, new=0, autoraise=True): pass

class BackgroundBrowser(GenericBrowser):
    def open(self, url, new=0, autoraise=True): pass

class UnixBrowser(BaseBrowser):
    raise_opts = Undefined(Any)
    background = Undefined(Any)
    redirect_stdout = Undefined(Any)
    remote_args = Undefined(Any)
    remote_action = Undefined(Any)
    remote_action_newwin = Undefined(Any)
    remote_action_newtab = Undefined(Any)
    def open(self, url, new=0, autoraise=True): pass

class Mozilla(UnixBrowser):
    raise_opts = Undefined(Any)
    remote_args = Undefined(Any)
    remote_action = Undefined(Any)
    remote_action_newwin = Undefined(Any)
    remote_action_newtab = Undefined(Any)
    background = Undefined(Any)

class Galeon(UnixBrowser):
    raise_opts = Undefined(Any)
    remote_args = Undefined(Any)
    remote_action = Undefined(Any)
    remote_action_newwin = Undefined(Any)
    background = Undefined(Any)

class Chrome(UnixBrowser):
    remote_args = Undefined(Any)
    remote_action = Undefined(Any)
    remote_action_newwin = Undefined(Any)
    remote_action_newtab = Undefined(Any)
    background = Undefined(Any)

class Opera(UnixBrowser):
    raise_opts = Undefined(Any)
    remote_args = Undefined(Any)
    remote_action = Undefined(Any)
    remote_action_newwin = Undefined(Any)
    remote_action_newtab = Undefined(Any)
    background = Undefined(Any)

class Elinks(UnixBrowser):
    remote_args = Undefined(Any)
    remote_action = Undefined(Any)
    remote_action_newwin = Undefined(Any)
    remote_action_newtab = Undefined(Any)
    background = Undefined(Any)
    redirect_stdout = Undefined(Any)

class Konqueror(BaseBrowser):
    def open(self, url, new=0, autoraise=True): pass

class Grail(BaseBrowser):
    def open(self, url, new=0, autoraise=True): pass

class WindowsDefault(BaseBrowser):
    def open(self, url, new=0, autoraise=True): pass

class MacOSX(BaseBrowser):
    name = Undefined(Any)
    def __init__(self, name): pass
    def open(self, url, new=0, autoraise=True): pass

class MacOSXOSAScript(BaseBrowser):
    def __init__(self, name): pass
    def open(self, url, new=0, autoraise=True): pass