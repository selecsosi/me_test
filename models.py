# -*- coding: utf-8 -*-
from mongoengine import Document
from mongoengine.fields import StringField, IntField, ListField, EmbeddedDocument, DateTimeField

class Segment(Document):
    operatingCarrier = StringField()
    departureDay = StringField()
    boardPoint = StringField()
    cabin = StringField()
    avlStatus = IntField()
    flightNumber = IntField()
    departueTime = StringField()
    travlTime = StringField()
    arrivalTime = StringField()
    bookingClass = StringField()
    equipmentType = StringField()
    arrivalDay = StringField()
    markentingCarrier = StringField()
    offPoint = StringField()


class FlightLeg(Document):
    segments = ListField(Segment)


class Request(Document):
    ptcGroup = ListField()
    type = StringField()
    flightLegs = ListField()
    totalQuotedFare = IntField()
    passengerTotal = IntField()


class Response(Document):
    option_token_link = StringField()
    option_21 = IntField()
    option_14 = IntField()
    option_7 = IntField()
    option_3 = IntField()
    option_24 = IntField()
    status = IntField()


class LogEntry(Document):
    service = StringField()
    clientID = StringField()
    source = StringField()
    request = EmbeddedDocument(Request)
    response = EmbeddedDocument(Response)
    timestamp = DateTimeField()
