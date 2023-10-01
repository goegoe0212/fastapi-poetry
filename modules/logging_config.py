"""
### 概要:

    このモジュールには、アプリケーションのロギング設定が含まれています。

### 属性:

    - logger: ロガーを返します。

"""

# Standard Library
import logging


def configure_logging() -> logging.Logger:
    """
    ### 概要:

        このモジュールには、アプリケーションのロギング設定が含まれています。

    ### 使用例:

        >>> from modules import logging_config

        >>> logger = logging_config.configure_logging()
        >>> logger.info("info message")
        >>> logger.debug("debug message")
        >>> logger.warning("warning message")
        >>> logger.error("error message")
    """
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
