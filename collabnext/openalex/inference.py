import polars as pl


def infer_author_topic_edges(df_edges: pl.DataFrame) -> pl.DataFrame:
    df_author_work_edges = df_edges.filter(
        pl.col("start_type") == "AUTHOR" & pl.col("end_type") == "WORK"
    )
    df_work_topic_edges = df_edges.filter(
        pl.col("start_type") == "WORK" & pl.col("end_type") == "TOPIC"
    )
    df_author_topic_edges = df_author_work_edges.join(
        df_work_topic_edges,
        on=pl.col("end") == pl.col("start"),
        how="inner",
        lsuffix="_author_work",
        rsuffix="_work_topic",
    )
    df_author_topic_edges = df_author_topic_edges.select(
        [
            pl.col("start_author_work").alias("start"),
            pl.col("end_work_topic").alias("end"),
            pl.lit("TOPIC").alias("label"),
            pl.lit("AUTHOR").alias("start_type"),
            pl.lit("TOPIC").alias("end_type"),
        ]
    )
    # Add id colum of the form "{start}-{end}"
    df_author_topic_edges = df_author_topic_edges.with_column(
        pl.concat_str(["start", "end"], "-").alias("id")
    )

    return df_author_topic_edges
