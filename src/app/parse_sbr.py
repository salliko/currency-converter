from db import currencies, engine

import requests

from sqlalchemy import insert
from sqlalchemy.orm import sessionmaker

import xmltodict


URL = 'https://www.cbr.ru/scripts/XML_daily.asp'


def to_float(number: str) -> float:
    """Функция конвертирует строку в число.
    :arg number
    """
    return float('.'.join(number.split(',')))


if __name__ == '__main__':
    response = requests.get(URL)
    xml_dict = xmltodict.parse(response.content)

    Session = sessionmaker(engine, future=True)

    with Session() as session:
        for valute in xml_dict['ValCurs']['Valute']:
            stmt = insert(currencies).values(
                char_code=valute['CharCode'],
                num_code=valute['NumCode'],
                nominal=valute['Nominal'],
                name=valute['Name'],
                value=to_float(valute['Value']),
            )
            session.execute(stmt)
        session.commit()
