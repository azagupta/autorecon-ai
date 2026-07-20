#!/bin/bash
DOMAIN=$1
MODE=${2:-quick}

if [ -z "$DOMAIN" ]; then
    echo "Usage: hunt <domain> [quick|full]"
    exit 1
fi

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
OUTPUT_DIR="$HOME/bugbounty/${DOMAIN}_$TIMESTAMP"
mkdir -p "$OUTPUT_DIR"

echo "🎯 Hunting $DOMAIN..."
echo "📁 Results: $OUTPUT_DIR"

if command -v subfinder &> /dev/null; then
    subfinder -d "$DOMAIN" -all -silent -o "$OUTPUT_DIR/subfinder.txt" 2>/dev/null
fi

if command -v amass &> /dev/null; then
    amass enum -passive -d "$DOMAIN" -o "$OUTPUT_DIR/amass.txt" 2>/dev/null
fi

cat "$OUTPUT_DIR"/*.txt 2>/dev/null | sort -u > "$OUTPUT_DIR/all_subdomains.txt"
TOTAL=$(wc -l < "$OUTPUT_DIR/all_subdomains.txt" 2>/dev/null || echo 0)

if command -v httpx &> /dev/null && [ -f "$OUTPUT_DIR/all_subdomains.txt" ]; then
    httpx -l "$OUTPUT_DIR/all_subdomains.txt" -threads 50 -silent -o "$OUTPUT_DIR/live_hosts.txt" 2>/dev/null
fi

echo "✅ Complete! Found $TOTAL subdomains"