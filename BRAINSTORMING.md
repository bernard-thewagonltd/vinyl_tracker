# STRUCTURE, CLASSES, FUNCTIONS, AND FILES

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
|   ├──     utils.py - Input validation, formatting helpers

```

## FLOW DIAGRAM

                   ┌────────────────────┐
                   │      main.py       │
                   └────────┬───────────┘
                            │
                            ▼
                    ┌─────────────┐
                    │   auth.py   │
                    │ - login()   │
                    │ - load_users│
                    └─────────────┘
                            │
                            ▼
                 ┌────────────────────┐
                 │ current_user (User)│
                 └─────────┬──────────┘
                           │
                           ▼
                   ┌────────────────┐
                   │ collection.py  │
                   │ - add_vinyl    │
                   │ - edit_vinyl   │
                   │ - remove_vinyl │
                   │ - display_vinyl│
                   └────────────────┘
                           │
          ┌────────────────┴────────────────┐
          ▼                                 ▼
┌────────────────────┐             ┌────────────────────┐
│   search.py        │             │ csv_handler.py      │
│ - search()         │             │ - import_csv()      │
│ - single_record_actions() │       │ - export_csv()      │
└────────────────────┘             └────────────────────┘
          │
          ▼
 ┌────────────────────┐
 │ Single Record Menu │
 │ - Edit Record      │
 │ - Delete Record    │
 │ - Back             │
 └────────────────────┘
          │
          ▼
 ┌────────────────────┐
 │ collection.py      │
 │ (auto-save JSON)   │
 └────────────────────┘



