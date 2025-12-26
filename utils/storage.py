from pathlib import Path
from uuid import uuid4

import aiofiles
from fastapi import UploadFile
from config import settings



async def save_upload_file(
    file: UploadFile,
    subdir: str | None = None,
) -> str:
    """
    Save an uploaded file to MEDIA_ROOT / subdir and return the URL path.

    Returns something like: /uploads/subdir/uuid.ext
    (You can store this directly in your DB.)
    """
    # 1) Create folder
    upload_dir = settings.MEDIA_ROOT
    if subdir:
        upload_dir = upload_dir / subdir

    upload_dir.mkdir(parents=True, exist_ok=True)

    # 2) Generate safe unique file name
    original_name = Path(file.filename or "")
    ext = original_name.suffix.lower()  # keep original extension
    filename = f"{uuid4().hex}{ext}"

    file_path = upload_dir / filename

    # 3) Save file in chunks (async)
    async with aiofiles.open(file_path, "wb") as out_file:
        while True:
            chunk = await file.read(1024 * 1024)  # 1 MB
            if not chunk:
                break
            await out_file.write(chunk)
    await file.close()

    # 4) Build URL path to store in DB
    parts = [settings.MEDIA_URL.strip("/")]
    if subdir:
        parts.append(subdir.strip("/"))
    parts.append(filename)

    url_path = "/" + "/".join(parts)   # e.g. "/uploads/images/uuid.png"
    return url_path
