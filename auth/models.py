from mongoengine import Document, StringField

class MongoUser(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    def check_password(self, raw): return self.password == raw