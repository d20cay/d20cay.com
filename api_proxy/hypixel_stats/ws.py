from constant import NUMBER_WORD_MAP, MODE_COUNTS_LIST


def build_ws(bedwars_src):
    stats = {}
    for mode in MODE_COUNTS_LIST:
        if max(mode) != 0:
            stats[f'{mode[0]}_{mode[1]}'] = build_mode_ws(bedwars_src, mode[0],
                                                          mode[1])
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
