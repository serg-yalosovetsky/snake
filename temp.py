
from typing import Iterable, Tuple, TypeVar

T = TypeVar('T', int, float, complex)


def loop_last(values: Iterable[T]) -> Iterable[Tuple[bool, T]]:
    """Iterate and generate a tuple with a flag for last value.
    """
    iter_values = iter(values)
    try:
        previous_value = next(iter_values)
    except StopIteration:
        return
    for value in iter_values:
        yield False, previous_value
        previous_value = value
    yield True, previous_value


import random
import time

from rich.live import Live
from rich.table import Table


def generate_table() -> Table:
    """Make a new table."""
    table = Table()
    table.add_column("ID")
    table.add_column("Value")
    table.add_column("Status")

    _list = []
    _s = ''
    for row in range(random.randint(2, 6)):
        value = random.random() * 100

        s = f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS"
        ss = f"{row} {value:3.2f}"

        _list.append(ss)
        _s += f'{ss}\n'
        table.add_row(s)
    return _s


with Live(generate_table(), refresh_per_second=4) as live:
    for _ in range(40):
        time.sleep(0.4)
        live.update(generate_table())
        