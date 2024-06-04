def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")  # Output: 'earth/mars/venus'
