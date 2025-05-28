from fastapi import APIRouter, HTTPException, Request
from main.security.jwt_required import jwt_required
from main.models.cmd_data import CmdData
from main.services.cmd_service import CmdService

router = APIRouter()


@router.post("/api/cmd")
@jwt_required()
async def run_cmd(request: Request, cmd_data: CmdData):
    output = CmdService().run_cmd(cmd_data.cmd)
    return {
        "message": output
    }
