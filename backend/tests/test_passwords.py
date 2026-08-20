from security.passwords import hash_password, verify_password


def test_verify_password_accepts_original_password():
    test_password = "123ABC"
    hashed_password = hash_password(test_password)
    assert verify_password(test_password, hashed_password)


def test_verify_password_rejects_wrong_password():
    test_password = "123ABC"
    hashed_password = hash_password(test_password)
    assert not verify_password("321CBA", hashed_password)


def test_hash_password_uses_fresh_salt():
    test_password = "123ABC"
    hashed_password_1 = hash_password(test_password)
    hashed_password_2 = hash_password(test_password)
    assert hashed_password_1 != hashed_password_2
