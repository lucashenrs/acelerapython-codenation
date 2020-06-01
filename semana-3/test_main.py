from main import get_temperature
import pytest
from unittest.mock import patch

temp_imputs = [
    (62, -14.235004, -51.92528, 16),
    ]

@patch('main.requests.get')
@pytest.mark.parametrize("temp_farenheit_input, lat, lng, \
                         celsius_expected_output", temp_imputs)

def test_get_temperature_by_lat_lng(mock_get, temp_farenheit_input,
                                    lat, lng, celsius_expected_output):

    mock_get.return_value.json.return_value = {
        "currently": {
            "temperature": temp_farenheit_input
        }
    }

    response = get_temperature(lat, lng)

    assert response == celsius_expected_output
