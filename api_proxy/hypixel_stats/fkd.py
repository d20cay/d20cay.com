from hypixel_stats.util import build_mode_statistic


def build_fkd(bedwars_src):
    return {
        'global': build_mode_fkd(bedwars_src, 0, 0),
        '8_1': build_mode_fkd(bedwars_src, 8, 1),
        '8_2': build_mode_fkd(bedwars_src, 8, 2),
        '4_3': build_mode_fkd(bedwars_src, 4, 3),
        '4_4': build_mode_fkd(bedwars_src, 4, 4),
        '2_4': build_mode_fkd(bedwars_src, 2, 4),
        }


def build_mode_fkd(bedwars_src, team_count, team_player_count):
    """
    :param bedwars_src: All bedwars stats
    :param team_count: Amount of teams in a game in this mode
    :param team_player_count: Amount of players on a team in this mode
    :return: Final kill, final death and fkd ratio in dict
    """
    return build_mode_statistic(bedwars_src, "final_kills", "final_deaths",
                                team_count,
                                team_player_count)
