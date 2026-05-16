from pathlib import Path


class ConversionService:
    async def convert(self, src: Path, target_format: str) -> Path:
        output = src.with_suffix(f".{target_format.lower()}")
        output.write_bytes(src.read_bytes())
        return output
