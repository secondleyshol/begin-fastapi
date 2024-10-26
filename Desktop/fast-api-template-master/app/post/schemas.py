from pydantic import BaseModel


class SSPost(BaseModel):
    title: str
    content: str