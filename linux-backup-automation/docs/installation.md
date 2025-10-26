# Installation Guide

## System Requirements
- Linux/Unix operating system
- Bash shell (version 4.0 or higher)
- Standard utilities: tar, gzip, date, find
- Minimum 100MB free disk space for temporary files

## Quick Installation
1. Download the script
2. Make executable: `chmod +x backup.sh`
3. Test: `./backup.sh /source /destination`

## System-wide Installation
```bash
sudo cp backup.sh /usr/local/bin/
sudo chmod +x /usr/local/bin/backup.sh