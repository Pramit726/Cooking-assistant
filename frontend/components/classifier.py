from llm.groq_qa import is_comment_question


def needs_reply_llm(comment: str) -> bool:
    return is_comment_question(comment)
