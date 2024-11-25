from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.plugins.mongodb import MongoClient

router = APIRouter()


@router.get("/contexts/{credential_type}/{version}", tags=["Public"])
async def get_context(credential_type: str, version: str):
    mongo = MongoClient()
    record = mongo.find_one(
        "CredentialTypeRecord", {"type": credential_type, "version": version}
    )
    if not record:
        raise HTTPException(
            status_code=404,
            detail="Resource not found",
        )
    return JSONResponse(status_code=200, content=record["context"])


@router.get("/bundles/{credential_type}/{version}", tags=["Public"])
async def get_oca_bundle(credential_type: str, version: str):
    mongo = MongoClient()
    record = mongo.find_one(
        "CredentialTypeRecord", {"type": credential_type, "version": version}
    )
    if not record:
        raise HTTPException(
            status_code=404,
            detail="Resource not found",
        )
    return JSONResponse(status_code=200, content=record["oca_bundle"])
