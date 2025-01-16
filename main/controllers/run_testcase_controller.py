from fastapi import APIRouter

from main.models.run_test_data import RunTestData
from main.testcases.service.run_test_service import RunTestService

router = APIRouter()


@router.post("/api/run_tests")
async def run_tests(data: RunTestData):
    print("---->> Run Test <<----", data)
    return RunTestService().run_tests(data.mark_type)
