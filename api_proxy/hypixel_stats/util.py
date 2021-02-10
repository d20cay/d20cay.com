from constant import NUMBER_WORD_MAP


def build_mode_statistic(bedwars_src, positive_statistic_name,
                         negative_statistic_name,
                         team_count, team_player_count):
    """
    :param bedwars_src: All bedwars stats
    :param positive_statistic_name: type of the positive statistic to be returned
    :param negative_statistic_name: type of the negative statistic to be returned
    :param team_count: Amount of teams in a game in this mode
    :param team_player_count: Amount of players on a team in this mode
    :return: Result positive thing, negative thing and positive/negative ratio
    """
    global_stats = team_count == 0 or team_player_count == 0
    if not global_stats:
        team_count_word = NUMBER_WORD_MAP[team_count]
        team_player_count_word = NUMBER_WORD_MAP[team_player_count]
    positive_statistic_key = f'{positive_statistic_name}_bedwars' if global_stats else f'{team_count_word}_{team_player_count_word}_{positive_statistic_name}_bedwars'
    negative_statistic_key = f'{negative_statistic_name}_bedwars' if global_stats else f'{team_count_word}_{team_player_count_word}_{negative_statistic_name}_bedwars'
    positive_statistic = bedwars_src[positive_statistic_key]
    negative_statistic = bedwars_src[negative_statistic_key]
    return {
        positive_statistic_name: positive_statistic,
        negative_statistic_name: negative_statistic,
        f'{positive_statistic_name}_{negative_statistic_name}_ratio': positive_statistic / negative_statistic,
        }


def mode_key(player_count, team_player_count):
    return 'global' if player_count == 0 or team_player_count == 0 else f'{player_count}_{team_player_count}'
