import check50
import check50

@check50.check()
def exists():
    """hello.c exists"""
    check50.exists("U1.c")
    
@check50.check(exists)
def compiles():
    """U1.c compiles."""
    check50.c.compile("U1o.c", lcs50=True)