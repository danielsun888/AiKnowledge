from django.db import models


from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,ArrayProperty,
    UniqueIdProperty, RelationshipTo)

from django_neomodel import DjangoNode

config.DATABASE_URL = 'neo4j://daniel:fighting@localhost:7687/aiknowledge'

class Verse(DjangoNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    bookID = IntegerProperty(unique_index=True, required=True)
    chapterID = IntegerProperty(unique_index=True, required=True)
    verseID = IntegerProperty(unique_index=True)
    text=StringProperty(unique_index=True)
    BookName = StringProperty()
    Volume = StringProperty()
    keyword = RelationshipTo('Keyword','have')


    class Meta:
        app_label = "graph"

class Keyword(DjangoNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    frequency = IntegerProperty()
    class Meta:
        app_label = "graph"
# for text
# class Country(DjangoNode):
#      code = StringProperty(unique_index=True, required=True)

# class Person(DjangoNode):
#     uid = UniqueIdProperty()
#     name = StringProperty(unique_index=True)
#     age = IntegerProperty(index=True, default=0)

#     # traverse outgoing IS_FROM relations, inflate to Country objects
#     country = RelationshipTo(Country, 'IS_FROM')

#     class Meta:
#         app_label = "bible"

