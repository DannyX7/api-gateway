from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.init import init

app = FastAPI(title="Guided Onboarding Gateway Service")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Register controllers
init(app)

@app.get("/")
def home():
    return "Gateway Started...."
