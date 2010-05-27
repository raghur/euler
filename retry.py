from time import sleep
# Getting decorators in python to work properly can even dissuade the
# best fanboys of python (case in point, is me).
# The idea:
# ==========
# Build a decorator that will allow arbitrary functions/methods to be
# retried in case of unexpected failures. The idea is not anything new
# and is used in a bunch of applications - perhaps, Gmail and Google
# Readers retry mechanism (with recursive backoff) when a network
# connection is unavailable is the most visible.
# Implementation Language
# =======================
# I picked python because I figured this must be the easiest of
# problems to solve in Python given its flexible and dynamic
# nature. And really, when it comes to coding for fun, what's better than
# python? Or so I thought.
# Decorator Semantics
# ===================
# Python decorator semantics are quite horrible. They may be
# necessarily so non-regular - but the fact that they work very very
# differently based on whether you want a decorator that can take args
# vs a no-arg decorator is enough to drive someone to the
# edge. Definitely not for the faint-hearted.
# No-arg case:
# ============
# In the no-arg decorator case, your decorator is passed in the
# function-to-be-decorated as an argument
# @decorate
# def doSomething(m,n):
#     print m,n
# class decorate(object):
#     def __init__(self, f):
#         # f passed in here
#         pass
#     def __call__(self,*args):
#         self.f(*args)
#         # *args is the argument set passed to original call.

# The decorater-with-args case:
# ============================
# now consider the protocol when you want the decorator to take args
# @decorate(something=5)
# def doSomething(m,n):
#     print m,n
# class decorate(object):
#     # init now does not get the function. Instead, it gets teh
# decorator args.
#     def __init__(self, something):
#         pass
#     def __call__(self, f):
#         # Only one arg to __call__ = the function to be decorated.
#         # This method is  expected to return a function pointer to the
# wrapped method
          # also, note that the __call__ is only used once - to get
          # the function pointer. Once that is available, that
          # function pointer is used for calls.
#         def wrapped(self,*args):
#              print args
#              f(args)
#          return wrapped
 
# The decorator problem again
# ===========================
# So what's the problem - well, what you have is that decorators must
# be coded very differently based on whether they need args or not.
# Secondly, if you want reasonable defaults for your decorator args,
# then beware - because when you use a decorator that can has args
# with default values, then the decorator convention used is based on
# whether you specify the decorator args or not! Guess what that means
# - writing a user friendly decorator is not trivial at all!
# 

class DecoratorBase(object):
    def __init__(self,klass, f=None):
        self.f = f
        self.klass = klass

    def __call__(self, *args):            
        if args and callable(args[0]):
            print "reassigning f"
            self.f = args[0]
            print "returning object"
            wrapper_obj =  self.wrap(*args[1:])
            return wrapper_obj
        else:
            print "calling"
            wrapper_obj =  self.wrap(*args)
            return wrapper_obj(*args)    
        
    def wrap(self, *args):
        print "Args:", args
        inst = self.klass.Wrapper(self,*args)
        return inst

class Retry(DecoratorBase):
    class Wrapper(object):
        def __init__(self, parent, *args):
            self.args = args
            self.parent = parent
        def __call__(self, *args):
            i = 0
            b = 1
            print "Trying function %s" % self.parent.f.__name__
            
            while i <= self.parent.times:
                print "Attempt:  %d" % i
                try:
                    return self.parent.f(*args)
                except Exception as inst:
                    print "Got an exception. checking if we can retry"
                    if i < self.parent.times:
                        i += 1
                        if self.parent.useBackoff:
                            b = 2*b
                            print "sleeping for %d s" % b
                            sleep(0)
                    else:
                        print "Failed after %d retries" % i
                        print "rethrowing exception"
                        self.parent.attempt = i
                        raise
                else:
                    print "Successful in the %d attempt" % i
                    self.parent.attempt = i
                    break

        def __getattr__(self, name):
            return self.parent.__getattribute__(name)
        
    def __init__(self, f=None,times=3, useBackoff=True):
        super(Retry, self).__init__( Retry, f)
        self.times = times
        self.useBackoff = useBackoff
        self.attempt = 0



import unittest

class RetryDecoratorTests(unittest.TestCase):
    def testWithoutMethodArgs(self):
        @Retry
        def decorated(arg="urghh!!"):
            print "in decorated"
            return "%s did something that didnt throw" % arg
        self.assert_(decorated() == "urghh!! did something that didnt throw", "unexpected output")
        self.assert_(decorated.attempt == 0, "Should have succeeded in the first attempt")

    def testMethodWithoutReturnValue(self):
        @Retry
        def decorated():
            print "in decorated"
        
        self.assert_(decorated() is None, "Expected None return")
        self.assert_(decorated.attempt == 0, "Should have succeeded first time")
    
    def testMethodThatFails(self):
        @Retry
        def decorated(arg="Eggs"):
            raise Exception(arg)
        try:
            decorated()
        except Exception as inst:
            self.assert_(decorated.attempt == 3, "count should be 3. is %d" % decorated.attempt)
            print inst
            self.assert_(inst.args[0] == "Eggs", "Exception not propogated properly")
        else:
            self.fail("Should never get here")

    def testDecoratorWithArgsSimple(self):
        @Retry(times=2)
        def decorated(arg="urghh!!"):
            print "in decorated 2"
            return "%s did something that didnt throw" % arg
        output = decorated()
        self.assert_(output == "urghh!! did something that didnt throw", "unexpected output: %s" % output)
        self.assert_(decorated.attempt == 0, \
                     "Should have succeeded in the first attempt")
        output = decorated("hmmm!")
        self.assert_(output == "hmmm! did something that didnt throw", "unexpected output: %s" % output)
        self.assert_(decorated.attempt == 0, "Should have succeeded in the first attempt")
        

@Retry(times=2)
def doSomethingSilly(arg="eggs"):
    raise  Exception (arg)



# print "Calling doSomethingStraightForward"
# doSomethingStraightForward()

# print "################################"
# print "Calling doSomethingStraightForward #2"
# doSomethingStraightForward("phew!!")

# print "################################"
# print "Calling doSomethingSilly"
# try:
#     doSomethingSilly()
# except Exception:
#     pass

# print "################################"
# print "Calling doSomethingSilly"
# doSomethingSilly("whew!!!")

def runTests():
    """
    """
    suite = unittest.TestLoader().loadTestsFromTestCase(RetryDecoratorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__== "__main__":
    runTests()


