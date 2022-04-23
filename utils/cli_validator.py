import click
import validators

from infra.http import get_status


def validate_positive_int(ctx, param, value):
    if value < 1:
        raise click.BadParameter(f"{param} should be positive integer greater than 0")
    return value


def validate_url(ctx, param, value):
    if not validators.url(value):
        if get_status("http", value) == 200:
            return f'http://{value}'
        if get_status("https", value) == 200:
            return f'https://{value}'
        raise click.BadParameter(f"{param}: {value} is not a valid url")

    return value
