# コーディング規則 (Coding Rules)

プログラム作成時は常にこのmdを参照してください。

## フォルダ構成 (Folder Structure)

### moduleフォルダ
- 各モジュールは`module`フォルダに配置してください
- モジュールごとに適切なファイル名を付けてください

### mdフォルダ
- mdファイルは`md`フォルダに配置してください
- ドキュメント類はすべてこのフォルダで管理します

### resultsフォルダ
- プログラムにより生成されるhtmlや、jsonは`results`フォルダに配置してください
- このフォルダ内のファイルは`.gitignore`により管理対象から除外されます

## 設定管理 (Configuration Management)

### config.py
- ハードコードされた設定値はトップレベルの`config.py`に記述してください
- `config.py`は`.gitignore`で履歴管理から除外されています
- `config.example.py`を履歴対象とし、常にリポジトリの`config.py`に差分を反映してください

### 設定ファイルの運用
1. `config.example.py`をコピーして`config.py`を作成
2. `config.py`に実際の設定値を記述
3. 設定項目の追加・変更時は`config.example.py`も更新

## ログ管理 (Logging)

### ログファイル
- logはトップレベルの`.app.log`に格納してください
- `.app.log`は管理対象から除外されています

### ログ設定
- `setup_logger.py`で定義されるloggerはソフト全体に適用されます
- ログ出力には以下の情報を含めてください：
  - 日付時刻
  - ファイル名
  - 実行行数
  - その他標準的な情報

### エラーハンドリング
- エラーは`exec=True`で、trace backを常に追跡するようにしてください
- 例外処理では詳細な情報をログに出力してください

### 関数実行ログ
- `inspect.currentframe().f_code.co_name`を用いて、すべての関数の頭に「関数〇〇を実行中」というログを出力してください
- ただし、`main`関数は除きます

## 使用例 (Usage Examples)

### ログ出力の例
```python
import logging
import inspect
from setup_logger import setup_logger

logger = setup_logger()

def example_function():
    logger.info(f"関数{inspect.currentframe().f_code.co_name}を実行中")
    try:
        # 処理内容
        pass
    except Exception as e:
        logger.error(f"エラーが発生しました: {e}", exc_info=True)
```

### config.pyの使用例
```python
from config import DATABASE_URL, API_KEY

# 設定値を使用した処理
```

## .gitignore 管理対象外ファイル

以下のファイル・フォルダは履歴管理から除外されています：
- `config.py`
- `results/`フォルダ内のすべてのファイル
- `.app.log`
- `.env`

## 注意事項 (Important Notes)

1. 設定ファイルには機密情報を含める可能性があるため、必ず`.gitignore`の設定を確認してください
2. ログファイルは定期的にローテーションまたは削除を検討してください
3. モジュールの依存関係は`requirements.txt`で管理してください
4. 新しい設定項目を追加する際は、必ず`config.example.py`も更新してください