from typing import List

from algorithms.singlePipe import get_pipeline
from constants import ACCOUNTANT, DIRECTOR_GENERAL
from db import is_role_by_name


def get_digest(role: str) -> List[str]:
    pipe = get_pipeline()
    if is_role_by_name(ACCOUNTANT, role):
        return pipe.get_digest(ACCOUNTANT)
    elif is_role_by_name(DIRECTOR_GENERAL, role):
        return pipe.get_digest(DIRECTOR_GENERAL)


def get_trends() -> List[str]:
    pipe = get_pipeline()
    return pipe.get_trends()


def get_insights() -> List[str]:
    pipe = get_pipeline()
    return pipe.get_insights()
