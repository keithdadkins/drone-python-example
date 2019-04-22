from foo import foo
def test_foo():
    '''foo should bar'''
    assert "bar" == str(foo.bar()), "foo != bar" 

