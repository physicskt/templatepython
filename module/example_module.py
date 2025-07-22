"""
Example module demonstrating the coding rules implementation.
This file shows how to properly use logging and function tracking.
"""

import inspect
import sys
import os

# Add parent directory to path to import setup_logger
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from setup_logger import get_logger

# Get logger for this module
logger = get_logger(__name__)


def example_function():
    """Example function demonstrating proper logging."""
    logger.info(f"関数{inspect.currentframe().f_code.co_name}を実行中")
    
    try:
        # Example processing
        result = "Example processing completed"
        logger.info(f"処理が正常に完了しました: {result}")
        return result
    except Exception as e:
        logger.error(f"エラーが発生しました: {e}", exc_info=True)
        raise


def another_example_function(param1, param2=None):
    """Another example function with parameters."""
    logger.info(f"関数{inspect.currentframe().f_code.co_name}を実行中")
    
    try:
        logger.debug(f"パラメータ: param1={param1}, param2={param2}")
        
        if param2 is None:
            param2 = "default_value"
            
        result = f"Processed {param1} with {param2}"
        logger.info(f"関数の実行が完了しました: {result}")
        return result
        
    except Exception as e:
        logger.error(f"関数実行中にエラーが発生しました: {e}", exc_info=True)
        raise


def main():
    """Main function - no logging of function entry as per rules."""
    logger.info("アプリケーションを開始します")
    
    try:
        # Example usage
        result1 = example_function()
        result2 = another_example_function("test_input", "test_param")
        
        logger.info("すべての処理が完了しました")
        
    except Exception as e:
        logger.error(f"アプリケーション実行中にエラーが発生しました: {e}", exc_info=True)


if __name__ == "__main__":
    main()