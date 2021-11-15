
from typing import List
from fastapi import FastAPI
from graphql.type.definition import GraphQLNonNull
from pydantic.tools import parse_obj_as
from starlette.graphql import GraphQLApp
import graphene
from .models import Event, Person, Chore
from fastapi.middleware.cors import CORSMiddleware

from .data import people, events, chores
from typing import List, Optional
from graphene_pydantic import PydanticInputObjectType, PydanticObjectType

app = FastAPI()

origins = ['*'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


people_data = parse_obj_as(List[Person], people)
print(people_data)

class EventObject(PydanticObjectType):
    class Meta:
        model = Event
        # exclude specified fields
    
    # NOTE: This is necessary for the GraphQL Union to be resolved correctly
    # where Person has a list of events/chores
    @classmethod
    def is_type_of(cls, root, info):
        return isinstance(root, (cls, Event))


class ChoreObject(PydanticObjectType):
    class Meta:
        model = Chore
        # exclude specified fields
    @classmethod
    def is_type_of(cls, root, info):
        return isinstance(root, (cls, Chore))


class PersonObject(PydanticObjectType):

    class Meta:
        model = Person
        # exclude specified fields

class Query(graphene.ObjectType):

    people = graphene.List(PersonObject)
    events = graphene.List(EventObject)
    chores = graphene.List(ChoreObject)
    # people_by_id = graphene.Field(PersonPydantic, person_id=graphene.Int(required=True))

    def resolve_people(parent, info):
        return people_data

    def resolve_event(parent, info):
        #return parse_obj_as(List[Event], events)
        ...

    def resolve_chore(parent, info):
        ...
        #return parse_obj_as(List[Chore], chores)

    # def resolve_person_by_id(self, info, person_id):
    #     return people.filter(lambda x: x.id == person_id)


class PersonInput(PydanticInputObjectType):
    class Meta:
        model = Person
        # exclude specified fields
        exclude_fields = ("id",)


class CreatePerson(graphene.Mutation):
    class Arguments:
        person = PersonInput(required=True)

    Output = PersonObject

    @staticmethod
    def mutate(parent, info, person):
        print(len(people))
        personModel = Person(id=len(people), name=person.name)
        # save PersonModel here
        people.append(personModel.json())
        return personModel

class Mutation(graphene.ObjectType):
    createPerson = CreatePerson.Field()

class EventInput(PydanticInputObjectType):
    class Meta:
        model = Event
        # exclude specified fields
        exclude_fields = ("id",)


# class CreateEvent(graphene.Mutation):
#     class Arguments:
#         event = EventInput()
#         participants: graphene.List(of_type=graphene.Int)

#     created:Event = None

#     @staticmethod
#     def mutate(root, info, event: EventInput, participants: List[int]):
#         id = len(events)
#         events.append(event.json())
#         events[id]["participants"] = participants
#         return CreateEvent(created=events[id])


# class EventMutation(graphene.ObjectType):
#     create = CreateEvent.Field()


app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query)))
