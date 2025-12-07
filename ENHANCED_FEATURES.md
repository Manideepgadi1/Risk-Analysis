# Riskometer v2.0 - Enhanced Features Guide

## 🎉 What's New

Your Riskometer application has been completely upgraded with advanced features for professional risk analysis!

## ✨ Key Enhancements

### 1. **New Risk Scale: -1 to +1**

The risk score now ranges from **-1 to +1** instead of 0 to 1:

- **-1.0 to -0.3**: 🟢 **Low Risk** - Very stable, low volatility
- **-0.3 to +0.3**: 🟡 **Moderate Risk** - Normal market conditions
- **+0.3 to +1.0**: 🔴 **High Risk** - High volatility, significant price fluctuations

**Example Values:**
- `-0.23`: Low risk (as you mentioned)
- `0.38`: High risk (as you mentioned)
- `0.00`: Neutral/moderate risk

### 2. **Time Period Filters (1Y to 10Y)**

11 time period buttons at the top:
- **1Y, 2Y, 3Y, 4Y, 5Y, 6Y, 7Y, 8Y, 9Y, 10Y, All**
- Click any button to filter data to that time period
- Default is **3 Years**
- Data automatically aggregates to show one point per month for better visualization

### 3. **Smart Zoom Functionality**

#### How Zoom Works:
1. **Monthly View (Default)**: Shows one data point per month for clean overview
2. **Scroll to Zoom**: Use mouse scroll wheel on chart to zoom in
3. **Auto-Switch to Daily**: When zoomed in close enough (< 6 months visible), automatically switches to daily data
4. **Drag to Pan**: Click and drag to move around the chart
5. **Reset Button**: Click "🔄 Reset Zoom" to return to original view

#### Manual Toggle:
- Click **"📊 Daily/Monthly"** button to manually switch between:
  - **Monthly View**: Aggregated data, one point per month
  - **Daily View**: All daily data points visible

### 4. **Enhanced UI/UX**

#### Visual Improvements:
- **Smooth Animations**: All elements fade and slide in beautifully
- **Hover Effects**: Cards lift up when hovered
- **Color-Coded Risk**: Automatic color indicators based on risk level
- **Gradient Backgrounds**: Beautiful purple gradient theme
- **Responsive Design**: Works perfectly on all screen sizes

#### Interactive Features:
- **Zoom Info Popup**: Shows "Scroll to zoom • Drag to pan" when you start zooming
- **Hover Tooltips**: Detailed information when hovering over chart points
- **Active State**: Selected time period button highlighted in purple
- **Loading States**: Smooth loading indicators

### 5. **Advanced Chart Features**

#### Risk Score Chart:
- **Y-axis**: Fixed from -1 to +1
- **Zero Line**: Bold line at 0 showing neutral point
- **Reference Lines**: Dotted lines at -0.5 and +0.5
- **Gradient Fill**: Color changes from green (bottom) to red (top)
- **Smooth Curves**: Tension set to 0.4 for smooth line rendering

#### Price Chart:
- **Synchronized Zoom**: Zoom controls match the risk chart
- **Auto-scaling Y-axis**: Adapts to price range
- **Green Theme**: Clearly distinguishable from risk chart

## 🎯 How to Use

### Basic Workflow:

1. **Select Index**: Choose from 120+ indices
2. **Choose Time Period**: Click 1Y, 2Y, 3Y, etc.
3. **Set Rolling Window**: Default 30 days (adjustable 5-252)
4. **Click "Analyze Risk"**: Generate the analysis

### Advanced Workflow:

#### For 3-Year Analysis (Your Example):
```
1. Click "3Y" button (it's default)
2. Select "NIFTY 50" from dropdown
3. Click "Analyze Risk"
4. View monthly aggregated data
5. Scroll to zoom into specific periods
6. Chart automatically switches to daily view when zoomed
```

#### Zoom to Specific Date Range:
```
1. Start with any time period (e.g., 5Y)
2. Scroll mouse wheel over chart to zoom in
3. Drag left/right to navigate
4. Keep zooming until you see daily data
5. Hover over points to see exact dates and values
```

#### Compare Different Periods:
```
1. Analyze with 1Y selected
2. Note the risk score
3. Click 5Y button
4. See how current risk compares to 5-year history
```

## 📊 Understanding the Data

### Risk Score Calculation:

```
Step 1: Daily Returns
r_t = (P_t - P_(t-1)) / P_(t-1)

Step 2: Rolling Volatility  
σ_t = sqrt((1/(N-1)) * Σ(r_i - r̄)²)

Step 3: Normalize to 0-1
normalized = (σ_t - σ_min) / (σ_max - σ_min)

Step 4: Scale to -1 to +1
Risk_t = (normalized * 2) - 1
```

### Monthly Aggregation:

When in monthly view, data is aggregated by:
- Taking the **first date** of each month
- **Averaging** prices across the month
- **Averaging** risk scores across the month

