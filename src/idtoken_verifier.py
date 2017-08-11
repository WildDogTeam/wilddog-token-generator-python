# -*- coding: utf-8 -*-

import urllib2
import json
from idtoken_verify_result import IdTokenResult
VALIDATE_IDTOKEN = "https://auth.wilddog.com/v2/{}/auth/verifyIdToken?idToken={}"
class IdTokenVerifier:
    def __init__(self, appid):
        self.appid = appid

    """
    检测idtoken的是否合法

    Args:
        idtoken - Wilddog Auth 中用户登录后授权的token。

    Returns:
        idtoken verify result.

    Raises:
        Exception
        URL ERROR
    """
    def verifyIdToken(self, idtoken):

        url = VALIDATE_IDTOKEN.format(self.appid, idtoken);
        req = urllib2.Request(url = url, data = {})
        response = urllib2.urlopen(req, None, 3)
        try:
            if response.getcode() == 200:
                httpResult = response.read()
                parseResult = json.loads(httpResult)
                isValid =  parseResult['isValid']
                if (isValid == True):
                    verifyResult = IdTokenResult(parseResult['idToken']['uid'], parseResult['idToken']['name'], parseResult['idToken']['email'], parseResult['idToken']['picture'])

                    return dict(isValid = isValid, idToken = verifyResult)
                else:
                    return dict(isValid = isValid, idToken = None)
            else:
                raise Exception("verifyIdToken request error")
        finally:
            if (response != None):
                response.close();



