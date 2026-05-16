from pathlib import Path

from fastapi import FastAPI, HTTPException

from api.schemas import CompressRequest, ConvertRequest, MergeRequest, SummaryRequest, TranslateRequest
from core.ai_tools.service import AIToolsService
from core.compressors.service import CompressionService
from core.converters.service import ConversionService

app = FastAPI(title="FileMaster API", version="0.1.0")
convert_service = ConversionService()
compress_service = CompressionService()
ai_service = AIToolsService()


@app.post("/convert")
async def convert_file(payload: ConvertRequest):
    src = Path(payload.source_path)
    if not src.exists():
        raise HTTPException(status_code=404, detail="Source file not found")
    out = await convert_service.convert(src, payload.target_format)
    return {"output_path": str(out)}


@app.post("/compress")
async def compress_file(payload: CompressRequest):
    src = Path(payload.source_path)
    if not src.exists():
        raise HTTPException(status_code=404, detail="Source file not found")
    out, original, compressed = await compress_service.compress(src)
    saved_pct = ((original - compressed) / original * 100) if original else 0
    return {
        "output_path": str(out),
        "original_size": original,
        "compressed_size": compressed,
        "saved_percentage": round(saved_pct, 2),
    }


@app.post("/merge")
async def merge_files(payload: MergeRequest):
    paths = [Path(p) for p in payload.source_paths]
    if not all(p.exists() for p in paths):
        raise HTTPException(status_code=404, detail="One or more files not found")
    merged = paths[0].with_name("merged_output.bin")
    merged.write_bytes(b"".join(p.read_bytes() for p in paths))
    return {"output_path": str(merged)}


@app.post("/summary")
async def summary(payload: SummaryRequest):
    return {"summary": await ai_service.summarize(payload.text)}


@app.post("/translate")
async def translate(payload: TranslateRequest):
    return {"translation": await ai_service.translate(payload.text, payload.target_lang)}


@app.get("/health")
async def healthcheck():
    return {"status": "ok", "service": "filemaster-api"}
