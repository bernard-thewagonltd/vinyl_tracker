from datetime import datetime

class User:
    def __init__(self, username: str, password: str):
        self.username = username.lower()
        self.password = password

    def __str__(self):
        return self.username.title()


class Vinyl:
    def __init__(self, artist: str, album: str, year: str, genre: str,
                 barcode: str, trackcount: int, dateadded: str, username: str):
        self.artist = artist.lower()
        self.album = album.lower()
        self.year = year
        self.genre = genre.lower()
        self.barcode = barcode
        self.trackcount = int(trackcount)
        self.dateadded = dateadded  # ISO string 'YYYY-MM-DD'
        self.username = username.lower()

    def display_date(self):
        dt = datetime.strptime(self.dateadded, "%Y-%m-%d")
        return dt.strftime("%d-%m-%Y")

    def display(self):
        """Return a nicely formatted string for displaying this vinyl."""
        return (f"Album: {self.album.title()}\n"
                f"Artist: {self.artist.title()}\n"
                f"Year: {self.year}\n"
                f"Genre: {self.genre.title()}\n"
                f"Barcode: {self.barcode}\n"
                f"Tracks: {self.trackcount}\n"
                f"Date Added: {self.display_date()}\n"
                f"Owner: {self.username.title()}")

    def summary(self):
        """Return a short summary string for multi-record views."""
        return (f"{self.album.title()} by {self.artist.title()} "
                f"({self.year}) - {self.genre.title()}")
    
    