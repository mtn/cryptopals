from ch1 import hex_to_base10


inp1 = "1c0111001f010100061a024b53535009181c"
inp2 = "686974207468652062756c6c277320657965"
expected = "746865206b696420646f6e277420706c6179"


def base10_to_hex(inp_int):
    hex_chars = "0123456789abcdef"
    assert len(hex_chars) == 16
    hex_out = []

    while inp_int:
        try:
            hex_out.append(hex_chars[inp_int % 16])
        except:
            print(inp_int % 16)
        inp_int //= 16

    return "".join(hex_out[::-1])


def xor_hex(inp1, inp2):
    inp1_b10 = hex_to_base10(inp1)
    inp2_b10 = hex_to_base10(inp2)

    xord = inp1_b10 ^ inp2_b10

    return base10_to_hex(xord)


assert expected == xor_hex(inp1, inp2)
