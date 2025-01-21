from fastapi import APIRouter, HTTPException
from main.models.cmd_data import CmdData
from main.services.cmd_service import CmdService

router = APIRouter()


@router.post("/api/cmd")
async def run_cmd(cmd_data: CmdData):
    output = CmdService().run_cmd(cmd_data.cmd)
    return {
        "message": output
    }
