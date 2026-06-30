import pandas as pd

from app.utils.logger import logger


class SettlementAggregationProcessor:

    def execute(
        self,
        df: pd.DataFrame,
        config: dict = None
    ) -> pd.DataFrame:

        if df is None or df.empty:

            logger.warning(
                "[AGGREGATION] empty dataframe"
            )

            return pd.DataFrame()

        logger.info(
            f"[AGGREGATION] input rows={len(df)}"
        )

        result = (
            df
            .groupby(
                "업체",
                as_index=False
            )
            .agg(
                주문건수=("주문번호", "count"),
                판매금액합=("판매금액", "sum"),
                수수료합=("수수료", "sum")
            )
        )

        result["정산금액"] = (
            result["판매금액합"]
            -
            result["수수료합"]
        )

        result = result[
            [
                "업체",
                "주문건수",
                "판매금액합",
                "수수료합",
                "정산금액"
            ]
        ]

        logger.info(
            "[AGGREGATION] "
            f"vendors={len(result)}"
        )

        logger.info(
            "[AGGREGATION] "
            f"total_sales="
            f"{result['판매금액합'].sum():,.0f}"
        )

        logger.info(
            "[AGGREGATION] "
            f"total_settlement="
            f"{result['정산금액'].sum():,.0f}"
        )

        return result