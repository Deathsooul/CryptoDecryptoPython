from cryptography.fernet import Fernet

#Gera a chave de criptografia
cipherKey = Fernet.generate_key()
cipher = Fernet(cipherKey)


def encryptMessage(payload:str):
  """Encriptografa uma mensagem a partir de uma string

  Args:
      payload (str): Mensagem a ser encriptografada

  Returns:
      str: Mensagem Criptografada
  """
  #Transforma em bytes
  msg = bytes(payload, 'utf-8')
  encryptMessage = cipher.encrypt(msg)
  #transforma em string
  outputMessage = encryptMessage.decode()
  return outputMessage

def decryptMessage(payload:str):
  """Decriptografa uma mensagem a partir de uma string

  Args:
      payload (str): Mensagem a ser decriptografada

  Returns:
      str: Mensagem Decriptografada
  """
  #Transforma para bytes
  encryptMessage = payload.encode()
  outputMessage = cipher.decrypt(encryptMessage)
  #Transforma em string
  outputMessage = outputMessage.decode()
  return outputMessage



# Exemplo
encrypt = encryptMessage("test")
print(encrypt)
print("*************************************************************")
decrypt = decryptMessage(encrypt)
print(decrypt)
