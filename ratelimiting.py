from fastapi import FastAPI, HTTPException, Request

app = FastAPI()  # <-- Uvicorn looks for this 'app' instance


req_counter={}
max_req=5

@app.get("/limit") 
def limit(request:Request):
    ip_address=request.client.host
    req_counter[ip_address]=req_counter.get(ip_address,0)+1
    print(req_counter)
 
    if req_counter[ip_address]>max_req:
        raise HTTPException(status_code=401,detail="limit reached")
    
    return{"message":f"request {req_counter[ip_address]} success"}