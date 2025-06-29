from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Simulated database
customer_data = {
    "+1 303 305 5294": "queue",
    "+13033055294": "queue",
    "+16282368824": "queue"
}

class PhoneRequest(BaseModel):
    phone_number: str

@app.post("/get-customer-name")
def get_customer_name(request: PhoneRequest):
    name = customer_data.get(request.phone_number)
    if name:
        return {"customerQueue": name}
    raise HTTPException(status_code=404, detail="Customer not found")
