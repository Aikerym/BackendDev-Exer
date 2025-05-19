from dataclasses import dataclass
import datetime

@dataclass
class Contact:
    LAST_UPDATE: str
    CLIENT_TYPE: int
    CLIENT_BIIN: str
    TYPE_ID: int
    INFO: str
    IS_MAIN: bool
    IS_ARCHIVED: bool
    UUID: str = None
    DESCRIPTION: str = None
    CREATED_DATE: str = None
    SOURCE: str = 'ASBUKA'

    def upsert_topic(self):
        return 'CDP.CONTACT.DEDUPSERT'


@dataclass
class LocalizedString:
    RU: str = None
    KZ: str = None
    EN: str = None

@dataclass
class Person:
    IIN: str
    LAST_UPDATE: str
    BIRTH_DATE: str
    IS_RESIDENT: bool
    FIRSTNAME: LocalizedString
    LASTNAME: LocalizedString
    MIDDLENAME: LocalizedString
    BRANCH_ID: int
    CITIZENSHIP_ID: int
    GENDER_ID: int
    TAX_RESIDENCE_ID: int
    SOURCE: str = 'ASBUKA'

    def upsert_topic(self):
        return 'CDP.PERSON.UPSERT'


def now():
    return datetime.datetime.now().isoformat() + 'Z'