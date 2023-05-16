from fastapi import APIRouter, FastAPI
from models.calendar import Event, EventCreate
router = APIRouter(
    prefix="/calendar",
)

events_db = []



@router.post("/events/", response_model=Event)
def create_event(event: EventCreate):
    # Aquí podrías añadir tu lógica para añadir el evento a una base de datos real.
    event_dict = event.dict()
    event_dict["id"] = len(events_db) + 1
    events_db.append(event_dict)
    return event_dict

@router.get("/events/", response_model=List[Event])
def read_events():
    # Aquí podrías añadir tu lógica para obtener los eventos de una base de datos real.
    return events_db

@router.get("/events/{event_id}", response_model=Event)
def read_event(event_id: int):
    # Aquí podrías añadir tu lógica para obtener un evento específico de una base de datos real.
    event = next((event for event in events_db if event["id"] == event_id), None)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event