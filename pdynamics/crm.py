import requests
from requests_ntlm import HttpNtlmAuth
import json
import uuid


def add_lookup_field(data, fieldname, entitytype, id):
    if(id is not None):
        id = parse_id(id)
        data[fieldname+"@odata.bind"] = "/"+entitytype+"(" + id + ")"


def parse_id(id):
    if('api/data' in id and '(' in id):
        id = id[id.index('(')+1:-1]
    uuid.UUID(id)
    return id


class client:
    api_version = "api/data/v9.0"
    access_token = ''

    def get_record_url(self, entity_set_name, record_id):
        return '{0}{1}/{2}({3})'.format(self.crmurl, self.api_version, entity_set_name, record_id)

    @property
    def crmurl(self):
        if self._crmurl.endswith('/'):
            return self._crmurl
        return self._crmurl+'/'

    def get_default_headers(self):
        headers = {"Accept": "application/json, */*", "content-type": "application/json; charset=utf-8",
                   "OData-MaxVersion": "4.0", "OData-Version": "4.0"}
        if(self.return_formatted_value):
            headers['Prefer'] = 'odata.include-annotations=OData.Community.Display.V1.FormattedValue'
        if(self.access_token):
            headers['Authorization'] = 'Bearer ' + self.access_token
        return headers

    def refresh_access_token(self):
        if(self.token_endpoint and not self.client_secret):
            tokenrequest = {
                'client_id': self.client_id,
                'resource': self.crmurl,
                'username': self.username,
                'password': self.password,
                'grant_type': 'password'
            }
        elif(self.client_secret):
            if(not self.token_endpoint):
                self.token_endpoint = 'https://login.microsoftonline.com/organizations/oauth2/v2.0/token'
            tokenrequest = {
                'client_id': self.client_id,
                'scope': self.crmurl+'/.default',
                'client_secret': self.client_secret,
                'username': self.username,
                'password': self.password,
                'grant_type': 'password'
            }
        if(self.client_id):
            token = requests.post(self.token_endpoint, data=tokenrequest)
            try:
                self.access_token = token.json()['access_token']
            except(Exception):
                print('Failed to get access token')

    def __init__(self, url, username=None, password=None, client_id=None, token_endpoint=None, client_secret=None, return_raw=False, formatted_value=True):
        self._crmurl = url
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.token_endpoint = token_endpoint
        self.return_raw = return_raw
        self.return_formatted_value = formatted_value
        self.Session = requests.Session()

        if(client_id is None and token_endpoint is None):
            self.Session.auth = HttpNtlmAuth(username, password)
        else:
            self.refresh_access_token()

    def _request(self, method, query, data=None,
                 json=None, headers=None, **kwargs):
        if(self.crmurl in query and self.api_version in query):
            url = query
        else:
            url = '{0}{1}/{2}'.format(self.crmurl,
                                      self.api_version, query)
        if(headers is None):
            headers = self.get_default_headers()
        response = self.Session.request(
            method, url, data=data, headers=headers, json=json, params=kwargs)
        return self.parse_response(response)

    def parse_response(self, response):
        no_content = response.status_code == 204
        created_or_no_content = response.status_code == 201 or no_content
        entityid_in_header = response.headers.get('OData-EntityId') != None
        if (created_or_no_content and entityid_in_header):
            return response.headers["OData-EntityId"]
        if(no_content):
            return True
        if(self.return_raw):
            return response.content
        return response.json()

    def get_data(self, query, json=None, data=None):
        return self._request('get', query, data=data, json=json)

    def create_data(self, entity_set_name=None, json=None, data=None):
        return self._request('post', entity_set_name, data=data, json=json)

    def update_data(self, entity_set_name=None, record_id=None, json=None, data=None):
        if entity_set_name is not None and record_id is not None:
            record_id = parse_id(record_id)
            url = '{0}({1})'.format(entity_set_name, record_id)
            return self._request('patch', url, data=data, json=json)
        raise Exception(
            "entity_set_name and record_id are both required in update_data method")

    def delete_data(self, entity_set_name=None, record_id=None, json=None, data=None):
        if entity_set_name is not None and record_id is not None:
            record_id = parse_id(record_id)
            return self._request('delete', '{0}({1})'.format(entity_set_name, record_id), data=data, json=json)
        raise Exception(
            "entity_set_name and record_id are both required in delete_data method")

    def put_data(self, query=None, json=None, data=None):
        return self._request('put', query, data=data, json=json)

    def test_connection(self):
        api_info = self.get_data('WhoAmI')
        if('BusinessUnitId' in api_info):
            print('User', api_info['UserId'], 'Connect to',
                  'Organization', api_info['OrganizationId'], 'is successful')
        else:
            print('Failed to setup connection to dynamics 365')
