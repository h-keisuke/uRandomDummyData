import re
from typing import Optional, Tuple

from faker import Faker
import pykakasi


def generate():
    fake = Faker("ja_JP")
    kakashi = pykakasi.kakasi()

    name_kanji = fake.name()

    converted = kakashi.convert(name_kanji)
    name_katakana = ''.join(map(lambda x: x['kana'], converted))

    postalCode = fake.zipcode()

    address = fake.address()

    split_address = parse_address(address)

    address1 = split_address[0] if split_address[0] is not None else ''
    address2 = split_address[1] if split_address[1] is not None else ''
    address3 = split_address[2] if split_address[2] is not None else ''
    address4 = split_address[3] if split_address[3] is not None else ''

    phone = fake.phone_number()

    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=100).strftime('%Y-%m-%d')

    return [
        name_kanji,
        name_katakana,
        postalCode,
        address1,
        address2,
        address3,
        address4,
        phone,
        birth_date
    ]


def parse_address(address: str) -> Tuple[Optional[str], Optional[str], Optional[str], Optional[str]]:
    match = re.match(r'([^都道府県]+[都道府県])([^市区町村]+[市区町村])(.*)', address)
    if match:
        [address1, address2, address3] = match.groups()
        splited = address3.split(' ')
        if len(splited) > 1:
            address3_1 = splited[0]
            address3_2 = splited[1]
        else:
            address3_1 = splited[0]
            address3_2 = None

        return address1, address2, address3_1, address3_2
    else:
        return None, None, None, None
