 **Version 1.0 Operations Cheat Sheet**--

# Daily Operations

## Run Manually

```bash
cd ~/projects/stock-tracker

source venv/bin/activate

python tracker.py
```

---

## Run Using Production Script

```bash
./run_tracker.sh
```

---

# Systemd Timer Commands

## Check Timer Status

```bash
systemctl status stock-tracker.timer
```

Expected:

```text
Active: active (waiting)
```

---

## Check Service Status

```bash
systemctl status stock-tracker.service
```

Expected after execution:

```text
Active: inactive (dead)
```

This is normal.

---

## List All Timers

```bash
systemctl list-timers
```

Filter:

```bash
systemctl list-timers | grep stock
```

---

## Start Timer

```bash
sudo systemctl start stock-tracker.timer
```

---

## Stop Timer

```bash
sudo systemctl stop stock-tracker.timer
```

---

## Restart Timer

```bash
sudo systemctl restart stock-tracker.timer
```

---

## Enable Timer After Boot

```bash
sudo systemctl enable stock-tracker.timer
```

---

## Disable Timer

```bash
sudo systemctl disable stock-tracker.timer
```

---

## Check If Enabled

```bash
systemctl is-enabled stock-tracker.timer
```

Expected:

```text
enabled
```

---

# Service Commands

## Run Immediately

This triggers a stock check now.

```bash
sudo systemctl start stock-tracker.service
```

---

## Restart Service

```bash
sudo systemctl restart stock-tracker.service
```

---

# Log Commands

## View Tracker Log

```bash
tail -50 logs/tracker.log
```

---

## Follow Tracker Log Live

```bash
tail -f logs/tracker.log
```

Exit:

```bash
Ctrl+C
```

---

## View Error Log

```bash
tail -50 logs/errors.log
```

---

## Follow Error Log Live

```bash
tail -f logs/errors.log
```

---

## View Systemd Output Log

```bash
tail -50 logs/systemd.log
```

---

## Follow Systemd Output Live

```bash
tail -f logs/systemd.log
```

---

# Journal Commands

## Service History

```bash
journalctl -u stock-tracker.service
```

---

## Last 50 Entries

```bash
journalctl -u stock-tracker.service -n 50
```

---

## Live Monitoring

```bash
journalctl -fu stock-tracker.service
```

---

# Database Commands

## Open Database

```bash
sqlite3 data/stock.db
```

---

## Show Tables

```sql
.tables
```

---

## Show Products

```sql
SELECT * FROM products;
```

---

## Show Scraper Health

```sql
SELECT * FROM scraper_health;
```

---

## Exit SQLite

```sql
.quit
```

---

## Check One Product

```sql
SELECT name,status,last_checked
FROM products;
```

---

## Force Product To OUT_OF_STOCK

Useful for testing notifications.

```sql
UPDATE products
SET status='OUT_OF_STOCK'
WHERE name='Amul High Protein Wheat Flour, 65 g | Pack of 30 Sachets';
```

---

# Notification Testing

## Test ntfy

```bash
python test_notify.py
```

or:

```bash
python -c "from notifier import send_notification; send_notification('Test','Hello from stock tracker')"
```

---

# Git Commands

## Status

```bash
git status
```

---

## Commit Changes

```bash
git add .
git commit -m "message"
```

---

## View Commit History

```bash
git log --oneline --decorate
```

---

## View Tags

```bash
git tag
```

---

## Create Version Tag

```bash
git tag -a v1.1 -m "Version 1.1"
```

---

# Service File Changes

Whenever you edit:

```text
/etc/systemd/system/stock-tracker.service
/etc/systemd/system/stock-tracker.timer
```

run:

```bash
sudo systemctl daemon-reload
```

Then:

```bash
sudo systemctl restart stock-tracker.timer
```

---

# Reboot Verification

After restart:

```bash
systemctl status stock-tracker.timer

systemctl list-timers | grep stock

tail -20 logs/tracker.log
```

---

# Emergency Recovery

## Restart Everything

```bash
sudo systemctl stop stock-tracker.timer

sudo systemctl daemon-reload

sudo systemctl start stock-tracker.timer
```

---

## Manual Test

```bash
cd ~/projects/stock-tracker

source venv/bin/activate

python tracker.py
```

If this works, the application is healthy.

---

# Project Files You Will Edit Most Often

```text
config/products.py      ← Add/remove products
scrapers/amul.py        ← Scraper logic
tracker.py             ← Main workflow
notifier.py            ← Notifications
logger.py              ← Logging
```

