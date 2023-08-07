from pydantic import BaseModel


class WebhookBody(BaseModel):
    base_id: str
    table_id: str
