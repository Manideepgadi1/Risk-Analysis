# Riskometer API Documentation

## Base URL
```
http://localhost:8000
```

## Endpoints

### 1. Get All Available Indices

**Endpoint:** `GET /api/indices`

**Description:** Returns a list of all available indices in the dataset.

**Response:**
```json
{
  "indices": [
    "NIFTY 50",
    "NIFTY NEXT 50",
    "NIFTY 100",
    "NIFTY BANK",
    ...
  ]
}
```

**Example:**
```bash
curl http://localhost:8000/api/indices
```

---

### 2. Get Riskometer Data for Single Index

**Endpoint:** `GET /api/riskometer/{index_name}`

**Description:** Calculate and return complete riskometer data for a specific index.

**Parameters:**
- `index_name` (path, required): Name of the index
- `window` (query, optional): Rolling window size in days (default: 30)

**Response:**
```json
{
  "index_name": "NIFTY 50",
  "window": 30,
  "data": [
    {
      "date": "2025-01-15",
      "price": 38366.88,
      "returns": 0.0023,
      "volatility": 0.0145,
      "risk_score": 0.45
    },
    ...
  ]
}
```

**Fields:**
- `date`: Date in YYYY-MM-DD format
- `price`: Closing price of the index
- `returns`: Daily return (percentage change)
- `volatility`: Rolling volatility (standard deviation)
- `risk_score`: Normalized risk score (0-1)

**Example:**
```bash
curl "http://localhost:8000/api/riskometer/NIFTY%2050?window=30"
```

---

### 3. Get Complete Statistics

**Endpoint:** `GET /api/riskometer/all/{index_name}`

**Description:** Get current values and statistical summary for an index.

**Parameters:**
- `index_name` (path, required): Name of the index
- `window` (query, optional): Rolling window size in days (default: 30)

**Response:**
```json
{
  "index_name": "NIFTY 50",
  "current_price": 38366.88,
  "current_risk_score": 0.45,
  "current_volatility": 0.0145,
  "statistics": {
    "avg_volatility": 0.0132,
    "max_volatility": 0.0287,
    "min_volatility": 0.0045
  }
}
```

**Example:**
```bash
curl "http://localhost:8000/api/riskometer/all/NIFTY%2050?window=30"
```

---

### 4. Compare Multiple Indices

**Endpoint:** `GET /api/riskometer/compare`

**Description:** Compare risk scores across multiple indices.

**Parameters:**
- `indices` (query, required): Comma-separated list of index names
- `window` (query, optional): Rolling window size in days (default: 30)

**Response:**
```json
{
  "window": 30,
  "comparison": {
    "NIFTY 50": [
      {
        "date": "2025-01-15",
        "risk_score": 0.45
      },
      ...
    ],
    "NIFTY BANK": [
      {
        "date": "2025-01-15",
        "risk_score": 0.62
      },
      ...
    ]
  }
}
```

**Example:**
```bash
curl "http://localhost:8000/api/riskometer/compare?indices=NIFTY%2050,NIFTY%20BANK&window=30"
```

---

## Formula Implementation

### Daily Returns
```python
def calculate_daily_returns(prices):
    returns = (prices - prices.shift(1)) / prices.shift(1)
    return returns
```

### Rolling Volatility
```python
def calculate_rolling_volatility(returns, window=30):
    volatility = returns.rolling(window=window).std()
    return volatility
```

### Risk Score Normalization
```python
def normalize_to_risk_scale(volatility):
    sigma_min = volatility.min()
    sigma_max = volatility.max()
    risk_score = (volatility - sigma_min) / (sigma_max - sigma_min)
    return risk_score
```

---

## Error Handling

All endpoints return appropriate HTTP status codes:

- **200 OK**: Success
- **404 Not Found**: Index not found
- **500 Internal Server Error**: Server error (e.g., data loading failed)

**Error Response Format:**
```json
{
  "detail": "Index 'INVALID_NAME' not found"
}
```

---

## Rate Limiting

Currently no rate limiting is implemented. For production use, consider implementing rate limiting using middleware.

---

## CORS

CORS is enabled for all origins. In production, restrict to specific domains:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    ...
)
```

---

## Data Requirements

The API expects a `data.csv` file with:
1. First column: DATE (format: DD/MM/YY)
2. Subsequent columns: Index prices (numeric)

Example:
```csv
DATE,NIFTY 50,NIFTY BANK
10/11/25,38366.88,80712.23
09/11/25,38366.88,80712.23
```

---

## Python Client Example

```python
import requests

# Base URL
BASE_URL = "http://localhost:8000/api"

