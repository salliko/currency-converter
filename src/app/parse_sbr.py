#!/usr/bin/env python3

import requests
import xmltodict

from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert

from db import engine, currencies


URL = 'https://www.cbr.ru/scripts/XML_daily.asp'


def to_float(number: str) -> float:
    return float('.'.join(number.split(",")))


if __name__ == '__main__':
    response = requests.get(URL)
    data = xmltodict.parse(response.content)

    Session = sessionmaker(engine, future=True)

    with Session() as session:
        for valute in data['ValCurs']['Valute']:
            stmt = insert(currencies).values(
                char_code=valute['CharCode'],
                num_code=valute['NumCode'],
                nominal=valute['Nominal'],
                name=valute['Name'],
                value=to_float(valute['Value'])
            )
            session.execute(stmt)
        session.commit()
