from fastapi import status


def test_rates(test_app):
    response = test_app.get('/rates/rub')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'rates': [
            {
                'char_code': 'AUD',
                'num_code': 36,
                'nominal': 1,
                'name': 'Австралийский доллар',
                'value': 52.5603,
            },
        ],
    }


def test_convert(test_app):
    response = test_app.get('/convert/aud/rub/10.5')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'value': 551.88315}
