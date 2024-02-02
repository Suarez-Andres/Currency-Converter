import proyect as p

def test_check_format_date():
    assert p.check_format("2020-01-01","date")=="2020-01-01"
    assert p.check_format("January 1, 2020","date")=="Date format: YYYY-MM-DD"
    assert p.check_format("2020-20-51","date")=="Invalid date"
    assert p.check_format("2020-6-50","date")=="Date format: YYYY-MM-DD"


def test_check_format_currency():
    assert p.check_format("US dollars","currency")=="Format: 3 uppercase letters"
    assert p.check_format("USD","currency")=="USD"
    assert p.check_format("JPY","currency")=="JPY"
    assert p.check_format("ABC","currency")=="Invalid currency"


def test_euro_to_dollar():
    assert p.euro_to_dollar(1,"2020-01-01")==1.12
    assert p.euro_to_dollar(20,"2020-01-01")==22.44
    assert p.euro_to_dollar(5280,"2020-01-01")==5923.26


def test_euro_to_other_currency():
    assert p.euro_to_other_currency(15,"JPY","2020-01-01")==1829.45
    assert p.euro_to_other_currency(2800,"CAD","2020-01-01")==4075.76
    assert p.euro_to_other_currency(2,"GBP","2020-01-01")==1.69