import pandas as pd
from src.utils import rename_columns, cast_columns, select_columns

def test_rename_columns():
    df = pd.DataFrame({"old_name": [1]})
    rename_map = {"old_name": "new_name"}
    renamed_df = rename_columns(df, rename_map)

    assert "new_name" in renamed_df.columns

def test_cast_columns():
    df = pd.DataFrame({"col": ["1", "2"]})
    casted_df = cast_columns(df, ["col"], int)

    assert casted_df["col"].dtype == int

def test_select_columns():
    df = pd.DataFrame({"col1": [1], "col2": [2]})
    selected_df = select_columns(df, ["col1"])

    assert "col2" not in selected_df.columns
