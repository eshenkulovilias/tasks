def nitro_salt(a):
    try:
        a = int(a)
        return int(a / 100)
    except ValueError:
        return 0
