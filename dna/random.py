from itertools import repeat
from random import choices
from datetime import datetime
from typing import List
from string import ascii_letters, digits
from dna.models import DNASequence, User

DNA_SYMBOLS: str = "ACGT".lower()
BENCHLING_ID_CHARS: str = ascii_letters + digits


def random_dna_sequence(k: int) -> str:
    return "".join(choices(DNA_SYMBOLS, k=k))


def random_benchling_id() -> str:
    return f"seq_{''.join(choices(BENCHLING_ID_CHARS, k=8))}"


def random_dna_object(k: int) -> DNASequence:
    return DNASequence(
        benchling_id=random_benchling_id(),
        name="random-dna-sequence",
        created_at=datetime.now(),
        bases=random_dna_sequence(k),
        creator=User(
            benchling_id="dna-sdk-user", name="DNA SDK User", handle="sdkuser"
        ),
    )


def random_dna_objects(k: int, n: int) -> List[DNASequence]:
    return list(map(random_dna_object, repeat(k, n)))
