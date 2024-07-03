"""This module helps you get the city according to the ip address"""
import geoip2.webservice
from license_key import api
_key
account_id = 1032814


def get_location(ip):
    client = geoip2.webservice.Client(account_id, license_key, host='geolite.info')

    try:
        response = client.city(ip)
        subdivision_name = response.city.names.get('en')
        return subdivision_name
    except geoip2.errors.GeoIP2Error as error:
        raise Exception(f"Failed to get location from IP: {error}")


# if __name__ == "__main__":
#     res = get_location("198.46.176.79")
#     print(res)
