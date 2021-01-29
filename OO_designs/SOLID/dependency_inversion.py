"""
high level modules should not depend upon low level modules. Both should depend upon abstractions

"""


class XMLHttpService(XMLHttpRequestService):
    pass


class Http:
    def __init__(self, xml_http_service: XMLHttpService):
        self.xml_http_service = xml_http_service

    def get(self, url, options: dict):
        self.xml_http_service.request(url, 'GET')

    def post(self, url, options: dict):
        self.xml_http_service.post(url, 'POST')


"""
Http is the high-level component whereas XMLHttpService is the low level component
the Http class is forced to depend upon the XMLHttpService class
if we change the Http connection service => we have to move through all the instances of Http to edit the code
=> violate OCP
"""


class Connection:
    def request(self, url: str, options: dict):
        raise NotImplementedError


class XMLHttpService(Connection):
    xhr = XMLHttpRequest()

    def request(self, url, options: dict):
        self.xhr.open()
        self.xhr.send()


class Http:
    def __init__(self, http_connection: Connection):
        self.http_connection = http_connection

    def get(self, url, options: dict):
        self.http_connection.request(url, 'GET')

    def post(self, url, options: dict):
        self.http_connection.request(url, 'POST')


class NodeHttpService(Connection):
    def request(self, url: str, options: dict):
        pass


class MockHttpService(Connection):
    def request(self, url: str, options: dict):
        pass


xml_http_service = XMLHttpService()
http = Http(xml_http_service)

"""
now we can see that both high-level module and low level module depend on abstractions.
This DIP will force us not to violate the Liskov Substitution Principle
"""