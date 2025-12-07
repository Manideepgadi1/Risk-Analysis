# Risk Analysis - Deployment Guide for Hostinger VPS

This guide will help you deploy the Risk Analysis application on your Hostinger VPS alongside your existing projects without any conflicts.

## 🎯 Deployment Strategy

The application will be deployed as:
- **URL Path**: `http://your-domain.com/risk-analysis`
- **Backend API**: `http://your-domain.com/risk-analysis/api/`
- **Port**: 8001 (internal, proxied through Nginx)

This setup ensures zero conflict with your existing projects.

## 📋 Prerequisites

On your VPS, ensure you have:
- Ubuntu/Debian Linux
- Python 3.8+
- Nginx (already installed for other projects)
- Git
- Root/sudo access

## 🚀 Quick Deployment

### Step 1: Clone the Repository on VPS

```bash
ssh your-vps-user@your-server-ip

# Navigate to web root
cd /var/www

# Clone the project
sudo git clone https://github.com/Manideepgadi1/Risk-Analysis.git risk-analysis
cd risk-analysis
```

### Step 2: Run Automated Deployment Script

```bash
# Make the deployment script executable
sudo chmod +x deployment/deploy.sh

# Run the deployment script
sudo ./deployment/deploy.sh
```

The script will automatically:
- Set up Python virtual environment
- Install all dependencies
- Configure systemd service
- Set up Nginx reverse proxy
- Start the application

### Step 3: Configure Your Domain

Edit the Nginx configuration:

```bash
sudo nano /etc/nginx/sites-available/risk-analysis
```

Replace `your-domain.com` with your actual domain.

### Step 4: Restart Nginx

```bash
sudo nginx -t  # Test configuration
sudo systemctl restart nginx
```

## 🔧 Manual Deployment (If Automated Script Fails)

### 1. Set Up Python Environment

```bash
cd /var/www/risk-analysis
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn
```

### 2. Configure Systemd Service

```bash
sudo cp deployment/risk-analysis.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable risk-analysis
sudo systemctl start risk-analysis
```

### 3. Configure Nginx

```bash
sudo cp deployment/nginx_config.conf /etc/nginx/sites-available/risk-analysis
sudo ln -s /etc/nginx/sites-available/risk-analysis /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 4. Set Permissions

```bash
sudo chown -R www-data:www-data /var/www/risk-analysis
sudo mkdir -p /var/log/risk-analysis
sudo chown -R www-data:www-data /var/log/risk-analysis
```

## 🔒 SSL/HTTPS Configuration (Recommended)

Install Certbot and obtain SSL certificate:

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

Or for subdomain:

```bash
sudo certbot --nginx -d risk-analysis.your-domain.com
```

## 📊 Monitoring & Logs

### Check Service Status

```bash
sudo systemctl status risk-analysis
```

### View Logs

```bash
# Service logs
sudo journalctl -u risk-analysis -f

# Nginx access logs
sudo tail -f /var/log/nginx/access.log

# Nginx error logs
sudo tail -f /var/log/nginx/error.log

# Application logs
sudo tail -f /var/log/risk-analysis/error.log
```

## 🔄 Updating the Application

```bash
cd /var/www/risk-analysis
sudo git pull origin main
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart risk-analysis
```

## 🛠️ Troubleshooting

### Port 8001 Already in Use

Check what's using the port:
```bash
sudo lsof -i :8001
```

Change the port in `/etc/systemd/system/risk-analysis.service`:
```bash
Environment="PORT=8002"
```

### Service Won't Start

```bash
sudo journalctl -u risk-analysis -n 50
```

### Nginx Configuration Conflicts

Test Nginx config:
```bash
sudo nginx -t
```

## 🌐 Access URLs

After deployment, access your application at:

- **Main App**: `http://your-domain.com/risk-analysis`
- **API Docs**: `http://your-domain.com/risk-analysis/api/docs`
- **Health Check**: `http://your-domain.com/risk-analysis/api/indices`

## 📁 Project Structure on VPS

```
/var/www/risk-analysis/
├── main.py                  # FastAPI application
├── data.csv                 # Market data
├── index.html               # Frontend
├── requirements.txt         # Python dependencies
├── venv/                    # Virtual environment
└── deployment/
    ├── nginx_config.conf    # Nginx configuration
    ├── risk-analysis.service # Systemd service
    ├── gunicorn_config.py   # Gunicorn config (optional)
    └── deploy.sh            # Deployment script
```

## 🔐 Security Best Practices

1. **Keep Dependencies Updated**
   ```bash
   pip list --outdated
   pip install --upgrade package-name
   ```

2. **Enable Firewall**
   ```bash
   sudo ufw allow 80/tcp
   sudo ufw allow 443/tcp
   sudo ufw enable
   ```

3. **Regular Backups**
   ```bash
   # Backup data
   sudo cp /var/www/risk-analysis/data.csv ~/backups/
   ```

## 💡 Alternative: Using Subdomain

If you prefer a subdomain instead of a path:

1. Edit Nginx config to use subdomain configuration (commented section in nginx_config.conf)
2. Set DNS A record: `risk-analysis.your-domain.com` → Your VPS IP
3. Update `server_name` in Nginx config
4. Get SSL: `sudo certbot --nginx -d risk-analysis.your-domain.com`

## 📞 Support

If you encounter issues:
1. Check logs: `sudo journalctl -u risk-analysis -n 100`
2. Verify service: `sudo systemctl status risk-analysis`
3. Test Nginx: `sudo nginx -t`
4. Check port: `sudo netstat -tulpn | grep 8001`

## 🎉 Success Verification

Once deployed, verify everything works:

1. Service is running: `sudo systemctl is-active risk-analysis` returns `active`
2. Port is listening: `sudo netstat -tulpn | grep 8001`
3. Web interface loads: Visit `http://your-domain.com/risk-analysis`
4. API responds: `curl http://localhost:8001/api/indices`
5. Nginx proxies correctly: Check main domain URL
