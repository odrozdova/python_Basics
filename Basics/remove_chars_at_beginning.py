
def remove_chars_at_beginning(text, count):
    i = 0
    removed_text = text[count:]

    return print("Initial text:", text,"\nRemoved first", count, "symbols: ", removed_text)

remove_chars_at_beginning("AbcdeAbcde", 5)