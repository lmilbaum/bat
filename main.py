#!/usr/bin/env python3

import click


def parse(data):
    pass


def load_makefile(pathname):
    with open(pathname, 'r') as fd:
        return fd.read()


@click.command()
@click.option(
    '-f', default='Dockerfile.mk', help='Docker Makefile path'
)
def main(f):
    d = load_makefile(f)
    parse(d)


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter
