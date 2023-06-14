from os import environ
from typing import Any

from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
url: str = environ.get("SUPABASE_URL")
key: str = environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# select
response: list[dict[str | Any]] = (
    supabase.table("pokemon")
    .select(
        "national_pokedex_id"
        ", pokemon_name"
        ", description"
        ", primary_type(type_name)"
        ", secondary_type(type_name)"
    )
    .execute()
    .data
)
for pokemon in response:
    for key, value in pokemon.items():
        print(key, value)
    print()

# insert
# supabase.table("pokemon").insert(
#     {
#         "national_pokedex_id": "0007",
#         "pokemon_name": "squirtle",
#         "primary_type": 1,
#         "description": "turtle pokemon",
#     }
# ).execute()
