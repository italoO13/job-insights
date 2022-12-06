from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    jobs = []
    try:
        with open(path, encoding="utf-8") as file:
            jobs_reader = csv.reader(file, delimiter=",", quotechar='"')
            headers, *data = jobs_reader
    except FileNotFoundError:
        print("Arquivo não encontrado")
    else:
        for row in data:
            dict_jobs = {}
            for index, header in enumerate(headers):
                dict_jobs[header] = row[index]
            jobs.append(dict_jobs)
        return jobs


def get_unique_job_types(path: str) -> List[str]:
    jobs_type = set()
    jobs = read(path)
    for job in jobs:
        jobs_type.add(job["job_type"])
    return list(jobs_type)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
