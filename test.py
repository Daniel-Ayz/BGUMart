def find(**keyvals):
    column_names = keyvals.keys()
    params = keyvals.values()
    print(type(keyvals), type(column_names), type(params))
    # params = list(keyvals.values())

    stmt = 'SELECT * FROM {} WHERE {}' \
        .format("self._table_name", ' AND '.join([str(key) + '=' + str(val) for key, val in keyvals.items()]))
    print(stmt)

find(id=3*5)
