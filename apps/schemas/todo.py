def todoEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "description": item["description"],
        "created_at": item["created_at"],
        "updated_at": item["updated_at"]
    }

def todosEntity(items) -> list:
    return [todoEntity(item) for item in items]