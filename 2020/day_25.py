cardPublic = 13135480
doorPublic = 8821721

#cardPublic = 5764801
#doorPublic = 17807724

cardTransform = 1
doorTransform = 1
subjectNumber = 7

cardSecretLoop = 0
doorSecretLoop = 0

while cardTransform != cardPublic:
    cardTransform = (cardTransform * subjectNumber) % 20201227
    cardSecretLoop += 1

while doorTransform != doorPublic:
    doorTransform = (doorTransform * subjectNumber) % 20201227
    doorSecretLoop += 1

print(cardSecretLoop, doorSecretLoop)

encryptionKey = 1
for i in range(cardSecretLoop):
    encryptionKey = (encryptionKey * doorPublic) % 20201227

print(encryptionKey)
