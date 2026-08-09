from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from release_tracker import crud
from release_tracker.dependencies import CurrentUserDep, SessionDep
from release_tracker.models import AccessToken, User, UserCreate, UserRead
from release_tracker.security import create_access_token, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token")
def login_for_access_token(
    session: SessionDep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> AccessToken:
    """OAuth2 compatible token login.

    Submit the email address as `username` and the password.
    """
    email = form_data.username.lower()
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect email or password",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user = crud.get_user_by_email(session, email)
    if user is None or not user.is_active:
        raise credentials_exception

    if not verify_password(form_data.password, user.hashed_password):
        raise credentials_exception

    access_token = create_access_token(subject=str(user.id))
    return AccessToken(access_token=access_token)


@router.post(
    "/register", response_model=UserRead, status_code=status.HTTP_201_CREATED
)
def register(session: SessionDep, payload: UserCreate) -> Any:
    return crud.create_user(
        session, email=payload.email, password=payload.password
    )


@router.get("/me", response_model=UserRead)
def read_current_User(current_user: CurrentUserDep) -> User:
    return current_user
