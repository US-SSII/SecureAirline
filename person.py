import hashlib

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def generate_hash(self):
        data = f'{self.name}{self.age}'.encode('utf-8')
        return hashlib.sha256(data).hexdigest()