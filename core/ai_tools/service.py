class AIToolsService:
    async def summarize(self, text: str) -> str:
        return text[:500]

    async def translate(self, text: str, target_lang: str) -> str:
        return f"[{target_lang}] {text}"
