# Vinyl Tracker Project Overview

### by: Bernard Borg, 
#### Submitted in partial fulfillment to Codecademy Computer Science Track - Portfolio Project: Python Terminal Utility

---
### Summary

This is a Vinyl Record Library - a Python terminal application for managing personal vinyl collections.

Key Features:

User authentication with login system
Add, search, edit, and delete vinyl records
Sort collections by year, artist, genre, or date acquired
JSON storage for persistence
CSV import/export for data sharing and backups

## STRUCTURE, CLASSES, FUNCTIONS, AND FILES

## FILE STRUCTURE

```

├── VINYL_TRACKER
|   ├──     main.py - Entry point, login + main loop
|   ├──     auth.py - Authentication & User Manaegement (User class +                     user creation from csv)
|   ├──     models.py - Data classes: User, Vinyl
|   ├──     collection.py - CRUD operations on vinyl records        
|   ├──     search.py - All search-related logic
|   ├──     sort_records.py - Sorting functions
|   ├──     storage_json.py - JSON save/load
|   ├──     storage_csv.py - CSV import/export
|   ├──     utils.py - Helpers: clear screen, input validation, etc.
|   ├──     user_manager.py - User creation, authentication, 
            and management
|   ├──     csv_handler.py - CSV import/export helpers

```

## FLOW DIAGRAM

! [Flow Diagram](https://github.com/bernard-thewagonltd/vinyl_tracker/blob/main/diagram-export-23-11-2025-15_40_33.png)
click to view    

## DATA MODELS

User Class
	•	username (string)
	•	password (string)

Vinyl Class
	•	artist (string)
	•	album (string)
	•	year (string)
	•	genre (string)
	•	barcode (string)
	•	track_count (int)
	•	date_added (date)
	•	username (string) — owner of the record

## ARCHITECTURE

The project follows a modular structure with separate modules for different concerns:

main.py - Entry point, login + main loop
auth.py - Authentication & User Management
models.py - Data classes: User, Vinyl
collection.py - CRUD operations on vinyl records
search.py - All search-related logic
sort_records.py - Sorting functions
storage_json.py - JSON save/load
storage_csv.py - CSV import/export
utils.py - Helpers: clear screen, input validation, etc.
csv_handler.py - CSV import/export helpers

All data is stored in lowercase for consistency and displayed in title case to users. The application provides both single-record detailed views and multi-record summary lists for efficient browsing.

## PERISISTENCE

Data is persisted in JSON files, one per user. CSV import/export is also supported for sharing and backups.

## KEY DATA FLOWS:
Login Flow: Main → Login → Authenticate → Find User → Load from JSON
Collection Loading: JSON files → Vinyl objects (deserialization)
Collection Saving: Vinyl objects → JSON files (serialization)
Search Flow: Search Menu → Search → Handle Results → Display/Actions
Single Record Actions: View → Edit/Delete → Save to JSON
CSV Operations: Import/Export between CSV files and collection

## IMPORTANT RELATIONSHIPS:
The storage_json.py layer handles conversion between dictionaries and Vinyl objects
Both list_vinyls and search results lead to single_record_actions for edit/delete
The clear_screen utility is used throughout for better UX (shown with dotted lines)

## VALIDATION

Validation is implemented for all user inputs to ensure data integrity and quality. All validation functions follow the same pattern:

---
#### NOTICE: THIS PROJECT IS NOT COMPLETE. IT IS A WORK IN PROGRESS. AUTHENTICATION IS NOT IMPLEMENTED, AS PASSWORDS ARE JUST BEING STORED IN PLAIN TEXT. THIS IS A SECURITY RISK. 
---