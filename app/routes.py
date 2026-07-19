from fastapi import APIRouter
from app.models import FlightSearchRequest, MilesCalculationResponse
from app.services import calculate_cpm

router = APIRouter()


@router.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/search/flights")
def search_flights(request: FlightSearchRequest) -> dict[str, object]:
    return {
        "origin": request.origin,
        "destination": request.destination,
        "departure_date": request.departure_date,
        "return_date": request.return_date,
        "passengers": request.passengers,
        "results": [
            {
                "airline": "Example Air",
                "price": 520.0,
                "currency": "BRL",
                "duration_hours": 4.5,
                "stops": 0,
            },
            {
                "airline": "Blue Sky",
                "price": 680.0,
                "currency": "BRL",
                "duration_hours": 5.2,
                "stops": 1,
            },
        ],
    }


@router.get("/milhas/calculadora", response_model=MilesCalculationResponse)
def miles_calculator(price: float, miles: int) -> MilesCalculationResponse:
    cpm, label = calculate_cpm(price, miles)
    return MilesCalculationResponse(price=price, miles=miles, cpm=cpm, label=label)
