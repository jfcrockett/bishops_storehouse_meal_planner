#!/bin/bash
streamlit run --server.address 0.0.0.0 --server.port $PORT app.py --client.showSidebarNavigation=false --theme.base=light --theme.primaryColor=#1C77FF