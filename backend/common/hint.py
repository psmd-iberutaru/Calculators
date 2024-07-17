"""Type hint functionality.

These are redefinitions and wrapping variables for type hints. Its purpose
is for just uniform hinting types.

This should only be used for types which are otherwise not native and would
require an import, including the typing module. The whole point of this is to
be a central collection of types for the purpose of type hinting.

This module should never be used for anything other than hinting. Use proper
imports to access these classes. Otherwise, you will likely get circular
imports and other nasty things.
"""

from collections import *
from collections.abc import *
from logging import *
from subprocess import CompletedProcess
from typing import *


# Arrays. We use ndarray instead as ArrayLike casts a rather larger union
# in the documentation.
from numpy import NDArray
