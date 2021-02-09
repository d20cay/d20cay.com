from constant import NUMBER_WORD_MAP


def build_wl(bedwars_src):
    return {
        'global': build_mode_wl(bedwars_src, 0, 0),
        '8_1': build_mode_wl(bedwars_src, 8, 1),
        '8_2': build_mode_wl(bedwars_src, 8, 2),
        '4_3': build_mode_wl(bedwars_src, 4, 3),
        '4_4': build_mode_wl(bedwars_src, 4, 4),
        '2_4': build_mode_wl(bedwars_src, 2, 4),
        }


def build_mode_wl(bedwars_src, team_count, team_player_count):
    """
    :param bedwars_src: All bedwars stats
    :param team_count: Amount of teams in a game in this mode
    :param team_player_count: Amount of players on a team in this mode
    :return: Final kill, final death and fkd ratio in dict
    """
    global_stats = team_count == 0 and team_player_count == 0
    if not global_stats:
        team_count_word = NUMBER_WORD_MAP[team_count]
        team_player_count_word = NUMBER_WORD_MAP[team_player_count]
    win_key = 'wins_bedwars' if global_stats else f'{team_count_word}_{team_player_count_word}_wins_bedwars'
    loss_key = 'losses_bedwars' if global_stats else f'{team_count_word}_{team_player_count_word}_losses_bedwars'
    wins = bedwars_src[win_key]
    losses = bedwars_src[loss_key]
    return {
        'wins': wins,
        'losses': losses,
        'wl_ratio': wins / losses,
        }
