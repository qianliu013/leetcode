# coding=utf-8

"""Employee Importance.

>>> solve = _solve
>>> solve()

"""


def _solve(employees, id):
    res = {employee.id: employee for employee in employees}

    def _dfs(id):
        return sum([_dfs(sub_id) for sub_id in res[id].subordinates]) + res[id].importance

    return _dfs(id)
