import re


class IPAddress:
    IP_ADDRESS_REGEX = re.compile(
        r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    )
    INCORRECT_IP_ADDRESS_FORMAT_MSG = "Incorrect IP Address format"

    def __init__(self, ip_address: str):
        self.__ipaddress: str = ip_address
        if not self.__check_if_ip_is_network():
            raise ValueError(self.INCORRECT_IP_ADDRESS_FORMAT_MSG)

    @property
    def ipaddress(self):
        return self.__ipaddress

    def __check_if_ip_is_network(self):
        """Supports protocol IPv4"""
        return bool(re.match(self.IP_ADDRESS_REGEX, self.__ipaddress))

    def remove_lead_zeros(self):
        """Remove leading zeros from an IP address e.g. 216.08.094.196
        to 216.8.94.196"""
        return re.sub(r"\.[0]*", ".", self.__ipaddress)


if __name__ == "__main__":
    ip_address_obj = IPAddress("216.08.094.196")
    assert ip_address_obj.remove_lead_zeros() == "216.8.94.196"
