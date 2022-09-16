from typing import Any, Optional

from pydantic import BaseModel, Field, root_validator



class BaseResponse(BaseModel):
    status_code: Optional[int] = Field(200, ge=200, le=599)
    message: str = ""
    data: Any = None
    error: Any = None

    class Config:
        validate_assignment = True

    @root_validator
    def set_status_code(cls, values):
        if values["error"] is not None:
            values["status_code"] = 400
        return values
