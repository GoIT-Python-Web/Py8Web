from jose import jwt, JWTError

secret = 'f4407b4661aa06f7fc6d215ad6928d356efcaade4fb58bb5fd0b7d8808797b7c'

payload = {"sub": "exapmle@api.com", "username": "kolobok", "role": "moderator"}

token = jwt.encode(payload, secret, algorithm='HS512')
print(token)
try:
    r = jwt.decode(token, secret, algorithms=['HS256', 'HS512'])
    print(r)
except JWTError as e:
    print(e)
