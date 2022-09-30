from fastapi import HTTPException


def not_found() -> HTTPException:
    raise HTTPException(
        status_code=404,
        detail=f"Not found"
    )


def conflict() -> HTTPException:
    raise HTTPException(
        status_code=409,
        detail=f"Already exists"
    )


def not_acceptable() -> HTTPException:
    raise HTTPException(
        status_code=406,
        detail="Not acceptable"
    )
