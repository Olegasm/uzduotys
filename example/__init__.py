import check50
import check50.c
import filecmp

@check50.check()
def exists():
    """hello.c egzistuoja"""
    check50.exists("U1.c")
    check50.include("1.txt", "2.txt")

@check50.check(exists)
def compiles():
    """U1.c kompiliuojasi"""
    check50.c.compile("U1.c", lcs50=True)

@check50.check(exists)
def compiles1():
    """testU1.cpp kompiliuojasi"""
    check50.c.compile("testU1.cpp", lcs50=True)

@check50.check()
def testingCPP():
    """Ar pasileidžia sukompiliuotas CPP file'as"""
    check50.run("./testU1").stdin("8").stdout(1)
#    out = check50.run("./testU1").stdin("8").stdout(1)
#    compare_values(out, open("2.txt").read())
    
@check50.check(exists)
def isOutput():
    """Rastas U1rez.txt"""
    check50.exists("U1rez.txt")
    
@check50.check(compiles)
def test1():
    """Tikrina U1rez.txt rezultato korektiškumą"""
#    out = check50.run("./U1 U1rez.txt").stdin("8").stdout()
#    compare_files(out, open("1.txt").read())
    compare_files(open("U1rez.txt").read(), open("1.txt").read())
    
def compare_files(output, correct):
    if output == correct:
        return 
    raise check50.Mismatch(correct, output, help= None)

def compare_values(output, correct):
    if output == correct:
        return 
    raise check50.Mismatch(correct, output, help= None)
