from constant import MODE_COUNTS_LIST
from hypixel_stats.util import build_mode_statistic, mode_key


def build_kd(bedwars_src):
    stats = {}
    for mode in MODE_COUNTS_LIST:
        stats[mode_key(*mode)] = build_mode_statistic(bedwars_src,
                                                             "kills",
                                                             "deaths",
                                                             mode[0],
                                                             mode[1])
    return stats
