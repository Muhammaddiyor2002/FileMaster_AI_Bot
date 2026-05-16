from pathlib import Path


class CompressionService:
    async def compress(self, src: Path) -> tuple[Path, int, int]:
        original_size = src.stat().st_size
        output = src.with_name(f"compressed_{src.name}")
        output.write_bytes(src.read_bytes())
        compressed_size = output.stat().st_size
        return output, original_size, compressed_size
