import sqlite3

connection = sqlite3.connect('trondelag_theatre.db')
cursor = connection.cursor()


def find_actor_and_coactors(actor_name):
    query = """
    SELECT DISTINCT
        a1.name AS ActorName,
        a2.name AS CoactorName,
        p.name AS PlayName
    FROM actors a1
    JOIN played_by pb1 ON a1.id = pb1.actor_id
    JOIN roles_in_act ria1 ON pb1.role_id = ria1.role_id
    JOIN acts act ON ria1.act_id = act.id
    JOIN plays p ON act.play_id = p.id
    JOIN roles_in_act ria2 ON act.id = ria2.act_id
    JOIN played_by pb2 ON ria2.role_id = pb2.role_id
    JOIN actors a2 ON pb2.actor_id = a2.id
    WHERE a1.name = ? AND a1.id != a2.id
    ORDER BY p.name, a1.name, a2.name;
    """

    cursor.execute(query, (actor_name,))
    results = cursor.fetchall()

    if results:
        print(f"Actors who have played with {actor_name} in the same act:")
        for actor1, actor2, play in results:
            print(f"- {actor1} and {actor2} in \"{play}\"")
    else:
        print(f"No co-actors found for {actor_name}.")

find_actor_and_coactors("Tom Hanks")
find_actor_and_coactors("Arturo Scotti")
find_actor_and_coactors("Snorre Ryen Tøndel")

connection.close()