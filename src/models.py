from typing import List

from constants import ACCOUNTANT, DIRECTOR_GENERAL
from db import is_role_by_name


def get_digest(role: str) -> List[str]:
    if is_role_by_name(ACCOUNTANT, role):
        return ["news1", "news2"]
    elif is_role_by_name(DIRECTOR_GENERAL, role):
        return ["news3", "news4"]


def get_trends() -> List[str]:
    return ["trend1", "trend2"]


def get_insights() -> List[str]:
    return ["insight1", "insight2"]
