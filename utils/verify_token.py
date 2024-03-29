from fastapi import Header, status, HTTPException
from core.config import settings
import jwt


async def verify_token(Authorization=Header(example="Bearer eyJ0...")):
    try:
        token = Authorization.split(" ")[1]
        jwt.decode(token, settings.JWT_SECRET, algorithms=settings.JWT_ALGORITHM)

    except IndexError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token type")

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    return token
