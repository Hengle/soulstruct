"""
linked:
0
82

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: 
168: 
170: 
172: 
174: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(0, 90005300, args=(1051550300, 1051550300, 0, 0.0, 0), arg_types="IIifi")


@NeverRestart(250)
def Event_250():
    """Event 250"""
    RunCommonEvent(0, 90005485, args=(1051550300,))