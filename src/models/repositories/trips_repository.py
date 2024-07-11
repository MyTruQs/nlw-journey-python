from typing import Dict, Tuple
from sqlite3 import Connection

class TripsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
        
    def create_trip(self, trips_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                INSERT INTO trips 
                    (id, destination, start_date, end_date, owner_name, owner_email)
                VALUES 
                    (?, ?, ?, ?, ?, ?)
            """, (
                trips_infos["id"],
                trips_infos["destination"],
                trips_infos["start_date"],
                trips_infos["end_date"],
                trips_infos["owner_name"],
                trips_infos["owner_email"]
            )
        )
        self.__conn.commit()
        
    def find_trip_by_id(self, trip_id: str) -> Tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                SELECT * FROM trips WHERE id = ?
            """, (trip_id,)
        )
        trip = cursor.fetchone()
        return trip
    
    def update_trip_status(self, trip_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                UPDATE trips
                SET status = CASE 
                    WHEN EXISTS (SELECT 1 FROM trips WHERE id = ?) 
                    THEN 1 
                    ELSE status 
                END
                WHERE id = ?
            """, (trip_id, trip_id)
        )
        if cursor.rowcount == 0:
            raise ValueError(f"The trip with the ID you chose does not exist..")
        self.__conn.commit()