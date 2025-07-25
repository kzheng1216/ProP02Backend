from fastapi import APIRouter, HTTPException, Request
from main.security.auth_required import AuthRequired
from main.models.run_test_data import RunTestData
from main.testcases.service.run_test_service import RunTestService

router = APIRouter()


@router.post("/api/run_tests")
@AuthRequired()
async def run_tests(request: Request, data: RunTestData):
    print("---->> Run Test <<----", data)
    if data.mark_type in ['api', 'ui', 'ut', 'e2e']:
        return RunTestService().run_tests(data.mark_type, data.report_type)

    return {
        "status": "error",
        "message": "mark_type is not available, should be ['api', 'ui', 'ut', 'e2e']"
    }

