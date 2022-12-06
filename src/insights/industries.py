from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    industries = set()
    jobs = read(path)
    for job in jobs:
        if job["industry"] != "":
            industries.add(job["industry"])
    return list(industries)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filter_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            filter_jobs.append(job)
    return filter_jobs
