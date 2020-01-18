
import trickt


URL_ENCODING_MAP = {
    "!": "%21",
    ' ': '%20',  # Out of order to prevent it getting stripped.
    "\"": "%22",
    "#": "%23",
    "$": "%24",
    "%": "%25",
    "&": "%26",
    "\'": "%27",
    "(": "%28",
    ")": "%29",
    "*": "%2A",
    "+": "%2B",
    ",": "%2C",
    "-": "%2D",
    ".": "%2E",
}


def test_url_encoded():
    url_encoded = ''.join([value for value in URL_ENCODING_MAP.values()]).encode('utf-8')
    url_decoded = ''.join([key for key in URL_ENCODING_MAP]).encode('utf-8')
    trickt_result = trickt.url_encoded(url_encoded)
    assert url_decoded == trickt_result[0]
    assert 1 == len(trickt_result)

def test_url_encoded_string_not_encoded():
    result = trickt.url_encoded(b'this has no percent signs')
    assert [] == result

def test_code_point():
    code_point_string = b"readpipe(chr(104)+.+chr(101)+.+chr(108)+.+chr(108)+.+chr(111))"
    decoded = b"hello"
    trickt_result = trickt.code_point(code_point_string)
    assert decoded == trickt_result[0]
    assert 1 == len(trickt_result)

def test_no_code_points():
    no_code_points = b"no code points here"
    assert [] == trickt.code_point(no_code_points)

def test_escaped_unicode():
    escaped_unicode = br"\u0068\u0065\u006c\u006c\u006f"
    result = b"hello"
    trickt_result = trickt.escaped_characters(escaped_unicode)
    assert result == trickt_result[0]
    assert 1 == len(trickt_result)

def test_escaped_hex():
    escaped_hex = br"\x68\x65\x6C\x6C\x6F"
    result = b"hello"
    trickt_result = trickt.escaped_characters(escaped_hex)
    assert result == trickt_result[0]
    assert 1 == len(trickt_result)

def test_no_escaped_chars():
    nothing_escaped = b"There are no escaped strings here"
    assert [] == trickt.escaped_characters(nothing_escaped)

def test_base64_match_custom_minimum_length():
    min_length = 6
    b64_string = b"aGV5Cg=="
    expected = b"hey"
    trickt_result = trickt.base64_decode(b64_string, minimum_length=min_length)
    assert expected == trickt_result[0]
    assert 1 == len(trickt_result)

def test_base64_without_custom_minimum_length_too_short():
    too_short = b"aGV5Cg=="
    trickt_result = trickt.base64_decode(too_short)
    assert [] == trickt_result

def test_base64_without_custom_min_length_should_catch_it():
    b64_string = b"dGhpcyBzaG91bGQgYmUgbG9uZ2VyIHRoYW4gMzIgY2hhcnMK"
    expected = b"this should be longer than 32 chars"
    trickt_result = trickt.base64_decode(b64_string)
    assert expected == trickt_result[0]
    assert 1 == len(trickt_result)

def test_base64_incorrect_padding():
    b64_string = b'dGhpcyBzaG91bGQgYmUgbG9uZ2VyIHRoYW4gMzIgY2hhcnM'
    trickt_result = trickt.base64_decode(b64_string)
    assert [] == trickt_result

