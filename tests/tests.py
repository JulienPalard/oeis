from oeis import oeis

def test_base():
    assert(True)

def test_base_function(begin,end):
    
    fix_names(tmpdir)
    assert(tmpdir / "hello_world.txt").exists()
    assert(tmpdir / "hello world.txt").exists()