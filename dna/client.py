from typing import List
from pydantic import parse_obj_as
from requests import JSONDecodeError, Session

from dna.models import DNABatchResponse, DNABatchStatus, DNASequence, DNASequenceList


class DNAService:
    def __init__(self, host: str = "localhost:8000") -> None:
        self._host = f"http://{host}"
        self._session = Session()

    def __enter__(self) -> "DNAService":
        return self

    def __exit__(self, *_):
        self.close()

    def close(self):
        self._session.close()

    @property
    def host(self) -> str:
        return self._host

    @property
    def session(self) -> Session:
        return self._session

    @property
    def dna(self) -> "DNAResource":
        return DNAResource(self)


class DNAResource:
    def __init__(self, service: DNAService) -> None:
        self._host = service.host
        self._endpoint = f"{self._host}/dna"
        self._session = service.session

    def list_dna_sequences(self):
        return DNASequenceList(__root__=self._session.get(f"{self._endpoint}").json())

    def get_dna_sequence(self, id: str):
        try:
            return DNASequence(**self._session.get(f"{self._endpoint}/{id}").json())

        except JSONDecodeError:
            raise ValueError(f"no dna sequence found: {id}")

    def dna_sequence_search(self, pattern: str):
        return DNASequenceList(
            __root__=self._session.get(
                f"{self._endpoint}", params=dict(pattern=pattern)
            ).json(),
        )

    def list_batch(self, id):
        return DNASequenceList(
            __root__=self._session.get(f"{self._endpoint}/batch/{id}").json()
        )

    def get_batch_status(self, id: int):
        response = self._session.get(f"{self._endpoint}/batch/{id}/status").json()

        if response:
            return DNABatchStatus(**response)
    

    def create_dna_sequence(self, dna: DNASequence):
        try:
            response = self._session.post(
                f"{self._endpoint}", data=dna.json(by_alias=True, exclude_unset=True)
            ).json()

            if response:
                return DNASequence(**response)

        except Exception as e:
            raise ValueError(f"problem occurred creating object: {dna}")

    def create_dna_sequence_batch(self, batch: List[DNASequence]):
        try:
            response = self._session.post(
                f"{self._endpoint}/batch",
                data=batch.json(by_alias=True, exclude_unset=True),
            ).json()

            if response:
                return DNABatchResponse(**response)

        except Exception as e:
            raise ValueError(f"problem occurred creating batch")
