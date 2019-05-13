from ds.stack import Stack

def test_constructor():
    # Create object s from Stack class:
    s = Stack()
    assert isinstance(s, Stack)
    # Call len() will call def __len__(self)
    assert len(s) == 0
