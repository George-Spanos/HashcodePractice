def get_teams(teams):
    two_person_teams = list(filter(two_person_filter, teams))
    three_person_teams = list(filter(three_person_filter, teams))
    four_person_teams = list(filter(four_person_filter, teams))
    return two_person_teams, three_person_teams, four_person_teams


def two_person_filter(team):
    return team.members == 2


def three_person_filter(team):
    return team.members == 3


def four_person_filter(team):
    return team.members == 4
