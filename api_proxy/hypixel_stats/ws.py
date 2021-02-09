from constant import NUMBER_WORD_MAP


def build_ws(bedwars_src):
    stats = {
        '8_1': build_mode_ws(bedwars_src, 8, 1),
        '8_2': build_mode_ws(bedwars_src, 8, 2),
        '4_3': build_mode_ws(bedwars_src, 4, 3),
        '4_4': build_mode_ws(bedwars_src, 4, 4),
        '2_4': build_mode_ws(bedwars_src, 2, 4),
        }
    stats['global'] = max(stats.values())
    return stats


def build_mode_ws(bedwars_src, team_count, team_player_count):
    """
    :param bedwars_src: All bedwars stats
    :param team_count: Amount of teams in a game in this mode
    :param team_player_count: Amount of players on a team in this mode
    :return: Current winstreak in dict
    """
    team_count_word = NUMBER_WORD_MAP[team_count]
    team_player_count_word = NUMBER_WORD_MAP[team_player_count]
    ws_key = f'{team_count_word}_{team_player_count_word}_winstreak'
    return bedwars_src[ws_key]
