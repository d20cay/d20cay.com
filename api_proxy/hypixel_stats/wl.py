from constant import MODE_COUNTS_LIST
from hypixel_stats.util import build_mode_statistic


def build_wl(bedwars_src):
    stats = {}
    for mode in MODE_COUNTS_LIST:
        stats[f'{mode[0]}_{mode[1]}'] = build_mode_statistic(bedwars_src,
                                                             "wins",
                                                             "losses",
                                                             mode[0],
                                                             mode[1])
    return stats
