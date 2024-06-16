"""Backend implementation of a lot of the calculators.

The modules listed are the backend implementations of the calculators of this
project. Each backend is limited to a single module file, corresponding to the 
calculator it represents. The calculators are supposed to be "simple" enough
so they they do not need entire dedicated libraries to function. Functions 
which many backends use can be found in the common module.
"""

# isort

# Common functions which all backends will likely be using.
# Best to import this first just in case.
from backend import common

# isort
