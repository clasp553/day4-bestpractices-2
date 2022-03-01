import simple_math
import pytest

@pytest.mark.parametrize("n1, n2, add, sub, mult, div", [
	(2,1,2,1,2,2)
])

def test_simple_math(n1,n2,add,sub,mult,div):
	assert simple_math.simple_add(n1,n2) == add
	assert simple_math.simple_sub(n1,n2) == sub
	assert simple_math.simple_mult(n1,n2) == mult
	assert simple_math.simple_div(n1,n2) == div

