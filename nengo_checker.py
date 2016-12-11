import nengo
from numpydoc.docscrape import NumpyDocString, ClassDoc

import inspect
import ipdb

doc = ClassDoc(nengo.Ensemble)
print(len(doc["Parameters"]))
argspec = inspect.getargspec(nengo.Ensemble.__init__)

# check for basic spelling errors
# TODO: skip 'self' for classes, but not for functions
for a_i, arg in enumerate(argspec.args[1:]):
    if arg != doc["Parameters"][a_i][0]:
        print("%s != %s" %(arg, doc["Parameters"][a_i][0]))

# for all parameters
# check that defaults are assigned correctly
# TODO: is it posssible for a non-optional argument to have a default
# yes, but I can't remember the difference
for a_i, arg in enumerate(argspec.args[1:]):
    att = getattr(nengo.Ensemble, arg)
    if issubclass(att, nengo.params.Parameter):
        if att.default is not None and :



