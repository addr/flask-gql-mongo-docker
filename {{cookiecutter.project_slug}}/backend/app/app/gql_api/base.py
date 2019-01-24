from flask import abort
from flask_jwt_extended import get_current_user, jwt_required
from graphene.types.objecttype import ObjectType, ObjectTypeOptions
from graphene import AbstractType, Int, String, Field, List, ID
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from mongoengine.queryset.visitor import Q
from abc import abstractmethod

from .list_metadata.types import ListMetadata


def default_model_resolver(self, info, id):
    return Node.get_node_from_global_id(info, id)


def default_query_resolver(type,
                           page=None,
                           perPage=10,
                           sortField=None,
                           sortOrder=None,
                           filter=None,
                           **kwargs):
    qs = type.objects.all()
    if sortField is not None and sortOrder is not None:
        sort_field = "-" + sortField if sortOrder != 'ASC' else sortField
        qs = qs.order_by(sort_field)
    if page is not None:
        start = page * perPage
        end = start + perPage
        qs = qs[start:end]
    if filter is not None:
        f_items = {
            k: v
            for k, v in filter.items() if v is not None and k != "ids"
        }
        qs = qs.filter(**f_items)
    return qs


class BaseQuery(ObjectType):
    class SingleField(Field):
        def __init__(self, type, resolver=default_model_resolver):
            super().__init__(type, id=ID(), resolver=resolver)

    class ListMetaField(Field):
        def __init__(self, filter, name, resolver):
            super().__init__(
                ListMetadata,
                page=Int(),
                perPage=Int(),
                sortField=String(),
                sortOrder=String(),
                filter=filter(),
                name=name,
                resolver=resolver)

    class QueryList(List):
        def __init__(self, type, filter, resolver):
            super().__init__(
                type,
                page=Int(),
                perPage=Int(),
                sortField=String(),
                sortOrder=String(),
                filter=filter(),
                resolver=resolver)


class BaseMutation(ObjectType):
    pass


class BaseSubscription(ObjectType):
    pass
