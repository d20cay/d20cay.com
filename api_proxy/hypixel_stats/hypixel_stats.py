from constant import NO_BEDWARS_STATS_ERROR, MODE_COUNTS_LIST, STATS_LIST, \
    NUMBER_WORD_MAP
from hypixel_stats.ws import build_ws


def bedwars_overview(stats_src):
    if not 'player' in stats_src.keys() or not 'stats' in stats_src[
        'player'].keys() or not 'Bedwars' in stats_src['player'][
        'stats'].keys():
        return NO_BEDWARS_STATS_ERROR
    return {
        'playername': stats_src['player']['playername'],
        'bedwars': build_bedwars(stats_src)
        }


def build_bedwars(stats_src):
    bedwars_stats = {}

    if 'player' in stats_src and 'stats' in stats_src['player'] and 'Bedwars' in \
            stats_src['player']['stats']:
        bedwars_src = stats_src['player']['stats']['Bedwars']

        bedwars_stats.update(build_general_info(stats_src))

        for mode in MODE_COUNTS_LIST:
            bedwars_stats[mode_key(*mode)] = {}
            for key in STATS_LIST:
                bedwars_stats[mode_key(*mode)][key] = build_mode_statistic(
                    bedwars_src,
                    STATS_LIST[key][0],
                    STATS_LIST[key][1],
                    mode[0],
                    mode[1])
        bedwars_stats['ws'] = build_ws(bedwars_src)

    return bedwars_stats


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

    if positive_statistic_key in bedwars_src:
        positive_statistic = bedwars_src[positive_statistic_key]
    else:
        positive_statistic = 0

    if negative_statistic_key in bedwars_src:
        negative_statistic = bedwars_src[negative_statistic_key]
    else:
        negative_statistic = 0

    return {
        positive_statistic_name: positive_statistic,
        negative_statistic_name: negative_statistic
        }


def mode_key(player_count, team_player_count):
    return 'global' if player_count == 0 or team_player_count == 0 else f'{player_count}_{team_player_count}'


def build_general_info(stats_src):
    stats = {}
    if 'achievements' in stats_src['player']:
        if 'bedwars_level' in stats_src['player']['achievements']:
            stats['level'] = stats_src['player']['achievements'][
                'bedwars_level']
    return stats
