import inspect

from numpydoc.docscrape import FunctionDoc

def myfunc(apples, bears):
    """
        Parameters
        ----------
        apples : int
            The number of apples.
        beards : int
            The number of bears to eat the apples.
    """

doc = FunctionDoc(myfunc)
argspec = inspect.getargspec(myfunc)

# check for basic spelling errors
for a_i, arg in enumerate(argspec.args):
    if arg != doc["Parameters"][a_i][0]:
        print("%s != %s" %(arg, doc["Parameters"][a_i][0]))
