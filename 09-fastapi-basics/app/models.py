from typing import Literal, Optional

from pydantic import BaseModel, Field


class ApplicationCreate(BaseModel):
    company: str = Field(..., min_length=1)
    role_title: str = Field(..., min_length=1)
    location: str = Field(..., min_length=1)
    work_mode: Literal["Hybrid", "Remote", "On-site"]
    status: Literal["Interested", "Applied", "Interview", "Rejected", "Offer"]
    deadline: Optional[str] = None
    applied_date: Optional[str] = None
    salary: str = "Unknown"
    notes: Optional[str] = None


class ApplicationStatusUpdate(BaseModel):
    status: Literal["Interested", "Applied", "Interview", "Rejected", "Offer"]