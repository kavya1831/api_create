from src.models import Asset , Token
from rest_framework import authentication, exceptions

class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):

        _token = request.META.get("HTTP_TOKEN", False)
        if _token:

            try:
                token = Token.objects.filter(access_token=_token)

                if(token.count() <= 0):
                    raise exceptions.AuthenticationFailed('Invalid access token')

            except Exception as e:
                raise exceptions.AuthenticationFailed('Invalid access token')
            user_id = token.user
            user = Asset.objects.get(user_id=user_id)
            return (user, token)

        else:
            return None
