import dsalgos.dstructs


def test_Data():
    empty_data = dsalgos.dstructs.Data()
    
    assert (
        empty_data.args == (),
        "'Data()' must have an empty 'args'"
    )
    
    assert (
        empty_data.kwargs == {},
        "'Data()' must have an empty 'kwargs'"
    )
    
    assert (
        empty_data.data == {},
        "'Data()' must have an empty 'data'"
    )
    
    
    args_data = dsalgos.dstructs.Data(*range(10))
    
    assert (
        args_data.args == tuple(range(10)),
        "Data(0, ..., 9) must have `(0, ..., 9)` as 'args'"
    )
    
    assert (
        args_data.kwargs == {},
        "'Data(0, ..., 9)' must have an empty 'kwargs'"
    )
    
    assert (
        args_data.data == {i: i for i in range(10)},
        "'Data(0, ..., 9)' must have `{0: 0, ..., 9: 9}` as 'data'"
    )
    
    
    kwargs_data = dsalgos.dstructs.Data(**{str(i): i for i in range(10)})
    
    assert (
        kwargs_data.args == (),
        "'Data(0=0, ..., 9=9)' must have empty 'args'"
    )
    
    assert (
        kwargs_data.kwargs == {str(i): i for i in range(10)},
        "'Data(0=0, ..., 9=9)' must have `{'0': 0, ..., '9': 9}` as 'kwargs'"
    )
    
    assert (
        kwargs_data.data == {str(i): i for i in range(10)},
        "'Data(0=0, ..., 9=9)' must have `{'0': 0, ..., '9': 9}` as 'kwargs'"
    )
    
    
    all_data = dsalgos.dstructs.Data(
        *range(5), **{
            str(i): i for i in range(5, 10)
        }
    )
    
    assert (
        all_data.args == tuple(range(5)),
        "'Data(0, ..., 4, 5=5, ..., 9=9)' must have `(0, ..., 4)` as 'args'"
    )
    
    assert (
        all_data.kwargs == {str(i): i for i in range(5, 10)},
        "'Data(0, ..., 4, 5=5, ..., 9=9)' must have `{'5': 5, ..., '9': 9}` as 'kwargs'"
    )
    
    assert (
        all_data.data == {
            **{i: i for i in range(5)},
            **{str(i): i for i in range(5, 10)}
        },
        "'Data(0, ..., 4, 5=5, ..., 9=9)' must have `{0: 0, ..., 4: 4, '5': 5, ..., '9': 9}` as 'data'"
    )
