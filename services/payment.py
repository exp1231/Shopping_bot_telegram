import logging
from aiogram.types import LabeledPrice
from config import settings

logger = logging.getLogger(__name__)

async def create_payment_invoice(chat_id, title, description, payload, prices):
    try:
        return {
            "chat_id": chat_id,
            "title": title,
            "description": description,
            "payload": payload,
            "provider_token": settings.PAYMENT_TOKEN,
            "currency": "RUB",
            "prices": [LabeledPrice(label=label, amount=amount) for label, amount in prices],
            "start_parameter": "payment",
            "need_name": True,
            "need_phone_number": True,
            "need_shipping_address": True
        }
    except Exception as e:
        logger.error(f"Error creating payment invoice: {e}")
        raise