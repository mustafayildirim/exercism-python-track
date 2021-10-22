def get_coordinate(record):
    """

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    _, coordinate = record
    return coordinate


def convert_coordinate(coordinate):
    """

    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """

    coordinates_tuple = []
    for crd in coordinate:
        coordinates_tuple.append(crd)

    return tuple(coordinates_tuple)


def compare_records(azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """

    _, azara_coordinate = azara_record
    _, rui_coordinate, _ = rui_record
    rui_c_1, rui_c_2 = rui_coordinate


    if rui_c_1 + rui_c_2 == azara_coordinate:
        return True

    return False


def create_record(azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """

    azara_trasure, azara_coordinate = azara_record
    rui_location, rui_coordinate, rui_quadrant = rui_record
    rui_c_1, rui_c_2 = rui_coordinate
    if rui_c_1 + rui_c_2 == azara_coordinate:
        return (azara_trasure, azara_coordinate, rui_location, rui_coordinate, rui_quadrant)

    return "not a match"


def clean_up(combined_record_group):
    """

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned".
    Excess coordinates and information removed.
    """

    report = ""
    for record in combined_record_group:
        list_record = list(record)
        del list_record[1]
        report = report + str(tuple(list_record)) + '\n'
    return report
