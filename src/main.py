from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Recommendation Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "recommendation-service", "features": ["ml_recommendations", "personalization"]}

@app.get("/recommendations/{user_id}")
async def get_user_recommendations(user_id: str):
    return {
        "recommendations": [
            {"product_id": "prod_1", "score": 0.95, "reason": "Similar purchases"},
            {"product_id": "prod_2", "score": 0.87, "reason": "Trending in category"}
        ],
        "user_id": user_id,
        "service": "recommendation-service"
    }

@app.get("/recommendations/trending")
async def get_trending():
    return {
        "trending": [
            {"product_id": "prod_1", "popularity": 95},
            {"product_id": "prod_2", "popularity": 87}
        ],
        "service": "recommendation-service"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3006)
