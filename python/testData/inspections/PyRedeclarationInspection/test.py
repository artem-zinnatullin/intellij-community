def test_class():
    class X:
        pass

    class <warning descr="Redeclared name defined above without usage">X</warning>:
        pass

def test_function():
    def foo():
        pass

    def <warning descr="Redeclared name defined above without usage">foo</warning>():
        pass


# Top-level variable test
def TopLevelBoo():
    pass


<warning descr="Redeclared name defined above without usage">TopLevelBoo</warning> = 1
<warning descr="Redeclared name defined above without usage">TopLevelBoo</warning> = 2


class <warning descr="Redeclared name defined above without usage">TopLevelBoo</warning>:
    pass


def test_decorated_function(decorator):
    def foo():
        pass

    @decorator
    def foo():
        pass

    def <warning descr="Redeclared name defined above without usage">foo</warning>():
        pass


def test_local_variable():
    x = 1
    x = 2


def conditional(c):
    def foo():
        pass

    if c:
        def foo():
            pass

    while c:
        def foo():
            pass

    try:
        def foo():
            pass
    except:
        pass
