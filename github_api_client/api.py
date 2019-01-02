from datetime import datetime

from flask import current_app

class GithubAPI(object):

    def __init__(self, access_token=None):
        self.access_token = access_token
        self.headers = self.build_headers()

    def build_headers(self, ):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/vnd.github.machine-man-preview+json'
        }
        return headers

    def get_user_information(self):
        endpoint = "/user" 
        return self.make_github_user_request(endpoint)

    def get_user_emails(self):
        endpoint = "/user/emails" 
        return self.make_github_user_request(endpoint)

    def get_user_repos(self, affiliation=None):
        endpoint = "/user/repos" 
        return self.make_github_user_request(endpoint, affiliation=affiliation)

    def get_user_orgs(self):
        endpoint = "/user/orgs" 
        return self.make_github_user_request(endpoint)

    def get_org_repos(self, org_name):
        endpoint = "/orgs/{}/repos".format(org_name)
        return self.make_github_user_request(endpoint)

    def make_github_user_request(self, endpoint, **kwargs):
        url = "https://api.github.com{}".format(endpoint)
        print(url)
        params = {
            'access_token': self.access_token,
        }
        if kwargs:
            params.update(**kwargs)
        response = requests.get(url, params=params, headers=self.headers)
        return response

    def retrieve_access_token(self, code):
        url = 'https://github.com/login/oauth/access_token'
        params = {
            'client_id': current_app.settings.CLIENT_ID,
            'client_secret': current_app.settings.CLIENT_SECRET,
            'code': code
        }
        headers = {'Accept': 'application/json'}

        response = requests.post(url, params=params, headers=headers)
        return response
