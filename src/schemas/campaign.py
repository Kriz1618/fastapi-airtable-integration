import json
from pydantic import BaseModel
from enum import Enum
from datetime import date
from typing import List


class CampaignStatus(str, Enum):
    UNLISTED = "Unlisted"
    PUBLISHED = "Published"


class TableImage(BaseModel):
    id: str
    width: int
    height: int
    url: str
    filename: str
    size: int
    type: str
    thumbnails: dict


class CampaignInput(BaseModel):
    title: str
    brand: List[str] | str
    locations: List[str]
    whatYouRecieve: str
    description: str
    brandStory: str
    retailValue: int
    startDate: date
    endDate: date
    targetCreatorSize: List[str]
    lowAge: int
    highAge: int
    niche: List[str]
    content: List[str]
    visualsTheme: str
    caption: str
    hashtagsMentions: str
    inspiration: str
    schedulingRequirements: str
    # campaignImage: Optional[TableImage]
    campaignCity: str
    count: str
    requirement: str
    neighborhood: List[str]
    goal: str
    status: CampaignStatus


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)


class Status(Enum):
    CREATED = "Created"
    IN_PROGRESS = "In progress"
    DONE = "Done"


class EventInput(BaseModel):
    title: str
    description: str
    email: str
    status: Status
    creators: int


class Event(EventInput):
    id: str
