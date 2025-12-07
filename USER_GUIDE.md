# Riskometer Application - User Guide

## What is Riskometer?

Riskometer is a financial risk analysis tool that calculates and visualizes the risk scores of various market indices. It uses volatility-based metrics to provide a normalized risk score between 0 (low risk) and 1 (high risk).

## Formula Explanation

The application implements the following calculation pipeline:

### 1. Daily Returns Calculation
```
r_t = (P_t - P_(t-1)) / P_(t-1)
```
- Calculates the percentage change in price from one day to the next
- Example: If price moves from 100 to 105, return = (105-100)/100 = 0.05 or 5%

### 2. Rolling Volatility Calculation
```
σ_t = sqrt( (1 / (N-1)) * Σ(r_i - r̄)² )
```
- Calculates the standard deviation of returns over a rolling N-day window
- Uses the unbiased estimator (dividing by N-1)
- r̄ is the mean return over the window
- Higher volatility = more price fluctuation = higher risk

### 3. Risk Score Normalization
```
Risk_t = (σ_t - σ_min) / (σ_max - σ_min)
```
- Normalizes volatility to a 0-1 scale
- σ_min: Minimum volatility in the entire dataset
- σ_max: Maximum volatility in the entire dataset
- Result: 0 = lowest risk, 1 = highest risk

## Quick Start

### Method 1: Using the Batch File (Recommended)
1. Double-click `start.bat`
2. Wait for the browser to open automatically
3. The application will be available at http://localhost:8000

### Method 2: Manual Start
1. Open PowerShell/Command Prompt
2. Navigate to the Riskometer directory:
   ```
   cd d:\Riskometer
   ```
3. Run the application:
   ```
   python main.py
   ```
4. Open browser and go to: http://localhost:8000

## How to Use the Dashboard

### Analyzing a Single Index

1. **Select Index**: Choose an index from the dropdown menu
   - Over 120 indices available (NIFTY 50, NIFTY BANK, etc.)

2. **Set Rolling Window**: 
   - Default: 30 days
   - Range: 5-252 days
   - Smaller window = more responsive to recent changes
   - Larger window = smoother, longer-term trend

3. **Click "Analyze Risk"**

4. **View Results**:
   - **Stats Panel**: Shows current metrics
     - Current Price
     - Risk Score (0-100%)
     - Risk Level (Low/Medium/High)
     - Current & Average Volatility
   
   - **Risk Score Chart**: Line graph showing risk over time
     - Green zone (0-33%): Low risk
     - Yellow zone (33-67%): Medium risk
     - Red zone (67-100%): High risk
   
   - **Price Chart**: Historical price movement
   
   - **Volatility Chart**: Rolling volatility over time

### Comparing Multiple Indices

1. **Select Multiple Indices**: 
   - Use the "Compare Multiple Indices" multi-select box
   - Hold Ctrl (Windows) or Cmd (Mac) to select multiple
   - Can select 2-8 indices for comparison

2. **Set Rolling Window**: Same as single index

3. **Click "Analyze Risk"**

4. **View Comparison**:
   - All selected indices shown on the same risk score chart
   - Different colors for each index
   - Easy to see which indices are currently riskier

## Understanding the Charts

### Risk Score Chart
- **Y-axis**: Risk score from 0 to 1 (0% to 100%)
- **X-axis**: Time (dates)
- **Lines**: 
  - Dotted line at 33%: Low/Medium risk boundary
  - Dotted line at 67%: Medium/High risk boundary
- **Interpretation**: Higher = more volatile = riskier

### Price Chart
- Shows the actual price movement of the index
- Helps correlate risk with price changes
- Uptrends and downtrends visible

### Volatility Chart
- Shows raw volatility values (as percentage)
- Before normalization
- Technical users can see actual volatility numbers

## Risk Level Interpretation

| Risk Score | Level | Meaning | Suggested Action |
|-----------|-------|---------|------------------|
| 0.0 - 0.33 | 🟢 Low | Stable market conditions | Suitable for conservative investors |
| 0.33 - 0.67 | 🟡 Medium | Moderate volatility | Balanced approach recommended |
| 0.67 - 1.0 | 🔴 High | High volatility/uncertainty | Higher risk, potential higher reward |

## Tips & Best Practices

1. **Window Size Selection**:
   - **Short-term traders**: Use 5-15 days
   - **Medium-term**: Use 20-60 days
   - **Long-term**: Use 60-252 days

2. **Interpretation**:
   - Risk score is relative to historical volatility
   - High risk doesn't mean "don't invest" - it means "higher volatility"
   - Compare across indices to find relative risk

3. **Data Updates**:
   - Replace `data.csv` with updated data
   - Restart the application to load new data

4. **Multiple Indices**:
   - Use comparison mode to identify diversification opportunities
   - Indices with different risk patterns can balance a portfolio

## API Usage (For Developers)

### Get All Indices
```
GET http://localhost:8000/api/indices
```

### Get Risk Data for Single Index
```
GET http://localhost:8000/api/riskometer/NIFTY 50?window=30
```

### Get Complete Statistics
```
GET http://localhost:8000/api/riskometer/all/NIFTY 50?window=30
```

### Compare Multiple Indices
```
GET http://localhost:8000/api/riskometer/compare?indices=NIFTY 50,NIFTY BANK&window=30
```

## Troubleshooting

### Server won't start
- Check if port 8000 is already in use
- Make sure Python and all dependencies are installed
- Run: `pip install -r requirements.txt`

### Data not loading
- Verify `data.csv` is in the same directory as `main.py`
- Check CSV format matches expected structure
- First column must be DATE in DD/MM/YY format

### Charts not displaying
- Clear browser cache
- Check browser console for errors (F12)
- Ensure JavaScript is enabled

### Empty or missing data in charts
- Some indices may have missing data for certain dates
- Try a different rolling window size
- Check if the selected index has sufficient historical data

## System Requirements

- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Edge, Safari)
- ~100MB free disk space
- Internet connection (first time only, for loading Chart.js library)

## Data Format

If you want to add your own data, ensure the CSV follows this format:

```csv
DATE,INDEX1,INDEX2,INDEX3
10/11/25,38366.88,99651.76,35940.79
09/11/25,38366.88,99651.76,35940.79
...
```

- DATE column must be first
- Date format: DD/MM/YY
- All other columns are treated as indices
- Numeric values for prices

## Support

For issues or questions:
- Check this user guide
- Review the README.md file
- Examine the formula implementation in main.py

## Version History

- **v1.0.0** (Current)
  - Initial release
  - Support for 120+ indices
  - Real-time risk calculation
  - Interactive charts
  - Multi-index comparison

---

**Happy Risk Analysis! 📊**
