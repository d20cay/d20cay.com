from constant import NO_BEDWARS_STATS_ERROR
from hypixel_stats.bbbl import build_bbbl
from hypixel_stats.fkd import build_fkd
from hypixel_stats.kd import build_kd
from hypixel_stats.wl import build_wl
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
        bedwars_stats['wl'] = build_wl(bedwars_src)
        bedwars_stats['fkd'] = build_fkd(bedwars_src)
        bedwars_stats['kd'] = build_kd(bedwars_src)
        bedwars_stats['bbbl'] = build_bbbl(bedwars_src)
        bedwars_stats['ws'] = build_ws(bedwars_src)

    return bedwars_stats


def build_general_info(stats_src):
    stats = {}
    if 'achievements' in stats_src['player']:
        if 'bedwars_level' in stats_src['player']['achievements']:
            stats['level'] = stats_src['player']['achievements'][
                'bedwars_level']
        if 'bedwars_wins' in stats_src['player']['achievements']:
            stats['wins'] = stats_src['player']['achievements'][
                'bedwars_wins']
    return stats
