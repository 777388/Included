import include
try:
    include(include)
except:
    import include

import importlib
import _imp
importlib.util.find_spec(str(include.__path__.__subclasshook__(_imp.acquire_lock)))