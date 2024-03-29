from flask import Response
from datetime import datetime
from service.response.base_response import base_response
from Config import Config


class response_authentication_token:
    config = Config()

    @classmethod
    def generate_response(self, body: dict, token: str) -> Response:
        response = base_response.generate_response(body)

        # tokenの有効期限は2日
        max_age = 60 * 60 * 24 * 2  # 2 days
        expires = int(datetime.now().timestamp()) + max_age
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        server_domain = self.config.SERVER_DOMAIN
        response.set_cookie("token", value=token,
                            httponly=True, samesite=None,
                            domain=server_domain, path='/', expires=expires)
        return response
