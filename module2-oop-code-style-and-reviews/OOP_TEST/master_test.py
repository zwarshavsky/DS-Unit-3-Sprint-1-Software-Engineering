from master import Speaker


def test_discount():
    object1 = Speaker()
    assert object1.apply_discount2() == 400


# sub = Speaker()
# print(sub.apply_discount2())
