from pydantic import BaseModel


class StrategyBaseValidator(BaseModel):
    pippo: str
