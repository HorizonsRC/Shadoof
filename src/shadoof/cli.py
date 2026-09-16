"""Command line client."""

import typer

from shadoof.uploader import write_to_hilltop, write_to_hilltop_chain
from typing import Annotated

app = typer.Typer(context_settings={"help_option_names": ["-h", "--help"]})


@app.command()
def main(
    input_file: Annotated[str, typer.Argument(help="Path of file to be uploaded")],
    destination: Annotated[
        str, typer.Argument(help="Path of hts file to receive data")
    ],
    pass_through_destination: Annotated[
        list[str],
        typer.Argument(help="Additional path of hts file to receive data chained"),
    ],
    raw_xml: Annotated[
        bool,
        typer.Option("--raw_xml", "-r", help="Whether to skip pre-xml parsing"),
    ] = False,
):
    if pass_through_destination is None:
        write_to_hilltop(input_file, destination, raw_xml=raw_xml)
    else:
        write_to_hilltop_chain(
            input_file, [destination] + pass_through_destination, raw_xml=raw_xml
        )


if __name__ == "__main__":
    main(
        r"\\Ares\Environmental Data Validation\Air Temperature\Documents\hydrobot_batch\402\at_depth_home\hydrobot_dsn.dsn",
        r"\\ares\Hydrology\Hydrology Workspace\Sam I\hydrobot_shadoof_demo\end_product_examples\tester.hts",
    )
