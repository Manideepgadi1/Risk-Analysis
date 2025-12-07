from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd
import numpy as np
from typing import Optional
import os

app = FastAPI(title="Riskometer API - Trailing 3-Year Returns", version="2.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FILE = "data.csv"

def load_data():
    """Load the CSV data"""
    try:
        df = pd.read_csv(DATA_FILE)
        df['DATE'] = pd.to_datetime(df['DATE'], format='%d/%m/%y')
        return df
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading data: {str(e)}")

def calculate_trailing_3yr_returns(prices: pd.Series, dates: pd.Series) -> pd.DataFrame:
    """
    Calculate riskometer using Growth Rate formula.
    
    Formula: Growth Rate = (Final Value / Initial Value)^(1 / Number of Periods) - 1
    
    Where:
    - Final Value = Current Price
    - Initial Value = Price 3 Years Ago
    - Number of Periods = 3 years
    
    Risk Score = Normalized growth rate (0 to 1 scale)
    """
    # Calculate growth rates for all points
    growth_rates = []
    valid_dates = []
    valid_prices = []
    
    for i in range(len(prices)):
        current_date = dates.iloc[i]
        current_price = prices.iloc[i]
        
        # Look back exactly 3 years
        lookback_date = current_date - pd.DateOffset(years=3)
        
        # Find the closest date to 3 years ago
        date_diffs = (dates - lookback_date).abs()
        closest_idx = date_diffs.idxmin()
        
        # Only calculate if we have data at least 3 years back
        if dates.iloc[closest_idx] <= current_date - pd.DateOffset(years=2, months=11):
            past_price = prices.iloc[closest_idx]
            
            if past_price > 0 and not pd.isna(past_price) and not pd.isna(current_price):
                # Calculate exact number of years (periods)
                years_diff = (current_date - dates.iloc[closest_idx]).days / 365.25
                
                if years_diff > 0:
                    # Growth Rate Formula: (Final Value / Initial Value)^(1/Number of Periods) - 1
                    growth_rate = ((current_price / past_price) ** (1 / years_diff)) - 1
                    
                    growth_rates.append(growth_rate)
                    valid_dates.append(current_date)
                    valid_prices.append(current_price)
    
    if len(growth_rates) == 0:
        return pd.DataFrame()
    
    # Convert growth rates to risk scores (0 to 1 scale)
    growth_array = np.array(growth_rates)
    
    # Normalize to 0-1: Higher growth = Lower risk, Lower growth = Higher risk
    min_growth = growth_array.min()
    max_growth = growth_array.max()
    
    if max_growth != min_growth:
        # Normalize: 0-1 scale
        normalized = (growth_array - min_growth) / (max_growth - min_growth)
        # Invert so high growth = low risk
        risk_scores = 1 - normalized
    else:
        risk_scores = np.zeros(len(growth_array))
    
    # Build results dataframe
    results = []
    for i in range(len(growth_rates)):
        results.append({
            'date': valid_dates[i],
            'price': valid_prices[i],
            'trailing_3yr_return': growth_rates[i],
            'risk_score': risk_scores[i]
        })
    
    return pd.DataFrame(results)

@app.get("/")
async def root():
    """Serve the frontend HTML"""
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        return HTMLResponse(content=html_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading HTML: {str(e)}")

@app.get("/api/indices")
async def get_indices():
    """Get list of all available indices"""
    df = load_data()
    indices = [col for col in df.columns if col != 'DATE']
    return {"indices": indices}

@app.get("/api/riskometer/{index_name}")
async def get_trailing_returns(
    index_name: str,
    years: Optional[int] = None
):
    """
    Get trailing 3-year returns for a specific index
    
    Parameters:
    - index_name: Name of the index
    - years: Filter data to last N years (optional)
    """
    df = load_data()
    
    if index_name not in df.columns:
        raise HTTPException(status_code=404, detail=f"Index '{index_name}' not found")
    
    # Filter by years if specified
    if years:
        cutoff_date = df['DATE'].max() - pd.DateOffset(years=years)
        df = df[df['DATE'] >= cutoff_date].reset_index(drop=True)
    
    # Calculate trailing 3-year returns
    result_df = calculate_trailing_3yr_returns(df[index_name], df['DATE'])
    
    # Remove NaN values
    result_df = result_df.dropna()
    
    # Convert to list of dictionaries
    data = []
    for _, row in result_df.iterrows():
        data.append({
            'date': row['date'].strftime('%Y-%m-%d'),
            'price': float(row['price']),
            'trailing_3yr_return': float(row['trailing_3yr_return']),
            'risk_score': float(row['risk_score'])
        })
    
    # Calculate statistics
    risk_scores = result_df['risk_score'].dropna()
    returns = result_df['trailing_3yr_return'].dropna()
    stats = {
        'current_risk': float(risk_scores.iloc[-1]) if len(risk_scores) > 0 else 0.0,
        'avg_risk': float(risk_scores.mean()) if len(risk_scores) > 0 else 0.0,
        'min_risk': float(risk_scores.min()) if len(risk_scores) > 0 else 0.0,
        'max_risk': float(risk_scores.max()) if len(risk_scores) > 0 else 0.0,
        'current_return': float(returns.iloc[-1] * 100) if len(returns) > 0 else 0.0
    }
    
    return {
        "index_name": index_name,
        "data": data,
        "statistics": stats
    }

if __name__ == "__main__":
    import uvicorn
    import os
    
    # Get port from environment variable or default to 8001
    port = int(os.environ.get("PORT", 8001))
    
    # Get host from environment variable or default to 0.0.0.0
    host = os.environ.get("HOST", "0.0.0.0")
    
    uvicorn.run(app, host=host, port=port)
