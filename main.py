import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)
    for name, info in data.items():
        race, created = Race.objects.get_or_create(
            name=info["race"]["name"],
            description=info["race"]["description"]
        )
        for skill in info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )
        if info["guild"]:
            guild, created = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                description=info["guild"]["description"]
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=name,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
