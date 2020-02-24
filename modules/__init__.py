from .help import Help
from .admin import Admin
from .backups import Backups
from .templates import Templates
from .basics import Basics


to_load = (Help, Admin, Backups, Basics, Templates)
