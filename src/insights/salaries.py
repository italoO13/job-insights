from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    salaries = []
    for job in jobs:
        if job["max_salary"] != "" and job["max_salary"].isdigit():
            salaries.append(int(job["max_salary"]))
    return max(salaries)


def get_min_salary(path: str) -> int:
    jobs = read(path)
    salaries = []
    for job in jobs:
        if job["min_salary"] != "" and job["min_salary"].isdigit():
            salaries.append(int(job["min_salary"]))
    return min(salaries)


def valida_salary_type(num: Union[int, str]) -> int:
    if num is None:
        raise ValueError("Erro de parametro")
    if type(num) is not str and type(num) is not int:
        raise ValueError("Erro de parametro")
    if type(num) is str and not num.isdigit():
        raise ValueError("Erro de parametro")
    return int(num)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if type(job) is not dict:
        raise ValueError("Erro de parametro")
    if len(list(job.keys())) != 2:
        raise ValueError("Erro de parametro")
    sal = valida_salary_type(salary)
    min = valida_salary_type(job["min_salary"])
    max = valida_salary_type(job["max_salary"])
    if min > max:
        raise ValueError("Erro de parametro")
    return min <= sal <= max


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
