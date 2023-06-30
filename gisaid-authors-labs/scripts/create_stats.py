#%%
import typer
import polars as pl

#%%
def main(
    input_file: str = typer.Argument(..., help="Path to input file"),
):
    df = pl.read_csv(input_file, separator="\t")
    print(df)

    # unique originating labs
    for col in df.get_columns():
        print(f"{col.name}: {col.n_unique()}")
    
    # For authors, take only first two words
    df = df.with_columns(
        name=pl.col("authors").str.split_exact(" ",1)
    )

    print(df)

    print(df.n_unique("name"))

    

#%%
if __name__ == "__main__":
    typer.run(main)