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


def valida_salary_type(num: Union[int, str]) -> bool:
    if num is None:
        return False
    if type(num) is not str and type(num) is not int:
        return False
    if type(num) is str and not num.isdigit():
        return False
    return True


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if type(job) is not dict:
        raise ValueError("Erro de parametro")
    if len(list(job.keys())) != 2:
        raise ValueError("Erro de parametro")
    if (
        not valida_salary_type(salary)
        or not valida_salary_type(job["min_salary"])
        or not valida_salary_type(job["max_salary"])
    ):
        raise ValueError("Erro de parametro")
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("Erro de parametro")
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    filter_job = []
    for job in jobs:
        min = job["min_salary"]
        max = job["max_salary"]
        if (valida_salary_type(min) and valida_salary_type(max)) and int(
            max
        ) > int(min):
            if matches_salary_range(job, salary):
                filter_job.append(job)
    return filter_job
