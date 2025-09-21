# Linux Backup Automation

Automated file backup system with time-based filtering and compression.

## Overview
Shell script that backs up files modified in the last 24 hours, creating timestamped compressed archives.

## Usage
```bash
./backup.sh <source_directory> <destination_directory>
```

## Features
- Smart file detection (24-hour modification window)
- Timestamp-based archiving
- Gzip compression
- Error handling and validation
- Cron job ready

## Installation
```bash
chmod +x backup.sh
./backup.sh /path/to/source /path/to/destination
```

## System Installation
```bash
sudo cp backup.sh /usr/local/bin/
```

## Cron Schedule (Daily at 2 AM)
```bash
0 2 * * * /usr/local/bin/backup.sh /data /backup
```

## Skills Demonstrated
- Shell scripting
- File system operations
- Automation & scheduling
- Error handling
- Production deployment