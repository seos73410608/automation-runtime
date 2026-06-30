import pandas as pd

from app.utils.logger import logger


def settlement_rule_group(df: pd.DataFrame):

    logger.info(
        f"[SETTLEMENT RULE] input={len(df)}"
    )

    mask = (
        (
            df["정산완료여부"] == "N"
        )
        &
        (
            df["취소여부"] == "N"
        )
        &
        (
            df["배송완료일"].notna()
        )
    )

    logger.info(
        f"[SETTLEMENT RULE] output={mask.sum()}"
    )

    return mask