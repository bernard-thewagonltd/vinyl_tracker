# CS101 Capstone – Python Terminal Utility

### Project Title:

## VINYL RECORD LIBRARY


### Summary

The Vinyl Record Library is a Python-based terminal application that allows users to manage their personal vinyl record collection. Users can add, remove, edit, and view records, with prompts to enter all relevant details. The system also supports searching, sorting, and persisting data through JSON files. CSV import/export functionality enables sharing and backing up collections.

---

### Core Functionality

Authentication
	•	Login screen with usernames and passwords.
	•	CSV import occurs during the login process.
	•	New users can create an account during login, 
		new users add username and password to users.json

Main Menu Options
	1.	Add Vinyl
	2.	Search Collection
	3.	List / Sort Records
	        •	Sort by year, date acquired, artist, or genre.
    4.	Export Collection
	5.	Exit and Save 

Record Management
	•	Create Record Form to add new entries.
	•	Search Function:
	•	If search returns one record → display full record details.
	•	If search returns multiple records → display a summary list.
	•	Edit/Delete options available from the single-record view.

Data Storage & Interoperability
	•	JSON storage for persistent user collections.
	•	CSV Export for sharing or transferring to another system.
	•	CSV Import on login to populate the collection.

---

### Data Models

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

All string fields are stored in lowercase for consistency, and converted to title case when displayed.

---

### Views

Start-up
	•	Login prompt displayed on application start.

Single Record View
	•	Displays all record attributes with full detail.

Multi Record View
	•	Displays a summary containing:
	•	Album
	•	Artist
	•	Year
	•	Genre

---

### Future Expansion Ideas
	•	Add image support for album art.
	•	Fetch metadata automatically from Discogs API using barcode lookup.
	•	Convert the system into an API to integrate with a modern UI application.
    •  Strengthen security with hashed passwords and encryption.

---




