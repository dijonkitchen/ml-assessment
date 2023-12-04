from apis.fakerpc import rpc1, rpc2


def test_rpc1():
    subject = rpc1("test")

    assert any(hit.label == "foo" for hit in subject.hits)
    assert any(hit.label == "bar" for hit in subject.hits)


def test_rpc2():
    subject = rpc2("test")

    assert any(hit.label == "foo" for hit in subject.hits)
    assert any(hit.label == "bar" for hit in subject.hits)
    assert any(hit.label == "baz" for hit in subject.hits)
