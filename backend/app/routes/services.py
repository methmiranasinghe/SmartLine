from fastapi import APIRouter
from app.databases import services_collection

router = APIRouter(prefix="/services", tags=["services"])

@router.get("/")
async def get_services():  # Made async for non-blocking I/O
    try:
        services = []
        for service in services_collection.find():
            services.append({
                "id": str(service["_id"]),
                "name": service["name"],
                "duration": service["duration"],
                "price": service["price"]
            })
        return services
    except Exception as e:
        # Basic error handling; customize as needed
        return {"error": f"Failed to retrieve services: {str(e)}"}