# Get all indices
response = requests.get(f"{BASE_URL}/indices")
indices = response.json()["indices"]
print(f"Available indices: {len(indices)}")

# Get riskometer data
index_name = "NIFTY 50"
window = 30
response = requests.get(
    f"{BASE_URL}/riskometer/{index_name}",
    params={"window": window}
)
data = response.json()
print(f"Data points: {len(data['data'])}")

# Get statistics
response = requests.get(
    f"{BASE_URL}/riskometer/all/{index_name}",
    params={"window": window}
)
stats = response.json()
print(f"Current risk score: {stats['current_risk_score']:.2%}")

# Compare indices
indices_to_compare = ["NIFTY 50", "NIFTY BANK"]
response = requests.get(
    f"{BASE_URL}/riskometer/compare",
    params={
        "indices": ",".join(indices_to_compare),
        "window": window
    }
)
comparison = response.json()
print(f"Comparing {len(comparison['comparison'])} indices")
```

---

## JavaScript Client Example

```javascript
const BASE_URL = 'http://localhost:8000/api';

// Get all indices
async function getIndices() {
    const response = await fetch(`${BASE_URL}/indices`);
    const data = await response.json();
    return data.indices;
}

// Get riskometer data
async function getRiskometer(indexName, window = 30) {
    const url = `${BASE_URL}/riskometer/${encodeURIComponent(indexName)}?window=${window}`;
    const response = await fetch(url);
    const data = await response.json();
    return data;
}

// Get statistics
async function getStats(indexName, window = 30) {
    const url = `${BASE_URL}/riskometer/all/${encodeURIComponent(indexName)}?window=${window}`;
    const response = await fetch(url);
    const data = await response.json();
    return data;
}

// Compare indices
async function compareIndices(indices, window = 30) {
    const indicesParam = indices.join(',');
    const url = `${BASE_URL}/riskometer/compare?indices=${encodeURIComponent(indicesParam)}&window=${window}`;
    const response = await fetch(url);
    const data = await response.json();
    return data;
}

// Usage
(async () => {
    const indices = await getIndices();
    console.log(`Available indices: ${indices.length}`);
    
    const data = await getRiskometer('NIFTY 50', 30);
    console.log(`Risk score: ${(data.data[data.data.length - 1].risk_score * 100).toFixed(2)}%`);
})();
```

---

## Performance Considerations

1. **Caching**: Consider implementing caching for frequently accessed indices
2. **Async Processing**: For large datasets, consider async processing
3. **Data Pagination**: For very large date ranges, implement pagination
4. **Compression**: Enable gzip compression for API responses

---

## Testing

### Using curl

```bash
# Test indices endpoint
curl -X GET "http://localhost:8000/api/indices"

# Test single index
curl -X GET "http://localhost:8000/api/riskometer/NIFTY%2050?window=30"

# Test statistics
curl -X GET "http://localhost:8000/api/riskometer/all/NIFTY%2050?window=30"

# Test comparison
curl -X GET "http://localhost:8000/api/riskometer/compare?indices=NIFTY%2050,NIFTY%20BANK&window=30"
```

### Using Python requests

```python
import requests

def test_api():
    base_url = "http://localhost:8000/api"
    
    # Test 1: Get indices
    r = requests.get(f"{base_url}/indices")
    assert r.status_code == 200
    print("✓ Indices endpoint working")
    
    # Test 2: Get riskometer data
    r = requests.get(f"{base_url}/riskometer/NIFTY 50?window=30")
    assert r.status_code == 200
    print("✓ Riskometer endpoint working")
    
    # Test 3: Get statistics
    r = requests.get(f"{base_url}/riskometer/all/NIFTY 50?window=30")
    assert r.status_code == 200
    print("✓ Statistics endpoint working")
    
    # Test 4: Compare indices
    r = requests.get(f"{base_url}/riskometer/compare?indices=NIFTY 50,NIFTY BANK&window=30")
    assert r.status_code == 200
    print("✓ Comparison endpoint working")
    
    print("\n✅ All tests passed!")

if __name__ == "__main__":
    test_api()
```

---

## WebSocket Support (Future Enhancement)

For real-time updates, consider implementing WebSocket support:

```python
from fastapi import WebSocket

@app.websocket("/ws/riskometer/{index_name}")
async def websocket_endpoint(websocket: WebSocket, index_name: str):
    await websocket.accept()
    while True:
        # Send real-time updates
        data = calculate_latest_risk(index_name)
        await websocket.send_json(data)
        await asyncio.sleep(60)  # Update every minute
```

---

## Deployment

### Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Production Server
```bash
# Using Gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# Or using Uvicorn directly
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

---

## License

This API is part of the Riskometer application.
