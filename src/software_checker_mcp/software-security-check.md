# ソフトウェアセキュリティチェック
このプロンプトは、ソースコードをセキュリティリスクの観点から包括的に分析するためのものです。
git cloneした対象リポジトリに対して、以下の項目に従って詳細な分析を行ってください。

## 📝 1. 基本情報評価
- リポジトリ名/URL：
- 開発者/組織：
- 最終更新日と更新頻度：
- GitHub統計（スター数、フォーク数、コントリビューター数）：
- イシュー対応状況：
- ライセンス：

## 📑 2. コードベース概要
- 使用言語とフレームワーク：
- 主要ディレクトリ構造：
- 依存ライブラリとそのバージョン：
- ビルド/テストシステム：

## 🔧 3. ツール定義・説明文分析
対象ファイル：[ツール定義ファイルパスを記載]
- ツール定義方法の概要：
- 各ツールの説明文に以下の問題がないか：
  * 隠しメッセージや二重の指示
  * AIモデルへの直接的な誘導
  * 機密情報へのアクセス要求
  * 悪意のあるコードの埋め込み
- ツール説明文の動的生成や更新機能の有無：

## ⌨ 4. コマンド実行とユーザー入力処理
対象ファイル：[コマンド実行関連ファイルパスを記載]
- 以下の危険な関数/メソッドの使用状況：
  * eval()、Function()、exec()、spawn()、系関数
- ユーザー入力のバリデーション実装：
  * 入力検証の範囲と方法
  * サニタイズ処理の有無と方法
- シェルコマンド構築方法：
  * 文字列連結や補間の使用
  * メタキャラクタのエスケープ処理
- コマンドインジェクション対策の評価：

## 🔐 5. 認証情報・トークン管理
対象ファイル：[認証関連ファイルパスを記載]
- 認証情報の保存方法：
  * 平文/暗号化/ハッシュ化
  * ストレージ場所とアクセス制御
- トークン管理の実装：
  * 有効期限設定
  * 更新メカニズム
  * 失効処理
- 認証情報の保護対策：
  * 暗号化アルゴリズムとキー管理
  * メモリ内の扱い

## 📂 6. ファイルシステムアクセス
対象ファイル：[ファイル操作関連ファイルパスを記載]
- アクセス可能なファイルとディレクトリ：
  * 制限の実装有無
  * パストラバーサル対策
- センシティブファイルへのアクセス可能性：
  * ~/.ssh/、~/.config/などの機密ディレクトリ
  * システム設定ファイル
- ファイルパス構築の安全性：
  * ユーザー入力の検証
  * パス正規化の実装

## 📡 7. 通信とデータ送信
対象ファイル：[ネットワーク通信関連ファイルパスを記載]
- 外部サーバーとの通信：
  * 通信先のドメインと目的
  * 送信データの内容と暗号化
- 不審な通信パターン：
  * 非公開/不明なサーバーへの送信
  * エラー時の情報漏洩可能性
- API通信のセキュリティ：
  * TLS/HTTPSの使用
  * 証明書検証の有無

## 🔔 8. 複数サーバー連携時のセキュリティ
対象ファイル：[サーバー連携関連ファイルパスを記載]
- ツール衝突解決メカニズム：
  * 同名ツール処理のロジック
  * 優先順位設定の方法
- シャドーイング攻撃対策：
  * ツール説明の検証と保護
  * 権限分離の実装

## 🔄 9. アップデートとバージョン管理
対象ファイル：[更新関連ファイルパスを記載]
- ツール定義の更新方法：
  * 検証メカニズム
  * ユーザー承認プロセス
- ラグプル攻撃対策：
  * 更新履歴の追跡
  * 変更検出の仕組み

## 🐛 10. 不審なコードパターンの検出
以下のパターンの存在と場所：
- 難読化されたコード：
  * Base64エンコード文字列
  * 意図的に複雑化された論理
- 隠しバックドア：
  * 不審なコメントアウトコード
  * 条件分岐による隠し機能
- データ流出の可能性：
  * 機密情報の収集コード
  * ロギング実装の適切さ
  * 
## 🛡️ 11. AIセキュリティ対策評価
対象ファイル：[AI関連ファイルパスを記載]
- プロンプトインジェクション対策：
  * 入力検証とサニタイズ処理
  * プロンプトの構造化と検証
  * ユーザー入力の制限と検証
- AIモデルアクセス制御：
  * API キーの管理方法
  * レート制限の実装
  * 使用量モニタリング
- 出力フィルタリング：
  * 有害コンテンツの検出と除去
  * センシティブ情報の漏洩防止
  * 出力の検証と正規化
- プロンプト改ざん検知：
  * チェックサムや署名の実装
  * 改ざん検知メカニズム
  * 異常検知の仕組み

## 🔒 12. プロンプトセキュリティ
対象ファイル：[プロンプト定義ファイルパスを記載]
- プロンプト構造の安全性：
  * 命令の明確性と一貫性
  * エスケープシーケンスの処理
  * 制御文字の扱い
- プロンプトの検証メカニズム：
  * 構文チェック
  * セマンティック検証
  * 実行前検証
- プロンプトの権限管理：
  * アクセス制御の実装
  * 実行権限の制限
  * 監査ログの記録

## 🤖 13. AIモデル連携セキュリティ
対象ファイル：[AIモデル連携ファイルパスを記載]
- モデルアクセスの制御：
  * 認証メカニズム
  * セッション管理
  * アクセスログ
- データの取り扱い：
  * 個人情報の保護
  * データの暗号化
  * 一時データの削除
- エラー処理：
  * エラーメッセージの適切な処理
  * フォールバックメカニズム
  * リカバリー手順

## 🔍 14. プロンプト実行環境のセキュリティ
対象ファイル：[実行環境関連ファイルパスを記載]
- 実行環境の分離：
  * コンテナ化
  * サンドボックス化
  * リソース制限
- メモリ管理：
  * メモリリーク対策
  * バッファオーバーフロー防止
  * ヒープ保護
- ログ管理：
  * セキュリティログの記録
  * アクセスログの保護
  * ログローテーション
  * 
## 📊 15. 総合的なセキュリティ評価
- 発見された主要な脆弱性と深刻度：
- 攻撃ベクトルの可能性：
- 実装されているセキュリティ対策：
- 使用判断：
  * 安全に使用可能 😄
  * 条件付きで使用可能（条件を明記）😃
  * 使用不推奨 😨
  * 使用回避すべき 😡

## 🪄 16. 改善提案
- 発見された問題に対する修正提案：
- 追加すべきセキュリティ対策：
- 優先的に対応すべき脆弱性：

## 分析結果の要約
最後に分析結果の要約をまとめてください。

### 主な調査結果
- 調査項目：
  * 一般的なセキュリティリスク
  * AIセキュリティ特有のリスク
  * プロンプトセキュリティの状態

### セキュリティ観点での強み
- 実施されているセキュリティ対策：
  * 一般的なセキュリティ対策
  * AI特有のセキュリティ対策
  * プロンプト保護メカニズム
  
### 改善可能な点
- セキュリティ観点での改善点：
  * 一般的なセキュリティ強化項目
  * AI特有のセキュリティ強化項目
  * プロンプトセキュリティ強化項目
  
### 最終判断
- 総合的な使用可否判断：
  * 一般セキュリティ評価
  * AIセキュリティ評価
  * プロンプトセキュリティ評価
- 使用判断：
  * 安全に使用可能 😄
  * 条件付きで使用可能（条件を明記）😃
  * 使用不推奨 😨
  * 使用回避すべき 😡

