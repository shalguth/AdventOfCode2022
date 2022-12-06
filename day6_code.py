def day_6(filename, marker_type):
    marker = []
    counter = 0
    if marker_type == "packet":
        magic_num = 4
    elif marker_type == "message":
        magic_num = 14
    with open(filename, "r") as f:
        buffer = f.readline()
        for char in buffer:
            if len(marker) == magic_num:
                return counter
            if char not in marker:
                # we have a unique character
                if len(marker) < magic_num:
                    # but are not full yet
                    marker.append(char)
                    counter += 1
                else:
                    # we are full and can return
                    print("How could we get here")
            else:
                # char is already in marker
                found_index = marker.index(char)
                for i in range(found_index+1):
                    marker.pop(0)
                marker.append(char)
                counter += 1


def main():
    marker_len_packet = day_6("day6_input.txt", "packet")
    print(marker_len_packet)

    marker_len_message = day_6("day6_input.txt", "message")
    print(marker_len_message)


if __name__ == main():
    main()
