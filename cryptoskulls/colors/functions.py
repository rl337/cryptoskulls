
def split_rgba(value):
    assert value.startswith("#"), "value must start with a #"
    l = len(value)
    assert l == 7 or l == 9, "Value must be either #RRGGBB or #RRGGBBAA"

    if l == 7:
        r = int(value[1:3], 16)
        g = int(value[3:5], 16)
        b = int(value[5:7], 16)
        return r, g, b, 0xFF

    r = int(value[1:3], 16)
    g = int(value[3:5], 16)
    b = int(value[5:7], 16)
    a = int(value[7:9], 16)
    return r, g, b, a


