import psutil


def cpu_count():
    return psutil.cpu_count()


def cpu_stats():
    return psutil.cpu_stats()
