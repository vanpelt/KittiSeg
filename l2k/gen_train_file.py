import click

@click.command()
@click.option('--min', default=0)
@click.option('--max', default=100)
@click.option('--prefix', default="")

def output(min, max, prefix):
    for i in range(min, max):
        print("%s%i.png %s%i_gt.png" % (prefix, i, prefix, i))


if __name__ == '__main__':
    output()
