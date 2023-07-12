import urwid


def has_digit(password):
    return any(char.isdigit() for char in password)


def is_very_long(password):
    return len(password) > 12


def has_letters(password):
    return any(char.isalpha() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbol(password):
    return any(not char.isalpha() and not char.isdigit() for char in password)


def get_rating(password):
    rating = 0
    check_list = (has_digit, is_very_long, has_letters, has_upper_letters, has_lower_letters, has_symbol)
    for check in check_list:
        if check(password):
            rating += 2
    reply.set_text('Рейтинг пароля: %s' % rating)


def on_ask_change(new_edit_text):
    rating = get_rating(new_edit_text)
    reply.set_text('Рейтинг пароля: %s' % rating)


def main():
    password = urwid.Edit('Введите пароль', mask='X')
    menu = urwid.Pile([password, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(password, 'change', on_ask_change)
    urwid.MainLoop(menu).run()
    rating = get_rating(password)
    print(rating)
       

if __name__ == '__main__':
    reply = urwid.Text('')
    main()