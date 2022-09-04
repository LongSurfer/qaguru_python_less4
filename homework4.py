def open_browser(chrome):
    pass


def go_to_companyname_homepage(Yandex, Google):
    pass


def find_registration_button_on_login_page():
    pass


functions = [open_browser, go_to_companyname_homepage, find_registration_button_on_login_page]


def function_name(func):
    for arg in func:
        print("The function name:", arg.__name__, end='. ')
        if not any(arg.__code__.co_varnames):
            print("No arguments")
        else:
            print("Function's arguments:", arg.__code__.co_varnames)


function_name(functions)