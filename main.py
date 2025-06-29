from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Simulated database
customer_data = {
    "+1234567890": "Queue1",
    "+16282368824": "Queue1"
}

class PhoneRequest(BaseModel):
    phone_number: str

@app.post("/get-customer-name")
def get_customer_name(request: PhoneRequest):
    name = customer_data.get(request.phone_number)
    if name:
        return {"customer_name": name}
    raise HTTPException(status_code=404, detail="Customer not found")
