#!/bin/bash

# Bishop's Storehouse Meal Planner Runner Script
# This script starts the Streamlit application with production settings

echo "Starting Bishop's Storehouse Meal Planner..."
echo "=========================================="

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "ERROR: Streamlit is not installed."
    echo "Please install it with: pip install streamlit"
    exit 1
fi

# Check if required files exist
if [ ! -f "app.py" ]; then
    echo "ERROR: app.py not found in current directory"
    exit 1
fi

if [ ! -f "ingredients.txt" ]; then
    echo "ERROR: ingredients.txt not found in current directory"
    exit 1
fi

if [ ! -f "meal_options.txt" ]; then
    echo "ERROR: meal_options.txt not found in current directory"
    exit 1
fi

echo "All required files found ✓"
echo "Starting application..."
echo ""

# Run Streamlit with configuration to hide menu elements
streamlit run app.py \
    --server.headless true \
    --browser.gatherUsageStats false \
    --server.fileWatcherType none \
    --theme.base light

echo ""
echo "Application stopped." 