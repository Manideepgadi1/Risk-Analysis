# Git Commands to Push to Repository

## Initial Setup (First Time Only)

```bash
cd "d:\Riskometer - Copy"

# Initialize git if not already done
git init

# Add remote repository
git remote add origin https://github.com/Manideepgadi1/Risk-Analysis.git

# Or if remote already exists, update it
git remote set-url origin https://github.com/Manideepgadi1/Risk-Analysis.git
```

## Push Your Code

```bash
# Check current status
git status

# Add all files
git add .

# Commit with message
git commit -m "Initial commit: Risk Analysis application with deployment configs"

# Push to main branch
git push -u origin main
```

## If You Get Conflicts

```bash
# Pull first if repository has existing files
git pull origin main --allow-unrelated-histories

# Then push
git push -u origin main
```

## After Pushing - Deploy on VPS

### SSH into your Hostinger VPS

```bash
ssh your-username@your-server-ip
```

### Clone and Deploy

```bash
# Navigate to web directory
cd /var/www

# Clone the repository
sudo git clone https://github.com/Manideepgadi1/Risk-Analysis.git risk-analysis

# Go into directory
cd risk-analysis

# Make deploy script executable
sudo chmod +x deployment/deploy.sh

# Run deployment
sudo ./deployment/deploy.sh
```

### Configure Domain

```bash
# Edit Nginx config with your domain
sudo nano /etc/nginx/sites-available/risk-analysis

# Replace 'your-domain.com' with your actual domain

# Test Nginx configuration
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx
```

### Enable SSL (Optional but Recommended)

```bash
sudo certbot --nginx -d your-domain.com
```

## Access Your Application

After deployment, access at:
- **Path-based**: `http://your-domain.com/risk-analysis`
- **Or subdomain**: `http://risk-analysis.your-domain.com` (if configured)

## Updating the Application Later

### On Local Machine

```bash
# Make your changes, then:
git add .
git commit -m "Description of changes"
git push origin main
```

### On VPS

```bash
cd /var/www/risk-analysis
sudo git pull origin main
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart risk-analysis
```

## Check if Everything is Running

```bash
# Check service status
sudo systemctl status risk-analysis

# Check logs
sudo journalctl -u risk-analysis -f

# Check Nginx
sudo systemctl status nginx

# Test API
curl http://localhost:8001/api/indices
```

## Troubleshooting

### Port Already in Use

```bash
# Find process using port 8001
sudo lsof -i :8001

# Kill if needed
sudo kill -9 <PID>

# Restart service
sudo systemctl restart risk-analysis
```

### Permission Issues

```bash
sudo chown -R www-data:www-data /var/www/risk-analysis
sudo chmod -R 755 /var/www/risk-analysis
```

### Nginx Not Starting

```bash
# Test configuration
sudo nginx -t

# Check logs
sudo tail -f /var/log/nginx/error.log
```

## Your Project is Now Live! 🎉

The project is designed to:
✅ Run on port 8001 (internal)
✅ Be accessible via Nginx reverse proxy
✅ Not conflict with your other 5 projects
✅ Have its own isolated environment
✅ Auto-start on system reboot
✅ Have proper logging

Access points:
- Frontend: `http://your-domain.com/risk-analysis`
- API: `http://your-domain.com/risk-analysis/api/`
- API Docs: `http://your-domain.com/risk-analysis/api/docs`
