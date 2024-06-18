from fastapi import APIRouter, Query

from starlette.requests import Request

from src.database.models import ExampleModel
from src.dependencies.database import DBAsyncSession
from src.utils import get_list_response
from src.schemas import ExampleSchema, PaginatorGenerator

from app.annotated_type import LimitQueryInt, OffsetQueryInt

router = APIRouter(tags=["Example"], prefix="/example")


@router.get("/", response_model=PaginatorGenerator[ExampleSchema])
async def get_list(
    request: Request,
    session: DBAsyncSession,
    limit: LimitQueryInt = 20,
    offset: OffsetQueryInt = 0,
):
    response = await get_list_response(
        session=session,
        model=ExampleModel,
        model_schema=ExampleSchema,
        limit=limit,
        offset=offset,
        request=request
    )
    return response
