from time import sleep

class DecoratorBase(object):
    def __init__(self, f=None):
        self.f = f

    def __call__(self, *args):
        def wrapped(*args):
            self.wrap(*args)
            
        if args and callable(args[0]):
            print "reassigning f"
            self.f = args[0]
            return wrapped
        else:
            wrapped(*args)    

    def wrap(self, *args):
        raise Exception("must be overridden")

class Retry(DecoratorBase):
    def __init__(self, f=None,times=3, useBackoff=True):
        super(Retry, self).__init__(f)
        self.times = times
        self.useBackoff = useBackoff

    def wrap(self, *args):
        i = 0
        b = 1
        print "Trying function %s" % self.f.__name__
        
        while i <= self.times:
            print "Attempt:  %d" % i
            try:
                self.f(*args)
            except Exception as inst:
                print "Got an exception. checking if we can retry"
                if i < self.times:
                    i += 1
                    if self.useBackoff:
                        b = 2*b
                        print "sleeping for %d s" % b
                        sleep(b)
                else:
                    print "Failed after %d retries" % i
                    print "rethrowing exception"
                    raise
            else:
                print "Successful in the %d attempt" % i
                break


@Retry(times=2)
def doSomethingSilly(arg="eggs"):
    raise  Exception (arg)


@Retry
def doSomethingStraightForward(arg="urghh!!"):
    print "%s did something that didnt throw" % arg

print "Calling doSomethingStraightForward"
doSomethingStraightForward()

print "################################"
print "Calling doSomethingStraightForward #2"
doSomethingStraightForward("phew!!")

print "################################"
print "Calling doSomethingSilly"
try:
    doSomethingSilly()
except Exception:
    pass

print "################################"
print "Calling doSomethingSilly"
doSomethingSilly("whew!!!")



