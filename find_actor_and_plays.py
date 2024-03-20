import sqlite3

connection = sqlite3.connect('trondelag_theatre.db')
cursor = connection.cursor()

def find_actor_and_plays(actor):
    query = """
    SELECT DISTINCT
        p.name AS PlayName,
        a.name AS ActorName,
        r.name AS RoleName
    FROM played_by pb
    JOIN actors a ON pb.actor_id = a.id
    JOIN roles r ON pb.role_id = r.id
    JOIN acts act ON act.id IN (SELECT act_id FROM roles_in_act WHERE role_id = pb.role_id)
    JOIN plays p ON act.play_id = p.id
    WHERE a.name = ?
    """

    cursor.execute(query, (actor,))
    results = cursor.fetchall()

    if results:
        print(f"{actor} appears in the following plays and roles:")
        for result in results:
            play_name, actor_name, role_name = result
            print(f"- Play: {play_name}, Role: {role_name}")
    else:
        print(f"{actor} does not appear in any plays.")

find_actor_and_plays("Tom Hanks")
find_actor_and_plays("Jo Saberniak")
find_actor_and_plays("Emma Caroline Deichmann")

connection.close()