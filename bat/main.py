#!/usr/bin/env python3

import click


@click.command()
@click.option(
    '--makefile', default='Makefile', help='Makefile path'
)
def main(makefile):
    pass


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter
