from kafka_client import KafkaClient
import datetime
from dataclasses import asdict
from models import (
    Contact,
    Person,
    LocalizedString
)
import os

def now():
    return datetime.datetime.now().isoformat() + 'Z'

def main():
    host = os.getenv('HOST')
    kafka_client = KafkaClient(host=host)

    person = Person(
        IIN='980404404404',
        LAST_UPDATE=now(),
        BIRTH_DATE=now(),
        IS_RESIDENT=True,
        FIRSTNAME=LocalizedString(RU='Астана'),
        LASTNAME=LocalizedString(RU='Астанаева'),
        MIDDLENAME=LocalizedString(RU='Астанаулы'),
        BRANCH_ID=1,
        CITIZENSHIP_ID=86,
        GENDER_ID=1,
        TAX_RESIDENCE_ID=86
    )

    contact = Contact(
        LAST_UPDATE=now(),
        CLIENT_TYPE=1,
        CLIENT_BIIN=person.IIN,
        TYPE_ID=3,
        INFO='87074444444',
        IS_MAIN=True,
        IS_ARCHIVED=False
    )

    kafka_client.send(person.upsert_topic(), asdict(person))
    kafka_client.send(contact.upsert_topic(), asdict(contact))


if __name__ == '__main__':
    main()
