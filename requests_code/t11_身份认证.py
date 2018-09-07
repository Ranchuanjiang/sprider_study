# 身份认证
import requests
from requests.auth import HTTPBasicAuth
r = requests.get("http://localhost:5000", auth=HTTPBasicAuth("username", "password"))
print(r.status_code)
# 此时如果用户名和密码正确 会返回200 状态码 如果认证失败就返回401
# 也可以简写成
r1 = requests.get("http://localhost:5000", auth=("username", "password"))
print(r1.status_code)

# 还提供其他认证方式 OAuth 认证 不过需要安装 oauth 包 pip install requests_oauthlib
# 使用oauth 认证
from requests_oauthlib import OAuth1
url = "https://api.twitercom/1.1/.account/verify_credentials.json"
auth = OAuth1("YOUR_APP_KEY", "YOUR_APP_SECRET", "USER_OAUTH_TOKEN", "USER_OAUTH_TOKEN_SECRET")
requests.get(url=url, auth=auth)