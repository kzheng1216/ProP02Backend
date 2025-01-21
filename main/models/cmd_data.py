from pydantic import BaseModel


class CmdData(BaseModel):
    cmd: str
