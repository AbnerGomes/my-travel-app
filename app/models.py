from pydantic import BaseModel, Field


class FlightSearchRequest(BaseModel):
    origin: str = Field(..., min_length=3)
    destination: str = Field(..., min_length=3)
    departure_date: str
    return_date: str | None = None
    passengers: int = Field(default=1, ge=1)


class MilesCalculationResponse(BaseModel):
    price: float
    miles: int
    cpm: float
    label: str
