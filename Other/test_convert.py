from convert_mini import convert_bn_dc, convert_dc_bn

def test_convert_dc_bn():
    
    x = convert_dc_bn(50)
    assert x == [1, 1, 0, 0, 1, 0]
    
def test_convert_bn_dc():

    y = convert_bn_dc(110010)
    assert y == 50
