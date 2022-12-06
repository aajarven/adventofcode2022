def add_to_buffer(character, buffer_):
    """
    Add a character to data buffer
    """
    if character in buffer_:
        buffer_[character] = buffer_[character] + 1
    else:
        buffer_[character] = 1


def remove_from_buffer(character, buffer_):
    """
    Remove a character from data buffer
    """
    if character not in buffer_:
        raise ValueError(f"Value {character} not present in buffer: cannot remove")
    if buffer_[character] > 1:
        buffer_[character] = buffer_[character] - 1
    else:
        buffer_.pop(character)


def packet_start(signal):
    """
    Return the index of the last character in the signal start marker.
    """
    data_buffer = {}
    for i in range(0, 4):
        add_to_buffer(signal[i], data_buffer)
    if len(data_buffer) == 4:
        return 4

    for i in range(4, len(signal)):
        add_to_buffer(signal[i], data_buffer)
        remove_from_buffer(signal[i - 4], data_buffer)
        if len(data_buffer) == 4:
            return i + 1

    raise ValueError("Signal without packet start encountered")


def message_start(signal):
    """
    Return the index of the last character in message start marker.
    """
    data_buffer = {}
    for i in range(0, 14):
        add_to_buffer(signal[i], data_buffer)
    if len(data_buffer) == 14:
        return 14

    for i in range(14, len(signal)):
        add_to_buffer(signal[i], data_buffer)
        remove_from_buffer(signal[i - 14], data_buffer)
        if len(data_buffer) == 14:
            return i + 1

    raise ValueError("Signal without message start encountered")
