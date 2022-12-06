from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    industries = set()
    jobs = read(path)
    for job in jobs:
        if job["industry"] != "":
            industries.add(job["industry"])
    return list(industries)


print(get_unique_industries("data/jobs.csv"))


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