This provides a cleaner view for long time periods.

## 🔧 Technical Features

### Performance Optimizations:
- **Lazy Loading**: Only loads data when needed
- **Efficient Rendering**: Uses Chart.js optimizations
- **Smart Aggregation**: Reduces data points for better performance
- **Caching**: Browser caches chart library

### Browser Compatibility:
- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Mobile browsers

### Keyboard Shortcuts:
- **Enter**: Trigger analysis (when in window size input)
- **Scroll**: Zoom in/out on charts
- **Click + Drag**: Pan around charts

## 💡 Pro Tips

### Tip 1: Spot Market Volatility
```
1. Select "All" time period
2. Analyze any index
3. Look for risk spikes (peaks going toward +1)
4. Zoom into those periods to see daily volatility
```

### Tip 2: Compare Crisis Periods
```
1. Use 10Y view to see multiple market cycles
2. Zoom into 2020 (COVID crash)
3. Compare with 2008 (if data available)
4. See how current risk compares
```

### Tip 3: Risk Trend Analysis
```
1. Look at 3Y or 5Y view
2. Observe if risk is trending up or down
3. Current position relative to historical range
4. Use this for portfolio decisions
```

### Tip 4: Sector Rotation
```
1. Analyze NIFTY IT with 2Y view
2. Note periods of high vs low risk
3. Compare with NIFTY BANK
4. Identify when each sector is volatile
```

## 🎨 Visual Guide

### Stats Panel Shows:
1. **Current Price**: Latest closing price
2. **Risk Score**: Current risk (-1 to +1) with color indicator
3. **Current Volatility**: Most recent volatility percentage
4. **Risk Range**: Min to Max risk in selected period

### Color Indicators:
- 🟢 **Green Badge**: Low Risk (-1 to -0.3)
- 🟡 **Yellow Badge**: Moderate Risk (-0.3 to +0.3)
- 🔴 **Red Badge**: High Risk (+0.3 to +1)

### Chart Legend:
- **Bottom Legend**: Explains risk level color coding
- **Top Legend**: Shows dataset name (index name)

## 🚀 Example Use Cases

### Use Case 1: Day Trader
```
- Select 1Y period
- Use 5-10 day rolling window
- Zoom to last 3 months
- Monitor daily risk changes
- High risk = volatility opportunities
```

### Use Case 2: Long-term Investor
```
- Select 5Y or 10Y period
- Use 60-90 day rolling window
- View monthly aggregation
- Look for risk trends
- Low risk = stable investment periods
```

### Use Case 3: Portfolio Manager
```
- Compare multiple indices
- Analyze 3Y periods
- 30-day rolling window
- Identify diversification opportunities
- Balance high-risk with low-risk indices
```

## 🔍 Troubleshooting

### Chart not zooming?
- Make sure you're scrolling **over** the chart area
- Try clicking on chart first
- Use the "Daily/Monthly" button to toggle view

### Data looks choppy?
- This is monthly aggregation
- Click "Daily/Monthly" for all data points
- Or zoom in to auto-switch to daily

### Want exact dates?
- Hover over any point on the chart
- Tooltip shows exact date and value
- In daily view, you see every single date

## 📱 Mobile Experience

The application is fully responsive:
- Time period buttons wrap nicely
- Charts are touch-enabled
- Pinch to zoom on mobile
- Swipe to pan
- All features work on tablets

## 🎓 Learning Resources

### Understand Risk Scores:
- **Negative scores**: Below-average volatility for this index
- **Positive scores**: Above-average volatility for this index
- **Zero**: Right at the average volatility

### Volatility Context:
- Risk is **relative** to the index's own history
- Different indices have different volatility profiles
- NIFTY BANK naturally more volatile than NIFTY 50
- Risk score normalizes this for comparison

## 🌟 Best Practices

1. **Start Broad, Then Narrow**:
   - Begin with 5Y or 10Y view
   - Identify interesting periods
   - Zoom in for details

2. **Adjust Window Size**:
   - Short-term: 5-15 days
   - Medium-term: 20-60 days  
   - Long-term: 60-252 days

3. **Use Multiple Timeframes**:
   - Check 1Y, 3Y, and 5Y
   - Compare current risk position
   - Understand trend context

4. **Regular Monitoring**:
   - Check weekly or monthly
   - Track risk changes
   - Adjust portfolio accordingly

## 🎉 Summary

You now have a professional-grade risk analysis tool with:
- ✅ Risk scores from -1 to +1 (negative to positive)
- ✅ Time period filters (1Y through 10Y)
- ✅ Smart zoom with auto-switch to daily data
- ✅ Beautiful, intuitive interface
- ✅ Monthly aggregation for clean visualization
- ✅ Professional charts with full interactivity

**Enjoy your enhanced Riskometer! 📊**
