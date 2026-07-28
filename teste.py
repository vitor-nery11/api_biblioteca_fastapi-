from security import criar_token

token = criar_token({
   "sub": "vitor@gmail.com"
}
)

print(token)