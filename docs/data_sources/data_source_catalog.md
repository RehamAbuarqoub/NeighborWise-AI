# NeighborWise AI - Data Source Catalog

This document tracks the reliable data sources used in the NeighborWise AI project.

## 1. Rent Data

| Field | Details |
|---|---|
| Dataset Name | CMHC Rental Market Data |
| Source Type | Official housing market data |
| Provider | Canada Mortgage and Housing Corporation (CMHC) |
| Data Use | Average rent by city, rental zone, bedroom type, and year |
| Format | CSV / Excel / Web table |
| Refresh Frequency | Annual or when new reports are available |
| Reliability | High |
| Status | Planned |

### Fields Needed

- city
- rental_zone
- bedroom_type
- average_rent
- vacancy_rate
- report_year
- reliability_code
- source_url
- last_updated

---

## 2. Current Asking Rent Data

| Field | Details |
|---|---|
| Dataset Name | Rental listing / market asking rent data |
| Source Type | Market listing data |
| Provider | Rentals.ca, Zumper, or licensed rental API |
| Data Use | Current asking rent and recent rental trends |
| Format | API / CSV / report |
| Refresh Frequency | Monthly or weekly if API is available |
| Reliability | Medium |
| Status | Planned |

### Fields Needed

- city
- neighborhood
- property_type
- bedroom_type
- asking_rent
- median_rent
- listing_date
- source_name
- source_url
- last_updated

---

## 3. School Information

| Field | Details |
|---|---|
| Dataset Name | School information and locations |
| Source Type | Official education/school data |
| Provider | Ontario school data, WRDSB, WCDSB |
| Data Use | School name, board, type, address, and location |
| Format | CSV / API / GIS layer |
| Refresh Frequency | Annual or when school data changes |
| Reliability | High |
| Status | Planned |

### Fields Needed

- school_name
- school_board
- school_type
- grade_level
- address
- city
- latitude
- longitude
- source_url
- last_updated

---

## 4. School Performance Indicators

| Field | Details |
|---|---|
| Dataset Name | EQAO School Achievement Results |
| Source Type | Official education performance data |
| Provider | EQAO |
| Data Use | Reading, writing, and math performance indicators |
| Format | CSV / Open Data |
| Refresh Frequency | Annual |
| Reliability | High |
| Status | Planned |

### Fields Needed

- school_name
- school_board
- school_year
- reading_score
- writing_score
- math_score
- school_performance_score
- source_url
- last_updated

---

## 5. School Boundaries

| Field | Details |
|---|---|
| Dataset Name | School boundary maps |
| Source Type | GIS boundary data |
| Provider | WRDSB / WCDSB |
| Data Use | School attendance boundaries |
| Format | GeoJSON / shapefile / ArcGIS layer |
| Refresh Frequency | Annual or when boundaries change |
| Reliability | High |
| Status | Planned |

### Fields Needed

- school_name
- school_board
- boundary_type
- geometry
- effective_year
- source_url
- last_updated

---

## 6. Safety Data

| Field | Details |
|---|---|
| Dataset Name | Public safety / incident data |
| Source Type | Open data / public safety reports |
| Provider | Waterloo Region / Police / City open data |
| Data Use | Safety score and incident trends by area |
| Format | CSV / API / GIS layer |
| Refresh Frequency | Monthly or quarterly |
| Reliability | Medium to High |
| Status | Planned |

### Fields Needed

- city
- neighborhood
- incident_type
- incident_count
- report_period
- latitude
- longitude
- safety_score
- safety_level
- source_url
- last_updated

---

## 7. GIS and Boundary Data

| Field | Details |
|---|---|
| Dataset Name | Neighborhood and city boundary data |
| Source Type | GIS open data |
| Provider | City of Kitchener / Region of Waterloo |
| Data Use | Neighborhood maps, zones, and spatial joins |
| Format | GeoJSON / shapefile |
| Refresh Frequency | As needed |
| Reliability | High |
| Status | Planned |

### Fields Needed

- boundary_name
- boundary_type
- city
- geometry
- source_url
- last_updated