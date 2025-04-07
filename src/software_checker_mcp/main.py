import os
from pathlib import Path
from fastmcp import FastMCP
import subprocess

# FastMCPインスタンスを作成
mcp = FastMCP("Graphic Recording MCP")

@mcp.tool()
def repository_quality_check(llm_model: str = "Claude 3.7 Sonnet") -> dict:
    """
    リポジトリ品質確認プロンプトを返す
    
    Args:
        llm_model: 使用するLLMモデル名 (デフォルト: "Claude 3.7 Sonnet")
    
    Returns:
        プロンプトと指示を含む辞書
    """
    # repo-review-prompt-v3.mdからプロンプトテンプレートを読み込む
    current_dir = Path(__file__).parent
    repo_review_path = current_dir / "repo-review-prompt-v3.md"
    
    try:
        with open(repo_review_path, "r", encoding="utf-8") as f:
            prompt_template = f.read()
    except FileNotFoundError:
        return {
            "error": "repo-review-prompt-v3.mdファイルが見つかりません。",
            "status": "error"
        }
    
    # 使用するLLMに応じた指示文を生成
    instruction = f"このプロンプトを{llm_model}に送信して、リポジトリの品質チェックを行ってください"
    
    # 特定のモデルに対する追加指示
    model_specific_notes = ""
    if "gpt" in llm_model.lower():
        model_specific_notes = "（注: GPTモデルの場合、チェックリストの完全な実施と出力形式の遵守が重要です）"
    elif "claude" not in llm_model.lower():
        model_specific_notes = "（注: 指定されたLLMがチェックリストの全項目を評価し、出力形式に従うよう指示してください）"
    
    if model_specific_notes:
        instruction += " " + model_specific_notes
    
    # クライアント側でLLMを実行するためのレスポンスを返す
    return {
        "prompt": prompt_template,
        "instruction": instruction,
        "status": "success",
        "llm_model": llm_model
    }

def get_latest_tags(count=2):
    """
    Gitリポジトリから最新のタグを取得する
    
    Args:
        count: 取得するタグの数
        
    Returns:
        タグのリスト（新しい順）
    """
    try:
        # タグを取得してバージョン順にソート
        result = subprocess.run(
            ["git", "tag", "--sort=-version:refname"],
            capture_output=True, 
            text=True, 
            check=True
        )
        tags = result.stdout.strip().split('\n')
        
        # 空の行や空白を除去
        tags = [tag for tag in tags if tag.strip()]
        
        # 指定した数のタグを返す（足りない場合は全て）
        return tags[:min(count, len(tags))]
    except subprocess.CalledProcessError:
        # エラーが発生した場合は空のリストを返す
        return []
    except Exception as e:
        print(f"タグ取得エラー: {e}")
        return []

@mcp.tool()
def generate_release_notes(
    current_tag: str = None, 
    previous_tag: str = None, 
    llm_model: str = "Claude 3.7 Sonnet"
) -> dict:
    """
    Gitリリースノート生成プロンプトを返す
    
    Args:
        current_tag: 現在のタグ（指定しない場合は最新のタグ）
        previous_tag: 前回のタグ（指定しない場合は現在のタグの一つ前）
        llm_model: 使用するLLMモデル名 (デフォルト: "Claude 3.7 Sonnet")
    
    Returns:
        プロンプトと指示を含む辞書
    """
    # タグが指定されていない場合は最新のタグを取得
    latest_tags = get_latest_tags(2)
    
    if not current_tag:
        if len(latest_tags) > 0:
            current_tag = latest_tags[0]
        else:
            return {
                "error": "タグが見つかりません。タグを手動で指定するか、リポジトリにタグを追加してください。",
                "status": "error"
            }
    
    if not previous_tag:
        if len(latest_tags) > 1:
            previous_tag = latest_tags[1]
        else:
            return {
                "error": "前回のタグが見つかりません。前回のタグを手動で指定するか、リポジトリに複数のタグを追加してください。",
                "status": "error"
            }
    
    # git-release-notes-generator-prompt_v1.mdからプロンプトテンプレートを読み込む
    current_dir = Path(__file__).parent
    release_notes_path = current_dir / "git-release-notes-generator-prompt_v1.md"
    
    try:
        with open(release_notes_path, "r", encoding="utf-8") as f:
            prompt_template = f.read()
    except FileNotFoundError:
        return {
            "error": "git-release-notes-generator-prompt_v1.mdファイルが見つかりません。",
            "status": "error"
        }
    
    # タグ情報をプロンプトに追加
    prompt_with_tags = (f"# Gitリリースノート作成: {previous_tag} から {current_tag} の変更\n\n"
                        f"{prompt_template}")
    
    # 使用するLLMに応じた指示文を生成
    instruction = (f"このプロンプトを{llm_model}に送信して、{previous_tag}から{current_tag}までの"
                  f"変更に関するGitリポジトリのリリースノートを生成してください")
    
    # 特定のモデルに対する追加指示
    model_specific_notes = ""
    if "gpt" in llm_model.lower():
        model_specific_notes = "（注: GPTモデルの場合、詳細なコミット分析と出力形式の遵守が重要です）"
    elif "claude" not in llm_model.lower():
        model_specific_notes = "（注: 指定されたLLMがGitコミット履歴を適切に分析し、指定された形式でリリースノートを生成するよう指示してください）"
    
    if model_specific_notes:
        instruction += " " + model_specific_notes
    
    # クライアント側でLLMを実行するためのレスポンスを返す
    return {
        "prompt": prompt_with_tags,
        "instruction": instruction,
        "status": "success",
        "llm_model": llm_model,
        "current_tag": current_tag,
        "previous_tag": previous_tag
    }

if __name__ == "__main__":
    mcp.run() 