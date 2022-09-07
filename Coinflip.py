from asyncio.windows_events import INFINITE
import random

möjliga_val=("Krona","Klave")

for _ in range(INFINITE):

    Krona_eller_klave=random.choice(möjliga_val)
    input(f"Det blev {Krona_eller_klave}")
