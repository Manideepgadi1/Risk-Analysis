# Riskometer - Index Risk Analysis Tool

A comprehensive risk analysis tool that calculates and visualizes the risk scores of financial indices using volatility-based metrics.

## Features

- **Risk Calculation**: Implements the complete riskometer formula
  - Daily returns calculation: `r_t = (P_t - P_(t-1)) / P_(t-1)`
  - N-day rolling volatility: `σ_t = sqrt((1 / (N-1)) * Σ(r_i - r̄)²)`
  - Normalized risk score: `Risk_t = (σ_t - σ_min) / (σ_max - σ_min)`

- **Interactive Dashboard**: Beautiful web interface with real-time charts
- **Multiple Indices**: Support for 120+ financial indices
- **Comparison Mode**: Compare risk scores across multiple indices
- **Customizable Window**: Adjust rolling window size (5-252 days)

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the FastAPI backend:
```bash
python main.py
```

2. Open your browser and navigate to:
```
http://localhost:8000
```

3. Select an index from the dropdown menu
4. Adjust the rolling window size (default: 30 days)
5. Click "Analyze Risk" to view the risk analysis

## API Endpoints

- `GET /api/indices` - List all available indices
- `GET /api/riskometer/{index_name}?window=30` - Get risk data for a specific index
- `GET /api/riskometer/all/{index_name}?window=30` - Get complete statistics
- `GET /api/riskometer/compare?indices=INDEX1,INDEX2&window=30` - Compare multiple indices

## Data Format

The application expects a CSV file named `data.csv` with:
- First column: DATE (format: DD/MM/YY)
- Remaining columns: Index prices

## Risk Score Interpretation

- **0.0 - 0.33**: Low Risk (Green)
- **0.33 - 0.67**: Medium Risk (Yellow)
- **0.67 - 1.0**: High Risk (Red)

## Technology Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Charts**: Chart.js
- **Data Processing**: Pandas, NumPy

## Project Structure

```
Riskometer/
├── main.py              # FastAPI backend
├── index.html           # Frontend interface
├── data.csv            # Index data
├── requirements.txt    # Python dependencies
└── README.md          # Documentation
```

## Author

Built with ❤️ for financial risk analysis
