import json

import click

from dna.client import DNAService
from dna.config import Config
from dna.models import DNASequence, DNASequenceList
from dna.random import random_dna_objects

config = Config()


@click.group()
def main():
    ...


@main.group()
def sequence():
    ...


@sequence.command()
@click.argument("id", type=int)
def get(id: int):
    with DNAService(config.dna_host) as svc:
        click.echo(svc.dna.get_dna_sequence(id).json(by_alias=True))


@sequence.command
@click.argument("pattern", type=str)
def search(pattern: str):
    with DNAService(config.dna_host) as svc:
        click.echo(svc.dna.dna_sequence_search(pattern).json(by_alias=True))


@sequence.command()
@click.argument("filename", type=click.Path(exists=True))
def create(filename: str):
    with open(filename) as dna_file, DNAService(config.dna_host) as svc:
        dna = DNASequence(**json.load(dna_file))
        dna = svc.dna.create_dna_sequence(dna)

        if dna:
            click.echo(dna.json())


@main.group()
def batch():
    ...


@batch.command()
@click.argument("id", type=int)
def get(id: int):
    with DNAService(config.dna_host) as svc:
        click.echo(svc.dna.list_batch(id).json(by_alias=True))


@batch.command()
@click.argument("id", type=int)
def status(id: int):
    with DNAService(config.dna_host) as svc:
        status = svc.dna.get_batch_status(id)

        if status:
            click.echo(status.json(by_alias=True))


@batch.command()
@click.option("-f", "--filename", type=click.Path(exists=True), required=False)
@click.option("--random", type=bool, required=False, is_flag=True)
@click.option("-k", type=int, required=False)
@click.option("-n", type=int, required=False)
def create(filename: str, random: bool, k: int, n: int):
    if filename:
        with open(filename) as batch_file:
            batch_data = json.load(batch_file)

    elif random and k and n:
        batch_data = random_dna_objects(k, n)

    with DNAService(config.dna_host) as svc:
        batch = DNASequenceList(__root__=batch_data)
        batch = svc.dna.create_dna_sequence_batch(batch)

        if batch:
            click.echo(batch.json(by_alias=True))
