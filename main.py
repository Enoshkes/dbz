from repository.json_repository import read_json, convert_from_json_to_warrior
from toolz import pipe, partial


if __name__ == '__main__':
    home_team = read_json("repository/home_team.json")
    print(
        pipe(
            home_team,
            partial(map, convert_from_json_to_warrior),
            list
        )
    )
