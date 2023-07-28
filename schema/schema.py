import graphene
from graphene_django import DjangoObjectType

from users.models import User as UserModel


class User(DjangoObjectType):
    class Meta:
        model = UserModel


class Query(graphene.ObjectType):  # Change here from DjangoObjectType to ObjectType
    users = graphene.List(User)

    def resolve_users(self, info):
        return UserModel.objects.all()


schema = graphene.Schema(query=Query)
