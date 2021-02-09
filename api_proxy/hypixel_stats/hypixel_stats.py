from constant import NO_BEDWARS_STATS_ERROR
from hypixel_stats.fkd import build_fkd
from hypixel_stats.kd import build_kd


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

    if 'player' in stats_src:
        if 'achievements' in stats_src['player']:
            if 'bedwars_level' in stats_src['player']['achievements']:
                bedwars_stats['level'] = stats_src['player']['achievements'][
                    'bedwars_level']
            if 'bedwars_wins' in stats_src['player']['achievements']:
                bedwars_stats['wins'] = stats_src['player']['achievements'][
                    'bedwars_wins']
        if 'stats' in stats_src['player'] and 'Bedwars' in stats_src['player'][
            'stats']:
            bedwars_src = stats_src['player']['stats']['Bedwars']

            bedwars_stats.update(build_general_info(bedwars_src))
            bedwars_stats.update(build_wl(bedwars_src, stats_src))
            bedwars_stats['kd'] = build_kd(bedwars_src)
            bedwars_stats['fkd'] = build_fkd(bedwars_src)
            bedwars_stats.update(build_ws(bedwars_src))

    return bedwars_stats


def build_general_info(bedwars_src):
    stats = {}
    if 'games_played_bedwars_1' in bedwars_src:
        stats['games_played'] = bedwars_src[
            'games_played_bedwars_1']
    if 'beds_broken_bedwars' in bedwars_src:
        stats['beds_broken'] = bedwars_src[
            'beds_broken_bedwars']
    if 'beds_lost_bedwars' in bedwars_src:
        stats['beds_lost'] = bedwars_src['beds_lost_bedwars']
    return stats


def build_wl(bedwars_src, stats_src):
    stats = {}
    if 'losses_bedwars' in bedwars_src:
        stats['losses'] = bedwars_src['losses_bedwars']
    if 'achievements' in stats_src['player'] and 'bedwars_wins' in \
            stats_src['player']['achievements']:
        stats['wins'] = stats_src['player']['achievements']['bedwars_wins']
    if 'achievements' in stats_src['player'] and 'bedwars_wins' in \
            stats_src['player'][
                'achievements'] and 'losses_bedwars' in bedwars_src:
        stats['wl_ratio'] = get_wl_ratio(stats_src),
    return stats


def build_ws(bedwars_src):
    stats = {}
    existing_winstreak_categories = []
    if 'eight_one_winstreak' in bedwars_src:
        existing_winstreak_categories.append(bedwars_src['eight_one_winstreak'])
    if 'eight_two_winstreak' in bedwars_src:
        existing_winstreak_categories.append(bedwars_src['eight_two_winstreak'])
    if 'two_four_winstreak' in bedwars_src:
        existing_winstreak_categories.append(bedwars_src['two_four_winstreak'])
    if 'four_three_winstreak' in bedwars_src:
        existing_winstreak_categories.append(
            bedwars_src['four_three_winstreak'])
    if 'four_four_winstreak' in bedwars_src:
        existing_winstreak_categories.append(bedwars_src['four_four_winstreak'])
    if (len(existing_winstreak_categories)):
        stats['winstreak'] = get_winstreak(existing_winstreak_categories)
    return stats

def get_winstreak(existing_winstreak_categories):
    return max(existing_winstreak_categories)


def get_wl_ratio(stats_src):
    return stats_src['player']['achievements']['bedwars_wins'] / \
           stats_src['player']['stats']['Bedwars']['losses_bedwars']
