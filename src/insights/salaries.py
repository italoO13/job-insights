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


def validate_salary_min_and_max(job: Dict):
    for obj in job:
        min = obj["min_salary"]
        max = obj["max_salary"]
        if max is None or min is None:
            raise ValueError("Erro de parametro")
        if not max.isdigit() or not min.isdigit():
            raise ValueError("Erro de parametro")
        if min > max:
            raise ValueError("Erro de parametro")


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if not salary.isdigit():
        raise ValueError("Erro de parametro")
    validate_salary_min_and_max(job)
    salary_min = get_min_salary("data/jobs.csv")
    salary_max = get_max_salary("data/jobs.csv")

    return salary_min < int(salary) < salary_max


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
