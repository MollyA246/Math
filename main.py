from groq import generate_response

import io, streamlit as st


SYSTEM_PROMPT= """You are a Math Mastermind. For every math problem: Show step-by-step solution.  Explain Reasoning.   Give alternative method if possible.   verify answer if possible.   use proper notation.   break complex problems into parts."""




def math_generate(problem: str, level: str, temperature=0.1, max_tokens=1024) -> str:
    prompt = f"{SYSTEM_PROMPT}\n\nMath Problem ({level}): {problem}"
    return generate_response(prompt, temperature=temperature, max_tokens=max_tokens)

def export_txt(history):
    txt = "\n\n".join([f"Q{i}: {h['q']}\nA{i}: {h['a']}" for i,h in enumerate(history, 1)])
    return io.BytesIO(txt.encode("utf-8"))

