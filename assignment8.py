#exercise:8.1
import mariadb
import sys


def database(ICAO_code):
    # Configuration dictionary for cleaner code
    config = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",

        "database": "airport"
    }

    try:
        # Establish the connection
        conn = mariadb.connect(**config)
        print("Successfully connected to MariaDB!")

        # Create a cursor to execute queries
        cur = conn.cursor()
        query = "SELECT name, municipality FROM airports WHERE ident=?"
        # Example: Fetching data
        cur.execute(query, (ICAO_code,))

        results = cur.fetchall()
        if results:
            for (name, municipality) in results:
                print(f"\nAirport Found!")
                print(f"Name: {name}")
                print(f"Location: {municipality}")
        else:
            print(f"\nNo airport found with ICAO code: {ICAO_code}")
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
        sys.exit(1)

    finally:
        # Always close the connection when done
        if 'conn' in locals():
            conn.close()


def main():
    ICAO_Code = input("Enter ICAO code of an airport: ")
    database(ICAO_Code)


main()




#exercise: 8.2
import mariadb
import sys


def database(area_code):
    config = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "Shirish.@1",
        "database": "airport"
    }

    try:
        conn = mariadb.connect(**config)
        print("Database connected")
        cur = conn.cursor()
        query = """ \
                SELECT type, COUNT(*) \
                FROM airports \
                WHERE iso_country = ? \
                GROUP BY type \
                ORDER BY type \
                 """

        cur.execute(query, (area_code,))

        results = cur.fetchall()

        print(f"{area_code} has ", end="")

        for index, (airport_type, count) in enumerate(results):

            name = airport_type.replace("_", " ")
            if count > 1:
                name += "s"

            if index == len(results) - 1:
                print(f"and {count} {name}.")
            else:
                print(f"{count} {name}, ", end="")



    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
        sys.exit(1)

    finally:
        # Always close the connection when done
        if 'conn' in locals():
            conn.close()


def main():
    area_code = input("Enter the area code (Eg FI for Finland): ")
    database(area_code)


main()


#exercise:8.3
import mariadb
import sys
from geopy.distance import geodesic


def get_coordinates(icao_code, cursor):
    query = """
            SELECT latitude_deg, longitude_deg
            FROM airports
            WHERE ident = ? \
            """
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()

    if result is None:
        return None

    return (result[0], result[1])


def main():
    config = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "Shirish.@1",
        "database": "airport"
    }

    icao1 = input("Enter first ICAO code: ").upper()
    icao2 = input("Enter second ICAO code: ").upper()

    try:
        conn = mariadb.connect(**config)
        print("Database connected")
        cursor = conn.cursor()

        coord1 = get_coordinates(icao1, cursor)
        coord2 = get_coordinates(icao2, cursor)

        if coord1 is None:
            print(f"Airport {icao1} not found.")
            return

        if coord2 is None:
            print(f"Airport {icao2} not found.")
            return

        distance = geodesic(coord1, coord2).kilometers

        print(f"The distance between {icao1} and {icao2} is {distance:.2f} km.")

    except mariadb.Error as e:
        print(f"Database error: {e}")
        sys.exit(1)

    finally:
        if 'conn' in locals():
            conn.close()


main()