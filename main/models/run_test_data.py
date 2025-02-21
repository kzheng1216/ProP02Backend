from pydantic import BaseModel


class RunTestData(BaseModel):
    mark_type: str
    report_type: str
