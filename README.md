# Wilddog Token Generator - Python

Wilddog允许用户使用自定义Token进行终端用户认证。Token采用的是安全的JSON Web Token(JWT)格式。

关于token格式，请参阅文档：[https://docs.wilddog.com/guide/auth/server/server.html#生成-Custom-Token] (https://docs.wilddog.com/guide/auth/server/server.html#生成-Custom-Token)

需要注意 : 本生成器只能生成适用于Auth2.0 sdk的 Custom Token 登录。


## 安全提示

由于token的生成需要Wilddog应用的超级密钥, 因此token生成工作只能在信任的服务器上进行。 绝对不要将Wilddog超级密钥嵌入到客户端应用中，以便于保障超级密钥不会泄漏。


## 生成token

要生成token, 必须要使用wilddog的超级密钥。使用浏览器进入应用的控制面板，在“超级密钥”tab中可以找到应用的超级密钥。

示例代码：

```python
from wilddog_token_generator import create_token

auth_payload = {"uid": "1", "claim": "xxx"}
token = create_token("<超级密钥>", auth_payload)
```

payload必须含有"uid"字段。uid字段必须是字符串类型，长度小于64字节。 最终生成的token必须小于1024字节。


## Token Options

调用 `create_token()` 时，可以传递第二个参数 `options`。

可选的options有：

* **expires** (number or DateTime) - 时间戳 (秒为单位) 或者一个 `DateTime`，代表的是token的有效期至。超过这个时间之后，此token将失效。

* **notBefore** (number or DateTime) - 时间戳 (秒为单位) 或者一个 `DateTime`，代表的是在此时间之前，这个token是无效的。

* **admin** (boolean) - 如果设置为"true"，那么用这个oken认证过的客户端将获得管理员权限，规则表达式不会对admin权限的客户端生效. admin权限的客户端拥有对所有数据的读写权限。

* **debug** (bool) - 如果设置为true，client将会接收到规则表达式执行过程的debug信息。


下面是设置options的示例代码:

```python
from wilddog_token_generator import create_token

auth_payload = {"uid": "1", "provider": "custom"}
options = {"admin": True}
token = create_token("<超级密钥>", auth_payload, options)
```