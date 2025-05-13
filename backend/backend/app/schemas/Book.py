from pydantic import BaseModel, ConfigDict

class Book(BaseModel):
    id: int
    title: str
    description:str
    author: str
    image_link: str
    category: str
    rating: float

    model_config = ConfigDict(from_attributes=True)
