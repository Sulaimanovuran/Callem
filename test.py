'''
Для отклика на эту вакансию необходимо ответить на вопрос работодателя.

Пожалуйста, решите следующую простую задачу. Можно использовать любые инструменты.
Дано: список dict-объектов вида вида {"key": "value"}, 
например [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}].

Напишите функцию, которая удаляет дубликаты из этого списка. 
Для примера выше возвращаемое значение может быть равно [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {"key2": "value2"}].
Обязательное условие: функция не должна иметь сложность O(n^2).
'''

# d = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]

# print(0 == False) # 1 == True, 1 > 1


a = '''
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAgO9q0YIIL/PbjNgCFDkCk3FrlJFWOs/MaJzz18MqtpnaKAQ8
WNh22fxs8HAnVRZD9eis0MyXc4cPKzT1gZdn2aRtMF9pUNWfmztYUQ0XHTax8fVd
iTvf4f3b5dbHMxu9vqMLaQ9LEpmc8RYcMUI6dUQNxhe+KLPzwE9eDVyJ9XYGdSmZ
z0gEqYE8SfscXVze44eV77xla5IsmIRPcctZIv3wRfW2t+xBaF14Fr3al0fZ+hma
6jEfWoZe0HSc7W+p/ET9HWCjXmbzZKw7qtMi6DF/rJs0sytjgs/lGTsWPHm/DJOq
UZlTpJxyWGIfl7rKnwMRHQsHDf0qAFGEwhDoRwIDAQABAoIBACAF1pzkU849HblU
aOfG5QnjsJl8o1MGCzmsSa+77F7fxVwM+UQDtzkaxZ/N6ybp2cU4nbtaJP9veuf7
RkKCbSuT9/58o/aMqBBw49V1j9kUnYt/qlSMR2WknDnwZxcde7neWtYkEzwyZNVH
7YaacVRwq48YlIUddJu92pks86K/7BFIpZDCD1YPakPftupqp2WEsSRCAYWPKnYw
FX8ZnO5hUJ0xt933BhtVZE/oyMWHE98ZQE/VvIifYjT7Y2WwDhKRnFnipgCQ2pYp
eDE6Yo3U+KGVPN+ywfKJoTz6OsGjz2CuU7hWwJuM0yWY1Gdj5J289J6dtVzGP1bd
X3o6KEECgYEAws/xMzqmYYuP0C6+xS3PBH0bIhwcYk6lQVCtTawvOeHV9tT6J2Er
aG4xr1jv7HZCjDeNbDnfHoQnnhhQpD6ARHGS4Q+3YghOR5v12GAYWUXnbkf7MYst
uPmbCkhzawL0pArYu0O7Ue5tJ54l1mpzmc8Jy4kb6LOOlBQuXW5llycCgYEAqW6S
LUc1skbOvNEEVmW2HneItGvR31rhwIbyVLeMLHdFdsR50i/IINzs5QPer2rteFD9
1xF8QgHj1+l0CQXzEKI+v4Dx/2cBhHbpZypqdDKVNSo24ZAVKz821wgGKMPuPrd3
9XnwzVlufZmZ0YxlBqr9JqHpLIAnNiOM8tWB2eECgYB36/enuIfpbjcWSWBIEx3n
vnewdKuIXK9f2KEGOmNL91h2PL7M9QT6oTLWpSH0ZwwqMpxNLgbKS0H0ETW7FXpy
J5PqFXmm0EQX0srw6p6yfdSsT4UzB2EbCBRHrTfXfRdJ0B+Aj35FPkdVZwYVyqvk
181IzNswUTAIua+c9jN1awKBgHprIcMFSI7fClDy1Kd4JfYtd+CkZqdzCtoIpt7/
H5ChPNdrbnmnfHoCJkfyW9ty7tGX81CJmbY3l2BRlT1PxyelkqDbkf5vdnE3Wbzo
sLH0OkqHjc+8Qw9URVNowMqDhohaF5qN2KcGjwbBDJqTTgtbUD2xjsBQeARt+1EZ
YxEBAoGAULGBnFje4w3Z1ouNkJTgIkeAONZW9lmluk3CcNq6mdnzV4o0M7vtrNAR
qGOsGiqa1wO1uQGZUaGez/kblMNv3IlBuL+MNB8oEKio8di+bXm2rfGyqCrQZcVj
01F7TrPh6O5J6Ux28g9y9DuGgFRfINyWTvezIANdF9uB+fnfvhI=
-----END RSA PRIVATE KEY-----
'''

print(len(a))