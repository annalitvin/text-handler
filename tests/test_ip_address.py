import pytest

from app.ip_address.ip_address import IPAddress


class TestIPAddress:
    INCORRECT_IP_ADDRESS_FORMAT_MSG = "Incorrect IP Address format"

    @pytest.mark.parametrize(
        "ip_address,expected",
        [
            ("216.08.094.196", "216.8.94.196"),
        ],
    )
    def test_change_date_format(self, ip_address, expected):
        ip_address_obj = IPAddress(ip_address)
        assert ip_address_obj.remove_lead_zeros() == expected

    @pytest.mark.parametrize(
        "ip_address",
        [
            "Anna Anna",
        ],
    )
    def test_incorrect_ipaddress_format(self, ip_address):
        with pytest.raises(ValueError) as error:
            IPAddress(ip_address)

        assert self.INCORRECT_IP_ADDRESS_FORMAT_MSG in str(error.value)
