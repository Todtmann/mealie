from db.database import db
from db.db_setup import generate_session
from fastapi import APIRouter, Depends
from schema.settings import SiteSettings
from schema.snackbar import SnackResponse
from sqlalchemy.orm.session import Session
from utils.post_webhooks import post_webhooks

router = APIRouter(prefix="/api/site-settings", tags=["Settings"])


@router.get("")
def get_main_settings(session: Session = Depends(generate_session)):
    """ Returns basic site settings """

    data = db.settings.get(session, 1)

    return data


@router.put("")
def update_settings(data: SiteSettings, session: Session = Depends(generate_session)):
    """ Returns Site Settings """
    db.settings.update(session, 1, data.dict())

    return SnackResponse.success("Settings Updated")


@router.post("/webhooks/test")
def test_webhooks():
    """ Run the function to test your webhooks """

    return post_webhooks()
