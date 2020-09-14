inp = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"


def hex_to_base10(inp_str):
    tot = 0
    exp = 1
    hex_chars = "0123456789abcdef"
    for c in inp_str[::-1]:
        tot += hex_chars.index(c) * exp
        exp *= 16

    return tot


def base10_to_base64(inp_int):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    assert len(base64_chars) == 64
    base64_out = []

    while inp_int:
        try:
            base64_out.append(base64_chars[inp_int % 64])
        except:
            print(inp_int % 64)
        inp_int //= 64

    return "".join(base64_out[::-1])


assert (
    "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    == base10_to_base64(hex_to_base10(inp))
)
