def normalize_id(channel_id: int):
    return -channel_id if channel_id > 0 else channel_id
