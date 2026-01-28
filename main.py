```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

# To run the application, use the following command:
# uvicorn main:app --reload
```

### Instructions to Run:
1. Make sure you have FastAPI and Uvicorn installed:
   ```bash
   pip install fastapi uvicorn
   ```
2. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
3. Open a browser and go to `http://localhost:8000/` to see the message.