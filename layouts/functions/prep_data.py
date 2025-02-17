import pandas as pd


def import_data(filename, **kwargs):
    """
    Reads file from local/s3 depending on environment.

    Parameters
    ----------
    filename: str
        Filename of the object to read in (.csv, .xlsx, .json, .geojson)
    **kwargs:
        Additional keyword arguments to pass onto underlying read_file method.
    """

    if filename.split(".")[-1] == "xlsx":
        return pd.read_excel(f"data/{filename}", **kwargs)

    else:
        return pd.read_csv(f"data/{filename}", **kwargs)
