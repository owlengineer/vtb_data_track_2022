from typing import List, Dict

from constants import DIRECTOR_GENERAL, ACCOUNTANT, NAME_OF_ROLE

# It the easiest implementation of db :)
DB: Dict[str, Dict[str, List[str]]] = {
    ACCOUNTANT: {
        NAME_OF_ROLE: ["бухгалтер", "бух", "accountant"]
    },
    DIRECTOR_GENERAL: {
        NAME_OF_ROLE: ["генеральный директор", "гендир", "director"]
    }
}


def get_available_roles() -> List[str]:
    roles = []
    for role in DB:
        for variant_of_role in DB[role][NAME_OF_ROLE]:
            roles.append(variant_of_role)
    return roles


def is_role_by_name(correct_role: str, role: str):
    return role.lower() in DB[correct_role][NAME_OF_ROLE]


def is_correct_role(role: str) -> bool:
    for real_role in DB:
        if role.lower() in DB[real_role][NAME_OF_ROLE]:
            return True
    return False
