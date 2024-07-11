from typing import Dict, Tuple, List
from sqlite3 import Connection

class ParticipantsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    
    def registry_participant(self, participant_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                INSERT INTO participants 
                    (id, trip_id, emails_to_invite_id, name)
                VALUES 
                    (?, ?, ?, ?)
            """, (
                participant_infos["id"],
                participant_infos["trip_id"],
                participant_infos["emails_to_invite_id"],
                participant_infos["name"]
            )
        )
        self.__conn.commit()
    
    def find_participants_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                SELECT p.id, p.name, p.is_confirmed, e.email
                FROM participants as p
                JOIN emails_to_invite as e ON e.id = p.emails_to_invite_id
                WHERE p.trip_id = ?
            """, (trip_id,)
        )
        participants = cursor.fetchall()
        return participants
    
    def update_participant_status(self, participant_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                UPDATE participants
                SET is_confirmed = CASE 
                    WHEN EXISTS (SELECT 1 FROM participants WHERE id = ?) 
                    THEN 1 
                    ELSE is_confirmed 
                END
                WHERE id = ?
            """, (participant_id, participant_id)
        )
        if cursor.rowcount == 0:
            raise ValueError(f"The participant with the ID you chose does not exist..")
        self.__conn.commit()