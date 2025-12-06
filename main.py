from bakery import assert_equal
from drafter import *
from dataclasses import dataclass
#hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
from meta import *

# hide_debug_information()
# set_website_framed(False)
set_website_title("Your Drafter Website")
set_site_information(
    "author",
    """
Your description can go here.
""",
    [],
    [],
    [],
)

@dataclass
class State:
    pass

@route
def index(state: State) -> Page:
    return Page(state, ["Hello ___!"])


start_server(State())
