from fastapi import APIRouter, HTTPException, Request
from main.models.cmd_data import CmdData
from main.services.cmd_service import CmdService
from main.security.auth_required import AuthRequired

router = APIRouter()


@router.post("/api/cmd")
@AuthRequired()
async def run_cmd(request: Request, cmd_data: CmdData):
    output = CmdService().run_cmd(cmd_data.cmd)
    return {
        "message": output
    }
