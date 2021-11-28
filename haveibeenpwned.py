import time
import urllib.parse

import requests

from NoSuccessError import NoSuccessError
from abstract_websites import AbstractWebsites


class HaveIBeenPwned(AbstractWebsites):
    __seconds_to_wait_between_requests = 5
    __max_retries = 4

    def __init__(self):
        self.website_name = "haveibeenpwned.com"
        self.website_url = "https://" + self.website_name
        self.service_url = self.website_url + "/unifiedsearch/{0}"
        # set init headers
        self.headers = {
            'Host': self.website_name,
            'User-Agent': self.generate_user_agent(),
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1'
        }

    def __update_headers(self, cookie):
        self.headers.update({
            'Referer': self.website_url + "/",
            'X-Requested-With': 'XMLHttpRequest',
            'Cookies': cookie,
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        })

    def __get_request_landing_page(self, session):
        for i in range(1, self.__max_retries):
            response = session.get(self.website_url, headers=self.headers)
            if response.status_code == 200:
                return session.cookies.get_dict()['__cf_bm']
            else:
                time.sleep(self.__seconds_to_wait_between_requests)
        # 0 successful requests
        raise NoSuccessError("No successful queries for " + self.website_name)

    def __get_request_webservice(self, session, email):
        # url encode the email (test@test.com -> test\40test.com)
        email = urllib.parse.quote(email)
        self.__formatted_service_url = self.service_url.format(email)

        for i in range(1, self.__max_retries):
            response = session.get(self.__formatted_service_url, headers=self.headers)
            if response.status_code == 200:
                return response.json()
            else:
                time.sleep(self.__seconds_to_wait_between_requests)
        # 0 successful requests
        raise NoSuccessError("No successful queries for " + self.website_name)

    @staticmethod
    def __count_json_list(json_list):
        if json_list is None:
            return 0
        else:
            return len(json_list)

    def __evaluate_json(self, json, email):
        if json is None:
            return False
        else:
            breach_count = self.__count_json_list(json["Breaches"])
            paste_count = self.__count_json_list(json["Pastes"])
            return breach_count > 0 or paste_count > 0

    def is_pwned(self, email):
        session = requests.session()
        cookie = self.__get_request_landing_page(session)
        self.__update_headers(cookie)
        time.sleep(self.__seconds_to_wait_between_requests)
        json = self.__get_request_webservice(session, email)
        return self.__evaluate_json(json, email)
