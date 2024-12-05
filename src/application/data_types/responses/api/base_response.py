from typing import Optional

from pydantic import BaseModel


class BaseApiResponse(BaseModel):
    success: bool
    message: Optional[str] = None
