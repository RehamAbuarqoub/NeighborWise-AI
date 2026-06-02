# API and Data Refresh Plan

This document explains how NeighborWise AI will keep data updated.

## Refresh Strategy

NeighborWise AI will use reliable APIs, open data downloads, or scheduled data extraction scripts. Data will be collected using Python, stored in the raw data layer, cleaned, transformed, and then loaded into processed files or a database for Power BI.

## Data Flow

```text
Reliable Data Sources
        ↓
Python Ingestion Scripts
        ↓
Raw Data Layer
        ↓
Python Transformation Scripts
        ↓
Processed Data / Data Warehouse
        ↓
Power BI Scheduled Refresh
        ↓
Dashboard + Virtual Assistant