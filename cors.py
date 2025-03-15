from fastapi.middleware.cors import CORSMiddleware

origins = [
    "https://mytrusteddomain.com",
    "https://another-trusted.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

