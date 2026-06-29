import pandas as pd

from app.utils.logger import logger


def validate_order(df):

    required_columns = [
        "userId",
        "orderId",
        "productId",
        "amount",
        "paymentMethod"
    ]

    for col in required_columns:

        if col not in df.columns:

            raise Exception(
                f"필수 컬럼 없음 : {col}"
            )

    valid_payment_methods = [
        "CARD",
        "BANK_TRANSFER",
        "VIRTUAL_ACCOUNT"
    ]

    mask = (
        df["userId"].notna()
        &
        df["orderId"].notna()
        &
        df["productId"].notna()
        &
        (
            pd.to_numeric(
                df["amount"],
                errors="coerce"
            ) > 0
        )
        &
        (
            df["paymentMethod"]
            .astype(str)
            .str.upper()
            .isin(valid_payment_methods)
        )
    )

    logger.info(
        f"[ORDER VALIDATION] "
        f"total={len(df)} "
        f"success={mask.sum()} "
        f"failed={len(df)-mask.sum()}"
    )

    return mask