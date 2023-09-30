# Standard Library
import logging


def configure_logging():
    # ロガーを作成する
    logger = logging.getLogger(__name__)

    # ログレベルを設定する
    logger.setLevel(logging.DEBUG)

    # ログハンドラを作成する
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # ログフォーマットを設定する
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    # ログハンドラをロガーに追加する
    logger.addHandler(handler)

    return logger
